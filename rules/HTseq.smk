rule HTSeq:
    input:
        bam = "results/aligner_results/{sample}_{condition}_Rep{rep}/Aligned.sortedByCoord.out.bam"
    output:
        R1 = "results/em_results/{sample}_{condition}_Rep{rep}/{sample}_{condition}_Rep{rep}.counts"
    message:
        "------HTSeq running....wait.."
    params:
        gtf= config['ref']['annotation']
    threads: 40
    shell:
        "htseq-count -s no -r pos -t exon -i gene_id -f bam {input.bam} {params.gtf} > {output.R1}" 
