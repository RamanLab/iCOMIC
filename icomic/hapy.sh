#!/bin/bash
python2.7 /data/Priyanka/hap.py-build/bin/hap.py --threads 20 -t ga4gh in_vcf /data/Priyanka/other_pipelines/iCOMIC/benchmark_data/benchmark_ga4gh/output.vcf.gz -f /data/Priyanka/other_pipelines/iCOMIC/benchmark_data/ConfidentRegions.bed.gz -o /data/Priyanka/other_pipelines/iCOMIC/benchmark_data/hap_results/happy1 -r /data/Priyanka/other_pipelines/iCOMIC/ref/hg38.fa
