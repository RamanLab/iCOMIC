library("maftools")
#if (!require("BiocManager"))
#  install.packages("BiocManager")
#BiocManager::install("maftools")
HG001_chr21.maf = maftools::annovarToMaf(annovar = ((snakemake@params)[[1]]), Center = NULL, refBuild = ((snakemake@params)[[2]]), tsbCol = NULL, table = "refGene", basename = "results_dna/variants", sep = "\t", MAFobj = FALSE)

