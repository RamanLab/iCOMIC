rule snpeff:
    input:
        "results_dna/filtered/all.vcf",
    output:
        vcf=report("results_dna/annotated/all.vcf.gz", caption="../report/vcf.rst", category="Calls"),
        csvstats="results_dna/snpeff/all.csv"
    log:
        "logs/snpeff.log"
    params:
        reference="{}".format(config["ref"]["name"]),
        extra="{}".format(config["params"]["SnpEff"])
    wrapper:
        "0.32.0/bio/snpeff"


