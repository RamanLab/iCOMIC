# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 19:40:45 2020

@author: malvika
Takes MAF file and results path as input and runs cTAG and saves results
"""
import os
import argparse
import logging
import os
import posixpath
import identifyTSGOG as ito
import convertMAF2cTAG as m2c
import createFeatureMat as fm
import callcTaG as cc
import warnings

warnings.filterwarnings('ignore')
# pass arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--ifile', action="store", required=True,
                    help="Name of input maf file")
parser.add_argument('-o', '--outputpath', action="store", required=True,
                    help="Path to save result files")
parser.add_argument('-c', '--ctagpath', action="store", required=True,
                    help="Path to cTaG")
parser.add_argument('-m', '--maxmut', action="store", required=False,
                    help="threshold for maximum number of mutations in a sample",
                    type=int)
parser.add_argument('-p', '--percentile', action="store", required=False,
                    help="Percentile threshold for consensus", type=int)
args = parser.parse_args()
inputfile = args.ifile
resultsPATH = args.outputpath
PATH = os.getcwd().replace(os.sep, posixpath.sep) + args.ctagpath
maxmut = args.maxmut
perc = args.percentile

#logging.basicConfig(filename= resultsPATH + '/ctag.log', level=logging.INFO)
logging.basicConfig(level=logging.INFO)

# convert MAF file to feature matrix
logging.info("Converting MAF to cTAG feature matrix.")
datactag = m2c.maf2ctag(inputfile, PATH=PATH)
if maxmut is not None:
    features_cd = fm.createFeatMat(datactag, PATH=PATH, maxmutations=maxmut)
else:
    features_cd = fm.createFeatMat(datactag, PATH=PATH)
logging.info("Generated cTAG feature matrix. Feature matrix stored in folder\
             data.")
     
# Run cTaG-CV
logging.info("Running cTAG.")
if perc is not None:
    cc.runcTaG(features_cd, resultsPATH, PATH=PATH, percentile=perc)
else:
    cc.runcTaG(features_cd, resultsPATH, PATH=PATH)
logging.info("Predictions using cTAG completed. Results for individual\
             CV model in CV folder.")
logging.info("Results stored in results folder")
