import pandas as pd
import numpy as np
import itertools
import subprocess

index = ['0','1']
options = ['yes', 'no']


tools_rna = pd.DataFrame(data=np.array([['hisat2', 'stringtie', 'ballgown'],['star', 'star', 'deseq2']]), columns=['Aligner', 'Expression_Modeller', 'Differential_Expression_Tools'])
def_params_rna = pd.DataFrame(data=np.array([[['-p 1', '--dta', '--rna-strandness RF'], ['-p 1', '--merge', '--rf', '-e', '-B'], ['-t 1']], [['j'], ['-p 1'], ['-t 1']] ]), columns=['Aligner', 'Expression_Modeller', 'Differential_Expression_Tools'])


print("\n Welcome to Icomic pipeline!\n \n Are you working with DNA-Seq or RNA-Seq data?? \n ")

data = {'Data': ['DNA-Seq','RNA-Seq']}
dat = pd.DataFrame(data)
print(dat)
pipe= int(input("\n Choose the numbers corresponding to your input \n"))
index_files = ['index-star', 'index-hisat2', 'index-salmon', 'index-bowtie2', 'annotation', 'fasta', 'transcript']
default_index= ['/data/Priyanka/other_pipelines/rna-seq-star-deseq2-master/Test_Run/Ref/star-index/', '/data/Priyanka/other_pipelines/rna-seq-star-deseq2-master/Test_Run/Ref/hisat2-index/hisat2-index', '/data/Priyanka/other_pipelines/rna-seq-star-deseq2-master/Test_Run/Ref/salmon-index/', '/data/Priyanka/other_pipelines/rna-seq-star-deseq2-master/Test_Run/Ref/bowtie2-index/bowtie2-index', '/data/Priyanka/other_pipelines/rna-seq-star-deseq2-master/Test_Run/Ref/gencode/gencode.v29.annotation.gtf', '/data/Priyanka/other_pipelines/rna-seq-star-deseq2-master/Test_Run/Ref/gencode/GRCh38.primary_assembly.genome.fa', '/data/Priyanka/other_pipelines/rna-seq-star-deseq2-master/Test_Run/Ref/gencode/gencode.v29.transcripts.fa']

#snake = open ('Snakefile',"w")
#snake.write('include: "rules/common.smk"\n\n')
#snake.write('include: "rules/qc.smk"\n')
#snake.write('include: "rules/cutadapt.smk"\n')
#snake.write('include: "rules/fastqc_after.smk"\n')
#snake.write('rule all:\n')
#snake.write('  input:\n')
#snake.write("    expand('results/fastqc/{sample}_{condition}_Rep{rep}_R1_fastqc.zip', sample=samples, condition=type, rep=reps),\n")
#snake.write("    expand('results/fastqc/{sample}_{condition}_Rep{rep}_R2_fastqc.zip', sample=samples, condition=type, rep=reps),\n")
#snake.write("    expand('results/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R1.fastq', sample=samples, condition=type, rep=reps),\n")
#snake.write("    expand('results/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R2.fastq', sample=samples, condition=type, rep=reps),\n")
#snake.write("    expand('results/summary_stats/{sample}_{condition}_Rep{rep}_cutadapt_summary.txt', sample=samples, condition=type, rep=reps),\n")
#snake.write("    expand('results/fastqc_after/{sample}_{condition}_Rep{rep}_cutadapt_R1_fastqc.zip', sample=samples, condition=type, rep=reps),\n")
#snake.write("    expand('results/fastqc_after/{sample}_{condition}_Rep{rep}_cutadapt_R2_fastqc.zip', sample=samples, condition=type, rep=reps),\n")
#snake.write('    "qc/multiqc.html"\n')
#snake.close()

