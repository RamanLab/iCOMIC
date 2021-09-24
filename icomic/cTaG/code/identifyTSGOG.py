#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 14:53:09 2017

@author: malvika
Contains all functions required for indentification of driver genes
path = "/home/malvika/Documents/code/IdentificationOfTSG-OG/data/COSMIC/v79/"
filename= "CosmicWGS_MutantExport.tsv"
filename = "dummy_allmut.tsv"
filename = path + filename
"""
import pandas as pd
import re
import numpy as np
from sklearn.metrics import accuracy_score, f1_score, precision_score
from sklearn.metrics import recall_score


def parseCDmutCosmic(filename, data=None):
    """
    Arguments:
        filename = string of file to be read
        data = dataframe containing data that need to be updated.
               Default is None
    Returns:
        data = dataframe containg gene information
    """
    # Checks if data passed and of correct dimensions
    col_values = ["Gene name", "Accession Number", "Gene CDS length",
                  "HGNC ID", "Sample name", "ID_sample", "ID_tumour",
                  "Primary site", "Site subtype 1", "Site subtype 2",
                  "Site subtype 3", "Primary histology", "Histology subtype 1",
                  "Histology subtype 2", "Histology subtype 3",
                  "Genome-wide screen", "Mutation ID", "Mutation CDS",
                  "Mutation AA", "Mutation Description", "Mutation zygosity",
                  "LOH", "GRCh", "Mutation genome position", "Mutation strand",
                  "SNP", "Resistance Mutation", "FATHMM prediction",
                  "FATHMM score", "Mutation somatic status", "Pubmed_PMID",
                  "ID_STUDY", "Sample source", "Tumour origin", "Age"]
    if data is not None:
        if list(data.columns.values) != col_values:
            print("Data columns do not match")
            return
    else:
        data = pd.DataFrame(columns=col_values)
    for chunk in pd.read_csv(filename, sep='\t', header=0, low_memory=False,
                             chunksize=10**6):
        data = pd.concat([data, chunk])
    return data


def getSampleIDs(data):
    """
    Function to get uniques sample IDs from COSMIC data
    Arguments:
        data = dataframe containing COSMIC data
    Returns:
        list of unique sample IDs
    """
    return list(set(data["ID_sample"]))


def getMutationIDs(data):
    """
    Function to get uniques mutation IDs from COSMIC data
    Arguments:
        data = dataframe containing COSMIC data
    Returns:
        list of unique mutation IDs
    """
    return list(set(data["Mutation ID"]))


def getMutationTypes(data):
    """
    Function to get uniques mutation types from COSMIC data
    Arguments:
        data = dataframe containing COSMIC data
    Returns:
        list of unique mutation types
    """
    return list(set(data["Mutation Description"]))


def getPrimarySites(data):
    """
    Function to get uniques primary site types from COSMIC data
    Arguments:
        data = dataframe containing COSMIC data
    Returns:
        list of unique primary site types
    """
    return list(set(data["Primary site"]))


def getNumMutations(data):
    """
    Function to retrieve number of mutations for each sample ID
    Arguments:
        data = dataframe containing COSMIC data
    Returns:
        sampleuni = list of unique sample IDs
        samplecount = list of counts corresponding to unique samples
    """
    # Get unique sample ids
    sampleuni = list(set(data["ID_sample"]))
    # Initialise list to store count
    samplecount = [0] * len(sampleuni)
    # Get list of sample ids(not unique)
    sampleids = list(data["ID_sample"])
    # For each sample id in list
    for i, sample in enumerate(sampleids):
        # Find the corresponding index of sample in list of unique samples
        idx = sampleuni.index(sample)
        # At the same index increase count by 1
        samplecount[idx] = samplecount[idx] + 1
    return [sampleuni, samplecount]


def filterSamples(data, numMutations=2000):
    """
    Function to filter samples that have more than numMutations number of
    mutations
    Arguments:
        data = dataframe containing COSMIC data
        numMutations = int number of mutations to be taken as threshold
    """
    [sampleuni, samplecount] = getNumMutations(data)
    filterSamples = [samp for samp, count in zip(sampleuni, samplecount) if
                     count > numMutations]
    for sample in filterSamples:
        data = data[(data["ID_sample"] != sample)]
    return data


def keep(data):
    """
    Keeps only relevant rows
    Arguments:
        data = dataframe containing COSMIC data
    Returns:
        data = filtered data
    """
    # Keep rows without missing data
    data = data[pd.notnull(data["Gene name"])]
    data = data[pd.notnull(data["Gene CDS length"])]
    data = data[pd.notnull(data["Mutation ID"])]
    data = data[pd.notnull(data["Mutation Description"])]
    # Drop rows if known SNP
    data = data[(data.SNP != 'y')]
    # Keep if genome wide screen
    data = data[(data["Genome-wide screen"] == 'y')]
    # Drop row if mutation type is unknown or whole gene deletion
    data = data[(data["Mutation Description"] != 'Unknown')]
    data = data[(data["Mutation Description"] != 'Whole gene deletion')]
    # Keep only one entry for duplicate mutations
    data = data.drop_duplicates(subset=["Mutation ID"])
    # Keep only complete missense mutations and other mutation types
    data = data[~((data["Mutation Description"] == 'Substitution - Missense') &
                  (data["Mutation CDS"] == 'c.?'))]
    data = data[~((data["Mutation Description"] == 'Substitution - Missense') &
                pd.isnull(data["GRCh"]))]
    data = data[~((data["Mutation Description"] == 'Substitution - Missense') &
                pd.isnull(data["Mutation genome position"]))]
    data = data.reset_index(drop=True)
    return data


def keep_v2(data):
    """
    Keeps only relevant rows
    Arguments:
        data = dataframe containing COSMIC data
    Returns:
        data = filtered data
    """
    # Filter data to keep rows only if following columns are not emplty
    data = data[pd.notnull(data["Gene name"])]
    data = data[pd.notnull(data["Gene CDS length"])]
    data = data[pd.notnull(data["Mutation ID"])]
    data = data[pd.notnull(data["Mutation Description"])]
    data = data[pd.notnull(data["GRCh"])]
    data = data[pd.notnull(data["Mutation genome position"])]
    
    # Drop rows if it is not a somatic mutation or not been repaorted as somatic
    # in any other cancer. If a given mutation is present in dbSNP but observed as
    # somatic in any sample, it is retained
    data = data[(data["Mutation somatic status"] == 'Confirmed somatic variant') |
                 (data["Mutation somatic status"] ==
                  'Reported in another cancer sample as somatic')]
    # Keep if genome wide screen
    data = data[(data["Genome-wide screen"] == 'y')]
    # Drop row if mutation type is unknown or whole gene deletion
    data = data[(data["Mutation Description"] != 'Unknown')]
    data = data[(data["Mutation Description"] != 'Whole gene deletion')]
    # Keep only complete missense mutations and other mutation types
    data = data[~(data["Mutation CDS"] == 'c.?')]
    data = data.reset_index(drop=True)
    return data


def getMissenseData(data):
    """
    Keeps only those rows that correspond to missense mutations and are not
    known SNPs.
    Arguments:
        data =  dataframe
    Returns:
        tp_data = dataframe
    """
    # Keep rows that have mutation type as "Substitution - Missense" and if it
    # is not known SNP
    tp_data = data[(data["Mutation Description"] == 'Substitution - Missense')]
    return tp_data


def getHifiMissenseData(data):
    """
    Keeps only those rows that correspond to HiFI missense mutations.
    Arguments:
        data =  dataframe
    Returns:
        tp_data = dataframe
    """
    tp_data = data[(data["Mutation Description"] == 'Substitution - Missense')]
    tp_data = tp_data[(tp_data["PP2_prob1"] >= 0.85)]
    return tp_data


def getFrameshiftData(data):
    """
    Keeps only those rows that correspond to frameshift mutations.
    Arguments:
        data =  dataframe
    Returns:
        fs_data = dataframe
    """
    fs_data = pd.concat([data[(data["Mutation Description"] ==
                               "Deletion - Frameshift")],
                         data[(data["Mutation Description"] ==
                               "Complex - frameshift")],
                         data[(data["Mutation Description"] ==
                               "Insertion - Frameshift")]], ignore_index=True)
    return fs_data


def getNonsenseData(data):
    """
    Keeps only those rows that correspond to nonsense mutations.
    Arguments:
        data =  dataframe
    Returns:
        ns_data = dataframe
    """
    ns_data = data[(data["Mutation Description"] == "Substitution - Nonsense")]
    return ns_data


def getSplicingData(data):
    """
    Keeps only those rows that correspond to splicing mutations.
    Arguments:
        data =  dataframe
    Returns:
        sp_data = dataframe
    """
    sp_data = data[(data["SpliceSite"] == 'yes')]
    return sp_data


def getPolyPhen2input(data, filesize=150000):
    """
    Reads data and creates files needed for PolyPhen2 input. Saves and returns
    file names to be used as input. File size is restricted to 150000.
    Arguments:
        data = dataframe containing COSMIC data
        filesize = int restricting lines in file. Default is 150000.
    Returns:
        filenames = list of file names
    """
    # Keep only missense rows
    tp_data = getMissenseData(data)
    # Initialise required variables
    filenames = []
    compleN = {"A": "T", "T": "A", "G": "C", "C": "G"}
    mutCDS = re.compile('^c\.\d+([ATGC])>([ATGC,]+)$')
    genpos = re.compile('^chr(\d{1,2}|X|Y|M)_?\w*_?\w*:(\d+)-(\d+)$')
    PP2list = []
    # For all rows with GRCh37 values, if value is not None, only then save
    # index and mutation in PolyPhen2 format
    for idx, mut, gen, strand in zip(tp_data.index, tp_data["Mutation CDS"],
                                     tp_data["GRCh37"],
                                     tp_data["Mutation strand"]):
        position = ""
        if gen:
            # Search patterns in respectives rows and retrieve relevant data
            mutation = mutCDS.search(mut)
            genLoc = genpos.search(gen)
            if mutation is not None:
                if int(genLoc.group(2)) == int(genLoc.group(3)):
                    if strand == '-':
                        # Store in temp variable
                        wt_N = compleN[mutation.group(1)]
                        mt_N = compleN[mutation.group(2)]
                        position = ("chr" + genLoc.group(1) + ":" +
                                    genLoc.group(2) + " " + wt_N + "/" + mt_N)
                    else:
                        # Store in temp variable
                        position = ("chr" + genLoc.group(1) + ":" +
                                    genLoc.group(2) + " " + mutation.group(1) +
                                    "/" + mutation.group(2))
                    # Append to list along with index in dataframe data
                    PP2list.append([idx, position])
    # Write into files
    # Get uniques location and mutations as same mutation may be present in
    # multiple samples
    uni_PP2list = list(set([item[1] for item in PP2list]))
    # Calulate number of files to be written for given filesize
    if len(uni_PP2list) % filesize:
        numFiles = (len(uni_PP2list)//filesize) + 1
    else:
        numFiles = (len(uni_PP2list)//filesize)
    # Initialise start and end index in list for first file
    start = 0
    if len(uni_PP2list) < filesize:
        end = len(uni_PP2list)
    else:
        end = filesize
    for i in range(numFiles):
        # initialise filename for PP2 output and add to list of filenames
        filename = "PP2ip" + str(i) + ".txt"
        filenames.append(filename)
        # Write position into file
        with open(filename, 'w') as f:
            for idx in range(start, end):
                f.write(uni_PP2list[idx] + "\n")
            # Initialise start and end index in list for next file
            start = end
            if len(uni_PP2list) < start + filesize:
                end = len(uni_PP2list)
            else:
                end = start + filesize
    return [PP2list, filenames]


def readPolyPhen2output(op_file, PP2list):
    """
    Reads list of files given as output by PolyPhen2 and returns list of
    Pohyphen2 scores and FDR.
    Arguments:
        op_file = list of filenames
        PP2list = output of getPolyPhen2input
    Returns:
        PP2scores
    """
    # Variable concats all files
    pp2file = []
    # Read and store data from files in list
    for filemane in op_file:
        with open(filemane) as f:
            ftemp = [line.strip() for line in f.readlines()]
        pp2file.extend(ftemp)
    # Dict for parsing data and storing PP2 output
    pp2 = dict()
    # Pattern to be processed to get input
    mut_ip = re.compile('^#\s(chr(\d{1,2}|X|Y|M)\:(\d+))\|([ATGC])([ATGC])\|.*\|.*\|.*$')
    # Parse each line fron files
    numfilelinescount = 0
    duplicatelines = 0
    for line in pp2file:
        # Skips headers and comment lines
        if re.search('^#.*$', line):
            notheader = False
        else:
            notheader = True
        # Split line at tabs
        line = line.split("\t")
        if notheader:
            numfilelinescount = numfilelinescount + 1
            # 13th element is matched for pattern
            mut_parse = mut_ip.search(line[13].strip())
            # Matched pattern is converte to PP2 input format
            mut_key = (mut_parse.group(1) + " " + mut_parse.group(4) + "/" +
                       mut_parse.group(5))
            # If the input in not already in dict, creates an entry else
            # appends the probability, FPR and TPR values.
            if mut_key not in pp2.keys():
                if (line[10].strip() != '?' and line[11].strip() != '?' and
                   line[12].strip() != '?'):
                    pp2[mut_key] = [[float(line[10].strip())],
                                    [float(line[11].strip())],
                                    [float(line[12].strip())], line[7].strip(),
                                    line[8].strip(), [line[0].strip()]]
            else:
                duplicatelines = duplicatelines + 1
                if line[0].strip() not in pp2[mut_key][5]:
                    pp2[mut_key][0].append(float(line[10].strip()))
                    pp2[mut_key][1].append(float(line[11].strip()))
                    pp2[mut_key][2].append(float(line[12].strip()))
                    pp2[mut_key][5].append(line[0].strip())
    # Variable to store index, PP2 probabilyt, FPR,TPR, ori_N, mut_N
    PP2scores = []
    count = 0
    for ip in PP2list:
        if ip[1] in pp2.keys():
            count = count + 1
            PP2scores.append([ip[0], pp2[ip[1]][0], pp2[ip[1]][1],
                              pp2[ip[1]][2]])
        else:
            PP2scores.append([ip[0], [np.nan], [np.nan], [np.nan]])
    return PP2scores


def getLiftOverInput(data, fromGRCh, filename=None):
    """
    Converts data from COSMIC file and saves as file that needs to be given as
    input to UCSC LiftOver genome annotation.
    Arguments:
        data = dataframe containing COSMIC data
        fromGRCh = ReferconverListence sequence assembly to cinvert from
    Returns:
        data
    """
    # Index and positions to be given as input to LiftOver
    indices = data.index[(data["GRCh"] == fromGRCh)]
    pos_list = list(data[(data["GRCh"] == fromGRCh)]["Mutation genome position"
                                                     ])
    # Change format of position to suit LiftOver. Chr 23, 24, 25 are X, Y, M
    # respectively. Other chr numbers remain the same.
    genpos = re.compile('^(\d+):(\d+)-(\d+)$')
    for idx, pos in enumerate(pos_list):
        genLoc = genpos.search(pos)
        if int(genLoc.group(1)) == 23:
            pos = "chrX:" + genLoc.group(2) + "-" + genLoc.group(3)
        elif int(genLoc.group(1)) == 24:
            pos = "chrY:" + genLoc.group(2) + "-" + genLoc.group(3)
        elif int(genLoc.group(1)) == 25:
            pos = "chrM:" + genLoc.group(2) + "-" + genLoc.group(3)
        else:
            pos = "chr" + pos
        pos_list[idx] = pos

    # Write in file if filename given
    if filename is not None:
        with open(filename, 'w') as f:
            for pos in pos_list:
                f.write("%s\n" % pos)
    return [indices, pos_list]


def readLiftOverOutput(converFile, errFile, Pos_List):
    """
    Reads the 2 files given by LiftOver as output and processes them.
    Arguments:
        converFile = name of file containing conversions
        errFile:= name of file containing conversion failures
        Pos_List = List of lists. Output returned by getLiftOverInput
            Pos_List[0] =  index of corressponding to data
            Pos_List[1] = list of positions to be converted
    Returns:
        converList = list of converted postitions
        converListIndex = index of converted postitions
        errList = list of positions not converted
    """
    # Assigns values from Pos_List(output from getLiftOverInput)
    [indices, pos_list] = Pos_List
    # Read converted file and parse data into list
    with open(converFile) as f:
        converList = [line.strip() for line in f.readlines()]
    # Read error file and parse data into list
    errList = []
    with open(errFile) as ferr:
        err = ferr.readlines()
        for line in err:
            match = re.search('^#.*', line)
            if not match:
                errList.append(line.strip())
    # Get index for converList by comparing input to error list
    converListIndex = [posidx for pos, posidx in zip(pos_list, indices) if
                       pos not in errList]
    return [converList, converListIndex, errList]


def getMissenseEntropy(gene_data):
    """
    Calculates missense entropy and frequency for a given gene
    Arguments:
        tp_data = DataFrame of missense mutations in given gene
    Returns:
        missenseEntropy
        fi = highest missense frequency
    """
    # get data for only missense mutations
    tp_data = getMissenseData(gene_data)
    if len(tp_data) == 0:
        return [0, 0]
    # Each mutation is defined as (loc, wt_N, mt_N)
    M = dict()
    # n = total number of missense mutations in a gene
    n = len(tp_data)
    # Patterns to be searched in genome position and mutation CDS
    mutCDS = re.compile('^c\.\d+([ATGC])>([ATGC,]+)$')
    genpos = re.compile('^(\d{1,2}_?\w*_?\w*:\d+)-(\d+)$')
    # For each mutation across sample for a given gene
    for loc, mut in zip(tp_data["Mutation genome position"],
                        tp_data["Mutation CDS"]):
        # Get (loc, wt_N, mt_N) by searching pattern
        mut_re = mutCDS.search(mut)
        pos_re = genpos.search(loc)
        if mut_re is not None and pos_re is not None:
            # Check if mutation already defined in dictionary M
            if (pos_re.group(1), mut_re.group(1), mut_re.group(2)) in M.keys():
                # increase count and update frequency
                ni = M[(pos_re.group(1), mut_re.group(1),
                        mut_re.group(2))][0] + 1
                fi = ni / n
                M[(pos_re.group(1), mut_re.group(1), mut_re.group(2))] = [ni,
                                                                          fi]
            else:
                # intialise count and frequency
                ni = 1
                fi = ni / n
                M[(pos_re.group(1), mut_re.group(1), mut_re.group(2))] = [ni,
                                                                          fi]
    # k =  number of unique mutations
    k = len(M.keys())
    if k != 0:
        # Calculate S and So
        S = 0
        for key in M.keys():
            S = S + (-M[key][1] * np.log(M[key][1]))
        So = np.log(k)
        missenseEntropy = So - S
        return [missenseEntropy, fi]
    else:
        return [0, 0]


def getFrameshiftEntropy(gene_data):
    """
    Calculates frameshift entropy and frequency for a given gene
    Arguments:
        tp_data = DataFrame of frameshift mutations in given gene
    Returns:
        frameshiftEntropy
        fi = highest frameshift entropy
    """
    fs_data = getFrameshiftData(gene_data)
    [frameshiftEntropy, fi] = getEntropy(fs_data)
    return [frameshiftEntropy, fi]


def getNonsenseEntropy(gene_data):
    """
    Calculates nonsense entropy  and frequency for a given gene
    Arguments:
        tp_data = DataFrame of nonsense mutations in given gene
    Returns:
        nonsenseEntropy
        fi = highest nonsense entropy
    """
    ns_data = getNonsenseData(gene_data)
    [nonsenseEntropy, fi] = getEntropy(ns_data)
    return [nonsenseEntropy, fi]


def getSplicingEntropy(gene_data):
    """
    Calculates splicing entropy  and frequency for a given gene
    Arguments:
        tp_data = DataFrame of splicing mutations in given gene
    Returns:
        splicingEntropy
        fi = highest splicing entropy
    """
    sp_data = getSplicingData(gene_data)
    [splicingEntropy, fi] = getEntropy(sp_data)
    return [splicingEntropy, fi]


def getEntropy(data):
    """
    Calculates  entropy  and frequency for a given gene depending on input
    mutation type. Function assumes the data sent as argument is of same
    mutation type. Can calculate for frameshift, nonsense and splicing
    mutations.
    Arguments:
        data = DataFrame of filtered mutations in given gene of a given
               mutation type
    Returns:
        entropy
        fi = highest mutation type frequency
    """
    if len(data) == 0:
        return [0, 0]
    # Each mutation is defined as loc
    M = dict()
    # n = total number of splicing mutations in a gene
    n = len(data)
    fi = 0
    # For each mutation across sample for a given gene
    for loc in data["Mutation genome position"]:
        # Check if mutation already defined in dictionary M
        if loc in M.keys():
            # increase count and update frequency
            ni = M[loc][0] + 1
            fi = ni / n
            M[loc] = [ni, fi]
        else:
            # intialise count and frequency
            ni = 1
            fi = ni / n
            M[loc] = [ni, fi]
    # k =  number of unique mutations
    k = len(M.keys())
    # Calculate S and So
    S = 0
    for key in M.keys():
        S = S + (-M[key][1] * np.log(M[key][1]))
    So = np.log(k)
    entropy = So - S
    return [entropy, fi]


def getSplicingMut_v2(data, ss_enst, ss_gene):
    """
    Function takes Dataframe and splice sites dictionary as input and checks if
    mutation occurs at splice donor or acceptor sites. Donor and Acceptor sites
    defined as 2bp after and before exon boundaries.
    Arguments:
        data
        SSiteFile: Filename of file containing splice site mutations
    Returns:
        splicingMutations: list. "yes" if splicing mutation
    """
    splicingMutation = [np.nan]*len(data)
    genpos = re.compile('^(\d+):(\d+)-(\d+)$')
    # TODO: remove next line
    count = 0
    for idx, (gene, enst, pos) in enumerate(zip(data['Gene name'],
                                                data['Accession Number'],
                                                data['Mutation genome position'])):
        # TODO: remove next 7 lines
        count = count + 1
        if count % 1000 == 0:
            print(count)
        if type(pos) != str and np.isnan(pos):
            print("!!!!!!!!!!!!!!Mutation genomic location is nan.")
            continue
        genLoc = genpos.search(pos)
        # Get splice stes for given gene or ensemble transcript. If gene not
        # found, append Nan and print gene not found.
        if enst in ss_enst.keys():
            temp = ss_enst[enst]
        elif gene in ss_gene.keys():
            temp = ss_gene[gene]
        else:
            try:
                genesplit = gene.split("_")
                temp = ss_gene[genesplit[0]]
            except KeyError:
                print(gene, "!!!!!!!!!!!!!!gene not found!")
                continue
        # Get all locations for given mutation and store as list loc
        loc = []
        if genLoc.group(2) == genLoc.group(3):
            loc.append(genLoc.group(0))
        else:
            for idxpos in range(int(genLoc.group(2)), int(genLoc.group(2))+1):
                loc.append(genLoc.group(1) + ":" + str(idxpos) + "-" +
                           str(idxpos))
        notsplice = True
        for lidx in loc:
            if notsplice:
                if lidx in temp:
                    splicingMutation[idx] = "yes"
                    notsplice = False
                    break
        if notsplice:
            splicingMutation[idx] = "no"
    return splicingMutation


def getSplicingMut(data, SSitefile="SpliceSites.txt"):
    """
    Function takes Dataframe and splice sites file as input and checks if
    mutation occurs at splice donor or acceptor sites. Donor and Acceptor sites
    defined as 2bp after and before exon boundaries.
    Arguments:
        data
        SSiteFile: Filename of file containing splice site mutations
    Returns:
        splicingMutations: list. "yes" if splicing mutation
    """
    splicingMutation = [np.nan]*len(data)
    # Read file containing splice sites
    spliceSites = pd.read_csv(SSitefile, sep="\t", header=0)
    # Make a single list containing unique splice sites from all 4 positions
    allSS = (list(spliceSites["Donor_pos1"]) +
             list(spliceSites["Donor_pos2"]) +
             list(spliceSites["Acceptor_pos1"]) +
             list(spliceSites["Acceptor_pos2"]))
    allSS = set(allSS)
    genpos = re.compile('^(\d+)_*\w*_*\w*:(\d+)-(\d+)$')
    # TODO: remove next line
    count = 0
    # Find intersection between splice site list and mutation position list.
    # This shortlisted list will be used to search for single bp mutations.
    knownSites = list(set(data['Mutation genome position']) & allSS)
    for idx, pos in enumerate(data['Mutation genome position']):
        # TODO: remove next 7 lines
        count = count + 1
        if count % 50000 == 0:
            print(count)
        # Check if mutation genomic position is given
        if type(pos) != str and np.isnan(pos):
            print("!!!!!!!!!!!!!!Mutation genomic location is nan.")
            continue
        # Search pattern in given location to get chr and start end positions
        genLoc = genpos.search(pos)
        # Check if its a single bp mutation, if yes, check in shortlist.
        # Else, get all locations for given mutation and store as list loc.
        # Find intersection with complete splice sites list.
        if genLoc.group(2) == genLoc.group(3):
            if genLoc.group(0) in knownSites:
                splicingMutation[idx] = "yes"
            else:
                splicingMutation[idx] = "no"
        else:
            loc = []
            for idxpos in range(int(genLoc.group(2)), int(genLoc.group(2))+1):
                loc.append(genLoc.group(1) + ":" + str(idxpos) + "-" +
                           str(idxpos))
            if len(list(set(loc) & allSS)) != 0:
                splicingMutation[idx] = "yes"
            else:
                splicingMutation[idx] = "no"
    return splicingMutation


def getCdMutFeatures(data):
    """
    Arguments:
        data
    Returns:
        feature_mat_old = dataframe of features
    """
    featCols = ["Silent/kb", "TotMissense", "TotSplicing", "TotLOF",
                "Missense/kb", "LOF/kb", "LOF/silent", "Splicing/silent",
                "Missense/silent", "Hifi/Lofi", "LOF/benign",
                "Splicing/benign", "Missense/benign", "Hifi/benign",
                "avgPolyphen2", "LOF/tot", "Missense/tot", "Splicing/tot",
                "LOF/missense", "Mifi/kb", "Nonstop/kb", "Inframe/kb",
                "Complex/kb", "Compound/benign", "Compound/kB", "Damaging/kb",
                "Damaging/benign", "Damaging/Lofi", "MissenseEntr",
                "HiMisFreq", "FSEntr", "HiFSFreq", "SplicEntr", "HiSplicFreq",
                "NonsenseEntr", "HiNonsenseFreq", "TotMifi"]

    gene_list = list(set(data["Gene name"]))
    feature_mat_old = pd.DataFrame(columns=featCols, index=gene_list)
    # TODO: remove next line
    i = 0
    for gene in feature_mat_old.index:
        # TODO: remove next 3 lines
        i = i + 1
        if i % 100 == 0:
            print(i, gene)
        temp = data[(data["Gene name"] == gene)]
        silent = 1 + len(temp[(temp["Mutation Description"] ==
                               "Substitution - coding silent")])
        gene_len = int(np.mean(list(temp["Gene CDS length"])))
        missense = 1 + (len(temp[(temp["Mutation Description"] ==
                                  "Substitution - Missense")]) +
                        len(temp[(temp["Mutation Description"] ==
                                  "Complex - compound substitution")]))
        splicing = len(temp[(temp["SpliceSite"] == "yes")])
        hifi = (len(temp[(temp["PP2_prob1"] >= 0.85)]) +
                len(temp[(temp["PP2_prob2"] >= 0.85)]))
        mifi = (len(temp[(temp["PP2_prob1"] > 0.15) &
                         (temp["PP2_prob1"] < 0.85)]) +
                len(temp[(temp["PP2_prob2"] > 0.15) &
                         (temp["PP2_prob2"] < 0.85)]))
        lofi = (1 + len(temp[(temp["PP2_prob1"] <= 0.15)]) +
                len(temp[(temp["PP2_prob2"] <= 0.15)]))
        avgpp2 = np.nanmean(list(temp["PP2_prob1"]) + list(temp["PP2_prob2"]))
        nonsense = len(temp[(temp["Mutation Description"] ==
                             "Substitution - Nonsense")])
        frameshift = (len(temp[(temp["Mutation Description"] ==
                                "Deletion - Frameshift")]) +
                      len(temp[(temp["Mutation Description"] ==
                                "Complex - frameshift")]) +
                      len(temp[(temp["Mutation Description"] ==
                                "Insertion - Frameshift")]))
        inframe = (len(temp[(temp["Mutation Description"] ==
                             "Insertion - In frame")]) +
                   len(temp[(temp["Mutation Description"] ==
                             "Deletion - In frame")]) +
                   len(temp[(temp["Mutation Description"] ==
                             "Complex - deletion inframe")]) +
                   len(temp[(temp["Mutation Description"] ==
                             "Complex - insertion inframe")]))
        nonstop = len(temp[(temp["Mutation Description"] ==
                            "Nonstop extension")])
        damaging = hifi + mifi
        complexmut = len(temp[(temp["Mutation Description"] == "Complex")])
        # Compound contains mutation counts for moderate functional impact
        # mutations like compound substitutions. These might not show high
        # repeatitions in genes as individual mutation types but might
        # contribute together.
        compound = missense - lofi + complexmut + inframe + nonstop
        lof = nonsense + frameshift
        benign = silent + lofi
        tot = len(temp)
        [MissenseEntr, HiMisFreq] = getMissenseEntropy(temp)
        [FSEntr, HiFSFreq] = getFrameshiftEntropy(temp)
        [NonsenseEntr, HiNonsenseFreq] = getNonsenseEntropy(temp)
        [SplicEntr, HiSplicFreq] = getSplicingEntropy(temp)
        feature_mat_old.loc[gene] = [silent / gene_len, missense, splicing,
                                     lof, missense / gene_len, lof / gene_len,
                                     lof / silent, splicing / silent,
                                     missense / silent, hifi / lofi,
                                     lof / benign, splicing / benign,
                                     missense / benign, hifi / benign, avgpp2,
                                     lof / tot, missense / tot, splicing / tot,
                                     lof / missense, mifi / gene_len,
                                     nonstop / gene_len, inframe / gene_len,
                                     complexmut / gene_len, compound / benign,
                                     compound / gene_len, damaging / gene_len,
                                     damaging / benign, damaging / lofi,
                                     MissenseEntr, HiMisFreq, FSEntr, HiFSFreq,
                                     SplicEntr, HiSplicFreq, NonsenseEntr,
                                     HiNonsenseFreq, mifi]
    return feature_mat_old


def getCdMutFeatures_v2(data, MAX_MULTIPLIER=2):
    """
    Arguments:
        data: dataframe of COSMIC data that has been processed for polyPhen2,
              liftOver and splice site data

    Returns:
        feature_mat_old = dataframe of features
    """
    featCols = ["Silent/kb", "TotMissense", "TotSplicing", "TotLOF",
                "Missense/kb", "LOF/kb", "LOF/silent", "Splicing/silent",
                "Missense/silent", "Hifi/Lofi", "LOF/benign",
                "Splicing/benign", "Missense/benign", "Hifi/benign",
                "avgPolyphen2", "LOF/tot", "Missense/tot", "Splicing/tot",
                "LOF/missense", "Mifi/kb", "Nonstop/kb", "Inframe/kb",
                "Complex/kb", "Compound/benign", "Compound/kB", "Damaging/kb",
                "Damaging/benign", "Damaging/Lofi", "MissenseEntr",
                "HiMisFreq", "FSEntr", "HiFSFreq", "SplicEntr", "HiSplicFreq",
                "NonsenseEntr", "HiNonsenseFreq", "TotMifi"]
    count_cols = ["gene_len", "silent", "missense", "splicing", "hifi", "mifi",
                  "lofi", "avgPP2", "nonsense", "frameshift", "inframe",
                  "nonstop", "complex", "damaging", "compound", "lof",
                  "benign", "total", "MissenseEntr", "HiMisFreq", "FSEntr",
                  "HiFSFreq", "SplicEntr", "HiSplicFreq", "NonsenseEntr",
                  "HiNonsenseFreq"]
    gene_list = list(set(data["Gene name"]))
    count_mat = pd.DataFrame(columns=count_cols, index=gene_list)
    feature_mat_old = pd.DataFrame(columns=featCols, index=gene_list)
    # TODO: remove next line
    i = 0
    for gene in feature_mat_old.index:
        # TODO: remove next 2 lines
        i = i + 1
        if i % 1000 == 0:
            print(i)
        temp = data[(data["Gene name"] == gene)]
        silent = int(len(temp[(temp["Mutation Description"] ==
                               "Substitution - coding silent")]))
        gene_len = int(np.mean(list(temp["Gene CDS length"])))
        missense = int(len(temp[(temp["Mutation Description"] ==
                                 "Substitution - Missense")]) +
                       len(temp[(temp["Mutation Description"] ==
                                 "Complex - compound substitution")]))
        splicing = int(len(temp[(temp["SpliceSite"] == "yes")]))
        hifi = int(len(temp[(temp["PP2_prob1"] >= 0.85)]) +
                   len(temp[(temp["PP2_prob2"] >= 0.85)]))
        mifi = int(len(temp[(temp["PP2_prob1"] > 0.15) &
                            (temp["PP2_prob1"] < 0.85)]) +
                   len(temp[(temp["PP2_prob2"] > 0.15) &
                            (temp["PP2_prob2"] < 0.85)]))
        lofi = int(len(temp[(temp["PP2_prob1"] <= 0.15)]) +
                   len(temp[(temp["PP2_prob2"] <= 0.15)]))
        temppp2 = float(np.nanmean(list(temp["PP2_prob1"]) +
                                  list(temp["PP2_prob2"])))
        if np.isnan(temppp2):
            avgpp2 = 0
        else:
            avgpp2 = temppp2
        nonsense = int(len(temp[(temp["Mutation Description"] ==
                                 "Substitution - Nonsense")]))
        frameshift = int(len(temp[(temp["Mutation Description"] ==
                                   "Deletion - Frameshift")]) +
                         len(temp[(temp["Mutation Description"] ==
                                   "Complex - frameshift")]) +
                         len(temp[(temp["Mutation Description"] ==
                                   "Insertion - Frameshift")]))
        inframe = int(len(temp[(temp["Mutation Description"] ==
                                "Insertion - In frame")]) +
                      len(temp[(temp["Mutation Description"] ==
                                "Deletion - In frame")]) +
                      len(temp[(temp["Mutation Description"] ==
                                "Complex - deletion inframe")]) +
                      len(temp[(temp["Mutation Description"] ==
                                "Complex - insertion inframe")]))
        nonstop = int(len(temp[(temp["Mutation Description"] ==
                                "Nonstop extension")]))
        damaging = hifi + mifi
        complexmut = int(len(temp[(temp["Mutation Description"] ==
                                   "Complex")]))
        # Compound contains mutation counts for moderate functional impact
        # mutations like compound substitutions. These might not show high
        # repeatitions in genes as individual mutation types but might
        # contribute together.
        compound = missense - lofi + complexmut + inframe + nonstop
        lof = nonsense + frameshift
        benign = silent + lofi
        tot = int(len(temp))
        [MissenseEntr, HiMisFreq] = getMissenseEntropy(temp)
        [FSEntr, HiFSFreq] = getFrameshiftEntropy(temp)
        [NonsenseEntr, HiNonsenseFreq] = getNonsenseEntropy(temp)
        [SplicEntr, HiSplicFreq] = getSplicingEntropy(temp)
        count_mat.loc[gene] = [gene_len, silent, missense, splicing, hifi,
                               mifi, lofi, avgpp2, nonsense, frameshift,
                               inframe, nonstop, complexmut, damaging,
                               compound, lof, benign, tot, MissenseEntr,
                               HiMisFreq, FSEntr, HiFSFreq, SplicEntr,
                               HiSplicFreq, NonsenseEntr, HiNonsenseFreq]
    max_vec = pd.DataFrame(columns=count_cols)
    max_vec.loc[0] = [max(count_mat[x]) for x in count_mat.columns]
    # TODO: remove next line
    i = 0
    for gene in feature_mat_old.index:
        # TODO: remove next 3 lines
        i = i + 1
        if i % 1000 == 0:
            print(i)
        silent__gene_len = ratio(count_mat.loc[gene, "silent"],
                                 count_mat.loc[gene, "gene_len"],
                                 max_vec["gene_len"], MAX_MULTIPLIER)
        missense_ = count_mat.loc[gene, "missense"]
        splicing_ = count_mat.loc[gene, "splicing"]
        lof_ = count_mat.loc[gene, "lof"]
        missense__gene_len = ratio(count_mat.loc[gene, "missense"],
                                   count_mat.loc[gene, "gene_len"],
                                   max_vec["gene_len"], MAX_MULTIPLIER)
        lof__gene_len = ratio(count_mat.loc[gene, "lof"],
                              count_mat.loc[gene, "gene_len"],
                              max_vec["gene_len"], MAX_MULTIPLIER)
        lof__silent = ratio(count_mat.loc[gene, "lof"],
                            count_mat.loc[gene, "silent"], max_vec["silent"],
                            MAX_MULTIPLIER)
        splicing__silent = ratio(count_mat.loc[gene, "splicing"],
                                 count_mat.loc[gene, "silent"],
                                 max_vec["silent"], MAX_MULTIPLIER)
        missense__silent = ratio(count_mat.loc[gene, "missense"],
                                 count_mat.loc[gene, "silent"],
                                 max_vec["silent"], MAX_MULTIPLIER)
        hifi__lofi = ratio(count_mat.loc[gene, "hifi"],
                           count_mat.loc[gene, "lofi"], max_vec["lofi"],
                           MAX_MULTIPLIER)
        lof__benign = ratio(count_mat.loc[gene, "lof"],
                            count_mat.loc[gene, "benign"], max_vec["benign"],
                            MAX_MULTIPLIER)
        splicing__benign = ratio(count_mat.loc[gene, "splicing"],
                                 count_mat.loc[gene, "benign"],
                                 max_vec["benign"], MAX_MULTIPLIER)
        missense__benign = ratio(count_mat.loc[gene, "missense"],
                                 count_mat.loc[gene, "benign"],
                                 max_vec["benign"], MAX_MULTIPLIER)
        hifi__benign = ratio(count_mat.loc[gene, "hifi"],
                             count_mat.loc[gene, "benign"], max_vec["benign"],
                             MAX_MULTIPLIER)
        avgpp2_ = count_mat.loc[gene, "avgPP2"]
        lof__tot = ratio(count_mat.loc[gene, "lof"],
                         count_mat.loc[gene, "total"], max_vec["total"],
                         MAX_MULTIPLIER)
        missense__tot = ratio(count_mat.loc[gene, "missense"],
                              count_mat.loc[gene, "total"], max_vec["total"],
                              MAX_MULTIPLIER)
        splicing__tot = ratio(count_mat.loc[gene, "splicing"],
                              count_mat.loc[gene, "total"], max_vec["total"],
                              MAX_MULTIPLIER)
        lof__missense = ratio(count_mat.loc[gene, "lof"],
                              count_mat.loc[gene, "missense"],
                              max_vec["missense"], MAX_MULTIPLIER)
        mifi__gene_len = ratio(count_mat.loc[gene, "mifi"],
                               count_mat.loc[gene, "gene_len"],
                               max_vec["gene_len"], MAX_MULTIPLIER)
        nonstop__gene_len = ratio(count_mat.loc[gene, "nonstop"],
                                  count_mat.loc[gene, "gene_len"],
                                  max_vec["gene_len"], MAX_MULTIPLIER)
        inframe__gene_len = ratio(count_mat.loc[gene, "inframe"],
                                  count_mat.loc[gene, "gene_len"],
                                  max_vec["gene_len"], MAX_MULTIPLIER)
        complexmut__gene_len = ratio(count_mat.loc[gene, "complex"],
                                     count_mat.loc[gene, "gene_len"],
                                     max_vec["gene_len"], MAX_MULTIPLIER)
        compound__benign = ratio(count_mat.loc[gene, "compound"],
                                 count_mat.loc[gene, "benign"],
                                 max_vec["benign"], MAX_MULTIPLIER)
        compound__gene_len = ratio(count_mat.loc[gene, "compound"],
                                   count_mat.loc[gene, "gene_len"],
                                   max_vec["gene_len"], MAX_MULTIPLIER)
        damaging__gene_len = ratio(count_mat.loc[gene, "damaging"],
                                   count_mat.loc[gene, "gene_len"],
                                   max_vec["gene_len"], MAX_MULTIPLIER)
        damaging__benign = ratio(count_mat.loc[gene, "damaging"],
                                 count_mat.loc[gene, "benign"],
                                 max_vec["benign"], MAX_MULTIPLIER)
        damaging__lofi = ratio(count_mat.loc[gene, "damaging"],
                               count_mat.loc[gene, "lofi"], max_vec["lofi"],
                               MAX_MULTIPLIER)
        MissenseEntr_ = count_mat.loc[gene, "MissenseEntr"]
        HiMisFreq_ = count_mat.loc[gene, "HiMisFreq"]
        FSEntr_ = count_mat.loc[gene, "FSEntr"]
        HiFSFreq_ = count_mat.loc[gene, "HiFSFreq"]
        SplicEntr_ = count_mat.loc[gene, "SplicEntr"]
        HiSplicFreq_ = count_mat.loc[gene, "HiSplicFreq"]
        NonsenseEntr_ = count_mat.loc[gene, "NonsenseEntr"]
        HiNonsenseFreq_ = count_mat.loc[gene, "HiNonsenseFreq"]
        mifi_ = count_mat.loc[gene, "mifi"]
        feature_mat_old.loc[gene] = [silent__gene_len, missense_, splicing_,
                                     lof_, missense__gene_len, lof__gene_len,
                                     lof__silent, splicing__silent,
                                     missense__silent, hifi__lofi,
                                     lof__benign, splicing__benign,
                                     missense__benign, hifi__benign, avgpp2_,
                                     lof__tot, missense__tot, splicing__tot,
                                     lof__missense, mifi__gene_len,
                                     nonstop__gene_len, inframe__gene_len,
                                     complexmut__gene_len, compound__benign,
                                     compound__gene_len, damaging__gene_len,
                                     damaging__benign, damaging__lofi,
                                     MissenseEntr_, HiMisFreq_, FSEntr_,
                                     HiFSFreq_, SplicEntr_, HiSplicFreq_,
                                     NonsenseEntr_, HiNonsenseFreq_, mifi_]
    return feature_mat_old


# FIXME: function getCdMutFeatures_v3 doesn't work as it should
def getCdMutFeatures_v3(data, MAX_MULTIPLIER=2):
    """
    Noramalizes for number of samples
    Arguments:
        data
    Returns:
        feature_mat_old = dataframe of features
    """
    featCols = ["Silent/kb", "TotMissense", "TotSplicing", "TotLOF",
                "Missense/kb", "LOF/kb", "LOF/silent", "Splicing/silent",
                "Missense/silent", "Hifi/Lofi", "LOF/benign",
                "Splicing/benign", "Missense/benign", "Hifi/benign",
                "avgPolyphen2", "LOF/tot", "Missense/tot", "Splicing/tot",
                "LOF/missense", "Mifi/kb", "Nonstop/kb", "Inframe/kb",
                "Complex/kb", "Compound/benign", "Compound/kB", "Damaging/kb",
                "Damaging/benign", "Damaging/Lofi", "MissenseEntr",
                "HiMisFreq", "FSEntr", "HiFSFreq", "SplicEntr", "HiSplicFreq",
                "NonsenseEntr", "HiNonsenseFreq", "TotMifi"]
    count_cols = ["gene_len", "silent", "missense", "splicing", "hifi", "mifi",
                  "lofi", "avgPP2", "nonsense", "frameshift", "inframe",
                  "nonstop", "complex", "damaging", "compound", "lof",
                  "benign", "total", "MissenseEntr", "HiMisFreq", "FSEntr",
                  "HiFSFreq", "SplicEntr", "HiSplicFreq", "NonsenseEntr",
                  "HiNonsenseFreq"]
    gene_list = list(set(data["Gene name"]))
    count_mat = pd.DataFrame(columns=count_cols, index=gene_list)
    feature_mat_old = pd.DataFrame(columns=featCols, index=gene_list)
    n_samp = len(getSampleIDs(data))
    # TODO: remove next line
    i = 0
    for gene in feature_mat_old.index:
        # TODO: remove next 2 lines
        i = i + 1
        print(i, gene)
        temp = data[(data["Gene name"] == gene)]
        silent = len(temp[(temp["Mutation Description"] ==
                           "Substitution - coding silent")]) / n_samp
        gene_len = int(np.mean(list(temp["Gene CDS length"])))
        missense = (len(temp[(temp["Mutation Description"] ==
                              "Substitution - Missense")]) +
                    len(temp[(temp["Mutation Description"] ==
                              "Complex - compound substitution")])) / n_samp
        splicing = len(temp[(temp["SpliceSite"] == "yes")]) / n_samp
        hifi = (len(temp[(temp["PP2_prob1"] >= 0.85)]) +
                len(temp[(temp["PP2_prob2"] >= 0.85)])) / n_samp
        mifi = (len(temp[(temp["PP2_prob1"] > 0.15) &
                         (temp["PP2_prob1"] < 0.85)]) +
                len(temp[(temp["PP2_prob2"] > 0.15) &
                         (temp["PP2_prob2"] < 0.85)])) / n_samp
        lofi = (len(temp[(temp["PP2_prob1"] <= 0.15)]) +
                len(temp[(temp["PP2_prob2"] <= 0.15)])) / n_samp
        temppp2 = float(np.nanmean(list(temp["PP2_prob1"]) +
                                  list(temp["PP2_prob2"])))
        if np.isnan(temppp2):
            avgpp2 = 0
        else:
            avgpp2 = temppp2
        nonsense = len(temp[(temp["Mutation Description"] ==
                             "Substitution - Nonsense")]) / n_samp
        frameshift = (len(temp[(temp["Mutation Description"] ==
                                "Deletion - Frameshift")]) +
                      len(temp[(temp["Mutation Description"] ==
                                "Complex - frameshift")]) +
                      len(temp[(temp["Mutation Description"] ==
                                "Insertion - Frameshift")])) / n_samp
        inframe = (len(temp[(temp["Mutation Description"] ==
                             "Insertion - In frame")]) +
                   len(temp[(temp["Mutation Description"] ==
                             "Deletion - In frame")]) +
                   len(temp[(temp["Mutation Description"] ==
                             "Complex - deletion inframe")]) +
                   len(temp[(temp["Mutation Description"] ==
                             "Complex - insertion inframe")])) / n_samp
        nonstop = len(temp[(temp["Mutation Description"] ==
                            "Nonstop extension")]) / n_samp
        damaging = hifi + mifi
        complexmut = len(temp[(temp["Mutation Description"] == "Complex")]) / n_samp
        # Compound contains mutation counts for moderate functional impact
        # mutations like compound substitutions. These might not show high
        # repeatitions in genes as individual mutation types but might
        # contribute together.
        compound = missense - lofi + complexmut + inframe + nonstop
        lof = nonsense + frameshift
        benign = silent + lofi
        tot = len(temp)
        [MissenseEntr, HiMisFreq] = getMissenseEntropy(temp)
        [FSEntr, HiFSFreq] = getFrameshiftEntropy(temp)
        [NonsenseEntr, HiNonsenseFreq] = getNonsenseEntropy(temp)
        [SplicEntr, HiSplicFreq] = getSplicingEntropy(temp)
        count_mat.loc[gene] = [gene_len, silent, missense, splicing, hifi,
                               mifi, lofi, avgpp2, nonsense, frameshift,
                               inframe, nonstop, complexmut, damaging,
                               compound, lof, benign, tot, MissenseEntr,
                               HiMisFreq, FSEntr, HiFSFreq, SplicEntr,
                               HiSplicFreq, NonsenseEntr, HiNonsenseFreq]
    max_vec = pd.DataFrame(columns=count_cols)
    max_vec.loc[0] = [max(count_mat[x]) for x in count_mat.columns]
    # TODO: remove next line
    i = 0
    for gene in feature_mat_old.index:
        # TODO: remove next 2 lines
        i = i + 1
        print(i, gene)
        silent__gene_len = ratio(count_mat.loc[gene, "silent"],
                                 count_mat.loc[gene, "gene_len"],
                                 max_vec["gene_len"], MAX_MULTIPLIER)
        missense_ = float(count_mat.loc[gene, "missense"])
        splicing_ = float(count_mat.loc[gene, "splicing"])
        lof_ = float(count_mat.loc[gene, "lof"])
        missense__gene_len = ratio(count_mat.loc[gene, "missense"],
                                   count_mat.loc[gene, "gene_len"],
                                   max_vec["gene_len"], MAX_MULTIPLIER)
        lof__gene_len = ratio(count_mat.loc[gene, "lof"],
                              count_mat.loc[gene, "gene_len"],
                              max_vec["gene_len"], MAX_MULTIPLIER)
        lof__silent = ratio(count_mat.loc[gene, "lof"],
                            count_mat.loc[gene, "silent"], max_vec["silent"],
                            MAX_MULTIPLIER)
        splicing__silent = ratio(count_mat.loc[gene, "splicing"],
                                 count_mat.loc[gene, "silent"],
                                 max_vec["silent"], MAX_MULTIPLIER)
        missense__silent = ratio(count_mat.loc[gene, "missense"],
                                 count_mat.loc[gene, "silent"],
                                 max_vec["silent"], MAX_MULTIPLIER)
        hifi__lofi = ratio(count_mat.loc[gene, "hifi"],
                           count_mat.loc[gene, "lofi"], max_vec["lofi"],
                           MAX_MULTIPLIER)
        lof__benign = ratio(count_mat.loc[gene, "lof"],
                            count_mat.loc[gene, "benign"], max_vec["benign"],
                            MAX_MULTIPLIER)
        splicing__benign = ratio(count_mat.loc[gene, "splicing"],
                                 count_mat.loc[gene, "benign"],
                                 max_vec["benign"], MAX_MULTIPLIER)
        missense__benign = ratio(count_mat.loc[gene, "missense"],
                                 count_mat.loc[gene, "benign"],
                                 max_vec["benign"], MAX_MULTIPLIER)
        hifi__benign = ratio(count_mat.loc[gene, "hifi"],
                             count_mat.loc[gene, "benign"], max_vec["benign"],
                             MAX_MULTIPLIER)
        avgpp2_ = count_mat.loc[gene, "avgPP2"]
        lof__tot = ratio(count_mat.loc[gene, "lof"],
                         count_mat.loc[gene, "total"], max_vec["total"],
                         MAX_MULTIPLIER)
        missense__tot = ratio(count_mat.loc[gene, "missense"],
                              count_mat.loc[gene, "total"], max_vec["total"],
                              MAX_MULTIPLIER)
        splicing__tot = ratio(count_mat.loc[gene, "splicing"],
                              count_mat.loc[gene, "total"], max_vec["total"],
                              MAX_MULTIPLIER)
        lof__missense = ratio(count_mat.loc[gene, "lof"],
                              count_mat.loc[gene, "missense"],
                              max_vec["missense"], MAX_MULTIPLIER)
        mifi__gene_len = ratio(count_mat.loc[gene, "mifi"],
                               count_mat.loc[gene, "gene_len"],
                               max_vec["gene_len"], MAX_MULTIPLIER)
        nonstop__gene_len = ratio(count_mat.loc[gene, "nonstop"],
                                  count_mat.loc[gene, "gene_len"],
                                  max_vec["gene_len"], MAX_MULTIPLIER)
        inframe__gene_len = ratio(count_mat.loc[gene, "inframe"],
                                  count_mat.loc[gene, "gene_len"],
                                  max_vec["gene_len"], MAX_MULTIPLIER)
        complexmut__gene_len = ratio(count_mat.loc[gene, "complex"],
                                     count_mat.loc[gene, "gene_len"],
                                     max_vec["gene_len"], MAX_MULTIPLIER)
        compound__benign = ratio(count_mat.loc[gene, "compound"],
                                 count_mat.loc[gene, "benign"],
                                 max_vec["benign"], MAX_MULTIPLIER)
        compound__gene_len = ratio(count_mat.loc[gene, "compound"],
                                   count_mat.loc[gene, "gene_len"],
                                   max_vec["gene_len"], MAX_MULTIPLIER)
        damaging__gene_len = ratio(count_mat.loc[gene, "damaging"],
                                   count_mat.loc[gene, "gene_len"],
                                   max_vec["gene_len"], MAX_MULTIPLIER)
        damaging__benign = ratio(count_mat.loc[gene, "damaging"],
                                 count_mat.loc[gene, "benign"],
                                 max_vec["benign"], MAX_MULTIPLIER)
        damaging__lofi = ratio(count_mat.loc[gene, "damaging"],
                               count_mat.loc[gene, "lofi"], max_vec["lofi"],
                               MAX_MULTIPLIER)
        MissenseEntr_ = count_mat.loc[gene, "MissenseEntr"]
        HiMisFreq_ = count_mat.loc[gene, "HiMisFreq"]
        FSEntr_ = count_mat.loc[gene, "FSEntr"]
        HiFSFreq_ = count_mat.loc[gene, "HiFSFreq"]
        SplicEntr_ = count_mat.loc[gene, "SplicEntr"]
        HiSplicFreq_ = count_mat.loc[gene, "HiSplicFreq"]
        NonsenseEntr_ = count_mat.loc[gene, "NonsenseEntr"]
        HiNonsenseFreq_ = count_mat.loc[gene, "HiNonsenseFreq"]
        mifi_ = count_mat.loc[gene, "mifi"]
        tot = sum([silent__gene_len, missense_, splicing_, lof_,
                   missense__gene_len, lof__gene_len, lof__silent,
                   splicing__silent, missense__silent, hifi__lofi,
                   lof__benign, splicing__benign, missense__benign,
                   hifi__benign, avgpp2_, lof__tot, missense__tot,
                   splicing__tot, lof__missense, mifi__gene_len,
                   nonstop__gene_len, inframe__gene_len, complexmut__gene_len,
                   compound__benign, compound__gene_len, damaging__gene_len,
                   damaging__benign, damaging__lofi,
                   MissenseEntr_, HiMisFreq_, FSEntr_,
                   HiFSFreq_, SplicEntr_, HiSplicFreq_,
                   NonsenseEntr_, HiNonsenseFreq_, mifi_])
        feature_mat_old.loc[gene] = [silent__gene_len / tot, missense_ / tot,
                                     splicing_ / tot,
                                     lof_ / tot, missense__gene_len / tot, lof__gene_len / tot,
                                     lof__silent / tot, splicing__silent / tot,
                                     missense__silent / tot, hifi__lofi / tot,
                                     lof__benign / tot, splicing__benign / tot,
                                     missense__benign / tot, hifi__benign / tot, avgpp2_ / tot,
                                     lof__tot / tot, missense__tot / tot, splicing__tot / tot,
                                     lof__missense / tot, mifi__gene_len / tot,
                                     nonstop__gene_len / tot, inframe__gene_len / tot,
                                     complexmut__gene_len / tot, compound__benign / tot,
                                     compound__gene_len / tot, damaging__gene_len / tot,
                                     damaging__benign / tot, damaging__lofi / tot,
                                     MissenseEntr_ / tot, HiMisFreq_ / tot, FSEntr_ / tot,
                                     HiFSFreq_ / tot, SplicEntr_ / tot, HiSplicFreq_ / tot,
                                     NonsenseEntr_ / tot, HiNonsenseFreq_ / tot, mifi_ / tot]
    return feature_mat_old


def ratio(num, denom, max_val, MAX_MULTIPLIER=2):
    """
    function to define ratio and handle o denominator
    """
    if denom == 0:
        return float(max_val * MAX_MULTIPLIER)
    else:
        return float(num / denom)


def ratio_v2(num, denom, med_num, med_denom):
    """
    function to define ratio and handle o denominator
    """
    return (num + (0.5 * med_num)) / (denom + (0.5 * med_denom))


#def metrics(train_y, pred_train, lab, test_y=None, pred_y=None):
#    """
#    Calculates accuracy, F1, precision and recall for the given labels
#    """
#    # calculate metrics and print to o/p file
#    f1_tr = f1_score(train_y, pred_train, average=None, labels=lab)
#    p_tr = precision_score(train_y, pred_train, average=None, labels=lab)
#    r_tr = recall_score(train_y, pred_train, average=None, labels=lab)
#    a_tr = accuracy_score(train_y, pred_train)
#    metric = {"F1_tr": f1_tr, "F1_ts": f1_ts, "Precision_tr": p_tr, "Precision_ts"}
#    if test_y is not None and pred_y is not None:
#        f1_ts = f1_score(test_y, pred_y, average=None, labels=lab)
#        p_ts = precision_score(test_y, pred_y, average=None, labels=lab)
#        r_ts = recall_score(test_y, pred_y, average=None, labels=lab)
#        a_ts = accuracy_score(test_y, pred_y)
#    metric = {"F1_tr": f1_tr, "F1_ts": f1_ts, "Precision_tr": p_tr, "Precision_ts"}
#    return metric
