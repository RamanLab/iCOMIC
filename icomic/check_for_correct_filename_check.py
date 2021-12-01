import numpy as np
import pandas as pd
import os
import re

test_dir = '/home/priyanka/Desktop/test_env/iCOMIC/Demo_dna/somatic_samples/'

if not any (file.endswith(".fastq") for file in os.listdir(test_dir)):
    print("No fastq files in the folder!", file=open('name_check.txt', 'w'))
else:
    for file in os.listdir(test_dir):
        if (file.endswith(".fastq")):
            f = file
            if re.match('/\w|.+_\w+_Rep\d+_R1|2.fastq$/', f):
                continue
            elif re.match('/\w|.+_\w+_Rep\d+_R2|1.fastq$/', f):
                continue
            else:
                print("Sample filenames not in specified format! Rename!", file=open('name_check.txt', 'w'))
        else:
            pass

# =============================================================================
# for file in os.listdir(test_dir):
#     if not any (file.endswith(".fastq")):
#         print("No fastq files in the folder!", file=open('name_check.txt', 'w'))
#     elif file.endswith(".fastq"):
#         f = file
#         if re.match('/\w|.+_\w+_Rep\d_R1|2.fastq$/', f):
#             continue
#         elif re.match('/\w|.+_\w+_Rep\d_R2|1.fastq$/', f):
#             continue
#         else:
#             print("Sample filenames not in specified format! Rename!", file=open('name_check.txt', 'w'))
# =============================================================================














