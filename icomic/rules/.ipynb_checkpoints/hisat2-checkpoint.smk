################# Rule Test #######################

rule hisat2:
    input:
        R1 = "results/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R1.fastq",
        R2 = "results/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R2.fastq"
    output:
        sam = "results/aligner_results/{sample}_{condition}_Rep{rep}_cutadapt.sam"
    message:
        "------aligning with hisat2....wait.."
    params:
        index= config['ref']['index-hisat2']
    threads: 40
    shell:
        "/data/Priyanka/softwares/hisat2-2.1.0/hisat2 -p {threads} -x {params.index} --dta  --rna-strandness RF -1 {input.R1} -2 {input.R2} -S {output.sam}"

rule create_bams:
    input:
        sam = "results/aligner_results/{sample}_{condition}_Rep{rep}_cutadapt.sam"
    output:
        bam = "results/aligner_results/{sample}_{condition}_Rep{rep}_cutadapt.bam"
    message:
        "---coverting sam to bam  and indexing the bam files"
    shell:
        "samtools view -bh {input.sam} | samtools sort - -o {output.bam}; samtools index {output.bam}"

#rule create_bams_called:
#    input:
#        sam = "results/hisat2/{sample}_{condition}_Rep{rep}_cutadapt.sam"
#    output:
#        bam = "results/called/{sample}_{condition}_Rep{rep}_cutadapt.bam"
#    message:
#        "---coverting sam to bam  and indexing the bam files"
#    shell:
#        "samtools view -bh {input.sam} | samtools sort - -o {output.bam}; samtools index {output.bam}"
#     
