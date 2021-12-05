#!/usr/bin/env Rscript
#input=vcf file built using the GrCH37 build of the reference genome containing the fields CHROM, POS, REF, ALT 
#output=file containing the feature matrix that will serve as input to the ML models
args<-commandArgs(TRUE)
name="vcf1"
BED_FILE_PATH="./NBDriver_ICOMIC/bed/"
suppressMessages(library(data.table,quietly=TRUE))
suppressMessages(library(VariantAnnotation,quietly=TRUE))
vcf <- fread(args[1])
#extract only the necessary fields
vcf_select=vcf[,c("#CHROM","POS","REF","ALT")]
#extract only the SNVs
vcf_select_only_snvs= vcf_select[c(which((nchar(vcf_select$ALT)==1) & (vcf_select$ALT %in% c("A","T","G","C")))),]
colnames(vcf_select_only_snvs)[1]="CHROM"
df=data.frame(Chr=paste("chr",vcf_select_only_snvs$CHROM,sep=""),Start=vcf_select_only_snvs$POS-11,End=vcf_select_only_snvs$POS+10)
fi=paste(BED_FILE_PATH,name,".bed",sep="")
write.table(df,fi,col.names = FALSE,row.names = FALSE,sep="\t",quote = FALSE)
write.table(vcf_select_only_snvs,"edited_vcf.txt",col.names = TRUE,row.names = FALSE,sep="\t",quote = FALSE)
