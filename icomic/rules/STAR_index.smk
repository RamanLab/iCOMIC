rule star_index:
    input:
        fasta = config["ref"] ["fasta"]
    output:
        directory("results/index/STAR/")
    message:
        "Creating STAR index"
    threads: config["threads"]
    params:
        annotate= config['ref']['annotation']
#        extra=""
    log:
        "logs_rna/STAR_index.log"
    shell:
        "STAR --runMode genomeGenerate --runThreadN {threads} --genomeDir {output} --genomeFastaFiles {input.fasta}"