rule cutadapt_pe:
    input:
        get_fastq
    output:
        fastq1="results_dna/trimmed/{sample}-{unit}.1.fastq.gz",
        fastq2="results_dna/trimmed/{sample}-{unit}.2.fastq.gz",
        qc="trimmed/{sample}-{unit}.qc.txt"
    log:
        "logs/cutadapt/{sample}-{unit}.log"
    params:
        config['params']['cutadapt']
    wrapper:
        "0.17.4/bio/cutadapt/pe"

rule cutadapt:
    input:
        get_fastq
    output:
        fastq="results_dna/trimmed/{sample}-{unit}.fastq.gz",
        qc="results_dna/trimmed/{sample}-{unit}.qc.txt"
    log:
        "logs/cutadapt/{sample}-{unit}.log"
    wrapper:
        "0.17.4/bio/cutadapt/se"
