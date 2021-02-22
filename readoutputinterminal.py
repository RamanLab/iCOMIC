#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 16:25:32 2019

@author: anjana
"""

import subprocess
import tempfile
from contextlib import redirect_stdout

#with tempfile.TemporaryFile() as tempf:
#    proc = subprocess.Popen(["snakemake", "--use-conda"], stdout=tempf)
#    proc.wait()
#    print(tempf.read())
    
#pipe = subprocess.Popen("pwd", shell=True, stdout=subprocess.PIPE).stdout
#output = pipe.read()

file_ = open("output.txt", "a")
subprocess.Popen(["snakemake", "--use-conda"], stdout=file_)

#with open('help.txt', 'a') as f:
#    with redirect_stdout(f):
#        print(subprocess.run(["snakemake", "--use-conda"]))

#ret_val = subprocess.Popen( run_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True )
#output, errors = ret_val.communicate()
#log_file.write(output)
#print output
