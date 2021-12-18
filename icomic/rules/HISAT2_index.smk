rule hisat2_index:
    input:
        fasta = config["ref"] ["fasta"]
    output:
        directory("results/index/HISAT2")
    params:
        prefix = "results/index/HISAT2/"
#        extra = ""
    log:
        "logs_rna/HISAT2_index.log"
    
    threads: config["threads"]
    wrapper:
        "0.35.0/bio/hisat2/index"