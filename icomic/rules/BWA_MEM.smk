
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
        "0.38.0/bio/samtools/index"


rule samtools_stats:
    input:
        "results_dna/mapped/{sample}-{unit}-{condition}.sorted.bam"
    output:
        "results_dna/qc/samtools-stats/{sample}-{unit}-{condition}.txt"
    log:
        "logs/samtools-stats/{sample}-{unit}-{condition}.log"
    wrapper:
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
    output:
        report("results_dna/multiqc/multiqc.html", caption="../report/multiqc.rst", category="Quality control")
    log:
        "logs/multiqc.log"
    params:
        dir= "results_dna/multiqc/",
        name= "multiqc.html"
    shell:
        "multiqc --force {input} -o {params.dir} -n {params.name}"
#    wrapper:
#        "0.35.0/bio/multiqc"

