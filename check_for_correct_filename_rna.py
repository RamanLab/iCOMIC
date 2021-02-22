import os
import re

test_dir = '/data/Priyanka/other_pipelines/iCOMIC/samp'

if not any (file.endswith(".fastq") for file in os.listdir(test_dir)):
    print("No fastq files in the folder!", file=open('name_check.txt', 'w'))
else:
    for file in os.listdir(test_dir):
        if (file.endswith(".fastq")):
            f = file
            if re.match('/\w|.+_\w+_Rep\d_R1|2.fastq$/', f):
                continue
            elif re.match('/\w|.+_\w+_Rep\d_R2|1.fastq$/', f):
                continue
            else:
                print("Sample filenames not in specified format! Rename!", file=open('name_check.txt', 'w'))
        else:
            pass