for column in dat:
    print("\n\n You are working with " + dat.iloc[pipe][column] + " data\n")
    if dat.iloc[pipe][column] == 'DNA-Seq':
        tools = pd.DataFrame(data=np.array([['BWA_MEM','GATK_HC' , 'SnpEff'], ['Bowtie2', 'bcftools_call' , 'Annovar']]), columns=['Aligner', 'Variant_caller', 'Annotator'],index = index)

        def_params = pd.DataFrame(data=np.array([[['-k 19' ,'-t 1', '-w 100', '-d 100'], ['-mbq 10', '-minReadsPerAlignStart 10', '-ploidy 2'], ['-i VCF', '-o VCF', '-t 1', 'variants_file STDIN]']], [['-p 1', '--ma 2', '--mp 6', '--np 1', '--rdg 5', '--rfg 5'], ['--threads 1', '-O v', '-s all samples'], ['-thread 1']]]), columns=['Aligner', 'Variant_caller', 'Annotator'])

        gatk = np.array(['HaplotypeCaller', 'GenotypeGVCFs', 'BaseRecalibrator', 'VariantRecalibrator'])
        


        files = ['samples', 'units']
        ref_files = ['genome ', 'known-variants']

        conf = open('config.yaml',"w") 
        for file in files:
            path = input("\n \n Enter the {} file name with path, (eg: /path/to/filename.extension) : \t".format(file))
            conf.write(file + ": " + path + "\n")
        conf.write("ref: " + "\n")
        name = input("\n \n Enter the reference name (for SnpEff) : \t")
        conf.write("  name: " + name + "\n")
        for ref_file in ref_files:
            ref_path = input("\n \n Enter the reference {} file name with path, (eg: /path/to/filename.extension) : \t".format(ref_file))
            conf.write("  " + ref_file + ": " + ref_path + "\n")
        conf.write("processing: \n")
        conf.write("  "+ "remove-duplicates: true\n")
        #cap_reg = input("\n\n Enter the restriction-regions file name with path (eg: /path/to/filename.extension) : \t")
        #conf.write("  "+"restrict-regions: " + cap_reg + "\n" )
        conf.write("filtering:\n")
        conf.write("  "+"vqsr: false\n")
        conf.write("  "+"hard:\n")
        conf.write("    "+"snvs:\n")
        conf.write("      " + '"QD < 2.0 || FS > 60.0 || MQ < 40.0 || MQRankSum < -12.5 || ReadPosRankSum < -8.0"\n')
        conf.write("    "+"indels:\n")
        conf.write("      "+'"QD < 2.0 || FS > 200.0 || ReadPosRankSum < -20.0"\n')
        conf.write("params: " + "\n")
        for col in tools:
            for number in [0,1]:
                if tools.iloc[number][col] != 'GATK_HC':
                    conf.write("  " + tools.iloc[number][col] + ': "" \n')
                elif tools.iloc[number][col] == "GATK_HC":
                    conf.write('  GATK_HC : \n')
                    for i in range(len(gatk)):
                        conf.write('    ' + gatk[i] + ': ""\n')
        conf.write('  cutadapt: "" \n')
        conf.write("  picard:\n")
        conf.write('    MarkDuplicates: "REMOVE_DUPLICATES=true"\n')
        conf.close() 

        snake = open('Snakefile', "w")
        snake.write('include: "rules/common_dna.smk"\n')
        snake.write('include: "rules/qc_dna.smk"\n')
        snake.write('include: "rules/cutadapt_dna.smk"\n')
        snake.write('include: "rules/fastqc_after_dna.smk"\n')
        snake.write('rule all:\n')
        snake.write('  input:\n')
        snake.write('    expand("qc/fastqc/{u.sample}-{u.unit}.html", u = units.itertuples()),\n')
        snake.write('    expand("qc/fastqc/{u.sample}-{u.unit}.zip", u = units.itertuples()),\n')
#        snake.write('    expand("trimmed/{u.sample}-{u.unit}.1.fastq.gz", u = units.itertuples()),\n')
#        snake.write('    expand("trimmed/{u.sample}-{u.unit}.2.fastq.gz", u = units.itertuples()),\n')
        snake.write('    expand("trimmed/{u.sample}-{u.unit}.fastq.gz", u = units.itertuples()),\n')
        snake.write('    expand("qc/fastqc/{u.sample}-{u.unit}.aftertrim.html", u = units.itertuples()),\n')
        snake.write('    expand("qc/fastqc/{u.sample}-{u.unit}.aftertrim.zip", u = units.itertuples()),\n')
