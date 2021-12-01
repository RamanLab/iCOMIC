############### Rule #########
#rule fastqc_after:
#    input:
#        R1 = ["results/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R1.fastq"],
#        R2 = ["results/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R2.fastq"]
#    output:
#        R1 = "results/fastqc_after/{sample}_{condition}_Rep{rep}_cutadapt_R1_fastqc.zip",
#        R2 = "results/fastqc_after/{sample}_{condition}_Rep{rep}_cutadapt_R2_fastqc.zip"
#    threads: 40
#    message:
#        "--- running fastqc again ---"
#    log:
#        "logs_rna/fastqc_after/{sample}_{condition}_Rep{rep}.log"
#    shell:
#        "fastqc -q -f fastq -o results/fastqc_after/ {input.R1} {input.R2}"


rule fastqc_after:
    input:
#        "results/cutadapt_se/{sample}_{condition}_Rep{rep}.fastq"
        get_trimmed
    output:
        html="results/cutadapt/fastqc_after/{sample}_{condition}_Rep{rep}.aftertrim.html",
        zip="results/cutadapt/fastqc_after/{sample}_{condition}_Rep{rep}.aftertrim.zip"
    log:
        "logs_rna/fastqc_after/{sample}_{condition}_Rep{rep}.aftertrim.log"
    threads: config["threads"]
#    threads : 10
    wrapper:
#        "0.65.0/bio/fastqc"
        "0.31.1/bio/fastqc"
