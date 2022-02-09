        
rule hisat2:
    input:
      idx = config['ref']['index-HISAT2'],
#      idx = "/home/priyanka/Desktop/test_env/iCOMIC/results/index/hisat2/",
      reads=get_fastq
    output:
      sam="results/aligner_results/{sample}_{condition}_Rep{rep}.sam"
    log:
      "logs_rna/HISAT2/HISAT2_{sample}_{condition}_Rep{rep}.log"
    message:
        "------aligning with HISAT2....wait.."
    params:
      extra = ""
    threads: config["threads"]
#    extra = config["params"]["HISAT2"]
    run:
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
    
rule create_bams:
    input:
        sam = "results/aligner_results/{sample}_{condition}_Rep{rep}.sam"
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
        "results/aligner_results/HISAT2/samtools-stats/{sample}_{condition}_Rep{rep}.txt"
    log:
        "logs/samtools-stats/HISAT2/{sample}_{condition}_Rep{rep}.logs"
    wrapper:
        "0.38.0/bio/samtools/stats"

rule multiqc:
    input:
        expand("results/aligner_results/HISAT2/samtools-stats/{sample}_{condition}_Rep{rep}.txt", sample=samples, condition=type, rep=reps)
    output:
        report("results/multiqc/multiqc.html", caption="../report/multiqc.rst", category="Quality control")
    log:
        "logs/multiqc.log"
    params:
        dir= "results/multiqc/",
        name= "multiqc.html"
    shell:
        "multiqc --force {input} -o {params.dir} -n {params.name}"
    wrapper:
        "0.38.0/bio/multiqc"


