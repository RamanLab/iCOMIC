###### Test Rule ######

rule deseq2:
    input: 
        expand("results/em_results/{sample}_{condition}_Rep{rep}.counts", sample=samples, condition=type, rep=reps)
    output: 
        "results/de_results/DESeq2_normalized_counts.txt", 
#        "results/de_results/hcc1395-results-with-normalized.csv", 
#        "results/de_results/hcc1395-test-conditions.csv",
#        "results/de_results/hcc1395-replaceoutliers.csv",
#        "results/de_results/hcc1395-replaceoutliers-results.csv"
    params: expand("{sample}", sample=samples),
            expand("{rep}", rep=reps)
#            expand("{condition}", condition=type)
    script:
        "../scripts/deseq2.R"

