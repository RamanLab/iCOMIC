
rule bwa_index:
    input:
        config["ref"]["genome"]
    output:
        "results_dna/index/BWA_MEM/" + config['ref']['genome-name'] + ".amb",
        "results_dna/index/BWA_MEM/" + config['ref']['genome-name'] + ".ann",
        "results_dna/index/BWA_MEM/" + config['ref']['genome-name'] + ".bwt",
        "results_dna/index/BWA_MEM/" + config['ref']['genome-name'] + ".pac",
        "results_dna/index/BWA_MEM/" + config['ref']['genome-name'] + ".sa"
    log:
        "logs/bwa_index/bwa.log"
    params:
        prefix="results_dna/index/BWA_MEM/" + config['ref']['genome-name'],
        algorithm="bwtsw"
    wrapper:
        "0.30.0/bio/bwa/index"
#    wrapper:
#        "samtools faidx {input} > {output}"
#    wrapper:
#        "0.31.1/bio/samtools/faidx"
