rule mpilup:
    input:
        # single or list of bam files
        ref=config["ref"]["genome"],
        # you can have a list of samples here
        tumor=get_sample_bams_tumor,
        normal=get_sample_bams_normal,
        bai = get_sample_bais
    output:
        "mpileup/{sample}-{unit}.mpileup.gz"
    log:
        "logs/samtools/mpileup/{sample}-{unit}.log"
    params:
        extra="",  # optional
    threads: config["threads"]
    conda:
        "../envs/samtools.yaml"
    shell:
        "samtools mpileup -f {input.ref} {params.extra} {input.normal} {input.tumor} > {output} 2> {log}"
        
        
rule varscan_somatic:
    input:
        # A pair of pileup files can be used *instead* of the mpileup
        # normal_pileup = ""
        # tumor_pileup = ""
        mpileup = "mpileup/{sample}-{unit}.mpileup.gz"
    output:
        snp="results_dna/called/{sample}-{unit}.snp.vcf",
        indel="results_dna/called/{sample}-{unit}.indel.vcf"
    message:
        "Calling somatic variants {wildcards.sample}"
    threads: config["threads"]
    params:
        prefix = "results_dna/called/{sample}-{unit}",
        extra = config["params"]["VarScan"]
#        extra = config["params"]["VarScan"]
    conda:
        "../envs/varscan.yaml"
    log:
        "logs/varscan/{sample}-{unit}.log"
    shell:
#        "varscan -h"
        "varscan somatic {input.mpileup} {params.prefix} --mpileup 1 --output-vcf {params.extra}"
        
def get_vcfs(wildcards):
    """Get all aligned normal reads of given sample."""
    return expand("results_dna/called/{sample}-{unit}.vcf.gz",
                  sample=wildcards.sample,
                  unit=wildcards.unit) 
                  
rule merge_variants:
    input:
        vcf=expand("results_dna/called/{u.sample}-{u.unit}.{type}.vcf",  u=units.itertuples(), type=['snp', 'indel'])
#        vcf=expand("results_dna/called/{u.sample}.{u.unit}.vcf", u=units.itertuples())
    output:
        vcf="results_dna/merged/all.vcf.gz"
    log:
        "logs/picard/merge-genotyped.log"
    wrapper:
        "0.27.1/bio/picard/mergevcfs"
        
def get_vartype_arg(wildcards):
    return "--select-type-to-include {}".format(
        "SNP" if wildcards.vartype == "snvs" else "INDEL")


rule select_calls:
    input:
        ref=config["ref"]["genome"],
        vcf="results_dna/merged/all.vcf.gz"
    output:
        vcf=temp("results_dna/filtered/all.{vartype}.vcf.gz")
    params:
        extra=get_vartype_arg
    log:
        "logs/gatk/selectvariants/{vartype}.log"
    wrapper:
        "0.27.1/bio/gatk/selectvariants"


def get_filter(wildcards):
    return {
        "snv-hard-filter":
        config["filtering"]["hard"][wildcards.vartype]}
        
rule hard_filter_calls:
    input:
        ref=config["ref"]["genome"],
        vcf="results_dna/filtered/all.{vartype}.vcf.gz"
    output:
        vcf=temp("results_dna/filtered/all.{vartype}.hardfiltered.vcf.gz")
    params:
        filters=get_filter
    log:
        "logs/gatk/variantfiltration/{vartype}.log"
    wrapper:
        "0.27.1/bio/gatk/variantfiltration"


rule recalibrate_calls:
    input:
        vcf="results_dna/filtered/all.{vartype}.vcf.gz"
    output:
        vcf=temp("results_dna/filtered/all.{vartype}.recalibrated.vcf.gz")
    params:
#        extra="{}".format(config["params"]["GATK_HC"]["VariantRecalibrator"])
    log:
        "logs/gatk/variantrecalibrator/{vartype}.log"
    wrapper:
        "0.27.1/bio/gatk/variantrecalibrator"


rule merge_calls:
    input:
        vcf=expand("results_dna/filtered/all.{vartype}.{filtertype}.vcf.gz",
                   vartype=["snvs", "indels"],
                   filtertype="recalibrated"
                              if config["filtering"]["vqsr"]
                              else "hardfiltered")
    output:
        vcf="results_dna/filtered/all.vcf.gz"
    log:
        "logs/picard/merge-filtered.log"
    wrapper:
        "0.27.1/bio/picard/mergevcfs" 