################# Rule Test #######################

#rule hisat2:
#    input:
#        R1 = "results/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R1.fastq",
#        R2 = "results/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R2.fastq"
#        reads=get_fastq
#        idx=config['ref']['index-hisat2']
#    output:
#      "results/aligner_results/{sample}_{condition}_Rep{rep}.sam"
#    message:
#        "------aligning with hisat2....wait.."
#    params:
#        idx= config['ref']['index-hisat2']
#    threads: 40
#    wrapper:
#        "/data/Priyanka/softwares/hisat2-2.1.0/hisat2 -p {threads} -x {params.index} --dta  --rna-strandness RF -1 {input.reads} -S {output.sam}"
#        "0.60.1/bio/hisat2/align"
        
        
rule hisat2:
    input:
      idx = config['ref']['index-hisat2'],
#      idx = "/home/priyanka/Desktop/test_env/iCOMIC/results/index/hisat2/",
      reads=get_fastq
    output:
#      sam="results/aligner_results/hisat2/{sample}_{condition}_Rep{rep}.sam"
      sam="results/aligner_results/{sample}_{condition}_Rep{rep}.sam"
    log:
      "logs_rna/hisat2/hisat2_{sample}_{condition}_Rep{rep}.log"
    message:
        "------aligning with hisat2....wait.."
    params:
      extra = ""
    threads: config["threads"]
    run:
#        n = len(input.sample)
#        assert n == 1 or n == 2, "input->sample must have 1 (single-end) or 2 (paired-end) elements."
#        if n == 1:
#            input_flags = "-U {}".format(*input.sample)
#        else:
#           input_flags = "-1 {} -2 {}".format(*input.sample)

        reads = input.reads
        if isinstance(reads, str):
            input_flags = "-U {0}".format(reads)
        elif len(reads) == 1:
            input_flags = "-U {0}".format(reads[0])
        elif len(reads) == 2:
            input_flags = "-1 {0} -2 {1}".format(*reads)
        else:
            raise RuntimeError(
                "Reads parameter must contain at least 1 and at most 2" " input files."
            )
        shell("hisat2  {params.extra} -p {threads}  -x {input.idx} {input_flags} --dta -S {output.sam}")
#        shell("/data/Priyanka/softwares/hisat2-2.1.0/hisat2  {params.extra} -p {threads} -5 11 --rna-strandness F -x {input.idx} {input_flags} --dta -S {output.sam}")
#        shell("/data/Priyanka/softwares/hisat2-2.1.0/hisat2  {params.extra} -p {threads} --rna-strandness F -x {input.idx} {input_flags} --dta -S {output.sam}")   
#rule hisat2:
#    input:
#        R1 = "results/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R1.fastq",
#        R2 = "results/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R2.fastq"
#        reads=get_fastq
#    output:
#        sam = "results/aligner_results/{sample}_{condition}_Rep{rep}_cutadapt.sam"
#    message:
#        "------aligning with hisat2....wait.."
#    params:
#        index= config['ref']['index-hisat2']
#    threads: 40
#    shell:
#        "/data/Priyanka/softwares/hisat2-2.1.0/hisat2 -p {threads} -x {params.index} --dta  --rna-strandness RF -U {input.reads} -S {output.sam}"
    
rule create_bams:
    input:
#        sam = "results/aligner_results/hisat2/{sample}_{condition}_Rep{rep}.sam"
        sam = "results/aligner_results/{sample}_{condition}_Rep{rep}.sam"
    output:
#        bam = "results/aligner_results/hisat2/{sample}_{condition}_Rep{rep}.bam"
        bam = "results/aligner_results/{sample}_{condition}_Rep{rep}.bam"
    message:
        "---coverting sam to bam  and indexing the bam files"
    shell:
        "samtools view -bh {input.sam} | samtools sort - -o {output.bam}; samtools index {output.bam}"

rule samtools_stats:
    input:
#        "results/aligner_results/hisat2/{sample}_{condition}_Rep{rep}.bam"
         "results/aligner_results/{sample}_{condition}_Rep{rep}.bam"
    output:
        "results/aligner_results/hisat2/samtools-stats/{sample}_{condition}_Rep{rep}.txt"
    log:
        "logs/samtools-stats/hisat2/{sample}_{condition}_Rep{rep}.logs"
    wrapper:
#        "0.27.1/bio/samtools/stats"
        "0.38.0/bio/samtools/stats"

rule multiqc:
    input:
        expand("results/aligner_results/hisat2/samtools-stats/{sample}_{condition}_Rep{rep}.txt", sample=samples, condition=type, rep=reps)
    output:
        report("results/multiqc/multiqc.html", caption="../report/multiqc.rst", category="Quality control")
    log:
        "logs/multiqc.log"
    wrapper:
#        "0.27.1/bio/multiqc"
        "0.38.0/bio/multiqc"


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
