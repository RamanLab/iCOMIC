rule multiqc:
    input:
        get_fastq_data(path = "results_dna/trimmed/fastqc_after/")
    output:
        "results_dna/qc/multiqc_after.html"
    wrapper:
        "0.35.0/bio/multiqc"
