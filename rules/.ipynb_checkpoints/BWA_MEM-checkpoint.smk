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
#        r1=temp("trimmed/{sample}-{unit}.1.fastq.gz"),
#        r2=temp("trimmed/{sample}-{unit}.2.fastq.gz"),
#        r1_unpaired=temp("trimmed/{sample}-{unit}.1.unpaired.fastq.gz"),
#        r2_unpaired=temp("trimmed/{sample}-{unit}.2.unpaired.fastq.gz"),
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
        reads=get_trimmed
    output:
        "results_dna/mapped/{sample}-{unit}.sorted.bam"
    log:
        "logs/bwa_mem/{sample}-{unit}.log"
    params:
        index=config["ref"]["genome"],
        extra=get_read_group,
        sort="samtools",
        sort_order="coordinate"
    wrapper:
        "0.31.1/bio/bwa/mem"


#rule mark_duplicates:
#    input:
#        "results_dna/mapped/{sample}-{unit}.sorted.bam"
#    output:
#        bam="results_dna/dedup/{sample}-{unit}.bam",
#        metrics="results_dna/qc/dedup/{sample}-{unit}.metrics.txt"
#    log:
#        "logs/picard/dedup/{sample}-{unit}.log"
#    params:
#        "{}".format(config["params"]["picard"]["MarkDuplicates"])
#    wrapper:
#        "0.26.1/bio/picard/markduplicates"
        
        
rule samtools_index:
    input:
        "{prefix}.bam"
    output:
        "{prefix}.bam.bai"
    wrapper:
        "0.27.1/bio/samtools/index"

        
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

