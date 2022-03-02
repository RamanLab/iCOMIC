import pandas as pd
import zipfile
import os
from snakemake.utils import validate

report: "../report/workflow.rst"


###### Config file and sample sheets #####
configfile: "config.yaml"
#validate(config, schema="../schemas/config.schema.yaml")

samples = pd.read_table(config["samples"]).set_index("sample", drop=False)

units = pd.read_table(config["units"], dtype=str).set_index(["sample", "unit", "condition"], drop=False)
units.index = units.index.set_levels([i.astype(str) for i in units.index.levels])  # enforce str in index


##### Wildcard constraints ######
wildcard_constraints:
    vartype="snvs|indels",
    sample="|".join(samples.index),
    unit="|".join(units["unit"]),
    condition = "|".join(units["condition"])
    
#### Helper functions #####


def get_fastq(wildcards):
    """Get fastq files of given sample-unit."""
    if os.path.exists("results_dna/trimmed"):
        if not is_single_end(**wildcards):
            return expand("results_dna/trimmed/{sample}-{unit}-{condition}.{group}.fastq.gz",
                          group=[1, 2], **wildcards)
        # single end sample
        return "results_dna/trimmed_se/{sample}-{unit}-{condition}.fastq.gz".format(**wildcards)
    else:
        return units.loc[(wildcards.sample, wildcards.unit, wildcards.condition), ["fq1", "fq2"]].dropna()
        if len(fastqs) == 2:
            return {"r1": fastqs.fq1, "r2": fastqs.fq2}
        return {"r1": fastqs.fq1}

def get_trimmed(wildcards):
    if not is_single_end(**wildcards):
        # paired-end sample
        return expand("results_dna/trimmed/{sample}-{unit}-{condition}.{group}.fastq.gz",
                      group=[1, 2], **wildcards)
    # single end sample
    return "results_dna/trimmed_se/{sample}-{unit}-{condition}.fastq.gz".format(**wildcards)          

    
def is_single_end(sample, unit, condition):
    """Return True if sample-unit is single end."""
    return pd.isnull(units.loc[(sample, unit, condition), "fq2"])

def get_read_group(wildcards):
    """Denote sample name and platform in read group."""
    return  config['params']['BWA_MEM'] + r" -R '@RG\tID:{sample}\tSM:{sample}-{unit}-{condition}\tPL:{platform}'".format(
        sample=wildcards.sample,
        unit=wildcards.unit,
        condition=wildcards.condition,
        platform="ILLUMINA") 
        
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

       
                
def get_read_group_gem3(wildcards):
    """Denote sample name and platform in read group."""
    return r" -r '@RG\tID:{sample}\tSM:{sample}-{unit}-{condition}\tPL:{platform}'".format(
        sample=wildcards.sample,
        unit=wildcards.unit,
        condition=wildcards.condition,
        platform="ILLUMINA")  

    
def get_sample_bams(wildcards):
    """Get all aligned reads of given sample."""
    return expand("results_dna/recal/{sample}-{unit}-{condition}.bam",
                  sample=wildcards.sample,
                  unit=units.loc[wildcards.sample].unit,
                  condition=units.loc[wildcards.sample, wildcards.unit].condition)
                 
def get_sample_bams_a(wildcards):
    """Get all aligned reads of given sample."""
    return expand("results_dna/recal/{sample}-{unit}-{condition}.bam",
                  sample=wildcards.sample,
                  unit=wildcards.unit,
                  condition=units.loc[wildcards.sample, wildcards.unit].condition)
                 
                  
def get_sample_bais(wildcards):
    """Get all aligned reads of given sample."""
    return expand("results_dna/mapped/{sample}-{unit}-{condition}.sorted.bam.bai",
                  sample=wildcards.sample,
                  unit=wildcards.unit,
                  condition=units.loc[wildcards.sample, wildcards.unit].condition)
                  

def get_sample_bais_rg(wildcards):
    """Get all aligned reads of given sample."""
    return expand("results_dna/dedup_rgadded/_{sample}-{unit}-{condition}.sorted.bam.bai",
                  sample=wildcards.sample,
                  unit=wildcards.unit,
                  condition=units.loc[wildcards.sample, wildcards.unit].condition)                  


def get_indelrealign_input(wildcards):
    """Get all aligned reads of given sample."""
    return expand("results_dna/realign/{sample}-{unit}-{condition}.intervals",
                  sample=wildcards.sample,
                  unit=units.loc[wildcards.sample].unit,
                  condition=units.loc[wildcards.sample, wildcards.unit].condition)
                  
def get_recal_bcf_input(wildcards):
    """Get all aligned reads of given sample."""
    return expand("results_dna/realign/{sample}-{unit}-{condition}.bam",
                  sample=wildcards.sample,
                  unit=units.loc[wildcards.sample].unit,
                  condition=units.loc[wildcards.sample, wildcards.unit].condition)

