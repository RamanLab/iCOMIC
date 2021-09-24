rule mutect2_call:
    input:
        ref=config["ref"]["genome"],
        # you can have a list of samples here
        tumor=get_sample_bams_tumor,
        normal=get_sample_bams_normal,
        bai = get_sample_bais
    output:
        vcf="results_dna/called/{sample}-{unit}.vcf"  # either .vcf or .bcf
    log:
        "logs_new/mutect2/{sample}-{unit}.log",
    params:
        tumor_id = get_sample_id_tumor,
        normal_id=get_sample_id_normal             
#        extra="{}".format(config["params"]["mutect2"]),         # optional parameters
#        chunksize=100000  # reference genome chunk size for parallelization (default: 100000)
#    threads: 2
    shell:
        "java -jar ./gatk-4.0.2.1/gatk-package-4.0.2.1-local.jar Mutect2 -R {input.ref} -I {input.tumor} -I {input.normal} -tumor {params.tumor_id} -normal {params.normal_id} -O {output.vcf}"
         
def get_vcfs(wildcards):
    """Get all aligned normal reads of given sample."""
    return expand("results_dna/called/{sample}-{unit}.vcf.gz",
                  sample=wildcards.sample,
                  unit=wildcards.unit)         

rule bcftools_merge:
    input:
        calls=expand("results_dna/called/{u.sample}-{u.unit}.vcf.gz", u=units.itertuples())
#        index=expand("results_dna/called/{sample}.{contig}.vcf.gz", sample=samples.index, contig=contigs) 
    output:
        "results_dna/filtered/all.vcf"
    params:
        ""  # optional parameters for bcftools concat (except -o)
    shell:
        "bcftools merge --force-samples {input.calls} {params} -Ov -o {output[0]} "
          
        
rule bgzip:
    input:
        "{prefix}.vcf"
    output:
        "{prefix}.vcf.gz"
    shell:
        "bgzip -c {input} > {output} && tabix -p vcf {output} "  