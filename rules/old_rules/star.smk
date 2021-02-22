########## Rule Test ###########
rule star:
    input:
        fq1 = ["results_test/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R1.fastq"],
        fq2 = ["results_test/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R2.fastq"]
    output:
        # see STAR manual for additional output files
        "results_test/star/{sample}_{condition}_Rep{rep}/Aligned.out.bam",
        "results_test/star/{sample}_{condition}_Rep{rep}/ReadsPerGene.out.tab"
    message:
        "------aligning with star....wait.."
    log:
        "results_test/logs/star/{sample}_{condition}_Rep{rep}.log"
    params:
        # path to STAR reference genome index
        index=config["ref"]["index-star"],
        # optional parameters
        # extra="--quantMode GeneCounts --sjdbGTFfile {} {}".format(config["ref"]["annotation"], config["params"]["star"])
        extra="{}".format(config["params"]["star"])
    threads: 80
    wrapper:
        "master/bio/star/align"

rule star_called:
    input:
        fq1 = ["results_test/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R1.fastq"],
        fq2 = ["results_test/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R2.fastq"]
    output:
        # see STAR manual for additional output files
        "results_test/called/{sample}_{condition}_Rep{rep}_cutadapt.bam",
        "results_test/called/{sample}_{condition}_Rep{rep}_ReadsPerGene.out.tab"
    message:
        "------aligning with star....wait..."
    log:
        "results_test/logs/called/star_{sample}_{condition}_Rep{rep}.log"
    params:
        # path to STAR reference genome index
        index=config["ref"]["index-star"],
        # optional parameters
        # extra="--quantMode GeneCounts --sjdbGTFfile {} {}".format(config["ref"]["annotation"], config["params"]["star"])
        extra="{}".format(config["params"]["star"])
    threads: 80
    wrapper:
        "master/bio/star/align"

