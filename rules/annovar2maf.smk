rule annovar2maf:
    input: 
        "results_dna/annotated/all." + config["ref"]["name"] + "_multianno.txt"                
    output: 
        "results_dna/variants.maf"
    params: 
        "results_dna/annotated/all." + config["ref"]["name"] + "_multianno.txt",
        config["ref"]["name"]
    script:
        "../scripts/vcf2maf.R"