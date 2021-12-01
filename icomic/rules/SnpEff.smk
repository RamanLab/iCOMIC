rule snpeff:
    input:
        "results_dna/filtered/all.vcf.gz",
    output:
        vcf=report("results_dna/annotated/all.vcf", caption="../report/vcf.rst", category="Calls"),
        csvstats="results_dna/snpeff/all.csv"
    log:
        "logs/snpeff.log"
    params:
        reference="{}".format(config["ref"]["name"]),
#        reference=config["ref"]["genome"],
        extra=config["params"]["SnpEff"]
    wrapper:
        "0.27.1/bio/snpeff"
#        "0.35.0/bio/snpeff"
#        "0.27.0/bio/snpeff"
        
#rule vcf_to_tsv:
#    input:
#        "results_dna/annotated/all.vcf"
#    output:
#        report("tables/calls_new.tsv.gz", caption="../report/calls.rst", category="Calls")
#    shell:
#        "bcftools view --apply-filters PASS --output-type u {input} | rbt vcf-to-txt -g --fmt DP AD --info ANN | gzip > {output}"


#rule plot_stats:
#    input:
#        "tables/calls_new.tsv.gz"
#    output:
#        depths=report("plots/depths.svg", caption="../report/depths.rst", category="Plots"),
#        freqs=report("plots/allele-freqs.svg", caption="../report/freqs.rst", category="Plots")
#    conda:
#        "../envs/stats.yaml"
#    script:
#        "../scripts/plot-depths.py"


