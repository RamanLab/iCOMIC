###### Test Rule ######

rule deseq2:
    input: 
        expand("results/em_results/{sample}_{condition}_Rep{rep}/{sample}_{condition}_Rep{rep}.counts", sample=samples, condition=type, rep=reps)
    output: 
        "results/de_results/hcc1395_DESeq2-results-with-normalized.csv",
        "results/de_results/hcc1395_DESeq2_normalized_counts.txt",
        "results/de_results/hcc1395_DESeq2-test-conditions.csv",
        "results/de_results/hcc1395_DESeq2-replaceoutliers.csv",
        "results/de_results/hcc1395_DESeq2-replaceoutliers-results.csv"
        
#    params: 
#        expand("{sample}", sample=samples),
#        expand("{rep}", rep=reps)
    script:
        "../scripts/deseq2.R"

