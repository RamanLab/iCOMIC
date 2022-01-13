rule multiqc:
    input:
        get_fastq_data(path = "results/cutadapt/fastqc_after/")
    output:
        "results/cutadapt/fastqc_after/multiqc_after.html"
    wrapper:
        "0.35.0/bio/multiqc"