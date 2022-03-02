rule star:
    input:
        reads=get_fastq
    output:
        "results/aligner_results/{sample}_{condition}_Rep{rep}/Aligned.out.sam"
    message:
        "------aligning with STAR....wait.."
    log:
        "logs_rna/STAR/STAR_{sample}_{condition}_Rep{rep}.log"
    params:
        prefix = "results/aligner_results/{sample}_{condition}_Rep{rep}/",
        index= config['ref']['index-STAR'],
        annotate= config['ref']['annotation'],
        extra=config['params']['STAR']
    threads: config["threads"]
    run:
        reads = input.reads
        if isinstance(reads, str):
            input_flags = " {0}".format(reads)
        elif len(reads) == 1:
            input_flags = " {0}".format(reads[0])
        elif len(reads) == 2:
            input_flags = " {0}  {1}".format(*reads)
        else:
            raise RuntimeError(
                "Reads parameter must contain at least 1 and at most 2" " input files."
            )      
        shell("STAR {params.extra} --runMode alignReads --runThreadN {threads} --genomeDir {params.index} --readFilesIn {input_flags} --outFileNamePrefix {params.prefix} --sjdbGTFfile {params.annotate} --outStd Log {log}--quantMode GeneCounts" )

rule create_bams:
    input:
        sam = "results/aligner_results/{sample}_{condition}_Rep{rep}/Aligned.out.sam"
    output:
        bam = "results/aligner_results/{sample}_{condition}_Rep{rep}.bam"
    message:
        "---coverting sam to bam  and indexing the bam files"
    shell:
        "samtools view -bh {input.sam} | samtools sort - -o {output.bam}; samtools index {output.bam}"

rule samtools_stats:
    input:
        "results/aligner_results/{sample}_{condition}_Rep{rep}.bam"
    output:
        "results/aligner_results/STAR/samtools-stats/{sample}_{condition}_Rep{rep}.txt"
    log:
        "logs_rna/samtools-stats/STAR/{sample}_{condition}_Rep{rep}.logs"
    wrapper:
        "0.38.0/bio/samtools/stats"

rule multiqc:
    input:
        expand("results/aligner_results/STAR/samtools-stats/{sample}_{condition}_Rep{rep}.txt", sample=samples, condition=type, rep=reps)
    output:
        report("results/multiqc/multiqc.html", caption="../report/multiqc.rst", category="Quality control")
    log:
        "logs_rna/multiqc.log"
    params:
        dir= "results/multiqc/",
        name= "multiqc.html"
    shell:
        "multiqc --force {input} -o {params.dir} -n {params.name}"

