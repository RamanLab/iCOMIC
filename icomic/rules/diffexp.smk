#samples = pd.read_table(config["samples"], index_col="sample")
#units = pd.read_table(config["units"], index_col=["sample", "unit"], dtype=str)
#samples = pd.read_table(config["samples"]).set_index("sample", drop=False)
#samples = pd.read_table(config["samples"], index_col="sample")
#units = pd.read_table(config["units"], dtype=str).set_index(["sample", "unit"], drop=False)
#units = pd.read_table(config["units"], index_col=["sample", "unit"], dtype=str)
#units.index = units.index.set_levels([i.astype(str) for i in units.index.levels])  # enforce str in index
#expand("star/{s}/ReadsPerGene.out.tab", s=samples)

rule count_matrix:
    input:
        #expand("star/{unit}/ReadsPerGene.out.tab", unit=config["units"])
	#expand("star/{unit.sample}-{unit.unit}/ReadsPerGene.out.tab", unit=units.itertuples())
	R1 = rules.cutadapt.output.R1,
	R2 = rules.cutadapt.output.R2,
	index=rules.index.output.directory
    output:
        "new/counts/all.tsv"
    #params:
        #units=units
    conda:
        "../envs/pandas.yaml"
    script:
        "../scripts/count-matrix.py"

def get_deseq2_threads(wildcards=None):
    # https://twitter.com/mikelove/status/918770188568363008
    few_coeffs = False if wildcards is None else len(get_contrast(wildcards)) < 10
    return 1 if len(samples) < 100 or few_coeffs else 6
    

rule deseq2_init:
    input:
        counts="/data/Priyanka/other_pipelines/rna-seq-star-deseq2-master/counts/all.tsv"
    output:
        "/data/Priyanka/other_pipelines/rna-seq-star-deseq2-master/deseq2/all.rds"
    params:
        samples=config["samples"]
    conda:
        "/data/Priyanka/other_pipelines/rna-seq-star-deseq2-master/envs/deseq2.yaml"
    log:
        "logs/deseq2/init.log"
    threads: get_deseq2_threads()
    script:
        "/data/Priyanka/other_pipelines/rna-seq-star-deseq2-master/scripts/deseq2-init.R"


rule pca:
    input:
        "/data/Priyanka/other_pipelines/rna-seq-star-deseq2-master/deseq2/all.rds"
    output:
        report("results/pca.svg", "../report/pca.rst")
    params:
        pca_labels=config["pca"]["labels"]
    conda:
        "/data/Priyanka/other_pipelines/rna-seq-star-deseq2-master/envs/deseq2.yaml"
    log:
        "/data/Priyanka/other_pipelines/rna-seq-star-deseq2-master/logs/pca.log"
    script:
        "/data/Priyanka/other_pipelines/rna-seq-star-deseq2-master/scripts/plot-pca.R"


def get_contrast(wildcards):
    return config["diffexp"]["contrasts"][wildcards.contrast]


rule deseq2:
    input:
        "/data/Priyanka/other_pipelines/rna-seq-star-deseq2-master/deseq2/all.rds"
    output:
        table=report("results/diffexp/{contrast}.diffexp.tsv", "../report/diffexp.rst"),
        ma_plot=report("results/diffexp/{contrast}.ma-plot.svg", "../report/ma.rst"),
    params:
        contrast=get_contrast
    conda:
        "/data/Priyanka/other_pipelines/rna-seq-star-deseq2-master/envs/deseq2.yaml"
    log:
        "/data/Priyanka/other_pipelines/rna-seq-star-deseq2-master/logs/deseq2/{contrast}.diffexp.log"
    threads: get_deseq2_threads
    script:
        "../scripts/deseq2.R"

