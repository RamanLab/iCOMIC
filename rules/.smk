#if "restrict-regions" in config["processing"]:
#    rule compose_regions:
#        input:
#            config["processing"]["restrict-regions"]
#        output:
#            "called/{contig}.regions.bed"
#        conda:
#            "../envs/bedops.yaml"
#        shell:
#            "bedextract {wildcards.contig} {input} > {output}"


rule call_variants: 
    input:
        bam=get_sample_bams,
        bai=get_sample_bais,
        ref=config["ref"]["genome"],
        known=config["ref"]["known-variants"],
        regions=config["processing"]["restrict-regions"]
    output:
        gvcf=protected("called/{sample}.{contig}.g.vcf.gz")
    log:
        "logs/gatk/haplotypecaller/{sample}.{contig}.log"
    wrapper:
        "0.27.1/bio/gatk/haplotypecaller"


rule combine_calls:
    input:
        ref=config["ref"]["genome"],
        gvcfs=expand("called/{sample}.{{contig}}.g.vcf.gz", sample=samples.index)
    output:
        gvcf="called/all.{contig}.g.vcf.gz"
    log:
        "logs/gatk/combinegvcfs.{contig}.log"
    wrapper:
        "0.27.1/bio/gatk/combinegvcfs"


rule genotype_variants:
    input:
        ref=config["ref"]["genome"],
        gvcf="called/all.{contig}.g.vcf.gz"
    output:
        vcf=temp("genotyped/all.{contig}.vcf.gz")
    params:
        extra=config["params"]["gatk"]["GenotypeGVCFs"]
    log:
        "logs/gatk/genotypegvcfs.{contig}.log"
    wrapper:
        "0.27.1/bio/gatk/genotypegvcfs"


rule merge_variants:
    input:
        vcf=expand("genotyped/all.{contig}.vcf.gz", contig=contigs)
    output:
        vcf="genotyped/all.vcf.gz"
    log:
        "logs/picard/merge-genotyped.log"
    wrapper:
        "0.27.1/bio/picard/mergevcfs"
