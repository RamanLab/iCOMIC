#rule target:
#    input:
#        "results/all.vcf.gz"

#rule unzip:
#    input:
#        "filtered/all.vcf.gz"
#    output:
#        "filtered/all.vcf"
#    shell:
#        "bgzip -b {input}"

rule prepare_input_file:
    input:
        "results_dna/filtered/all.vcf"
    output:
        "results_dna/filtered/all.vcf4"
    shell:
        "perl /data/anjana/annovar/convert2annovar.pl {input} -format vcf4 > {output}"
        
rule annovar:
    input:
        "results_dna/filtered/all.vcf4"
    output:
        "results_dna/annotated/all.vcf.variant_function",
        "results_dna/annotated/all.vcf.exonic_variant_function"
    log:
        "logs/annovar.log"
    shell:
        "perl /data/anjana/annovar/annotate_variation.pl -downdb -buildver hg19 refGene filtered/ && perl /data/anjana/annovar/annotate_variation.pl --buildver hg19 --downdb seq filtered/hg19_seq && perl /data/anjana/annovar/retrieve_seq_from_fasta.pl filtered/hg19_refGene.txt -seqdir filtered/hg19_seq -format refGene -outfile filtered/hg19_refGeneMrna.fa && perl /data/anjana/annovar/annotate_variation.pl {input} -dbtype refGene -buildver hg19 filtered/ -out results_dna/annotated/all.vcf"
        
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