#        snake.write('    expand("mapped/{u.sample}-{u.unit}.bam", u = units.itertuples()),\n')
#        snake.write('    expand("called/{u.sample}.{contig}.bcf", u = units.itertuples(), contig = contigs),\n')
#        snake.write('    "qc/multiqc.html",\n')
#        snake.write('    "filtered/all.vcf"\n')
        snake.close()

        print(tools)
        
    elif dat.iloc[pipe][column] == 'RNA-Seq':
        conf = open('config.yaml',"w")
        conf.write("ref: " + "\n")
        for file in index_files: 
            index_path = input("\n \n Enter the {} file name with path, (eg: /path/to/filename.extension) : \t".format(file)) 
       	    conf.write("  "+file + ": " + '"' + index_path + '"' + "\n")
        conf.write("params: " + "\n")
        conf.write('  cutadapt: "" \n')
        for col in tools_rna:
            for number in [0,1]:
                conf.write("  " + tools_rna.iloc[number][col] + ': "" \n')
        conf.close()
        
        snakef = open('Snakefile', 'w')
        snakef.write('include: "rules/common_rna.smk"\n')
        snakef.write('include: "rules/qc_rna.smk"\n')
        snakef.write('include: "rules/cutadapt_rna.smk"\n')
        snakef.write('include: "rules/fastqc_after_rna.smk"\n')
        snakef.write('rule all:\n')
        snakef.write('  input:\n')
        snakef.write("    expand('results/fastqc/{sample}_{condition}_Rep{rep}_R1_fastqc.zip', sample=samples, condition=type, rep=reps),\n")
        snakef.write("    expand('results/fastqc/{sample}_{condition}_Rep{rep}_R2_fastqc.zip', sample=samples, condition=type, rep=reps),\n")
        snakef.write("    expand('results/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R1.fastq', sample=samples, condition=type, rep=reps),\n")
        snakef.write("    expand('results/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R2.fastq', sample=samples, condition=type, rep=reps),\n")
        snakef.write("    expand('results/summary_stats/{sample}_{condition}_Rep{rep}_cutadapt_summary.txt', sample=samples, condition=type, rep=reps),\n")
        snakef.write("    expand('results/fastqc_after/{sample}_{condition}_Rep{rep}_cutadapt_R1_fastqc.zip', sample=samples, condition=type, rep=reps),\n")
        snakef.write("    expand('results/fastqc_after/{sample}_{condition}_Rep{rep}_cutadapt_R2_fastqc.zip', sample=samples, condition=type, rep=reps),\n")
        snakef.close()

        #rule = open('rule_all.txt', 'r')
        #snake = open ('Snakefile',"a")
        #for line in rule:
        #    for col in tools_rna:
        #        if tools_rna.iloc[nu][col] in line:
        #            snake.write(line)
        #snake.write('include: "rules/qc.smk"\n')
        #snake.write('include: "rules/cutadapt.smk"\n')
        #rule.close()
        #snake.close()

        print(tools_rna)
        
            

while True:
    answer_qc = input("\n \n Have you done quality check? \t") or "yes"
    if (answer_qc not in options):
        print("\n Your entry should be either 'yes' or 'no'")
        continue
    if answer_qc == "no":
        print("\n \n Running FastQC!! Check qc results in the folder qc/fastqc !!")
        subprocess.run(["snakemake", "--use-conda", "-U", "fastqc"])
    print("\n \n Preparing to run cutadapt with default parameters ['-j 1', '-e 0.1', '-n 1', '-O 3']!! Check the qc results after trimming in the folder qc/fastqc !! ")
    while True:
        answer = input("\n \n Do you want to run cutadapt with default parameters? \t") or "yes"
        if (answer not in options):
            print("\n Your entry should be either 'yes' or 'no'")
            continue
        if answer == "no":
            cut_params_list = input("\n\n Press enter to list out the parameters for cutadapt : ")
            if cut_params_list == "":
                a = open("cutadapt.txt", "r")
                print(a.read())
