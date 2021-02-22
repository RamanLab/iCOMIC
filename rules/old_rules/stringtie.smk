########### Rule Test ###############

rule stringtie:
    input:
        bam = "results/hisat2/{sample}_{condition}_Rep{rep}_cutadapt.bam"
    output:
        R1 = "results/stringtie/{sample}_{condition}_Rep{rep}/{sample}_{condition}_Rep{rep}_transcript.gtf",
        #R2 = "results_test/stringtie/{sample}_{condition}_Rep{rep}/{sample}_{condition}_Rep{rep}_gene_abundances.tsv",
        #R3 = "results_test/stringtie/{sample}_{condition}_Rep{rep}/{sample}_{condition}_Rep{rep}_cov_ref.gtf"
    params:
        gtf= config['ref']['annotation']
    shell:
        "/data/Priyanka/softwares/stringtie-1.3.4d.Linux_x86_64/stringtie -G {params.gtf} --rf -o {output.R1} {input.bam}"

#rule mergelist:
#    input:
#        gtf = expand("results_test/stringtie/{sample}_{condition}_Rep{rep}/{sample}_{condition}_Rep{rep}_transcript.gtf", sample=samples, condition=type, rep=reps)
#    output:
#        txt = "results_test/stringtie/{sample}_mergelist.txt"
#    shell:
#        "echo {input.gtf} | tr \" \" \"\n\" >{output.txt}"
#
#rule stringtie_merge_list:
#    input: expand("stringtie/assembled/{sample}.gtf", sample=SAMPLES)
#    output: "stringtie/merged_list.txt"
#    run:
#        with open(output[0], 'w') as f:
#            for gtf in input:
#                print(Path(gtf).resolve(), file=f)

rule mergelist_mod:
    input:
        gtf = expand("results/stringtie/{sample}_{condition}_Rep{rep}/{sample}_{condition}_Rep{rep}_transcript.gtf", sample=samples, condition=type, rep=reps)
    output:
        txt = "results/stringtie/{sample}_mergelist.txt"
    run:
        from pathlib import Path
	with open(output[0], 'w') as f:
            for gtf in input:
                print(Path(gtf).resolve(), file=f)

rule gtf_merge:
    input:
        list = "results/stringtie/{sample}_mergelist.txt"
    output:
        R1 = "results/stringtie/{sample}_merge_transcripts.gtf"
    params:
        gtf= config['ref']['annotation']
    threads: 40
    shell:
        "/data/Priyanka/softwares/stringtie-1.3.4d.Linux_x86_64/stringtie -p {threads} --merge  -G {params.gtf} -o {output.R1} {input.list}"

rule stringtie_counts:
    input:
        bam = "results/hisat2/{sample}_{condition}_Rep{rep}_cutadapt.bam",
        gtf = "results/stringtie/{sample}_merge_transcripts.gtf"
    output:
        R1 = "results/stringtie_counts/{sample}_{condition}_Rep{rep}/{sample}_{condition}_Rep{rep}_transcripts.gtf",
        #R2 = "results_test/stringtie/{sample}_{condition}_Rep{rep}/{sample}_{condition}_Rep{rep}_gene_abundances.tsv",
        #R3 = "results_test/stringtie/{sample}_{condition}_Rep{rep}/{sample}_{condition}_Rep{rep}_cov_ref.gtf"
    #params:
        #gtf= config['ref']['annotation']
    shell:
        "/data/Priyanka/softwares/stringtie-1.3.4d.Linux_x86_64/stringtie -G {input.gtf} --rf -e -B -o {output.R1} {input.bam}"


#rule stringtie:
#    input:
#        bam = "results_test/hisat2/{sample}_{condition}_Rep{rep}_cutadapt.bam"
#    output:
#        R1 = "results_test/stringtie/{sample}_{condition}_Rep{rep}/{sample}_{condition}_Rep{rep}_transcript.gtf",
#        R2 = "results_test/stringtie/{sample}_{condition}_Rep{rep}/{sample}_{condition}_Rep{rep}_gene_abundances.tsv",
#        R3 = "results_test/stringtie/{sample}_{condition}_Rep{rep}/{sample}_{condition}_Rep{rep}_cov_ref.gtf"
#    params:
#        gtf= config['ref']['annotation']
#    shell:
#        "/data/Priyanka/softwares/stringtie-1.3.4d.Linux_x86_64/stringtie -G {params.gtf} --rf -e -B -o {output.R1} -A {output.R2} -C {output.R3} {input.bam}"
#
