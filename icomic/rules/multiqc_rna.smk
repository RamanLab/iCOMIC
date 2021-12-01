rule multiqc:
    input:
        get_fastq_data(path = "results/fastqc/")
    output:
        "results/fastqc/multiqc.html"
    log:
        "logs/fastqc/multiqc.log"
#    conda:
#        "../envs/multiqc.yaml"
    wrapper:
#        "0.27.1/bio/multiqc"
#        "0.65.0/bio/multiqc"
#        "0.30.0/bio/multiqc"
#        "0.38.0/bio/multiqc"
#        "0.66.0/bio/multiqc"
#        "0.79.0/bio/multiqc"
        "0.35.0/bio/multiqc"