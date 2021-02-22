################# Renaming Files ###########################
import pandas as pd
import os
from os import rename
import csv
import re

##############from table#################
table = pd.read_table(os.getcwd()+"/table_rna.tsv")
#print(table)
#for i in table.iterrows():

for i in range(len(table)):
    filepath = os.path.dirname(str(table.iloc[i]["fq1"]))
    if not any (file.endswith(".fastq") for file in os.listdir(filepath)):
        print("No fastq files in the folder!", file=open('rename_check.txt', 'w'))
    else:
        for file in os.listdir(filepath):
            if (file.endswith(".fastq")):
                f = file
                if re.match('/\w|.+_\w+_Rep\d_R1|2.fastq$/', f):
                    continue
                elif re.match('/\w|.+_\w+_Rep\d_R2|1.fastq$/', f):
                    continue
                else:
                    if pd.isnull(table.iloc[i]["fq2"]):
                        oldfile = str(table.iloc[i]["fq1"])
                        if os.path.exists(oldfile):
                #        filepath = os.path.dirname(str(table.iloc[i]["fq1"]))
                #        print(oldfile)
                            sample = table.iloc[i]["sample"]
                            unit = str(table.iloc[i]["unit"])
                            condition = table.iloc[i]["condition"]
                            length = str(1)
                    #        print(sample, unit, condition, length)
                            newfile = filepath + "/"+ sample + "_" + condition + "_Rep" + unit + "_R" + length + ".fastq"
                            rename(oldfile, newfile)
                            rename_dict = dict()
                            rename_dict[oldfile] = newfile
                    #        print(rename_dict)
                            with open("rename_filenames.csv", 'w') as rf:
                                root = csv.writer(rf, delimiter='\t')
                                root.writerow(["Old_Name", "New_Name"])
                                for i,j in rename_dict.items():
                                    root.writerow([i, j])
                        else:
                            print("Fastq files doesn't exist in the folder! Check the table!", file=open('rename_check.txt', 'w'))
                    else:
                        oldfile1 = str(table.iloc[i]["fq1"])
                        oldfile2 = str(table.iloc[i]["fq2"])
                        if (os.path.exists(oldfile1) and os.path.exists(oldfile2)):
                #        filepath = os.path.dirname(str(table.iloc[i]["fq1"]))
                #        filepath2 = os.path.dirname(str(table.iloc[i]["fq2"]))
                #        print(oldfile1)
                #        print(oldfile2)
                            sample = table.iloc[i]["sample"]
                            unit = str(table.iloc[i]["unit"])
                            condition = table.iloc[i]["condition"]
                            length1 = str(1)
                            length2 = str(2)
                    #        print(sample, unit, condition, length1, length2)
                            newfile1 = filepath + "/"+ sample + "_" + condition + "_Rep" + unit + "_R" + length1 + ".fastq"
                            newfile2 = filepath + "/"+ sample + "_" + condition + "_Rep" + unit + "_R" + length2 + ".fastq"
                            rename(oldfile1, newfile1)
                            rename(oldfile2, newfile2)
                            rename_dict = dict()
                            rename_dict[oldfile1] = newfile1
                            rename_dict[oldfile2] = newfile2
                    #        print(rename_dict)
                            with open("rename_filenames.csv", 'w') as rf:
                                root = csv.writer(rf, delimiter='\t')
                                root.writerow(["Old_Name", "New_Name"])
                                for i,j in rename_dict.items():
                                    root.writerow([i, j])
                        else:
                            print("Fastq files doesn't exist in the folder! Check the table!", file=open('rename_check.txt', 'w'))
            else:
                pass
# =============================================================================
#     if len(table.columns) == 4:
#         oldfile = str(table.iloc[i]["fq1"])
# #        filepath = os.path.dirname(str(table.iloc[i]["fq1"]))
# #        print(oldfile)
#         sample = table.iloc[i]["sample"]
#         unit = str(table.iloc[i]["unit"])
#         condition = table.iloc[i]["condition"]
#         length = str(1)
# #        print(sample, unit, condition, length)
#         newfile = filepath + "/"+ sample + "_" + condition + "_Rep" + unit + "_R" + length + ".fastq"
#         rename(oldfile, newfile)
#         rename_dict = dict()
#         rename_dict[oldfile] = newfile
# #        print(rename_dict)
#         with open("rename_filenames.csv", 'w') as rf:
#             root = csv.writer(rf, delimiter='\t')
#             root.writerow(["Old_Name", "New_Name"])
#             for i,j in rename_dict.items():
#                 root.writerow([i, j])
#     elif len(table.columns) == 5:
#         oldfile1 = str(table.iloc[i]["fq1"])
#         oldfile2 = str(table.iloc[i]["fq2"])
# #        filepath = os.path.dirname(str(table.iloc[i]["fq1"]))
# #        filepath2 = os.path.dirname(str(table.iloc[i]["fq2"]))
# #        print(oldfile1)
# #        print(oldfile2)
#         sample = table.iloc[i]["sample"]
#         unit = str(table.iloc[i]["unit"])
#         condition = table.iloc[i]["condition"]
#         length1 = str(1)
#         length2 = str(2)
# #        print(sample, unit, condition, length1, length2)
#         newfile1 = filepath + "/"+ sample + "_" + condition + "_Rep" + unit + "_R" + length1 + ".fastq"
#         newfile2 = filepath + "/"+ sample + "_" + condition + "_Rep" + unit + "_R" + length2 + ".fastq"
#         rename(oldfile1, newfile1)
#         rename(oldfile2, newfile2)
#         rename_dict = dict()
#         rename_dict[oldfile1] = newfile1
#         rename_dict[oldfile2] = newfile2
# #        print(rename_dict)
#         with open("rename_filenames.csv", 'w') as rf:
#             root = csv.writer(rf, delimiter='\t')
#             root.writerow(["Old_Name", "New_Name"])
#             for i,j in rename_dict.items():
#                 root.writerow([i, j])
# =============================================================================

        #df = pd.DataFrame(rename_dict.items(), columns=["Old_fileame", "New_filename"])
#print(df)
#==============================================================================
#         with open('renamed_samples.txt', 'w') as renamefile:
#             for k, v in rename_dict.items():
#                 renamefile.write( k +'--'+ str(v) +" \n" )
#==============================================================================
#        rename(oldfile, newfile)

        
#==============================================================================
#     print(table.iloc[i]["fq1"])
#     print(i)
#==============================================================================
#==============================================================================
#     if len(table.columns) == 4:
#         oldfile = os.path.basename(str(table.iloc[i][3]))
#         print(oldfile)
#==============================================================================
        
#        rename(oldfile, newfile)
