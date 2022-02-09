rule multiqc:
    input:
        get_fastq_data(path = "results_dna/qc/fastqc/")
    output:
        "results_dna/qc/multiqc.html"
    params:
        dir= "results_dna/qc/fastqc/",
        name= "multiqc.html"
    log:
        "logs/qc/fastqc/multiqc.log"
    shell:
        "multiqc --force {input} -o {params.dir} -n {params.name}"