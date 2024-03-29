
import os
from snakemake.utils import validate

report: "../report/workflow.rst"

################# Running Test Data ###########################

shell.prefix("set +o pipefail; ")
import re
import pandas as pd
import yaml
import zipfile
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

 
print(test_data_dir)

print("you are executing script in " + test_data_dir)


(samples, type, reps, lens)=glob_wildcards(test_data_dir+"/{sample}_{condition}_Rep{rep}_R{len}.fastq")

samples=sorted(list(set(samples)))
regex = re.compile(r'cutadapt')
samples = [i for i in samples if not regex.search(i)]
print(samples)
type=sorted(list(set(type)))
reps=sorted(list(set(reps)))
regex = re.compile(r'cutadapt')
reps = [i for i in reps if not regex.search(i)]
print(reps)
lens=sorted(list(set(lens)))
print(lens)


units = pd.read_table(config["units"], dtype=str).set_index(["sample", "unit", "condition"], drop=False)
units.index = units.index.set_levels([i.astype(str) for i in units.index.levels])  # enforce str in index

#### Helper functions #####

def get_fastq(wildcards):
    """Get fastq files of given sample-unit."""
    if os.path.exists("results/cutadapt"):
        if not is_single_end(**wildcards):
            return expand("results/cutadapt/{sample}_{condition}_Rep{rep}_R{group}.fastq",
                          group=[1, 2], **wildcards)
        # single end sample
        return "results/cutadapt_se/{sample}_{condition}_Rep{rep}.fastq".format(**wildcards)
    else:
        return units.loc[(wildcards.sample, wildcards.rep, wildcards.condition), ["fq1", "fq2"]].dropna()
        if len(fastqs) == 2:
            return {"r1": fastqs.fq1, "r2": fastqs.fq2}
        return {"r1": fastqs.fq1}

def get_trimmed(wildcards):
    if not is_single_end(**wildcards):
        # paired-end sample
        return expand("results/cutadapt/{sample}_{condition}_Rep{rep}_R{group}.fastq",
                      group=[1, 2], **wildcards)
    # single end sample
    return "results/cutadapt_se/{sample}_{condition}_Rep{rep}.fastq".format(**wildcards)
    
def is_single_end(sample, rep, condition):
    """Return True if sample-unit is single end."""
    return pd.isnull(units.loc[(sample, rep, condition), "fq2"])


def get_fastq_data(path):
    file_list = []
    name_list = []
    for file in os.listdir(path):
        if file.endswith('zip'):
            file_list.append(file)
            for file_ in file_list:
                filepath = path + file_
                zip_file = zipfile.ZipFile(filepath)
                for names in zip_file.namelist():
                    zip_file.extract(names,path)
                    if names.endswith('.txt'):
                        input = path + names
                    else:
                        pass
            name_list.append(input)
        else:
            pass
    return name_list









