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

rule mutect2_call:
    input:
        ref=config["ref"]["genome"],
        # you can have a list of samples here
        tumor=get_sample_bams_tumor,
        normal=get_sample_bams_normal,
        bai = get_sample_bais
    output:
        vcf="results_dna/called/{sample}-{unit}.vcf"  # either .vcf or .bcf
    params:
        tumor_id = get_sample_id_tumor,
        normal_id=get_sample_id_normal             
#        extra="{}".format(config["params"]["mutect2"]),         # optional parameters
#        chunksize=100000  # reference genome chunk size for parallelization (default: 100000)
#    threads: 2
    log:
        "logs/mutect2/{sample}-{unit}.log"
    conda:
        "../envs/gatk.yaml"
    shell:
        "gatk Mutect2 -R {input.ref} -I {input.tumor} -I {input.normal} -tumor {params.tumor_id} -normal {params.normal_id} -O {output.vcf} "


rule mutect2_filter:
    input:
        vcf="results_dna/called/{sample}-{unit}.vcf",
        ref = config["ref"]["genome"]
    output:
        vcf="results_dna/mutect2_filter/{sample}-{unit}.vcf"
    conda:
        "../envs/gatk.yaml"
    shell:
        "gatk FilterMutectCalls -V {input.vcf} -R {input.ref} -O {output.vcf}" 
         
def get_vcfs(wildcards):
    """Get all aligned normal reads of given sample."""
    return expand("results_dna/called/{sample}-{unit}.vcf.gz",
                  sample=wildcards.sample,
                  unit=wildcards.unit)    
                  
     
rule merge_variants:
    input:
        vcf=expand("results_dna/mutect2_filter/{u.sample}-{u.unit}.vcf", u=units.itertuples())
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
