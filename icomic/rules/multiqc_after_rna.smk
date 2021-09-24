rule multiqc:
    input:
        get_fastq_data(path = "results/fastqc_after/")
    output:
        "results/fastqc_after/multiqc_after.html"
    wrapper:
        "0.35.0/bio/multiqc"
#        "0.31.1/bio/multiqc"