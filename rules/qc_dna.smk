rule fastqc:
    input:
        unpack(get_fastq)
    output:
        html="results_dna/qc/fastqc/{sample}-{unit}-{condition}.html",
        zip="results_dna/qc/fastqc/{sample}-{unit}-{condition}.zip"
    log:
        "logs_new/fastqc/{sample}-{unit}-{condition}.log"
    threads: config["threads"]
    wrapper:
        "0.31.1/bio/fastqc"
        

#rule multiqc:
#    input:
#        get_fastq_data(path = "results_dna/qc/fastqc/")
#    output:
#        "results_dna/qc/multiqc.html"
#    wrapper:
#        "0.31.1/bio/multiqc"