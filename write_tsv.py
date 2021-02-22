import numpy as np
import pandas as pd
import os
import re

test_dir = '/data/Priyanka/other_pipelines/iCOMIC/sample_demo/'

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
        elif re.match('/\w|.+_\w+_Rep\d_R2|1.fastq$/', f):
            fq2.append(test_dir+file)

    else:
        break
        print("something wrong")
#            sample.append(re.findall(r'(/\w|.+)_\w+_Rep\d_R1|2.fastq$/', f))

if len(fq2) == 0:
    fq2 = np.full(len(fq1), np.nan).tolist()
elif len(fq1) == len(fq2):
    pass
# =============================================================================
# print(fq1)
# print(fq2)
# print(sample)
# print(condition)
# print(np.unique(sample))
# =============================================================================
samples_file = pd.DataFrame({'sample': np.unique(sample)})
units_file = pd.DataFrame({'sample': sample,
                           'unit': unit,
                           'condition': condition,
                           'fq1': fq1,
                           'fq2': fq2})

for i in range(len(units_file)):
    if units_file['condition'][i] in units_file['fq1'][i]:
#        print('match fq1')
        pass
    elif not units_file['condition'][i] in units_file['fq1'][i]:
#        print('mismatch fq1')
        temp = units_file['fq1'][i]
        units_file['fq1'][i]=units_file['fq1'][i+1]
        units_file['fq1'][i+1]=temp
    if not str(units_file['fq2'][i]) == 'nan':
        if units_file['condition'][i] in units_file['fq2'][i]:
    #        print('match fq2')
            pass
        elif not units_file['condition'][i] in units_file['fq2'][i]:
    #        print('mismatch fq2')
            temp = units_file['fq2'][i]
            units_file['fq2'][i]=units_file['fq2'][i+1]
            units_file['fq2'][i+1]=temp
    else:
        pass
units_file.to_csv('units.tsv', sep = '\t', index=False)
samples_file.to_csv('samples.tsv', sep = '\t', index=False)
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

