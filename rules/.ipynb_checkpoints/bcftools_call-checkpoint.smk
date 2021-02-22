#rule samtools_index:
#    input:
#        "{prefix}.sorted.bam"
#    output:
#        "{prefix}.sorted.bam.bai"
#    wrapper:
#        "0.27.1/bio/samtools/index"

#rule samtools_sort:
#    input:
#        "{prefix}.bam"
#    output:
#        "{prefix}.sorted.bam"
#    params:
#        "-m 4G"
#    threads: 8
#    wrapper:
#        "0.27.1/bio/samtools/sort"
        
rule bcftools_call:
    input:
        ref=config["ref"]["genome"],
        samples=get_sample_bams,
        indexes=get_sample_bais
    output:
        # Here, we optionally use a region as wildcard and constrain it to the
        # format accepted by samtools mpileup.
        "results_dna/called/{sample}.{contig}.bcf"
    params:
        # Optional parameters for samtools mpileup (except -g, -f).
        # In this example, we forward the region wildcard from the output file to mpileup.
        #mpileup="--region {contig}",
        # Optional parameters for bcftools call (except -v, -o, -m).
        call="{}".format(config["params"]["bcftools_call"])
    log:
        "logs/bcftools_call/{sample}.{{contig}}.log"
#    wrapper:
#        "0.27.1/bio/bcftools/call"
    shell:
        "bcftools mpileup -f {input.ref} {input.samples} | bcftools call -m {params.call} -mv -o {output}  2> {log}" 
    
    
#rule bcf_to_vcf:
#    input:
#        "{prefix}.bcf"
#    output:
#        "{prefix}.vcf"
#    params:
        ""  # optional parameters for bcftools view (except -o)
 #    wrapper:
 #        "0.31.1/bio/bcftools/view"
#    shell:
#        "bcftools view {input} -o {output} "
        
#rule bgzip:
#    input:
#        "{prefix}.vcf"
#    output:
#        "{prefix}.vcf.gz"
#    shell:
#        "bgzip -c {input} > {output} && tabix -f -p vcf {output}"
        
 #rule tabix:
 #    input:
 #        "{prefix}.vcf.gz"
 #    output:
 #        "{prefix.vcf.gz.tbi}"
 #    shell:
 #        "tabix -p vcf {input} -o {output}"
        

        
#rule bcftools_merge:
#    input:
#        calls=expand("called/{sample}.{contig}.vcf.gz", sample=samples.index, contig=contigs),
 #        index=expand("called/{sample}.{contig}.vcf.gz.tbi", sample=samples.index, contig=contigs) 
#    output:
#        "filtered/all.vcf.gz"
#    params:
#        ""  # optional parameters for bcftools concat (except -o)
 #    wrapper:
 #       "0.27.1/bio/bcftools/merge"    
#    shell:
#        "bcftools merge {input.calls} {params} -o {output}"
        
rule bcftools_merge:
    input:
        calls=expand("results_dna/called/{sample}.{contig}.bcf.gz", sample=samples.index, contig=contigs),
#        index=expand("results_dna/called/{sample}.{contig}.vcf.gz", sample=samples.index, contig=contigs) 
    output:
        "results_dna/filtered/all.vcf"
    params:
        ""  # optional parameters for bcftools concat (except -o)
    shell:
        "bcftools merge {params} -Ov -o {output[0]} "
        "{input.calls}"

rule bgzip:
    input:
        "{prefix}.bcf"
    output:
        "{prefix}.bcf.gz"
    shell:
        "bgzip -c {input} > {output} && tabix -f -p bcf {output}"        

#rule bgunzip:
#    input:
#        "filtered/all.bcf.gz"
#    output:
#        "filtered/all.bcf"
#    shell:
#        "bgzip -b {input} > {output}"

#rule bcf_to_vcf:
#    input:
#        "filtered/all.bcf"
#    output:
#        "filtered/all.vcf"
#    wrapper:
#        "0.31.1/bio/bcftools/view"
