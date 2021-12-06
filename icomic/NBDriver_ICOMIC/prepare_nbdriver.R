#!/usr/bin/env Rscript
#input consists of a vcf file containing chr/pos/ref/alt
#output consists of a dataframe containing chr/pos/ref/alt/nbd/type
name="NBDriver_vcf"
edited_vcf <- read.table(commandArgs(TRUE)[1],header = TRUE)
nbd_fa<-read.table(commandArgs(TRUE)[2])
edited_vcf$nbd=nbd_fa$V1
edited_vcf$nbd=toupper(edited_vcf$nbd)
edited_vcf$Type=paste(edited_vcf$REF,edited_vcf$ALT,sep="")
edited_vcf$Type=factor(edited_vcf$Type)
levels(edited_vcf$Type)<-c("1","2","3","4","5","6","7","8","9","10","11","12")
colnames(edited_vcf)=c("Chromosome","Pos","Ref","Alt","new_nbd","Type")
write.table(edited_vcf,"input_data_nbdriver.txt",col.names = TRUE,row.names = FALSE,sep="\t",quote = FALSE)       
