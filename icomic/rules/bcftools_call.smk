        
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
    
        
rule merge_variants:
    input:
        vcf=expand("results_dna/called/{u.sample}-{u.unit}-{u.condition}.vcf", u=units.itertuples())
    output:
        vcf="results_dna/merged/all.vcf.gz"
    log:
        "logs/picard/merge-genotyped.log"
    wrapper:
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

        
    