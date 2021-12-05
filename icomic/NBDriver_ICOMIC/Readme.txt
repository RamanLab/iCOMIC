Requirements:
1. R
2. bedtools
3. R packages: VariantAnnotation
4. Bedtools (install command: conda install -c bioconda bedtools)
5. pip install imbalanced_learn
6. pip install scikit-learn==0.22.1
7. conda install pandas=0.25.3
8. 





How to run:
1. First, open the directory NBDriver_ICOMIC in terminal
2. chmod +x run.sh
3. Open the file run.sh
	a. Change the value of the variable "name" to the name of the vcf file (vcf1 in this case)	
	b. REF_GENOME_PATH to the path containing the hg19.fa file
	c. VCF_FILE_PATH to the folder named "vcf" in the NBDriver_ICOMIC directory
	d. BED_FILE_PATH to the folder named "bed" in the NBDriver_ICOMIC directory
	e. processed_file_path to the folder "NBDriver_ICOMIC"
4. Open the file extract_nbd.R and set the value of the variable BED_FILE_PATH similar to point 3 above 
5. Open the file extract_nbd.R and set the value of the variable "name" to the name of the vcf file (vcf1 in this case)
6. Open the file prepare_nbdriver.R and set the value of the variable "name" to the name of the vcf file (vcf1 in this case)
7. Change path for the second last line of run.sh or 
python -W ignore NBDriver_ICOMIC.py /path/to/input_data_nbdriver.txt
8. Open the file NBDriver_ICOMIC.py and change the paths present in the function read_model_params() to the appropriate files
