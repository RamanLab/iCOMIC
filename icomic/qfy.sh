#!/bin/bash

python2.7 /data/Priyanka/hap.py-build/bin/qfy.py --threads 10 -t ga4gh /data/Priyanka/other_pipelines/iCOMIC/benchmark_data/benchmark_ga4gh/output.vcf.gz -f /data/Priyanka/other_pipelines/iCOMIC/benchmark_data/ConfidentRegions.bed.gz -o /data/Priyanka/other_pipelines/iCOMIC/benchmark_data/hap_results/happy2 -r /data/Priyanka/other_pipelines/iCOMIC/ref/hg38.fa --roc QUAL
