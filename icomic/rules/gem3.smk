rule gem3:
    input:
        sample=get_trimmed_reads
    output:
        "results_dna/mapped/{sample}-{unit}.sorted.bam"
    params:
        index= "index/gem3/genome.gem"
    run:
        n = len(input.sample)
        assert n == 1 or n == 2, "input->sample must have 1 (single-end) or 2 (paired-end) elements."
        if n == 1:
            reads = "-i {}".format(*input.sample)
        else:
            reads = "-1 {} -2 {}".format(*input.sample)

        shell("gem-mapper -I {params.index} {reads} -o {output}")

