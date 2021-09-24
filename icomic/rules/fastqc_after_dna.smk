rule fastqc_after:
    input:
        get_trimmed
    output:
        html= "results_dna/trimmed/fastqc_after/{sample}-{unit}-{condition}.aftertrim.html",
        zip="results_dna/trimmed/fastqc_after/{sample}-{unit}-{condition}.aftertrim.zip"
    log:
        "logs/fastqc/{sample}-{unit}-{condition}.aftertrim.log"
    threads: config["threads"]
    wrapper:
        "0.31.1/bio/fastqc"
#        "0.66.0/bio/fastqc"
#        "0.31.1/bio/fastqc"
        
#rule multiqc_after:
#    input:
#        get_fastq_data(path = "results_dna/qc/fastqc_after/")
#    output:
#        "results_dna/qc/multiqc_after.html"
#    wrapper:
#        "0.31.1/bio/multiqc"