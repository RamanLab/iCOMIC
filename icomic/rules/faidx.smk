rule fasta_index:
    input:
        config["ref"]["genome"]
    output:
        config["ref"]["genome"]+ ".fai",
    wrapper:
        "0.31.1/bio/samtools/faidx"

rule create_dict:
    input:
        config["ref"]["genome"]
    output:
        config["ref"]["genome"].split('.')[0] + '.dict'
    log:
        "logs/picard/create_dict.log"
    params:
        extra=""  # optional: extra arguments for picard.
    wrapper:
        "0.31.1/bio/picard/createsequencedictionary"
    