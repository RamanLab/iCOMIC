rule bowtie2_index:
    input:
        config["ref"]["genome"]
    params:
        basename = "results_dna/index/Bowtie2/" + config['ref']['genome-name']
    output:
        out1 = "results_dna/index/Bowtie2/" + config['ref']['genome-name'] + ".1.bt2",
        out2 = "results_dna/index/Bowtie2/" + config['ref']['genome-name'] + ".2.bt2",
        out3 = "results_dna/index/Bowtie2/" + config['ref']['genome-name'] + ".3.bt2",
        out4 = "results_dna/index/Bowtie2/" + config['ref']['genome-name'] + ".4.bt2",
        out5 = "results_dna/index/Bowtie2/" + config['ref']['genome-name'] + ".rev.1.bt2",
        out6 = "results_dna/index/Bowtie2/" + config['ref']['genome-name'] + ".rev.2.bt2",
    threads: config["threads"]
    conda:
        "../envs/bowtie2.yaml"
    shell:"""
        bowtie2-build --threads {threads} {input} {params.basename}
    """
