#rule trim_reads_se:
#    input:
#        unpack(get_fastq)
#    output:
#        temp("trimmed/{sample}-{unit}.fastq.gz")
#    params:
#        extra="",
#        **config["params"]["trimmomatic"]["se"]
#    log:
#        "logs/trimmomatic/{sample}-{unit}.log"
#    wrapper:
#        "0.30.0/bio/trimmomatic/se"


#rule trim_reads_pe:
#    input:
#        unpack(get_fastq)
#    output:
#        r1=temp("results_dna_new/trimmed/{sample}-{unit}.1.fastq"),
#        r2=temp("results_dna_new/trimmed/{sample}-{unit}.2.fastq"),
#        r1_unpaired=temp("results_dna_new/trimmed/{sample}-{unit}.1.unpaired.fastq"),
#        r2_unpaired=temp("results_dna_new/trimmed/{sample}-{unit}.2.unpaired.fastq"),
#        trimlog="trimmed/{sample}-{unit}.trimlog.txt"
#    params:
#        extra=lambda w, output: "-trimlog {}".format(output.trimlog),
#        **config["params"]["trimmomatic"]["pe"]
#    log:
#        "logs/trimmomatic/{sample}-{unit}.log"
#    wrapper:
#        "0.30.0/bio/trimmomatic/pe"



rule map_reads:
    input:
        reads=get_fastq
    output:
        "results_dna/mapped/{sample}-{unit}-{condition}.sorted.bam"
    log:
        "logs/bwa_mem/{sample}-{unit}-{condition}.log"
    params:
        index=config["index"]["BWA_MEM"],
        extra=get_read_group,
        sort="samtools",
        sort_order="coordinate"
    threads: config["threads"]
    wrapper:
        "0.31.1/bio/bwa/mem"


rule mark_duplicates:
    input:
        "results_dna/mapped/{sample}-{unit}-{condition}.sorted.bam"
    output:
        bam="results_dna/dedup/{sample}-{unit}-{condition}.bam",
        metrics="results_dna/qc/dedup/{sample}-{unit}-{condition}.metrics.txt"
    log:
        "logs_new/picard/dedup/{sample}-{unit}-{condition}.log"
    params:
        "-Xmx4g " + "{}".format(config["params"]["picard"]["MarkDuplicates"])
    wrapper:
        "0.26.1/bio/picard/markduplicates"
        
        
rule samtools_index:
    input:
        "{prefix}.bam"
    output:
        "{prefix}.bam.bai"
    wrapper:
#        "0.27.1/bio/samtools/index"
        "0.38.0/bio/samtools/index"

#rule samtools_index:
#    input:
#        "results_dna/mapped/{sample}-{unit}-{condition}.sorted.bam"
#    output:
#        "results_dna/mapped/{sample}-{unit}-{condition}.sorted.bam.bai"
#    wrapper:
#        "0.31.1/bio/samtools/index"

        
#rule recalibrate_base_qualities:
#    input:
#        bam=get_recal_input(),
#        bai=get_recal_input(bai=True),
#        ref=config["ref"]["genome"],
#        known=config["ref"]["known-variants"]
#    output:
#        bam=protected("results_dna/recal/{sample}-{unit}.bam")
#    params:
#        extra="{}".format(config["params"]["GATK_HC"]["BaseRecalibrator"])
#    log:
#        "logs/gatk/bqsr/{sample}-{unit}.log"
#    wrapper:
#        "0.27.1/bio/gatk/baserecalibrator"

rule samtools_stats:
    input:
        "results_dna/mapped/{sample}-{unit}-{condition}.sorted.bam"
    output:
        "results_dna/qc/samtools-stats/{sample}-{unit}-{condition}.txt"
    log:
        "logs/samtools-stats/{sample}-{unit}-{condition}.log"
    wrapper:
#        "0.27.1/bio/samtools/stats"
        "0.38.0/bio/samtools/stats"


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
#        get_fastq_data(path = "results_dna/qc/fastqc/")
    output:
        report("results_dna/multiqc/multiqc.html", caption="../report/multiqc.rst", category="Quality control")
    log:
        "logs/multiqc.log"
    wrapper:
        "0.35.0/bio/multiqc"
#        "0.65.0/bio/multiqc"
#        "0.27.1/bio/multiqc"

