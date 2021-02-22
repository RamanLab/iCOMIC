######### Rule Test ###########

rule salmon_quant:
    input:
        R1 = 'results_test/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R1.fastq',
        R2 = 'results_test/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R2.fastq'
    output:
        B1 = directory('results_test/salmon/{sample}_{condition}_Rep{rep}_cutadapt_salmon_quant')
     #version:
     #shell("salmon --version")
    log:
        'results_test/logs/salmon/{sample}_{condition}_Rep{rep}_salmon.log'
    message:
        "..wait...aligning and quantifying sequence files....."
    #priority: 85
    params: 
        index=config["ref"]["index-salmon"]
    threads: 40
    shell:
        "/data/Priyanka/softwares/salmon-latest_linux_x86_64/bin/salmon quant -i {params.index} -l A -1 {input.R1} -2 {input.R2} -o {output.B1} -q --useVBOpt --gcBias --seqBias --posBias -p {threads} --numBootstraps 30 &> {log}"

