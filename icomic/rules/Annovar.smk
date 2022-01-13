
rule prepare_input_file:
    input:
        "results_dna/filtered/all.vcf.gz"
    output:
        "results_dna/filtered/all.avinput"
    shell:
        "perl ./annovar/convert2annovar.pl -format vcf4 {input} > {output} -allsample -withfreq -include"
        


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
        
