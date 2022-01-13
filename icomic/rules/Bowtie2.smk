

def get_trimmed_reads(wildcards):
    if not is_single_end(**wildcards):
        return expand("trimmed/{sample}-{unit}.{group}.fastq.gz", group=[1, 2], **wildcards)
    return expand("trimmed/{sample}-{unit}.fastq.gz".format(**wildcards))

rule bowtie2:
    input:
        sample=get_fastq
    output:
        "results_dna/mapped/{sample}-{unit}-{condition}.bam"
    log:
        "logs/bowtie2/{sample}-{unit}-{condition}.log"
    params:
        index=config["index"]["Bowtie2"],  # prefix of reference genome index (built with bowtie2-build)
        extra=""  # optional parameters
    threads: config["threads"]
    wrapper:
        "0.36.0/bio/bowtie2/align"


        
rule samtools_sort:
    input:
        "results_dna/mapped/{sample}-{unit}-{condition}.bam"
    output:
        "results_dna/mapped/{sample}-{unit}-{condition}.sorted.bam"
    params:
        "-m 4G"
    wrapper:
        "0.36.0/bio/samtools/sort"

rule mark_duplicates:
    input:
        "results_dna/mapped/{sample}-{unit}-{condition}.sorted.bam"
    output:
        bam="results_dna/dedup/{sample}-{unit}-{condition}.bam",
        metrics="results_dna/qc/dedup/{sample}-{unit}-{condition}.metrics.txt"
    log:
        "logs_new/picard/dedup/{sample}-{unit}-{condition}.log"
    params:
        "{}".format(config["params"]["picard"]["MarkDuplicates"])
    wrapper:
        "0.26.1/bio/picard/markduplicates"

rule samtools_index:
    input:
        "{prefix}.sorted.bam"
    output:
        "{prefix}.sorted.bam.bai"
    wrapper:
        "0.35.0/bio/samtools/index"

        
rule samtools_stats:
    input:
        "results_dna/mapped/{sample}-{unit}-{condition}.sorted.bam"
    output:
        "results_dna/qc/samtools-stats/{sample}-{unit}-{condition}.txt"
    log:
        "logs/samtools-stats/{sample}-{unit}-{condition}.log"
    wrapper:
        "0.38.0/bio/samtools/stats"
        
rule replace_rg:
    input:
        "results_dna/dedup/{sample}-{unit}-{condition}.bam"
    output:
        "results_dna/dedup_rgadded/{sample}-{unit}-{condition}.bam"
    log:
        "logs/picard/replace_rg/{sample}-{unit}-{condition}.log"
    params:
        "VALIDATION_STRINGENCY=SILENT SO=coordinate RGLB=lib1 RGPL=illumina RGPU={sample}-{unit}-{condition} RGSM={sample}-{unit}-{condition}"
    wrapper:
        "0.35.0/bio/picard/addorreplacereadgroups"
        
rule bcf_stat:
    input:
        "results_dna/filtered/all.vcf.gz"
    output:
        "results_dna/bcftools_stats/all.txt"
    shell:
        "bcftools stats {input} > {output}"

rule multiqc:
    input:
        expand(["results_dna/qc/samtools-stats/{u.sample}-{u.unit}-{u.condition}.txt",
                "results_dna/qc/dedup/{u.sample}-{u.unit}-{u.condition}.metrics.txt"],
               u=units.itertuples()),
        "results_dna/bcftools_stats/all.txt",
        get_multiqc_data(),
    output:
        report("results_dna/multiqc/multiqc.html", caption="../report/multiqc.rst", category="Quality control")
    log:
        "logs/multiqc.log"
    wrapper:
        "0.35.0/bio/multiqc"
