rule freebayes:
    input:
        ref=config["ref"]["genome"],
        # you can have a list of samples here
        samples=get_sample_bams
    output:
        "results_dna/called/{sample}.{contig}.vcf"  # either .vcf or .bcf
    log:
        "logs/freebayes/{sample}.{{contig}}.log"
    params:
        extra="{}".format(config["params"]["freebayes"]),         # optional parameters
        chunksize=100000  # reference genome chunk size for parallelization (default: 100000)
#    threads: 2
    wrapper:
        "0.36.0/bio/freebayes"
    
rule bcftools_merge:
    input:
        calls=expand("results_dna/called/{sample}.{contig}.vcf.gz", sample=samples.index, contig=contigs),
#        index=expand("results_dna/called/{sample}.{contig}.vcf.gz", sample=samples.index, contig=contigs) 
    output:
        "results_dna/filtered/all.vcf"
    params:
        ""  # optional parameters for bcftools concat (except -o)
    wrapper:
        "0.37.1/bio/bcftools/concat"
#    shell:
#        "bcftools merge {params} -Ov -o {output[0]} "
#        "{input.calls}"  
        
rule bgzip:
    input:
        "{prefix}.vcf"
    output:
        "{prefix}.vcf.gz"
    shell:
        "bgzip -c {input} > {output} && tabix -p vcf {output} "       
