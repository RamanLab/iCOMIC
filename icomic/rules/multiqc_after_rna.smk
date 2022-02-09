rule multiqc:
    input:
        get_fastq_data(path = "results/cutadapt/fastqc_after/")
    output:
        "results/cutadapt/fastqc_after/multiqc_after.html"
    params:
        dir= "results/cutadapt/fastqc_after/",
        name= "multiqc.html"
    log:
        "logs/fastqc_after/multiqc.log"
    shell:
        "multiqc --force {input} -o {params.dir} -n {params.name}"