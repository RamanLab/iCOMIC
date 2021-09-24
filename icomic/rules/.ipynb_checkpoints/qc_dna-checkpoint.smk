rule fastqc:
    input:
        unpack(get_fastq)
    output:
        html="results_dna_new/qc/fastqc/{sample}-{unit}-{condition}.html",
        zip="results_dna_new/qc/fastqc/{sample}-{unit}-{condition}.zip"
    log:
        "logs/fastqc_new/{sample}-{unit}-{condition}.log"
    wrapper:
        "0.31.1/bio/fastqc"
        

#rule samtools_stats:
#    input:
#        "mapped/{sample}-{unit}.sorted.bam"
#    output:
#        "qc/samtools-stats/{sample}-{unit}.txt"
#    log:
#        "logs/samtools-stats/{sample}-{unit}.log"
#    wrapper:
#        "0.27.1/bio/samtools/stats"


