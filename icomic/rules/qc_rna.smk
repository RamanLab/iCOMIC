############Test Rule############
rule fastqc:
    input:
        R1 = config["sample"]+'/{sample}_{condition}_Rep{rep}_R1.fastq',
        R2 = config["sample"]+'/{sample}_{condition}_Rep{rep}_R2.fastq'
#        unpack(get_fastq)
    output:
        R1 = "results/fastqc/{sample}_{condition}_Rep{rep}_R1_fastqc.zip",
        R2 = "results/fastqc/{sample}_{condition}_Rep{rep}_R2_fastqc.zip"
    threads: 40
    message:
        "--- running fastqc ---"
    shell:
        "fastqc -q -f fastq -o results/fastqc/ {input.R1} {input.R2}"

#rule qc_after:
#    input:
#        R1 = "results_test/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R1.fastq",
#        R2 = "results_test/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R2.fastq"
#    output:
#        R1 = "results_test/fastqc_ba/{sample}_{condition}_Rep{rep}_R1_cutadapt_fastqc.zip", 
#        R2 = "results_test/fastqc_ba/{sample}_{condition}_Rep{rep}_R2_cutadapt_fastqc.zip"
#    threads: 40
#    message:
#        "--- running fastqc again ---"
#    shell:
#        "fastqc {input.R1} {input.R2} -q -f fastq -o results_test/fastqc_ba/ {output.R1} {output.R2}"
