import numpy as np
import pandas as pd
import os
import re

test_dir = '/data/Priyanka/other_pipelines/iCOMIC/Test/Demo_rna/samples/'

fq1 = []
fq2 = []
sample = []
condition = []
unit = []


for file in os.listdir(test_dir):
    if file.endswith(".fastq"):
        f = file
        if re.match('/\w|.+_\w+_Rep\d+_R1|2.fastq$/', f):
            fq1.append(test_dir+file)
            sample_item = re.findall(r'(/\w|.+)_\w+_Rep\d+_R1|2.fastq$/', f)
            for item in sample_item:
                sample.append(item)
            condition_list = re.findall(r'/\w|.+_(\w+)_Rep\d+_R1|2.fastq$/', f)
            for cond in condition_list:
                condition.append(cond)
            unit_list = re.findall(r'/\w|.+_\w+_Rep(\d+)_R1|2.fastq$/', f)
            for i in unit_list:
                unit.append(i)
        elif re.match('/\w|.+_\w+_Rep\d+_R2|1.fastq$/', f):
            fq2.append(test_dir+file)
    else:
        break
        print("something wrong")
#            sample.append(re.findall(r'(/\w|.+)_\w+_Rep\d_R1|2.fastq$/', f))
fq2_all = []
for i in range(len(fq1)):
    fq2_all.append(fq1[i][:-8]+"R2.fastq")

for i in range(len(fq2_all)):
    if fq2_all[i] in fq2:
        pass
    else:
        fq2_all[i] = np.nan
#print(fq1)

# =============================================================================
# print(fq1)
# print(fq2)
# print(sample)
# print(condition)
# print(np.unique(sample))
# =============================================================================
#samples_file = pd.DataFrame({'sample': np.unique(sample)})
units_file = pd.DataFrame({'sample': sample,
                           'unit': unit,
                           'condition': condition,
                           'fq1': fq1,
                           'fq2': fq2_all})
#for i in range(len(units_file)):
#    if units_file['condition'][i] in units_file['fq1'][i]:
##        print('match fq1')
#        pass
#    elif not units_file['condition'][i] in units_file['fq1'][i]:
##        print('mismatch fq1')
#        temp = units_file['fq1'][i]
#        units_file['fq1'][i]=units_file['fq1'][i+1]
#        units_file['fq2'][i+1]=temp
#    if units_file['condition'][i] in units_file['fq2'][i]:
##        print('match fq2')
#        pass
#    elif not units_file['condition'][i] in units_file['fq2'][i]:
##        print('mismatch fq2')
#        temp = units_file['fq2'][i]
#        units_file['fq2'][i]=units_file['fq2'][i+1]
#        units_file['fq2'][i+1]=temp
# =============================================================================
# for i in range(len(units_file)):
#     for item in fq1:
#         if units_file['sample'][i]+"_"+units_file['condition'][i]+"_Rep"+units_file['unit'][i]+"R1.fastq" in item:
#             units_file['fq1'][i]== item
#         else:
#             print('wrong')
#     for item in fq2:
#         if units_file['sample'][i]+"_"+units_file['condition'][i]+"_Rep"+units_file['unit'][i]+"R2.fastq" in item:
#             units_file['fq1'][i]== item
#         else:
#             pass
# =============================================================================
# =============================================================================
#
# for i in range(len(units_file)):
#     if len(fq1) == len(fq2):
#         units_file['fq2'][i] == units_file['fq1'][i][:-8]+"R2.fastq"
#     else:
#         if not units_file['fq1'][i][:-8]+"R2.fastq" in fq2:
#             units_file['fq2'][i] == np.nan
# =============================================================================


units_sort = units_file.sort_values(['sample', 'unit', 'condition'])

#units_file.to_csv('units_unsorted.tsv', sep = '\t', index=False)
units_sort.to_csv('units.tsv', sep = '\t', index=False)
#samples_file.to_csv('samples.tsv', sep = '\t', index=False)
# =============================================================================
# print(units_file)
# =============================================================================
#print(conditon_list)


# =============================================================================
#         print(file)
#         if file[-7] == '1':
#             fq1.append(test_dir+file)
#         else:
#             fq2.append(test_dir+file)
# =============================================================================
# =============================================================================
# print(fq1)
# print(fq2)
#
# =============================================================================