#            else:
#                print("Press the enter key!!!")
#                continue
            try:
                o = int(input("\n How many parameters do you want to add for cutadapt : \t"))
            except ValueError:
                print("\n Sorry, entry should be a positive integer!!")
                continue

            cut_new_params = []
            for j in range(1,o+1):
                cut_add_params = (input("\n Enter the additional parameter for cutadapt, for example j 4 : \t"))
                cut_new_params.append(cut_add_params)

            r = open('config.yaml').read()
            r = r.replace('  cutadapt: "" \n', "  cutadapt: " + ' '.join(map(lambda x: '"-' + x + '"\n', cut_new_params)) + "\n")
            y = open("config.yaml", 'w')
            y.write(r)
            y.close()
        elif (answer == "yes"):
            print("\n \n You have chosen to work with the parameters ['-j 1', '-e 0.1', '-n 1', '-O 3'] !!")
            subprocess.run(["snakemake", "--use-conda", "-U", "fastqc_after", "--unlock"])
        answer_align = input("\n \n Do you want to Proceed with alignment? \t") or "yes"
        if answer_align == "no":
            continue
        else:
            if dat.iloc[pipe][column] == 'DNA-Seq':
                for col in tools.columns:
                    while True:
                        try:
                            number = int( input(" \n\n Enter the number associated with your choice of {} : \t".format(col)))
                        except ValueError:
                            print("\n Sorry, entry should be a positive integer!!")
                            continue

                        if number >= len(tools):
                            print("\n Invalid choice of", col ,"!!!")
                            continue

                        else:
                            print("\n You have chosen the ", col ,"," ,tools.iloc[number][col])
                            with open('Snakefile','a') as snakefile:
                                snakefile.write('include: "rules/' + tools.iloc[number][col] + '.smk" \n')
                                snakefile.close()
                            print("\n The default parameters for ", col, tools.iloc[number][col] , " are " , def_params.iloc[number][col])
                            params_list = input("\n \n Press enter to list out the parameters : ")
                            if params_list == "":
                                    f = open(tools.iloc[number][col]+".txt", "r")
                                    print(f.read())
    #                        else:
    #                            print("\n \n Press the enter key alone!!!")
    #                            continue

                            while True:
                                answer = input("\n \n Do you want to work with default parameters? \t") or "yes"
                                if (answer not in options):
                                    print("\n Your entry should be either 'yes' or 'no'")
                                    continue
                                if answer == "no":
                                    if tools.iloc[number][col] == 'GATK_HC':
                                        for i in range(len(gatk)):
                                            gatk_params_list = input("\n\n Press enter to list out the parameters for " + gatk[i] + ": ")
                                            if gatk_params_list == "":
                                                f = open(gatk[i] +".txt", "r")
                                                print(f.read())
                                                f.close()
    #                                        else:
    #                                            print("Press the enter key!!!")
                #                                continue
                                            try:
                                                g = int(input("\n How many parameters do you want to add for {} : \t".format(gatk[i])))
                                            except ValueError:
                                                print("\n Sorry, entry should be a positive integer!!")
                                                continue

                                            gatk_new_params = []
                                            for y in range(1,g+1):
                                                gatk_add_params = (input("\n Enter the additional parameter for {}, for example j 4 : \t".format(gatk[i])))
                                                gatk_new_params.append(gatk_add_params)
                                            print(gatk_new_params)
                                            k = open('config.yaml').read()
                                            k = k.replace('    ' + gatk[i] + ': ""\n', "    " + gatk[i] + ": " + ' '.join(map(lambda x: '"-' + x + '"\n', gatk_new_params)) + "\n")
                                            t = open("config.yaml", 'w')
                                            t.write(k)
                                            t.close()

                                    else:
                                        try:
                                            p = int(input("\n How many parameters do you want to add? \t"))
                                        except ValueError:
                                            print("\n Sorry, entry should be a positive integer!!")
                                            continue
                                        new_params = []
                                        for r in range(1,p+1):
                                            add_params = (input("\n Enter the additional parameter {for example j 4 } : \t"))
                                            new_params.append(add_params)


                                    w = open('config.yaml').read()
                                    w = w.replace("  " + tools.iloc[number][col] + ': "" \n', "  " + tools.iloc[number][col] + ": " + ' '.join(map(lambda x: '"-' + x + '"\n', new_params)))
                                    fl = open("config.yaml", 'w')
                                    fl.write(w)
                                    fl.close()
                                    all_params = def_params.iloc[number][col] + (new_params)


                                    print("\n \n You have chosen to work with ", col , tools.iloc[number][col] , " with the parameters " , all_params)
                                    break
                                elif (answer == "yes"):
                                    print("\n \n You have chosen to work with ", col , tools.iloc[number][col], " with the parameters " , def_params.iloc[number][col])

                                    break
                            break  
            else:
                for col in tools_rna.columns:
                    while True:
                        try:
                            nu = int( input(" \n\n Enter the number associated with your choice of {} : \t".format(col)))
                        except ValueError:
                            print("\n Sorry, entry should be a positive integer!!")
                            continue

                        if nu >= len(tools_rna):
                            print("\n Invalid choice of", col ,"!!!")
                            continue

                        else:
                            print("\n You have chosen the ", col ,"," ,tools_rna.iloc[nu][col])
                            rule = open('rule_all.txt', 'r')
                            snake = open ('Snakefile',"a")
                            for line in rule:
                                if tools_rna.iloc[nu][col] in line:
                                    snake.write(line)
                            rule.close()
        #                    snake.write('include: "rules/' + tools_rna.iloc[nu][col] + '.smk" \n')
                            snake.close()
                           # with open('Snakefile', 'a') as snakef:
                           #     snakef.write('include: "rules/qc.smk"\n')
                           #     snakef.write('include: "rules/cutadapt.smk"\n')
                           #     snakef.close()	
                          # with open('Snakefile','a') as snakefile:
                          #      snakefile.write('include: "rules/' + tools_rna.iloc[nu][col] + '.smk" \n')
                          #      snakefile.close()
                            print("\n The default parameters for ", col, tools_rna.iloc[nu][col] , " are " , def_params_rna.iloc[nu][col])
                            params_list = input("\n \n Press enter to list out the parameters : ")
                            if params_list == "":
                                    f = open(tools_rna.iloc[nu][col]+".txt", "r")
                                    print(f.read())
    #                        else:
    #                            print("\n \n Press the enter key alone!!!")
    #                            continue

                            while True:
                                answer = input("\n \n Do you want to work with default parameters? \t") or "yes"
                                if (answer not in options):
                                    print("\n Your entry should be either 'yes' or 'no'")
                                    continue
                                if answer == "no":
                                    try:
                                        p = int(input("\n How many parameters do you want to add? \t"))
                                    except ValueError:
                                        print("\n Sorry, entry should be a positive integer!!")
                                        continue
                                    new_params = []
                                    for r in range(1,p+1):
                                        add_params = (input("\n Enter the additional parameter {for example j 4 } : \t"))
                                        new_params.append(add_params)


                                    w = open('config.yaml').read()
                                    w = w.replace("  " + tools_rna.iloc[nu][col] + ': "" \n', "  " + tools_rna.iloc[nu][col] + ": " + ' '.join(map(lambda x: '"-' + x + '"\n', new_params)) + "\n")
                                    fl = open("config.yaml", 'w')
                                    fl.write(w)
                                    fl.close()
                                    all_params = def_params_rna.iloc[nu][col] + (new_params)

                                    print("\n \n You have chosen to work with ", col , tools_rna.iloc[nu][col] , " with the parameters " , all_params)
                                    break
                                elif answer == "yes":
                                    print("\n \n You have chosen to work with ", col , tools_rna.iloc[nu][col], " with the parameters " , def_params_rna.iloc[nu][col])

                                    break
                        break  
                    
                
                
                break

        
        
        break
    break
    #        break 
