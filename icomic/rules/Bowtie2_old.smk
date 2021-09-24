
#rule bowtie2:
#    input:
#        sample=get_trimmed
#    output:
#       temp("mapped/{sample}-{unit}.bam")
#   log:
#        "logs/bowtie2/{sample}-{unit}.log"
#   params:
#        index=config["ref"]["genome"] + ".index",  # prefix of reference genome index (built with bowtie2-build)
#        extra=""  # optional parameters
#    threads: 8
#    wrapper:
#        "0.27.1/bio/bowtie2/align"


#def bowtie2_inputs(wildcards):
#    if not is_single_end:
#        return expand("trimmed/{sample}-{unit}.{group}.fastq.gz", group=[1, 2], **wildcards)
#    return expand("trimmed/{sample}-{unit}.fastq.gz".format(**wildcards))



#rule bowtie2:
#    input:
#        sample=bowtie2_inputs,
#    output:
#        temp("mapped/{sample}-{unit}.bam")
#    log:
#        "logs/bowtie2/{sample}-{unit}.log"
#    params:
#        index=config["ref"]["genome"] + ".index",  # prefix of reference genome index (built with bowtie2-build)
#        extra=""  # optional parameters
#    threads: 8
    
#    n = len(snakemake.input.sample)
#    assert n == 1 or n == 2, "input->sample must have 1 (single-end) or 2 (paired-end) elements."

#    if n == 1:
#        reads = "-U {}".format(*snakemake.input.sample)
#    else:
#        reads = "-1 {} -2 {}".format(*snakemake.input.sample)

 #   run:
 #       if not is_single_end:
 #           shell("bowtie2 -x {input} -1 {input.forward} -2 {input.reverse} > {output}")
 #       
 #       shell("bowtie2 -x {input} -U {input.reads} > {output}")


def get_trimmed_reads(**wildcards):
    if not is_single_end(**wildcards):
        return {"r1": "trimmed/{sample}-{unit}.1.fastq.gz", **wildcards, "r2": "trimmed/{sample}-{unit}.2.fastq.gz", **wildcards}
    return {"r": "trimmed/{sample}-{unit}.fastq.gz".format(**wildcards)}

#rule bowtie2:
#    input:
#        sample=get_trimmed
#    output:
#        temp("mapped/{sample}-{unit}.bam")
#    log:
#        "logs/bowtie2/{sample}-{unit}.log"
#    params:
#        index=config["ref"]["genome"] + ".index",  # prefix of reference genome index (built #with bowtie2-build)
#        extra= ""  # optional parameters
#    wrapper:
#        "0.32.0/bio/bowtie2/align"
    


rule bowtie2_pe:
    input:
        sample=expand("results_dna/trimmed/{sample}-{unit}.{group}.fastq.gz", group=[1, 2], sample = samples.index, unit=units.index)
    output:
        "results_dna/mapped/{sample}-{unit}.bam"
    log:
        "logs/bowtie2/{sample}-{unit}.log"
    params:
        index=config["ref"]["genome"] + ".index",  # prefix of reference genome index (built with bowtie2-build)
        extra="{}".format(config["params"]["Bowtie2"])  # optional parameters
    shell:
        "bowtie2 -x {params.index} {params.extra} -1 {input.r1} -2 {input.r2} > {output}"
          
rule bowtie2_se:
    input:
        sample="results_dna/trimmed/{sample}-{unit}.fastq.gz"
    output:
        "results_dna/mapped/{sample}-{unit}.bam"
    log:
        "logs/bowtie2/{sample}-{unit}.log"
    params:
        index=config["ref"]["genome"] + ".index",  # prefix of reference genome index (built with bowtie2-build)
        extra="{}".format(config["params"]["Bowtie2"])  # optional parameters
    shell:
        "bowtie2 -x {params.index} {params.extra} -U {input} > {output}"
        
rule mark_duplicates:
    input:
        "results_dna/mapped/{sample}-{unit}.sorted.bam"
    output:
        bam="results_dna/dedup/{sample}-{unit}.bam",
        metrics="results_dna/qc/dedup/{sample}-{unit}.metrics.txt"
    log:
        "logs/picard/dedup/{sample}-{unit}.log"
    params:
        "{}".format(config["params"]["picard"]["MarkDuplicates"])
    wrapper:
        "0.26.1/bio/picard/markduplicates"
        
        
rule samtools_index:
    input:
        "{prefix}.bam"
    output:
        "{prefix}.bam.bai"
    wrapper:
        "0.27.1/bio/samtools/index"

        
rule recalibrate_base_qualities:
    input:
        bam=get_recal_input(),
        bai=get_recal_input(bai=True),
        ref=config["ref"]["genome"],
        known=config["ref"]["known-variants"]
    output:
        bam=protected("results_dna/recal/{sample}-{unit}.bam")
    params:
        extra="{}".format(config["params"]["GATK_HC"]["BaseRecalibrator"])
    log:
        "logs/gatk/bqsr/{sample}-{unit}.log"
    wrapper:
        "0.27.1/bio/gatk/baserecalibrator"


rule samtools_sort:
    input:
        "{prefix}.bam"
    output:
        "{prefix}.sorted.bam"
    params:
        "-m 4G"
    wrapper:
        "0.27.1/bio/samtools/sort"

rule samtools_stats:
    input:
        "results_dna/mapped/{sample}-{unit}.sorted.bam"
    output:
        "results_dna/qc/samtools-stats/{sample}-{unit}.txt"
    log:
        "logs/samtools-stats/{sample}-{unit}.log"
    wrapper:
        "0.27.1/bio/samtools/stats"

rule multiqc:
    input:
        expand(["results_dna/qc/samtools-stats/{u.sample}-{u.unit}.txt",
               "results_dna/qc/fastqc/{u.sample}-{u.unit}.zip",
               "results_dna/qc/fastqc/{u.sample}-{u.unit}.aftertrim.zip"],
               u=units.itertuples()),
    output:
        report("results_dna/qc/multiqc.html", caption="../report/multiqc.rst", category="Quality control")
    log:
        "logs/multiqc.log"
    wrapper:
        "0.27.1/bio/multiqc"

