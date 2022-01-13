
rule deseq2:
    input: 
        expand("results/em_results/{sample}_{condition}_Rep{rep}.counts", sample=samples, condition=type, rep=reps)
    output: 
        "results/de_results/DESeq2_normalized_counts.txt", 
    params: expand("{sample}", sample=samples),
            expand("{rep}", rep=reps)
#            extra=config['params']['DESeq2']
#            expand("{condition}", condition=type)
    script:
        "../scripts/deseq2.R"

