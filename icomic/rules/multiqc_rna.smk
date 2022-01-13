rule multiqc:
    input:
        get_fastq_data(path = "results/fastqc/")
    output:
        "results/fastqc/multiqc.html"
    log:
        "logs/fastqc/multiqc.log"
    wrapper:
        "0.35.0/bio/multiqc"