#if "restrict-regions" in config["processing"]:
#    rule compose_regions:
#        input:
#            config["processing"]["restrict-regions"]
#        output:
#            "called/{contig}.regions.bed"
#        conda:
#            "../envs/bedops.yaml"
#        shell:
#            "bedextract {wildcards.contig} {input} > {output}"

rule recalibrate_base_qualities:
    input:
        bam=get_recal_input(),
        bai=get_recal_input(bai=True),
        ref=config["ref"]["genome"],
        known=config["ref"]["known-variants"]
    output:
        bam=protected("results_dna/recal/{sample}-{unit}.bam")
    params:
        extra = ""
#        extra="{}".format(config["params"]["GATK_HC"]["BaseRecalibrator"])
    log:
        "logs/gatk/bqsr/{sample}-{unit}.log"
    wrapper:
        "0.27.1/bio/gatk/baserecalibrator"


rule call_variants: 
    input:
        bam=get_sample_bams,
        bai=get_sample_bais,
        ref=config["ref"]["genome"],
        known=config["ref"]["known-variants"],
        regions=[]
    output:
        gvcf=protected("results_dna/called/{sample}.{contig}.g.vcf.gz")
    log:
        "logs/gatk/haplotypecaller/{sample}.{contig}.log"
    params:
        extra="{}".format(config["params"]["GATK_HC"])
#        extra="{}".format(config["params"]["GATK_HC"]["HaplotypeCaller"])
    wrapper:
        "0.27.1/bio/gatk/haplotypecaller"


rule combine_calls:
    input:
        ref=config["ref"]["genome"],
        gvcfs=expand("results_dna/called/{sample}.{{contig}}.g.vcf.gz", sample=samples.index)
    output:
        gvcf="results_dna/called/all.{contig}.g.vcf.gz"
    log:
        "logs/gatk/combinegvcfs.{contig}.log"
    wrapper:
        "0.27.1/bio/gatk/combinegvcfs"


rule genotype_variants:
    input:
        ref=config["ref"]["genome"],
        gvcf="results_dna/called/all.{contig}.g.vcf.gz"
    output:
        vcf="results_dna/genotyped/all.{contig}.vcf.gz"
    params:
        extra = ""
#        extra=config["params"]["GATK_HC"]["GenotypeGVCFs"]
    log:
        "logs/gatk/genotypegvcfs.{contig}.log"
    wrapper:
        "0.27.1/bio/gatk/genotypegvcfs"


rule merge_variants:
    input:
        vcf=expand("results_dna/genotyped/all.{contig}.vcf.gz", contig=contigs)
    output:
        vcf="results_dna/genotyped/all.vcf.gz"
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
        vcf="results_dna/genotyped/all.vcf.gz"
    output:
        vcf="results_dna/filtered/all.{vartype}.vcf.gz"
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
        vcf="results_dna/filtered/all.{vartype}.hardfiltered.vcf.gz"
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
        extra = ""
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
        vcf="results_dna/filtered/all.vcf"
    log:
        "logs/picard/merge-filtered.log"
    wrapper:
        "0.27.1/bio/picard/mergevcfs"
