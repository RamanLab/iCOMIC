library("maftools")
HG001_chr21.maf = maftools::annovarToMaf(annovar = "all.hg38_multianno.vcf", Center = NULL, refBuild = "hg38", tsbCol = NULL, table = "refGene", basename = NULL, sep = "\t", MAFobj = FALSE)
write.csv(HG001_chr21.maf, file = "variants.maf")

