rule multiqc:
    input:
        get_fastq_data(path = "results_dna/trimmed/fastqc_after/")
    output:
        "results_dna/qc/multiqc_after.html"
    params:
        dir= "results_dna/qc/",
        name= "multiqc.html"
    log:
        "logs/qc/fastqc_after/multiqc.log"
    shell:
        "multiqc --force {input} -o {params.dir} -n {params.name}"