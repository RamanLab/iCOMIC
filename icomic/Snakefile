include: "rules/common_dna.smk"
rule all:
  input:
    expand("results_dna/mapped/{u.sample}-{u.unit}-{u.condition}.sorted.bam", u = units.itertuples()),
    expand("results_dna/dedup/{u.sample}-{u.unit}-{u.condition}.bam", u = units.itertuples()),
    "results_dna/filtered/all.vcf.gz",
    "results_dna/multiqc/multiqc.html",
    "results_dna/filtered/all.avinput",
    config["ref"]["genome-dict"]+ ".dict",
    config["ref"]["genome"]+ ".fai",
    "results_dna/annotated/all." + config["ref"]["name"] + "_multianno.vcf", 

include: "rules/BWA_MEM.smk" 
include: "rules/Mutect2.smk" 
include: "rules/Annovar.smk" 
