###### Test Rule ######
rule ballgown:
    input: expand("results/stringtie_counts/{sample}_{condition}_Rep{rep}/{sample}_{condition}_Rep{rep}_transcripts.gtf", sample=samples, condition=type, rep=reps)
    output: "results/ballgown/SigDE.txt"
    params: expand("{sample}", sample=samples),
            expand("{rep}", rep=reps)
    script:
        "/data/Priyanka/other_pipelines/rna-seq-star-deseq2-master/scripts/ballgown.R"
