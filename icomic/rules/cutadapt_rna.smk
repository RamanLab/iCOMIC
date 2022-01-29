############ Rule ############

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
        others = config["params"]["cutadapt"]
    threads: config["threads"]
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
    threads: config["threads"]
    log:
        "logs_rna/cutadapt_se/{sample}_{condition}_Rep{rep}.log"
    wrapper:
        "0.17.4/bio/cutadapt/se"        
        
