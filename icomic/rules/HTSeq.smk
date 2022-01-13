rule HTSeq:
    input:
        bam = "results/aligner_results/{sample}_{condition}_Rep{rep}.bam"
    output:
        R1 = "results/em_results/{sample}_{condition}_Rep{rep}.counts"
    message:
        "------HTSeq running....wait.."
    params:
        gtf= config['ref']['annotation']
#        extra=config['params']['HTSeq']
#    threads: config["threads"]
    log:
        "logs_rna/HTSeq/{sample}_{condition}_Rep{rep}.log"
    shell:
        "htseq-count -t exon -i gene_id -f bam {input.bam} {params.gtf} > {output.R1}"
rule table:
    input:
        expand("results/em_results/{sample}_{condition}_Rep{rep}.counts", sample=samples, condition=type, rep=reps)
    output:
        "results/em_results/emtable.tsv"
    shell:
        "./deseq_tsv.py"