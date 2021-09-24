rule fastqc_after:
    input:
        get_trimmed
    output:
        html= "results_dna/qc/fastqc/{sample}-{unit}.aftertrim.html",
        zip="results_dna/qc/fastqc/{sample}-{unit}.aftertrim.zip"
    log:
        "logs/fastqc/{sample}-{unit}.aftertrim.log"
    wrapper:
        "0.31.1/bio/fastqc"
        
#rule multiqc:
#    input:
#        expand(["qc/samtools-stats/{u.sample}-{u.unit}.txt",
#               "qc/fastqc/{u.sample}-{u.unit}.zip",
#               "qc/fastqc/{u.sample}-{u.unit}.aftertrim.zip"],
#               u=units.itertuples()),
#    output:
#        report("qc/multiqc.html", caption="../report/multiqc.rst", category="Quality control")
#    log:
#        "logs/multiqc.log"
#    wrapper:
#        "0.27.1/bio/multiqc"
