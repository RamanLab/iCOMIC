############### Rule #########
rule fastqc_after:
    input:
        R1 = ["results/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R1.fastq"],
        R2 = ["results/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R2.fastq"]
    output:
        R1 = "results/fastqc_after/{sample}_{condition}_Rep{rep}_cutadapt_R1_fastqc.zip",
        R2 = "results/fastqc_after/{sample}_{condition}_Rep{rep}_cutadapt_R2_fastqc.zip"
    threads: 40
    message:
        "--- running fastqc again ---"
    log:
        "results/logs/fastqc_after/{sample}_{condition}_Rep{rep}.log"
    shell:
        "fastqc -q -f fastq -o results/fastqc_after/ {input.R1} {input.R2}"
