rule fastqc:
    input:
        get_fastq
    output:
        html="results/fastqc/{sample}_{condition}_Rep{rep}.html",
        zip="results/fastqc/{sample}_{condition}_Rep{rep}.zip"
    log:
        "logs_rna/fastqc/{sample}_{condition}_Rep{rep}.log"
    threads: config["threads"]
    wrapper:
        "0.31.1/bio/fastqc"
