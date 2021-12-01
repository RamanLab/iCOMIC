rule star_index:
    input:
        fasta = config["ref"] ["fasta"]
    output:
        directory("results/index/star/")
#        directory = "results/index/star"
    message:
        "Creating STAR index"
    threads: config["threads"]
    params:
        annotate= config['ref']['annotation']
#        extra=""
    log:
        "logs_rna/star_index.log"
#    wrapper:
#        "0.65.0/bio/star/index"
    shell:
        "/home/priyanka/miniconda3/envs/snakemake/bin/STAR --runMode genomeGenerate --runThreadN {threads} --genomeDir {output} --genomeFastaFiles {input.fasta}"
#        "/data/Priyanka/softwares/STAR-2.7.5c/bin/Linux_x86_64/STAR --runMode genomeGenerate --runThreadN {threads} --genomeSAindexNbases 11 --genomeDir {output} --genomeFastaFiles {input.fasta} --sjdbGTFfile {params.annotate} --sjdbOverhang 75"