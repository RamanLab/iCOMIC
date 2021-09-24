############ Test Rule ###########

rule salmon_deseq2:
    output:
        'results_test/salmon_deseq2_results/salmon_results.Rdata'
    version: shell("R --version")
    #priority: 80
    script:
        "/data/Priyanka/other_pipelines/rna-seq-star-deseq2-master/scripts/salmon-deseq2.R"

