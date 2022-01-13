def get_fq(wildcards):
    """Get fastq files of given sample-unit."""
    return units.loc[(wildcards.sample, wildcards.unit, wildcards.condition), ["fq1", "fq2"]].dropna()
    if len(fastqs) == 2:
        return {"r1": fastqs.fq1, "r2": fastqs.fq2}
    return {"r1": fastqs.fq1}
    
def get_fq_not_needed(wildcards):
    return units.loc[(wildcards.sample, wildcards.unit, wildcards.condition), ["fq1", "fq2"]].dropna()
    if not is_single_end(**wildcards):
        # paired-end sample
        return {"r1": fastqs.fq1, "r2": fastqs.fq2}
    # single end sample
    return {"r1": fastqs.fq1}


rule cutadapt_pe:
    input:
        get_fq
    output:
        fastq1="results_dna/trimmed/{sample}-{unit}-{condition}.1.fastq.gz",
        fastq2="results_dna/trimmed/{sample}-{unit}-{condition}.2.fastq.gz",
        qc="results_dna/trimmed/{sample}-{unit}-{condition}.qc.txt"
    log:
        "logs/cutadapt/{sample}-{unit}-{condition}.log"
    threads: config["threads"]
    params: config["params"]["cutadapt"]
    wrapper:
        "0.17.4/bio/cutadapt/pe"
        
rule cutadapt:
    input:
        get_fq
    output:
        fastq="results_dna/trimmed_se/{sample}-{unit}-{condition}.fastq.gz",
        qc="results_dna/trimmed_se/{sample}-{unit}-{condition}.qc.txt"
    log:
        "logs/cutadapt/{sample}-{unit}-{condition}.log"
    params: config["params"]["cutadapt"]
    threads: config["threads"]
    wrapper:
        "0.17.4/bio/cutadapt/se"