if dat.iloc[pipe][column] == 'DNA-Seq':
    with open('Snakefile', 'r+') as fd:
        contents = fd.readlines()
        if tools.iloc[number]['Annotator'] == 'Annovar':
            contents.insert(11, '    expand("mapped/{u.sample}-{u.unit}.sorted.bam", u = units.itertuples()),\n    "qc/multiqc.html",\n    "filtered/all.vcf",\n    "annotated/all.vcf.variant_function"\n')  # new_string should end in a newline
            fd.seek(0)  # readlines consumes the iterator, so we need to start over
            fd.writelines(contents) 
        else:
            contents.insert(11, '    expand("mapped/{u.sample}-{u.unit}.sorted.bam", u = units.itertuples()),\n    "qc/multiqc.html",\n    "filtered/all.vcf",\n    "annotated/all.vcf.gz"\n')
            fd.seek(0)  # readlines consumes the iterator, so we need to start over
            fd.writelines(contents)
if dat.iloc[pipe][column] == 'RNA-Seq':
    with open('Snakefile', 'a') as snk:
#        snk.write('include: "rules/qc.smk"\n')
#        snk.write('include: "rules/cutadapt.smk"\n')
        for col in tools_rna:
            snk.write('include: "rules/' + tools_rna.iloc[nu][col] + '.smk" \n')
        snk.close()
subprocess.run(["snakemake", "--use-conda"])

