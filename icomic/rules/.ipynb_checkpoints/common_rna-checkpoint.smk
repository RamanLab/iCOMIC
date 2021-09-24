################# Running Test Data ###########################

shell.prefix("set +o pipefail; ")
import re
import pandas as pd
import yaml
from snakemake.utils import validate, min_version
from snakemake.io import expand
from snakemake.utils import R
from snakemake.io import glob_wildcards
from os.path import join
shell.executable("/bin/bash")
shell.prefix("source ~/.bashrc; ")

###### set minimum snakemake version #####

min_version("5.1.2")

####### load config and sample sheets #####

with open("config.yaml", 'r') as ymlfile:
   config = yaml.safe_load(ymlfile)

configfile: "config.yaml"
#validate(config, schema="schemas/config.schema.yaml")
print(config)

test_data_dir = config["sample"]

#test_data_dir = "/data/Priyanka/other_pipelines/iCOMIC" 
#test_data_dir = "/data/Priyanka/other_pipelines/iCOMIC" 
#test_data_dir = "/data/Priyanka/other_pipelines/iCOMIC" 
#test_data_dir = "/data/Priyanka/other_pipelines/iCOMIC" 
print(test_data_dir)

print("you are executing script in" + test_data_dir)

#print (glob_wildcards(test_data_dir+ "{sample}_{condition}_Rep{rep}_R{len}.fastq"))

(samples, type, reps, lens)=glob_wildcards(test_data_dir+"/{sample}_{condition}_Rep{rep}_R{len}.fastq")

samples=sorted(list(set(samples)))
#print(samples)
regex = re.compile(r'cutadapt')
samples = [i for i in samples if not regex.search(i)]
print(samples)
type=sorted(list(set(type)))
#print(type)
reps=sorted(list(set(reps)))
#print(reps)
regex = re.compile(r'cutadapt')
reps = [i for i in reps if not regex.search(i)]
print(reps)
lens=sorted(list(set(lens)))
print(lens)
