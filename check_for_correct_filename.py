import numpy as np
import pandas as pd
import os
import re

test_dir = '/data/anjana/tumornormal/bam_split'

for file in os.listdir(test_dir):
    if file.endswith(".fastq"):
        f = file
        if re.match('/\w|.+_\w+_Rep\d_R1|2.fastq$/', f):
            continue
        elif re.match('/\w|.+_\w+_Rep\d_R2|1.fastq$/', f):
            continue
        else:
            print("Sample filenames not in specified format! Rename!", file=open('name_check.txt', 'w'))














