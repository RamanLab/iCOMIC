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
 
print(test_data_dir)

print("you are executing script in " + test_data_dir)

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


#### Helper functions #####

def get_fastq(wildcards):
    """Get fastq files of given sample-unit."""
    if os.path.exists("results_dna/trimmed"):
        if not is_single_end(**wildcards):
            return expand("results_dna/trimmed/{sample}-{unit}-{condition}.{group}.fastq.gz",
                          group=[1, 2], **wildcards)
        # single end sample
        return "results_dna/trimmed/{sample}-{unit}-{condition}.fastq.gz".format(**wildcards)
    else:
        return units.loc[(wildcards.sample, wildcards.unit, wildcards.condition), ["fq1", "fq2"]].dropna()
        if len(fastqs) == 2:
            return {"r1": fastqs.fq1, "r2": fastqs.fq2}
        return {"r1": fastqs.fq1}
   
def is_single_end(sample, unit, condition):
    """Return True if sample-unit is single end."""
    return pd.isnull(units.loc[(sample, unit, condition), "fq2"])