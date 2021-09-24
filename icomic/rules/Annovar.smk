#rule target:
#    input:
#        "results/all.vcf.gz"

#rule unzip:
#    input:
#        "results_dna/filtered/all.vcf.gz"
#    output:
#        "filtered/all.vcf"
#    shell:
#        "bgzip -b {input}"


rule prepare_input_file:
    input:
        "results_dna/filtered/all.vcf.gz"
    output:
        "results_dna/filtered/all.avinput"
    shell:
        "perl ./annovar/convert2annovar.pl -format vcf4 {input} > {output} -allsample -withfreq -include"
#        "perl ./annovar/convert2annovar.pl {input} -format vcf4 > {output}"
        

#        "results_dna/annotated/all.vcf.variant_function",
#        "results_dna/annotated/all.vcf.exonic_variant_function"
#        prefix = "results_dna/annotated/all",
rule annovar:
    input:
        "results_dna/filtered/all.vcf.gz",
    output:
        vcf="results_dna/annotated/all." + config["ref"]["name"] + "_multianno.vcf"
    params:
        prefix="results_dna/annotated/all",
        name=config["ref"]["name"]
    log:
        "logs/annovar.log"
    shell:
        "perl ./annovar/annotate_variation.pl -buildver {params.name} -downdb -webfrom annovar refGene humandb/ && perl ./annovar/annotate_variation.pl -buildver {params.name} -downdb cytoBand humandb/ && perl ./annovar/annotate_variation.pl -buildver {params.name} -downdb -webfrom annovar exac03 humandb/ && perl ./annovar/annotate_variation.pl -buildver {params.name} -downdb -webfrom annovar avsnp147 humandb/ && perl ./annovar/annotate_variation.pl -buildver {params.name} -downdb -webfrom annovar dbnsfp30a humandb/ && perl ./annovar/table_annovar.pl {input} humandb/ -buildver {params.name} -out myanno -remove -protocol refGene,cytoBand,exac03,avsnp147,dbnsfp30a -operation g,r,f,f,f -nastring . -vcfinput -polish --outfile {params.prefix} "
#        "perl ./annovar/annotate_variation.pl -downdb -buildver hg19 refGene filtered/ && perl ./annovar/annotate_variation.pl --buildver hg19 --downdb seq filtered/hg19_seq && perl ./annovar/retrieve_seq_from_fasta.pl filtered/hg19_refGene.txt -seqdir filtered/hg19_seq -format refGene -outfile filtered/hg19_refGeneMrna.fa && perl ./annovar/annotate_variation.pl {input} -dbtype refGene -buildver hg19 filtered/ -out results_dna/annotated/all.vcf"
        
#rule zip:
#    input:
#        "annotated/all.vcf.variant_function"
#    output:
#        "annotated/all.vcf.variant_function.gz"
#    shell:
#        "gzip {input}" 
        
#rule vcf_to_tsv:
#    input:
#        "annotated/all.vcf.variant_function.gz"
#    output:
#        report("tables/calls.tsv.gz", caption="../report/calls.rst", category="Calls")
#    conda:
#        "../envs/rbt.yaml"
#    shell:
#        "bcftools view --apply-filters PASS --output-type u {input} | "
#        "rbt vcf-to-txt -g --fmt DP AD --info ANN | "
#        "gzip > {output}"


#rule plot_stats:
#    input:
#        "tables/calls.tsv.gz"
#    output:
#        depths=report("plots/depths.svg", caption="../report/depths.rst", category="Plots"),
#        freqs=report("plots/allele-freqs.svg", caption="../report/freqs.rst", category="Plots")
#    conda:
#        "../envs/stats.yaml"
#    script:
#        "../scripts/plot-depths.py"
