#!/bin/bash
name="vcf1"
REF_GENOME_PATH="./NBDriver_ICOMIC/hg19.fa"
VCF_FILE_PATH="./NBDriver_ICOMIC/vcf/"
VCF_FILE_PATH+="$name.vcf"
BED_FILE_PATH="./NBDriver_ICOMIC/bed/"
BED_FILE_PATH+="$name.bed"
echo "Extracting neighborhood sequences for the given set of mutations..."
./NBDriver_ICOMIC/extract_nbd.R $VCF_FILE_PATH
echo "Done"
echo "Preparing data for the pre-trained machine learning model"
bedtools getfasta -fi $REF_GENOME_PATH -bed $BED_FILE_PATH -fo snv_nbd.fa
sed -n 2~2p NBDriver_ICOMIC/snv_nbd.fa > NBDriver_ICOMIC/snv_nbd_extract.fa
./NBDriver_ICOMIC/prepare_nbdriver.R NBDriver_ICOMIC/edited_vcf.txt NBDriver_ICOMIC/snv_nbd_extract.fa
echo "Done"
echo "Obtaining predictions"
python -W ignore NBDriver_ICOMIC/NBDriver_ICOMIC.py ./NBDriver_ICOMIC/input_data_nbdriver.txt
echo "Done! The predictions are in the dataframe NBDriver_Predictions.csv"

