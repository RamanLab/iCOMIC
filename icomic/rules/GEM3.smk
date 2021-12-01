
#def gem3_cmd():
#    n = len(snakemake.input.sample)
#    assert n == 1 or n == 2, "input->sample must have 1 (single-end) or 2 (paired-end) elements."
#    if n == 1:
#        return(("gem-mapper -I {params.index} -i {input.sample} -q offset-64 -o {output} -m 3 -e 0 -s 0"))
#    else:
#        return(("gem-mapper -I {params.index} -i {input.sample} -q offset-64 -o {output} -m 3 -e 0 -s 0 -p -E 0.30"))

rule gem3:
    input:
        sample=get_fastq
    output:
        "results_dna/mapped/{sample}-{unit}-{condition}.bam"
    params:
        index= config['index']['GEM3'],
        extra=get_read_group_gem3
    threads: config["threads"]
    log:
        "logs/gem3/{sample}-{unit}-{condition}.log"
    run:
        n = len(input.sample)
        assert n == 1 or n == 2, "input->sample must have 1 (single-end) or 2 (paired-end) elements."
        if n == 1:
            reads = "-i {}".format(*input.sample)
        else:
            reads = "-1 {} -2 {}".format(*input.sample)

        shell("gem-mapper {params.extra} -t {threads} -I {params.index} {reads} -o {output} 2> {log}")

rule samtools_sort:
    input:
        "results_dna/mapped/{sample}-{unit}-{condition}.bam"
    output:
        "results_dna/mapped/{sample}-{unit}-{condition}.sorted.bam"
    params:
        "-m 4G"
    wrapper:
        "0.36.0/bio/samtools/sort"
        
rule mark_duplicates:
    input:
        "results_dna/mapped/{sample}-{unit}-{condition}.sorted.bam"
    output:
        bam="results_dna/dedup/{sample}-{unit}-{condition}.bam",
        metrics="results_dna/qc/dedup/{sample}-{unit}-{condition}.metrics.txt"
    log:
        "logs/picard/dedup/{sample}-{unit}-{condition}.log"
    params:
        config["params"]["picard"]["MarkDuplicates"]
    wrapper:
        "0.36.0/bio/picard/markduplicates"


rule samtools_index:
    input:
        "{prefix}.bam"
    output:
        "{prefix}.bam.bai"
    wrapper:
#        "0.27.1/bio/samtools/index"
        "0.35.0/bio/samtools/index"

rule samtools_stats:
    input:
        "results_dna/mapped/{sample}-{unit}-{condition}.sorted.bam"
    output:
        "results_dna/qc/samtools-stats/{sample}-{unit}-{condition}.txt"
    log:
        "logs/samtools-stats/{sample}-{unit}-{condition}.log"
    wrapper:
#        "0.27.1/bio/samtools/stats"
        "0.38.0/bio/samtools/stats"

rule replace_rg:
    input:
        "results_dna/dedup/{sample}-{unit}-{condition}.bam"
    output:
        "results_dna/dedup_rgadded/{sample}-{unit}-{condition}.bam"
    log:
        "logs/picard/replace_rg/{sample}-{unit}-{condition}.log"
    params:
        "VALIDATION_STRINGENCY=SILENT SO=coordinate RGLB=lib1 RGPL=illumina RGPU={sample}-{unit}-{condition} RGSM={sample}-{unit}-{condition}"
#        "VALIDATION_STRINGENCY=SILENT SO=coordinate RGLB=lib1 RGPL=illumina RGPU={sample}-{unit}-{condition} RGSM={sample}-{unit}-{condition}"
    wrapper:
        "0.35.0/bio/picard/addorreplacereadgroups"

rule bcf_stat:
    input:
        "results_dna/filtered/all.vcf.gz"
    output:
        "results_dna/bcftools_stats/all.txt"
    shell:
        "bcftools stats {input} > {output}"

rule multiqc:
    input:
        expand(["results_dna/qc/samtools-stats/{u.sample}-{u.unit}-{u.condition}.txt",
                "results_dna/qc/dedup/{u.sample}-{u.unit}-{u.condition}.metrics.txt"],
               u=units.itertuples()),
        "results_dna/bcftools_stats/all.txt",
        get_multiqc_data(),
#        get_fastq_data(path = "results_dna/qc/fastqc/")
    output:
        report("results_dna/multiqc/multiqc.html", caption="../report/multiqc.rst", category="Quality control")
    log:
        "logs/multiqc.log"
#    conda:
#        "../envs/multiqc.yaml"
#    shell:
#        "multiqc --force -o os.path.dirname({output[0]}) -n os.path.basename({output[0]}) set(os.path.dirname{input} {log}"
    wrapper:
        "0.35.0/bio/multiqc"
#        "0.31.1/bio/multiqc"
#        "0.65.0/bio/multiqc"
#        "0.17.0/bio/multiqc"
#        "0.27.1/bio/multiqc"
        

#rule gem3_pe:
#    input:
#        sample=expand("trimmed/{sample}-{unit}.{group}.fastq.gz", group=[1, 2], sample = samples.index, unit=units.index)
#    output:
#        "gem3/mapped/{sample}-{unit}.sorted.bam"
#    params:
#        index= "gem3/index"
#    shell:
#        "gem-mapper -I {params.index} -i {input.sample} -q offset-64 -o {output} -m 3 -e 0 -s 0 -p -E 0.30"
