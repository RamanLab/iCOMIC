
rule stringtie:
    input:
        bam = "results/aligner_results/{sample}_{condition}_Rep{rep}.bam"
    output:
        R1 = "results/em_results/{sample}_{condition}_Rep{rep}/{sample}_{condition}_Rep{rep}_transcript.gtf",
        R2 = "results/em_results/{sample}_{condition}_Rep{rep}/{sample}_{condition}_Rep{rep}_gene_abundances.tsv",
        R3 = "results/em_results/{sample}_{condition}_Rep{rep}/{sample}_{condition}_Rep{rep}_cov_ref.gtf"
    params:
        gtf= config['ref']['annotation']
#        extra = config["params"]["StringTie"]
    threads: config["threads"]
    shell:
        "stringtie -G {params.gtf} --rf -e -B -p {threads} -o {output.R1} -A {output.R2} -C {output.R3} --rf {input.bam}"

