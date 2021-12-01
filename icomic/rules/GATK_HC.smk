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

rule faidx:
    input:
        config["ref"]["genome"]
    output:
        config["ref"]["genome"]+".fai"
    params:
        "" # optional params string
    conda:
        "../envs/samtools.yaml"
    shell:
        "samtools faidx  {input} > {output}"
#    wrapper:
#        "0.35.0/bio/samtools/faidx"
        
rule create_dict:
    input:
        config["ref"]["genome"]
    output:
        config["ref"]["genome-dict"]+ ".dict"
    log:
        "logs/picard/create_dict.log"
    params:
        extra=""  # optional: extra arguments for picard.
    conda:
        "../envs/picard.yaml"
    shell:
        "picard CreateSequenceDictionary R={input} O={output}"
#    wrapper:
#        "0.63.0/bio/picard/createsequencedictionary"

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
        
rule tabix:
    input:
        config["ref"]["known-variants"]
    output:
        config["ref"]["known-variants"]+".tbi"
    params:
        # pass arguments to tabix (e.g. index a vcf)
        "-p vcf"
    conda:
        "../envs/tabix.yaml"
    log:
        "logs/tabix/tabix.log"
    shell:
        "tabix -f -p vcf {input} > {output}"
        
rule recalibrate_base_qualities:
    input:
        bam=get_recal_input_rgadded(),
        bai=config["ref"]["known-variants"]+".tbi",
#        bai=get_recal_input(bai=True),
        ref=config["ref"]["genome"],
        known=config["ref"]["known-variants"]
    output:
        bam=protected("results_dna/recal/{sample}-{unit}-{condition}.bam")
    params:
        extra = "",
#        index=config["ref"]["genome-dict"]+ ".dict"
#        extra="{}".format(config["params"]["GATK_HC"]["BaseRecalibrator"])
    log:
        "logs/gatk/bqsr/{sample}-{unit}-{condition}.log"
    wrapper:
        "0.27.1/bio/gatk/baserecalibrator"
#        "0.35.0/bio/gatk/baserecalibrator"
#        "0.79.0/bio/gatk/baserecalibrator"
#rule recalibrate_base_qualities_vqsr:
#    input:
#        bam=get_recal_input(),
#        bai=get_recal_input(bai=True),
#        ref=config["ref"]["genome"],
#        known=config["ref"]["known-variants"]
#    output:
#        recal_table="results_dna/recal/{sample}-{unit}-{condition}.grp"
##        bam=protected("results_dna/recal/{sample}-{unit}-{condition}.bam")
#    params:
#        extra = ""
##        extra="{}".format(config["params"]["GATK_HC"]["BaseRecalibrator"])
#    log:
#        "logs/gatk/bqsr/{sample}-{unit}-{condition}.log"
#    wrapper:
#        "0.60.0/bio/gatk/baserecalibrator"
        
#rule gatk_applybqsr:
#    input:
#        bam=get_recal_input(),
#        ref=config["ref"]["genome"],
#        dict=config["ref"]["genome-dict"]+ ".dict",
#        recal_table="results_dna/recal/{sample}-{unit}-{condition}.grp"
#    output:
#        bam="results_dna/recal/{sample}-{unit}-{condition}.bam"
#    log:
#        "logs/gatk/gatk_applybqsr/{sample}-{unit}-{condition}.log"
#    params:
#        extra="",  # optional
#        java_opts="", # optional
#    wrapper:
#        "0.63.0/bio/gatk/applybqsr"
        



rule call_variants: 
    input:
        bam=get_sample_bams_a,
        bai=config["ref"]["genome"]+ ".fai",
        ref=config["ref"]["genome"],
#        known=config["ref"]["known-variants"],
        regions=[]
    output:
        gvcf=protected("results_dna/called/{sample}-{unit}-{condition}.g.vcf.gz")
    log:
        "logs/gatk/haplotypecaller/{sample}-{unit}-{condition}.log"
    params:
#        extra = "",
        extra="{} ".format(config["params"]["GATK_HC"]),
        java_opts="-Xmx4g"
#        extra="{}".format(config["params"]["GATK_HC"]["HaplotypeCaller"])
    wrapper:
        "0.35.0/bio/gatk/haplotypecaller"


