#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 16:58:41 2018

@author: malvika
"""

import os
import glob
import pickle
import numpy as np
import identifyTSGOG as ito
import pandas as pd

def createFeatMat(dataCosmic, PATH, maxmutations=2000):
    """
    Creates feature matrix from data
    
    Arguments:
        dataCosmic
        PATH = Path to cTaG

    Returns:
        features_cd = DataFrame with genes and calculation of all features
                      values
    """
    DATAPATH = PATH + "/data"

    # Filters samples that are hypermutated
    dataCosmic = ito.filterSamples(dataCosmic, numMutations=maxmutations)

    # Find splicing mutations
    os.chdir(DATAPATH)
    SSitefile = "SpliceSites.txt"
    spliceSite = ito.getSplicingMut(dataCosmic, SSitefile)
    dataCosmic["SpliceSite"] = spliceSite
    splIdx = dataCosmic[dataCosmic["Mutation Description"] == "Splice"].index
    dataCosmic.loc[splIdx, "SpliceSite"] = 'yes'

    # Block of lines to be executed only to retain genes mutated in at least
    # 10 percent of the samples (ver 5)
    status = True
    perc_samps = 10
    tot_samps = len(set(dataCosmic["ID_sample"]))
    dataFiltered = pd.DataFrame(columns=dataCosmic.columns)
    if status:
        for gene in set(dataCosmic["Gene name"]):
            temp = dataCosmic[dataCosmic["Gene name"] == gene]
            uni_samps = len(set(temp["ID_sample"]))
#            print("{} : {}".format(gene, uni_samps))
            if uni_samps >= perc_samps * tot_samps / 100:
                dataFiltered = pd.concat([dataFiltered, temp])
    dataCosmic = dataFiltered.copy()

    # read TSG and OG gene lists
    os.chdir(DATAPATH)
    TSGfile = "onlyTSG.txt"
    OGfile = "onlyOG.txt"
    with open(TSGfile) as f:
        TSGlist = [tsg.strip() for tsg in f.readlines()]
    with open(OGfile) as f:
        OGlist = [og.strip() for og in f.readlines()]

    dataCosmic.replace({'PP2_prob1': '.'}, np.nan, inplace=True)
    dataCosmic = dataCosmic.astype({'PP2_prob1': float})
    # Create multiple feature matrices for different MAX_MULTIPLIER
    max_mulultiplier = 2
    # Create feature matrix
    features_cd = ito.getCdMutFeatures_v2(dataCosmic, max_mulultiplier)

    # Labels for all genes
    Label = [None] * len(features_cd)
    for idx, gene in enumerate(features_cd.index):
        if gene in TSGlist:
            Label[idx] = "TSG"
        elif gene in OGlist:
            Label[idx] = "OG"
        else:
            Label[idx] = "Neutral"
    # for all feature matrix versions
    features_cd["Label"] = Label

#    # save as pickle and also write as a csv file
#    # TODO: change the path to where you want the files to be saved
#    os.chdir(DATAPATH)
#    featFName = "OralFeat_v5_maxmul{:03d}.txt".format(max_mul)
#    features_cd.to_csv(featFName, sep='\t')
#    os.chdir(DATAPATH + "/FeatureMat/oral")
#    featFName = "OralFeat_v5_maxmul{:03d}.pkl".format(max_mul)
#    with open(featFName, 'wb') as f:
#        pickle.dump(features_cd, f)
    return features_cd