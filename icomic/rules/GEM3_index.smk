rule gem_index:
    input:
        config["ref"]["genome"]
    output:
        "results_dna/index/GEM3/" + config['ref']['genome-name'] + ".gem"
    params:
        basename = "results_dna/index/GEM3/" + config['ref']['genome-name']
    threads: config["threads"]
    shell:
        "gem-indexer -t {threads} -i {input} -o {params.basename}"
