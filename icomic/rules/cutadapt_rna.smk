############ Rule ############
#rule cutadapt:
#    input:
#        R1 = config["sample"]+'/{sample}_{condition}_Rep{rep}_R1.fastq',
#        R2 = config["sample"]+'/{sample}_{condition}_Rep{rep}_R2.fastq'
#    output:
#        summary_stats = "results/summary_stats/{sample}_{condition}_Rep{rep}_cutadapt_summary.txt",
#        R1 = "results/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R1.fastq",
#        R2 = "results/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R2.fastq"
#    log:
#        "results/logs/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt.log"
#    shell:
#        "cutadapt -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCA -A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT -u 15 -q 30,30 -m 35 -o {output.R1} -p {output.R2} {input.R1} {input.R2} 2> {output.summary_stats}"
##        "cutadapt -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC -A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT -o {output.R1} -p {output.R2} {input.R1} {input.R2} 2> {output.summary_stats}"

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

def get_fq(wildcards):
    """Get fastq files of given sample-unit."""
    return units.loc[(wildcards.sample, wildcards.rep, wildcards.condition), ["fq1", "fq2"]].dropna()
    if len(fastqs) == 2:
        return {"r1": fastqs.fq1, "r2": fastqs.fq2}
    return {"r1": fastqs.fq1}
    print("r1")
    
def get_fq_not_needed(wildcards):
    return units.loc[(wildcards.sample, wildcards.rep, wildcards.condition), ["fq1", "fq2"]].dropna()
    if not is_single_end(**wildcards):
        # paired-end sample
        return {"r1": fastqs.fq1, "r2": fastqs.fq2}
    # single end sample
    return {"r1": fastqs.fq1}

rule cutadapt_pe:
    input:
        get_fq
    output:
        fastq1="results/cutadapt/{sample}_{condition}_Rep{rep}_R1.fastq",
        fastq2="results/cutadapt/{sample}_{condition}_Rep{rep}_R2.fastq",
        qc= "results/cutadapt/{sample}_{condition}_Rep{rep}.qc.txt"
    params:
#        adapters = config["params"]["cutadapt"],
        others = config["params"]["cutadapt"]
    threads: config["threads"]
#    threads : 10
    log:
        "logs_rna/cutadapt/{sample}_{condition}_Rep{rep}.log"
    wrapper:
        "0.17.4/bio/cutadapt/pe"
#        "0.65.0/bio/cutadapt/pe"

        
rule cutadapt:
    input:
        get_fq
    output:
        fastq="results/cutadapt_se/{sample}_{condition}_Rep{rep}.fastq",
        qc="results/cutadapt_se/{sample}_{condition}_Rep{rep}.qc.txt"
    params: config["params"]["cutadapt"]
#        adapters = " ",
#        others = config["params"]["cutadapt"]
    threads: config["threads"]
#    threads: 10
    log:
        "logs_rna/cutadapt_se/{sample}_{condition}_Rep{rep}.log"
    wrapper:
#        "0.17.4/bio/cutadapt/se"
        "0.35.0/bio/cutadapt/se"        
        
