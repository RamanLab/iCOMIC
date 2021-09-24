rule hisat2_index:
    input:
        fasta = config["ref"] ["fasta"]
    output:
        directory("results/index/hisat2")
    params:
        prefix = "results/index/hisat2/"
    log:
        "logs/hisat2_index.log"
    threads: 2
    wrapper:
        "0.36.0/bio/hisat2/index"