def is_normal(sample, unit, condition):
    return units.loc[(sample, unit, condition), "condition"] == "normal"

def get_sample_bams_normal_old(wildcards):
    """Get all aligned normal reads of given sample."""
    if (units.loc[(wildcards.sample, wildcards.unit, wildcards.condition), "condition"]) == "normal":
        return expand("results_dna/mapped/{sample}-{unit}-{condition}.sorted.bam",
                      sample=wildcards.sample,
                      unit=units.loc[wildcards.sample].unit,
                      condition = units.loc[wildcards.sample, wildcards.unit].condition)  
                      
def get_sample_bams_normal(wildcards):
    """Get all aligned normal reads of given sample."""
    return expand("results_dna/dedup_rgadded/_{sample}-{unit}-normal.sorted.bam",
                  sample=wildcards.sample,
                  unit=wildcards.unit)
      
                      
def get_sample_bams_tumor_old(wildcards):
    """Get all aligned reads of given sample."""
    if (units.loc[(wildcards.sample, wildcards.unit, wildcards.condition), "condition"]) == "tumor":
        return expand("results_dna/mapped/{sample}-{unit}-{condition}.sorted.bam",
                      sample=wildcards.sample,
                      unit=units.loc[wildcards.sample].unit,
                      condition = units.loc[wildcards.sample, wildcards.unit].condition)
    

def get_sample_bams_tumor(wildcards):
    """Get all aligned reads of given sample."""
    return expand("results_dna/dedup_rgadded/_{sample}-{unit}-tumor.sorted.bam",
                  sample=wildcards.sample,
                  unit=wildcards.unit)

def get_sample_id_normal(wildcards):
    return expand("{sample}-{unit}-{condition}",
        sample=wildcards.sample,
        unit=wildcards.unit,
        condition ="normal")
        
def get_sample_id_tumor(wildcards):
    return expand("{sample}-{unit}-{condition}",
        sample=wildcards.sample,
        unit=wildcards.unit,
        condition ="tumor")
                  
def get_bam(wildcards):
    """Get all aligned reads of given sample."""
    return units.loc[(wildcards.sample, wildcards.unit), ["condition"]].dropna()
    if len(condition) == len(units.loc[(wildcards.sample, wildcards.unit), ["condition"]]):
        return {"normal": expand("results_dna/mapped/{sample}-{unit}-normal.sorted.bam",
                  sample=wildcards.sample,
                  unit=units.loc[wildcards.sample].unit),
                  "tumor": expand("results_dna/mapped/{sample}-{unit}-tumor.sorted.bam",
                  sample=wildcards.sample,
                  unit=units.loc[wildcards.sample].unit)}
    return expand("results_dna/mapped/{sample}-{unit}-{condition}.sorted.bam",
                  sample=wildcards.sample,
                  unit=units.loc[wildcards.sample].unit,
                  condition = units.loc[wildcards.sample, wildcards.unit].condition)


def get_regions_param(regions=config["processing"].get("restrict-regions"), default=""):
    if regions:
        params = "--intervals '{}' ".format(regions)
        padding = config["processing"].get("region-padding")
        if padding:
            params += "--interval-padding {}".format(padding)
        return params
    return default


def get_call_variants_params(wildcards, input):
    return (get_regions_param(regions=input.regions, default=f"--intervals {wildcards.contig}") +
            config["params"]["gatk"]["HaplotypeCaller"])

def get_multiqc_data():
    if os.path.exists("results_dna/snpeff"):
        return "results_dna/snpeff/all.csv"
    else:
        return "results_dna/bcftools_stats/all.txt"

def get_recal_input(bai=False):
    # case 1: no duplicate removal
    f = "results_dna/mapped/{sample}-{unit}-{condition}.sorted.bam"
    if config["processing"]["remove-duplicates"]:
        # case 2: remove duplicates
        f = "results_dna/dedup/{sample}-{unit}-{condition}.bam"
    if bai:
        if config["processing"].get("restrict-regions"):
            # case 3: need an index because random access is required
            f += ".bai"
            return f
        else:
            # case 4: no index needed
            return []
    else:
        return f

def get_recal_input_rgadded_old(bai=False):
    f = "results_dna/dedup_rgadded/{sample}-{unit}-{condition}.bam"
    return f
    
def get_recal_input_rgadded(bai=False):
    # case 1: no duplicate removal
    f = "results_dna/mapped/{sample}-{unit}-{condition}.sorted.bam"
    if config["processing"]["remove-duplicates"]:
        # case 2: remove duplicates
        f = "results_dna/dedup_rgadded/{sample}-{unit}-{condition}.bam"
    if bai:
        if config["processing"].get("restrict-regions"):
            # case 3: need an index because random access is required
            f += ".bai"
            return f
        else:
            # case 4: no index needed
            return []
    else:
        return f
