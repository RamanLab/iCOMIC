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
        