rule combine_calls:
    input:
        ref=config["ref"]["genome"],
        gvcfs=expand("results_dna/called/{u.sample}-{u.unit}-{u.condition}.g.vcf.gz", u=units.itertuples())
    output:
        gvcf="results_dna/called/all.{unit}.g.vcf.gz"
    log:
        "logs/gatk/combinegvcfs.{unit}.log"
    wrapper:
        "0.27.1/bio/gatk/combinegvcfs"


rule genotype_variants:
    input:
        ref=config["ref"]["genome"],
        gvcf="results_dna/called/all.{unit}.g.vcf.gz"
    output:
        vcf="results_dna/genotyped/all.{unit}.vcf.gz"
    params:
        extra = ""
#        extra=config["params"]["GATK_HC"]["GenotypeGVCFs"]
    log:
        "logs/gatk/genotypegvcfs.{unit}.log"
    wrapper:
        "0.27.1/bio/gatk/genotypegvcfs"


rule merge_variants:
    input:
        vcf=expand("results_dna/genotyped/all.{u.unit}.vcf.gz", u=units.itertuples())
    output:
        vcf="results_dna/genotyped/all.vcf.gz"
    log:
        "logs/picard/merge-genotyped.log"
    wrapper:
        "0.27.1/bio/picard/mergevcfs"

def get_vartype_arg(wildcards):
    return "--select-type-to-include {}".format(
        "SNP" if wildcards.vartype == "snvs" else "INDEL")


rule select_calls:
    input:
        ref=config["ref"]["genome"],
        vcf="results_dna/genotyped/all.vcf.gz"
    output:
        vcf="results_dna/filtered/all.{vartype}.vcf.gz"
    params:
        extra=get_vartype_arg
    log:
        "logs/gatk/selectvariants/{vartype}.log"
    wrapper:
        "0.27.1/bio/gatk/selectvariants"


def get_filter(wildcards):
    return {
        "snv-hard-filter":
        config["filtering"]["hard"][wildcards.vartype]}


rule hard_filter_calls:
    input:
        ref=config["ref"]["genome"],
        vcf="results_dna/filtered/all.{vartype}.vcf.gz"
    output:
        vcf="results_dna/filtered/all.{vartype}.hardfiltered.vcf.gz"
    params:
        filters=get_filter
    log:
        "logs/gatk/variantfiltration/{vartype}.log"
    wrapper:
        "0.27.1/bio/gatk/variantfiltration"


#rule recalibrate_calls:
#    input:
#        vcf="results_dna/filtered/all.{vartype}.vcf.gz",
#        ref=config["ref"]["genome"]
#    output:
#        vcf="results_dna/filtered/all.{vartype}.recalibrated.vcf.gz",
#        tranches="results_dna/filtered/all.{vartype}.tranches"
#    params:
#        extra = ""
#        extra="{}".format(config["params"]["GATK_HC"]["VariantRecalibrator"])
#        filters=get_filter
#        mode = "BOTH",
#        resources={"hapmap": {"known": False, "training": True, "truth": True, "prior": 15.0},
#                   "omni":   {"known": False, "training": True, "truth": False, "prior": 12.0},
#                   "g1k":   {"known": False, "training": True, "truth": False, "prior": 10.0},
#                   "dbsnp":  {"known": True, "training": False, "truth": False, "prior": 2.0}},
#        annotation=["QD", "FisherStrand"]
#    log:
#        "logs/gatk/variantrecalibrator/{vartype}.log"
#    wrapper:
#        "0.27.1/bio/gatk/variantrecalibrator"


rule merge_calls:
    input:
        vcf=expand("results_dna/filtered/all.{vartype}.{filtertype}.vcf.gz",
                   vartype=["snvs", "indels"],
                   filtertype="recalibrated"
                              if config["filtering"]["vqsr"]
                              else "hardfiltered")
    output:
        vcf="results_dna/filtered/all.vcf.gz"
    log:
        "logs/picard/merge-filtered.log"
    wrapper:
        "0.27.1/bio/picard/mergevcfs"
#        "0.79.0/bio/picard/mergevcfs"
