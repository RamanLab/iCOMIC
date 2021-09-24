###### Test Rule ######
rule ballgown:
    input: expand("results/em_results/{sample}_{condition}_Rep{rep}/{sample}_{condition}_Rep{rep}_transcript.gtf", sample=samples, condition=type, rep=reps)
    output: "results/de_results/SigDE.txt"
    params: expand("{sample}", sample=samples),
            expand("{rep}", rep=reps)
    script:
        "../scripts/ballgown.R"
