#rule multiqc:
#    input:
#        expand(expand(["results_dna/qc/fastqc/{u.sample}-{u.unit}-{u.condition}.zip"],
#               u=units.itertuples()))
#    output:
#        "multiqc_report.html"
#    wrapper:
#        "0.31.1/bio/multiqc"


        
rule multiqc:
    input:
        get_fastq_data(path = "results_dna/qc/fastqc/")
    output:
        "results_dna/qc/multiqc.html"
    wrapper:
        "0.35.0/bio/multiqc"
#        "0.65.0/bio/multiqc"
#        "0.17.0/bio/multiqc"
#        "0.31.1/bio/multiqc"