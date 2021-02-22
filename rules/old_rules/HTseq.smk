rule HTSeq:
    input:
        R1 = "results_test/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R1.fastq",
        R2 = "results_test/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R2.fastq"
    output:
        sam = "results_test/hisat2/{sample}_{condition}_Rep{rep}_cutadapt.sam"
    message:
        "------aligning with hisat2....wait.."
    params:
        index= config['ref']['index-hisat2']
    threads: 40
    shell:
        "/data/Priyanka/softwares/hisat2-2.1.0/hisat2 -p {threads} -x {params.index} --dta  --rna-strandness RF -1 {input.R1} -2 {input.R2} -S {output.sam}"

