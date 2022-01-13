        
rule multiqc:
    input:
        get_fastq_data(path = "results_dna/qc/fastqc/")
    output:
        "results_dna/qc/multiqc.html"
    wrapper:
        "0.35.0/bio/multiqc"
