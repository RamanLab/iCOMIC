############ Rule ############
rule cutadapt:
    input:
        R1 = config["sample"]+'/{sample}_{condition}_Rep{rep}_R1.fastq',
        R2 = config["sample"]+'/{sample}_{condition}_Rep{rep}_R2.fastq'
    output:
        summary_stats = "results/summary_stats/{sample}_{condition}_Rep{rep}_cutadapt_summary.txt",
        R1 = "results/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R1.fastq",
        R2 = "results/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R2.fastq"
    log:
        "results/logs/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt.log"
    shell:
#        "cutadapt -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCA -A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT -u 15 -q 30,30 -m 35 -o {output.R1} -p {output.R2} {input.R1} {input.R2} 2> {output.summary_stats}"
        "cutadapt -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC -A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT -o {output.R1} -p {output.R2} {input.R1} {input.R2} 2> {output.summary_stats}"

##########
#rule cutadapt:
#    input:
#       R1 = "{sample}_{condition}_Rep{rep}_R1.fastq",
#       R2 = "{sample}_{condition}_Rep{rep}_R2.fastq"
#    output:
#       R1 = "results_test/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R1.fastq",
#       R2 = "results_test/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R2.fastq"
#    threads: 10 
#    wrapper:
#    shell:
#       "cutadapt --quiet -j {threads} -q 30,30 -o  {output.R1}  -p {output.R2}  {input.R1} {input.R2}  &> {log}"
