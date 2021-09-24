rule fastqc:
    input:
        unpack(get_fastq)
    output:
        html="results_dna_new/qc/fastqc/{sample}-{unit}-{condition}.html",
        zip="results_dna_new/qc/fastqc/{sample}-{unit}-{condition}.zip"
    log:
        "logs_new/fastqc/{sample}-{unit}-{condition}.log"
    wrapper:
        "0.31.1/bio/fastqc"