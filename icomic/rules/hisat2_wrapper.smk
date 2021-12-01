################# Rule Test #######################

rule hisat2_align:
    input: 
        idx = config['ref']['index-hisat2'],
#        idx = "/data/Priyanka/other_pipelines/iCOMIC/Test/ucsc/index_refGene/hisat2-index",
        reads = ["results/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R1.fastq", "results/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R2.fastq" ]
    output:
        "results/hisat2/{sample}_{condition}_Rep{rep}_cutadapt.bam"
    message:
        "------aligning with hisat2....wait.."
#    log:
#        "logs/hisat2_align_{sample}.log"
#   params:
#        extra = config['params']['hisat2']
    threads: 40
#    shell:
#        "/data/Priyanka/softwares/hisat2-2.1.0/hisat2 -p {threads} -x {params.index} --dta  --rna-strandness RF -1 {input.R1} -2 {input.R2} -S {output.sam}"
    wrapper:
        "0.36.0/bio/hisat2/align"

#rule create_bams:
#   input:
#        sam = "results/hisat2/{sample}_{condition}_Rep{rep}_cutadapt.sam"
#    output:
#        bam = "results/hisat2/{sample}_{condition}_Rep{rep}_cutadapt.bam"
#    message:
#        "---coverting sam to bam  and indexing the bam files"
#    shell:
#        "samtools view -bh {input.sam} | samtools sort - -o {output.bam}; samtools index {output.bam}"
#    wrapper:
#        "0.36.0/bio/samtools/view"

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
