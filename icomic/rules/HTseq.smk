#def get_bams(wildcards):
##    "get input files from the respective tools"
#    if os.path.exists("results/aligner_results/hisat2"):
#        return "results/aligner_results/hisat2/{sample}_{condition}_Rep{rep}.bam"
#    else:
#        return "results/aligner_results/star/{sample}_{condition}_Rep{rep}/Aligned.sortedByCoord.out.bam"
rule HTSeq:
    input:
#        bam = "results/aligner_results/star/{sample}_{condition}_Rep{rep}/Aligned.sortedByCoord.out.bam"
        bam = "results/aligner_results/{sample}_{condition}_Rep{rep}.bam"
#        bam = get_bams
    output:
#        R1 = "results/em_results/{sample}_{condition}_Rep{rep}/{sample}_{condition}_Rep{rep}.counts"
        R1 = "results/em_results/{sample}_{condition}_Rep{rep}.counts"
    message:
        "------HTSeq running....wait.."
    params:
        gtf= config['ref']['annotation']
#    threads: config["threads"]
    log:
        "logs_rna/HTseq/{sample}_{condition}_Rep{rep}.log"
    shell:
        "htseq-count -s no -r pos -t exon -i gene_id -f bam {input.bam} {params.gtf} > {output.R1}" 
#        "htseq-count -s reverse -r pos -a 10 -m union -f bam {input.bam} {params.gtf}  > {output.R1}"
#        "/data/Priyanka/softwares/htseq-release_0.11.0/build/scripts-3.6/htseq-count -s no -r pos -t exon -i gene_id -f bam {input.bam} {params.gtf} > {output.R1}"
#        "htseq-count -s no -r pos -f bam {input.bam} {params.gtf}  > {output.R1}"

rule table:
    input:
        expand("results/em_results/{sample}_{condition}_Rep{rep}.counts", sample=samples, condition=type, rep=reps)
    output:
        "results/em_results/emtable.tsv"
    shell:
        "./deseq_tsv.py"