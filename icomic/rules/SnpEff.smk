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
        extra=config["params"]["SnpEff"]
    wrapper:
        "0.27.1/bio/snpeff"
        

