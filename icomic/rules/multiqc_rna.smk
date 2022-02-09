rule multiqc:
    input:
        get_fastq_data(path = "results/fastqc/")
    output:
        "results/fastqc/multiqc.html"
    params:
        dir= "results/fastqc/",
        name= "multiqc.html"
    log:
        "logs/fastqc/multiqc.log"
    shell:
        "multiqc --force {input} -o {params.dir} -n {params.name}"