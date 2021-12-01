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

#rule realignertargetcreator:
#    input:
#        bam=get_recal_input,
#        ref=config["ref"]["genome"],
#        known=config["ref"]["known-variants"]
#    output:
#        "results_dna/realign/{sample}-{unit}-{condition}.intervals"
#    log:
#        "logs/gatk/realignertargetcreator/{sample}-{unit}-{condition}.log"
#    params:
#        extra="",  # optional
#        java_opts="",
#    threads: 1
#    conda:
#        "../envs/gatk.yaml"
#    shell:
#        "gatk3-register -jar /data/anjana//gatk-4.0.2.1/gatk-package-4.0.2.1-local.jar && gatk3 -T RealignerTargetCreator {params.extra} -I {input.bam} -R {input.ref}"
#        " --known {input.known}"
#        " -o {output}"
#        " {log}"
##    wrapper:
##        "bio/gatk3/realignertargetcreator"

#rule indelrealigner:
#    input:
#        bam=get_recal_input,
#        ref=config["ref"]["genome"],
#        known=config["ref"]["known-variants"],
#        target_intervals=get_indelrealign_input
#    output:
#        bam="results_dna/realign/{sample}-{unit}-{condition}.bam"
#    log:
#        "logs/gatk3/indelrealigner/{sample}-{unit}-{condition}.log"
#    params:
#        extra="",  # optional
#        java_opts="", # optional
#    threads: 1
#    conda:
#        "../envs/gatk.yaml"
#    shell:
#        "gatk3 -T IndelRealigner {params.extra} -I {input.bam} -R {input.ref}"
#        " --known {input.known}"
#        "--targetIntervals {input.target_intervals}"
#        " -o {output.bam}"
#        " {log}"
##    wrapper:
##        "bio/gatk/indelrealigner"
        
rule recalibrate_base_qualities:
    input:
        bam=get_recal_input(),
        bai=get_recal_input(bai=True),
        ref=config["ref"]["genome"],
        known=config["ref"]["known-variants"]
    output:
        bam=protected("results_dna/recal/{sample}-{unit}-{condition}.bam")
    params:
        extra = ""
#        extra="{}".format(config["params"]["GATK_HC"]["BaseRecalibrator"])
    log:
        "logs/gatk/bqsr/{sample}-{unit}-{condition}.log"
    wrapper:
        "0.27.1/bio/gatk/baserecalibrator"
        
rule bcftools_call:
    input:
        ref=config["ref"]["genome"],
        samples=get_sample_bams,
        indexes=get_sample_bais
    output:
        # Here, we optionally use a region as wildcard and constrain it to the
        # format accepted by samtools mpileup.
        "results_dna/called/{sample}-{unit}-{condition}.bcf"
    params:
        # Optional parameters for samtools mpileup (except -g, -f).
        # In this example, we forward the region wildcard from the output file to mpileup.
        mpileup=" ",
        # Optional parameters for bcftools call (except -v, -o, -m).
        call="{}".format(config["params"]["bcftools_call"])
    log:
        "logs/bcftools_call/{sample}-{unit}-{condition}.log"
    threads: config["threads"]
    wrapper:
        "0.27.1/bio/bcftools/call"
#    shell:
#        "bcftools mpileup -f {input.ref} {input.samples} | bcftools call -m {params.call} -mv -o {output}  2> {log}" 
    
    
rule bcf_to_vcf:
    input:
        "{prefix}.bcf"
    output:
        "{prefix}.vcf"
    params:
        ""  # optional parameters for bcftools view (except -o)
    log:
        "logs/bcftovcf/{prefix}.log"
    conda:
        "../envs/bcftools.yaml"
    shell: 
        "bcftools view {input} -o {output}"
#    wrapper:
#        "0.66.0/bio/bcftools/view"
#        "0.31.1/bio/bcftools/view"
    
        
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
        

        
rule merge_variants:
    input:
        vcf=expand("results_dna/called/{u.sample}-{u.unit}-{u.condition}.vcf", u=units.itertuples())
#        vcf=expand("results_dna/called/{u.sample}.{u.unit}.vcf", u=units.itertuples())
    output:
        vcf="results_dna/merged/all.vcf.gz"
    log:
        "logs/picard/merge-genotyped.log"
    wrapper:
#        "0.27.1/bio/picard/mergevcfs"
        "0.35.0/bio/picard/mergevcfs"
        
rule filter_vcfs:
    input:
        vcf = "results_dna/merged/all.vcf.gz"
    output:
        vcf= "results_dna/filtered/all.vcf.gz"
    params:
        ""  # optional parameters for bcftools view (except -o)
    conda:
        "../envs/bcftools.yaml"
    shell:
        "bcftools filter -O z -o {output.vcf} -s LOWQUAL -i'%QUAL>20' {input.vcf}"

#def get_vartype_arg(wildcards):
#    return "--select-type-to-include {}".format(
#        "SNP" if wildcards.vartype == "snvs" else "INDEL")


#rule select_calls:
#    input:
#        ref=config["ref"]["genome"],
#        vcf="results_dna/merged/all.vcf.gz"
#    output:
#        vcf=temp("results_dna/filtered/all.{vartype}.vcf.gz")
#    params:
#        extra=get_vartype_arg
#    log:
#        "logs/gatk/selectvariants/{vartype}.log"
#    wrapper:
#        "0.27.1/bio/gatk/selectvariants"


#def get_filter(wildcards):
#    return {
#        "snv-hard-filter":
#        config["filtering"]["hard"][wildcards.vartype]}


#rule hard_filter_calls:
#    input:
#        ref=config["ref"]["genome"],
#        vcf="results_dna/filtered/all.{vartype}.vcf.gz"
#    output:
#        vcf=temp("results_dna/filtered/all.{vartype}.hardfiltered.vcf.gz")
#    params:
#        filters=get_filter
#    log:
#        "logs/gatk/variantfiltration/{vartype}.log"
#    wrapper:
#        "0.27.1/bio/gatk/variantfiltration"


#rule recalibrate_calls:
#    input:
#        vcf="results_dna/filtered/all.{vartype}.vcf.gz"
#    output:
#        vcf=temp("results_dna/filtered/all.{vartype}.recalibrated.vcf.gz")
#    params:
##        extra="{}".format(config["params"]["GATK_HC"]["VariantRecalibrator"])
#    log:
#        "logs/gatk/variantrecalibrator/{vartype}.log"
#    wrapper:
#        "0.27.1/bio/gatk/variantrecalibrator"


#rule merge_calls:
#    input:
#        vcf=expand("results_dna/filtered/all.{vartype}.{filtertype}.vcf.gz",
#                   vartype=["snvs", "indels"],
#                   filtertype="recalibrated"
#                              if config["filtering"]["vqsr"]
#                              else "hardfiltered")
#    output:
#        vcf="results_dna/filtered/all.vcf.gz"
#    log:
#        "logs/picard/merge-filtered.log"
#    wrapper:
#        "0.27.1/bio/picard/mergevcfs" 
        
    