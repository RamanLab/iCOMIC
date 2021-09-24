rule fasta_index:
    input:
        config["ref"]["genome"]
    output:
        config["ref"]["genome"]+ ".fai",
    wrapper:
        "0.31.1/bio/samtools/faidx"
#        dict = config["ref"]["genome"].split('.')[0] + '.dict'
#    shell:
#        "samtools faidx {input} > {output.fai} &&  java -jar /data/anjana/./picard/picard.jar CreateSequenceDictionary R={input} O={output.dict}"

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
    