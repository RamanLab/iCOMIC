rule fasta_index:
    input:
        config["ref"]["genome"]
    output:
        fai = config["ref"]["genome"]+ "fai",
        dict = config["ref"]["genome"].split('.')[0] + '.dict'
    shell:
        "samtools faidx {input} > {output.fai} &&  java -jar /data/anjana/./picard/picard.jar CreateSequenceDictionary R={input} O={output.dict}"

contigs = pd.read_table(config["ref"]["genome"] + ".fai",
                        header=None, usecols=[0], squeeze=True, dtype=str)
contig="|".join(contigs)

rule MuSE_txt:
    input:
        ref=config["ref"]["genome"],
        # you can have a list of samples here
        tumor=get_sample_bams_tumor,
        normal=get_sample_bams_normal,
        bai = get_sample_bais
    output:
        txt="results_dna/called/{sample}-{unit}.MuSE.txt",  # either .vcf or .bcf
        
    log:
        "logs/muse/{sample}-{unit}.log"
    params:
        prefix="results_dna/called/{sample}-{unit}"
#        extra="{}".format(config["params"]["mutect2"]),         # optional parameters
#        chunksize=100000  # reference genome chunk size for parallelization (default: 100000)
#    threads: 2
    shell:
        "MuSE-master/MuSE call -O {params.prefix} -f {input.ref} {input.tumor} {input.normal}  2> {log}"


rule MuSE_vcf:
    input:
        txt="results_dna/called/{sample}-{unit}.MuSE.txt"
    output:
        vcf="results_dna/called/{sample}-{unit}.vcf",
#        prefix ="results_dna/called/{sample}-{unit}"
    shell:
        "MuSE-master/./MuSE sump -I {input.txt} -G -O {output.vcf}"
         
def get_vcfs(wildcards):
    """Get all aligned normal reads of given sample."""
    return expand("results_dna/called/{sample}-{unit}.vcf.gz",
                  sample=wildcards.sample,
                  unit=wildcards.unit)    
                  
#rule combine_calls:
#    input:
#        ref=config["ref"]["genome"],
#        gvcfs=expand("results_dna/mutect2_filter/{u.sample}-{u.unit}.vcf", u=units.itertuples())
#    output:
#        gvcf="results_dna/called/all.{unit}.vcf.gz"
#    params:
#        extra= "",
#        java_opts="-Xmx4g",
#    log:
#        "logs/gatk/combinegvcfs.{unit}.log"
#    shell:
#        "java -jar {params.java_opts} ./gatk-4.0.2.1/gatk-package-4.0.2.1-local.jar CombineGVCFs -V {input.gvcfs} -R {input.ref} -O {output.gvcf} {log}"
##    wrapper:
##        "0.31.1/bio/gatk/combinegvcfs"

#rule genotype_variants:
#    input:
#        ref=config["ref"]["genome"],
#        gvcf="results_dna/called/all.{unit}.vcf.gz"
#    output:
#        vcf=temp("results_dna/genotyped/all.{unit}.vcf.gz")
#    params:
#        ""
##        extra=config["params"]["gatk"]["GenotypeGVCFs"]
#    log:
#        "logs/gatk/genotypegvcfs.{unit}.log"
#    wrapper:
#        "0.27.1/bio/gatk/genotypegvcfs"     
        
rule merge_variants:
    input:
        vcf=expand("results_dna/called/{u.sample}-{u.unit}.vcf", u=units.itertuples())
#        vcf=expand("results_dna/called/{u.sample}.{u.unit}.vcf", u=units.itertuples())
    output:
        vcf="results_dna/merged/all.vcf.gz"
    log:
        "logs/picard/merge-genotyped.log"
    wrapper:
        "0.27.1/bio/picard/mergevcfs"

#rule bcftools_merge:
#    input:
#        calls=expand("results_dna/called/{u.sample}-{u.unit}.vcf.gz", u=units.itertuples())
#        index=expand("results_dna/called/{sample}.{contig}.vcf.gz", sample=samples.index, contig=contigs) 
#    output:
#        "results_dna/merged/all.vcf"
#    params:
#        ""  # optional parameters for bcftools concat (except -o)
#    shell:
#        "bcftools merge --force-samples {input.calls} {params} -Ov -o {output[0]} "
          
        
#rule bgzip:
#    input:
#        "{prefix}.vcf"
#    output:
#        "{prefix}.vcf.gz"
#    shell:
#        "bgzip -c {input} > {output} && tabix -p vcf {output} " 

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
