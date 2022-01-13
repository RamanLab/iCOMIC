import numpy as np
import pandas as pd
import os
import re

test_dir = '/home/priyanka/Desktop/test_env/iCOMIC/Demo_rna/samples/'

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
fq2_all = []
for i in range(len(fq1)):
    fq2_all.append(fq1[i][:-8]+"R2.fastq")

for i in range(len(fq2_all)):
    if fq2_all[i] in fq2:
        pass
    else:
        fq2_all[i] = np.nan

units_file = pd.DataFrame({'sample': sample,
                           'unit': unit,
                           'condition': condition,
                           'fq1': fq1,
                           'fq2': fq2_all})


units_sort = units_file.sort_values(['sample', 'unit', 'condition'])

units_sort.to_csv('units.tsv', sep = '\t', index=False)
