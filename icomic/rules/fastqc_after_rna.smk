
rule fastqc_after:
    input:
        get_trimmed
    output:
        html="results/cutadapt/fastqc_after/{sample}_{condition}_Rep{rep}.aftertrim.html",
        zip="results/cutadapt/fastqc_after/{sample}_{condition}_Rep{rep}.aftertrim.zip"
    log:
        "logs_rna/fastqc_after/{sample}_{condition}_Rep{rep}.aftertrim.log"
    threads: config["threads"]
    wrapper:
        "0.31.1/bio/fastqc"
