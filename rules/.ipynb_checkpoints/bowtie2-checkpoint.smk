################# Rule Test #######################

rule bowtie2:
    input:
        R1 = "results_test/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R1.fastq",
        R2 = "results_test/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R2.fastq"
    output:
        sam = "results_test/bowtie2/{sample}_{condition}_Rep{rep}_cutadapt.sam"
    message:
        "------aligning with bowtie2....wait.."
    params:
        index= config['ref']['index-bowtie2']
    threads: 1 
    shell:
        "bowtie2 -p {threads} -x {params.index} --dta --rna-strandness RF -1 {input.R1} -2 {input.R2} -S {output.sam}"

