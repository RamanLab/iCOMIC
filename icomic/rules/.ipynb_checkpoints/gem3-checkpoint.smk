rule gem_index:
    input:
        config["ref"]["genome"]
    output:
        "gem3/index/genome.gem"
    params:
        extra = "--sampling-rate 16"
    shell:
        "gem-indexer -i {input} {params.extra} -o {output}"