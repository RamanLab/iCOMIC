

rule mark_duplicates:
    input:
        "results_dna/mapped/{sample}-{unit}.sorted.bam"
    output:
        bam="results_dna/dedup/{sample}-{unit}.bam",
        metrics="results_dna/qc/dedup/{sample}-{unit}.metrics.txt"
    log:
        "logs/picard/dedup/{sample}-{unit}.log"
    params:
        "{}".format(config["params"]["picard"]["MarkDuplicates"])
    wrapper:
        "0.26.1/bio/picard/markduplicates"
        
rule recalibrate_base_qualities:
    input:
        bam=get_recal_input(),
        bai=get_recal_input(bai=True),
        ref=config["ref"]["genome"],
        known=config["ref"]["known-variants"]
    output:
        bam=protected("results_dna/recal/{sample}-{unit}.bam")
    params:
        extra="{}".format(config["params"]["GATK_HC"]["BaseRecalibrator"])
    log:
        "logs/gatk/bqsr/{sample}-{unit}.log"
    wrapper:
        "0.27.1/bio/gatk/baserecalibrator"