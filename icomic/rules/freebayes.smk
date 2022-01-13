rule faidx:
    input:
        config["ref"]["genome"]
    output:
        config["ref"]["genome"]+".fai"
    params:
        "" # optional params string
    wrapper:
        "0.63.0/bio/samtools/faidx"
        
rule create_dict:
    input:
        config["ref"]["genome"]
    output:
        config["ref"]["genome-dict"]+ ".dict"
    log:
        "logs/picard/create_dict.log"
    params:
        extra=""  # optional: extra arguments for picard.
    wrapper:
        "0.63.0/bio/picard/createsequencedictionary"
        

        
rule recalibrate_base_qualities:
    input:
        bam=get_recal_input_rgadded(),
        bai=config["ref"]["genome"]+".fai",
        ref=config["ref"]["genome"],
        known=config["ref"]["known-variants"],
        dict = config["ref"]["genome-dict"]+ ".dict"
    output:
        bam=protected("results_dna/recal/{sample}-{unit}-{condition}.bam")
    params:
        extra = ""
    log:
        "logs/gatk/bqsr/{sample}-{unit}-{condition}.log"
    wrapper:
        "0.27.1/bio/gatk/baserecalibrator"

rule freebayes:
    input:
        ref=config["ref"]["genome"],
        # you can have a list of samples here
        samples=get_sample_bams
    output:
        "results_dna/called/{sample}-{unit}-{condition}.vcf"  # either .vcf or .bcf
    log:
        "logs/freebayes/{sample}-{unit}-{condition}.log"
    params:
        extra="{}".format(config["params"]["freebayes"]),         # optional parameters
        chunksize=100000  # reference genome chunk size for parallelization (default: 100000)
    threads: config["threads"]
    wrapper:
        "0.36.0/bio/freebayes"
    
rule merge_variants:
    input:
        vcf=expand("results_dna/called/{u.sample}-{u.unit}-{u.condition}.vcf", u=units.itertuples())
    output:
        vcf="results_dna/merged/all.vcf.gz"
    log:
        "logs/picard/merge-genotyped.log"
    wrapper:
        "0.30.0/bio/picard/mergevcfs"


rule filter_vcfs:
    input:
        vcf = "results_dna/merged/all.vcf.gz"
    output:
        vcf= "results_dna/filtered/all.vcf.gz"
    params:
        ""  # optional parameters for bcftools view (except -o)
    conda:
        "../envs/bcftools.yaml"
    shell:
        "bcftools filter -O z -o {output.vcf} -s LOWQUAL -i'%QUAL>20' {input.vcf}"

