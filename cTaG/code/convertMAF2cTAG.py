#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 17:47:45 2018

@author: malvika
Converts MAF-like format data into cTAG accepted format
"""

import os
import pandas as pd
import numpy as np
import re


def maf2ctag(fname, PATH):
    """
    Converts MAF file to format similar to COSMIC
    
    Arguments:
        fname = str, MAF file name
        PATH = Path to cTaG
        
    Returns:
        datactag = Dataframe in format similar to COSMIC mutation file
    """
    DATAPATH = PATH + "/data"
    os.chdir(DATAPATH)
    datamaf = pd.read_csv(fname, sep=",", header=0, comment="#", index_col=0)
    datamaf = datamaf[(datamaf["Func.refGene"] == "exonic") |
                      (datamaf["Func.refGene"] == "splicing")]

    # Load required supporting files
    os.chdir(DATAPATH)
    geneLen = pd.read_csv("GeneLengths2.txt", sep="\t", header=0,
                          index_col="Ensembl_gene")
#    os.chdir(DATAPATH)
#    geneInfo = pd.read_csv("Homo_sapiens.gene_info", sep="\t", header=0,
#                           index_col="GeneID")
#    geneInfo["Ensembl_gene"] = [re.search('^.*Ensembl:(ENSG\d+)\|.*$',
#                     details).group(1) if
#                     re.search('^.*Ensembl:(ENSG\d+)\|.*$', details) else
#                     "" for details in geneInfo["dbXrefs"]]


#    # Update gene symbols using GeneInfo data
#    # List of genes (Entrez ID) not found in GeneLengths2 file (Symbol not
#    # found) 
#    idNotFound = list(set([y for x, y in zip(list(datamaf["Hugo_Symbol"]),
#                                             list(datamaf["Entrez_Gene_Id"]))
#                           if x not in list(geneLen["Gene_name"])]))
#    newSymbols = list(geneInfo.reindex(idNotFound)["Symbol"])
#    for gid, sym in zip(idNotFound, newSymbols):
#        if type(sym) == str:
#            idx = datamaf[datamaf["Entrez_Gene_Id"] == gid].index
#            datamaf.loc[idx, "Hugo_Symbol"] = sym
#    # Add column for Ensemble gene ID for datamaf
#    for sym, gid in zip(datamaf["Hugo_Symbol"], datamaf["Entrez_Gene_Id"]):
#        if gid == 0 or gid =="0":
#            continue
#        elif gid in list(geneInfo.index):
#            datamaf.loc[datamaf[datamaf["Entrez_Gene_Id"] == gid].index,
#                         "Ensembl_gene"] = geneInfo.loc[gid , "Ensembl_gene"]
#        else:
#            print("Couldn't find Ensembl gene id for {}, {}".format(gid, sym))

#    col_values = ["Gene name", "Accession Number", "Gene CDS length",
#                  "HGNC ID", "Sample name", "ID_sample", "ID_tumour",
#                  "Primary site", "Site subtype 1", "Site subtype 2",
#                  "Site subtype 3", "Primary histology", "Histology subtype 1",
#                  "Histology subtype 2", "Histology subtype 3",
#                  "Genome-wide screen", "Mutation ID", "Mutation CDS",
#                  "Mutation AA", "Mutation Description", "Mutation zygosity",
#                  "LOH", "GRCh", "Mutation genome position", "Mutation strand",
#                  "SNP", "Resistance Mutation", "FATHMM prediction",
#                  "FATHMM score", "Mutation somatic status", "Pubmed_PMID",
#                  "ID_STUDY", "Sample source", "Tumour origin", "Age"]
#    col_values = ['Unnamed: 0', 'Hugo_Symbol', 'Chromosome', 'Start_Position',
#                  'End_Position', 'Reference_Allele', 'Tumor_Seq_Allele2',
#                  'Variant_Classification', 'tx', 'exon', 'txChange',
#                  'aaChange', 'Variant_Type', 'sample_id', 'Func.refGene',
#                  'Gene.refGene', 'GeneDetail.refGene', 'ExonicFunc.refGene',
#                  'AAChange.refGene', 'cytoBand', 'SIFT_score', 'SIFT_pred',
#                  'Polyphen2_HDIV_score', 'Polyphen2_HDIV_pred',
#                  'Polyphen2_HVAR_score', 'Polyphen2_HVAR_pred', 'LRT_score',
#                  'LRT_pred', 'MutationTaster_score', 'MutationTaster_pred',
#                  'MutationAssessor_score', 'MutationAssessor_pred',
#                  'FATHMM_score', 'FATHMM_pred', 'PROVEAN_score',
#                  'PROVEAN_pred', 'VEST3_score', 'CADD_raw', 'CADD_phred',
#                  'DANN_score', 'fathmm-MKL_coding_score',
#                  'fathmm-MKL_coding_pred', 'MetaSVM_score', 'MetaSVM_pred',
#                  'MetaLR_score', 'MetaLR_pred', 'integrated_fitCons_score',
#                  'integrated_confidence_value', 'GERP++_RS',
#                  'phyloP7way_vertebrate', 'phyloP20way_mammalian',
#                  'phastCons7way_vertebrate', 'phastCons20way_mammalian',
#                  'SiPhy_29way_logOdds', 'hgnc_symbol',
#                  'Entrez', 'ens_id', 'Entrez_Gene_Id']
    datactag = pd.DataFrame()
# TODO: Assign correct column for gene symbol
    datactag["Gene name"] = datamaf['Hugo_Symbol']
#    datactag["Gene name"] = datamaf['Gene.refGene']
    datactag['Accession Number'] = datamaf['Gene.refGene']
    datactag["Gene CDS length"] = ([geneLen.loc[gene, "Gene_length"] if
                                   gene in geneLen.index else None for gene in
                                   datamaf["ens_id"]])
    for idx, cds, sym, in zip(datactag.index, datactag["Gene CDS length"],
                              datactag["Gene name"]):
        if np.isnan(cds) and sym in list(geneLen["Gene_name"]):
            datactag.loc[idx, "Gene CDS length"] = max(geneLen[geneLen["Gene_name"] == sym]["Gene_length"])
#    datactag["HGNC ID"] = datamaf["HGNC_ID"]
    datactag["HGNC ID"] = datamaf["hgnc_symbol"]
    datactag["Sample name"] = datamaf["Tumor_Sample_Barcode"]
#    datactag["Sample name"] = datamaf["sample_id"]
    datactag["ID_sample"] = datamaf["Tumor_Sample_Barcode"]
#    datactag["ID_tumour"] = datamaf["tumor_bam_uuid"]


    datactag["Primary site"] = [None] * len(datamaf)
    datactag["Site subtype 1"] = [None] * len(datamaf)
    datactag["Site subtype 2"] = [None] * len(datamaf)
    datactag["Site subtype 3"] = [None] * len(datamaf)
    datactag["Primary histology"] = [None] * len(datamaf)
    datactag["Histology subtype 1"] = [None] * len(datamaf)
    datactag["Histology subtype 2"] = [None] * len(datamaf)
    datactag["Histology subtype 3"] = [None] * len(datamaf)
    datactag["Genome-wide screen"] = ['y'] * len(datamaf)
    temp_list = ["{}_{}_{}_{}_{}".format(samp, gene, chrm[3:], strt, end) for samp,
                 gene, chrm, strt, end in zip(datamaf["Tumor_Sample_Barcode"],
                                              datamaf['Hugo_Symbol'],
                                              datamaf["Chromosome"],
                                              datamaf["Start_Position"],
                                              datamaf["End_Position"])]
#    temp_list = ["{}_{}_{}_{}_{}".format(samp, gene, chrm[3:], strt, end) for samp,
#                 gene, chrm, strt, end in zip(datamaf["sample_id"],
#                                              datamaf['Gene.refGene'],
#                                              datamaf["Chromosome"],
#                                              datamaf["Start_Position"],
#                                              datamaf["End_Position"])]
    datactag["Mutation ID"] = temp_list
#    datactag["Mutation CDS"] = datamaf["HGVSc"]
#    datactag["Mutation AA"] = datamaf["HGVSp_Short"]
    datactag["Mutation CDS"] = datamaf["txChange"]
    datactag["Mutation AA"] = datamaf["aaChange"]
    temp_list = []
    for mut_type, ref, mut in zip(datamaf['Variant_Classification'],
                                  datamaf["Reference_Allele"],
                                  datamaf["Tumor_Seq_Allele2"]):
        if mut_type == "In_Frame_Ins":
            temp_list.append("Insertion - In frame")
        elif mut_type == "Silent":
            temp_list.append("Substitution - coding silent")
#        elif mut_type == "Splice_Site" or mut_type == "Splice_Region":
#            temp_list.append("Splice")
        elif mut_type == "Splice_Site":
            temp_list.append("Splice")
#        elif mut_type == "Translation_Start_Site":
#            temp_list.append("Complex")
        elif mut_type == "Frame_Shift_Del":
            temp_list.append("Deletion - Frameshift")
        elif mut_type == "Missense_Mutation":
            if len(ref) == 1 and len(mut):
                temp_list.append("Substitution - Missense")
            elif len(ref) == len(mut) != 1:
                temp_list.append("Complex - compound substitution")
            else:
                temp_list.append("Complex")
        elif mut_type == "Nonsense_Mutation":
            temp_list.append("Substitution - Nonsense")
        elif mut_type == "In_Frame_Del":
            temp_list.append("Deletion - In frame")
        elif mut_type == "Frame_Shift_Ins":
            temp_list.append("Insertion - Frameshift")
        elif mut_type == "Nonstop_Mutation":
            temp_list.append("Nonstop extension")
        else:
            temp_list.append(mut_type)
    datactag["Mutation Description"] = temp_list
    # FIXME: Check if this is the same as tumour call
    datactag["Mutation zygosity"] = [None] * len(datamaf)
    datactag["LOH"] = [None] * len(datamaf)
#    datactag["GRCh"] = [x[4:] for x in datamaf["NCBI_Build"]]
    chr_list = [x[3:] for x in datamaf["Chromosome"]]
    chr_list = ["23" if x == "X" else x for x in chr_list]
    chr_list = ["24" if x == "Y" else x for x in chr_list]
    chr_list = ["25" if x == "M" else x for x in chr_list]
    temp_list = ["{}:{}-{}".format(chrm, strt, end) for chrm, strt,
                 end in zip(chr_list, datamaf["Start_Position"],
                            datamaf["End_Position"])]
    datactag["Mutation genome position"] = temp_list
#    datactag["Mutation strand"] = ["+" if x == 1 else x for x in datamaf["TRANSCRIPT_STRAND"]]
#    datactag["Mutation strand"] = ["-" if x == -1 else x for x in datactag["Mutation strand"]]
    # FIXME: check if SNP means SNV or known human variants (col: variant type)
    # if given an dbSNP ID, considers the mutation as an SNP
    # v3 considers no mutation is SNP
    # datactag["SNP"] = ['n' if x is np.nan else 'y' for x in datamaf["dbSNP rs"]]
#    temp = []
#    for snp in datamaf["dbSNP_RS"]:
#        try:
#            if snp[:2] == "rs":
#                temp.append("y")
#            else:
#                temp.append("n")
#        except:
#            temp.append("n")
#    datactag["SNP"] = temp
    datactag["Resistance Mutation"] = ['-'] * len(datamaf)
    datactag["FATHMM prediction"] = [None] * len(datamaf)
    datactag["FATHMM score"] = [None] * len(datamaf)
#    datactag["Mutation somatic status"] = ['Confirmed somatic variant' if status == "Somatic" else "not known" for status in datamaf["Mutation_Status"]]
#    datactag["Pubmed_PMID"] = datamaf["PUBMED"]
    datactag["ID_STUDY"] = [None] * len(datamaf)
    datactag["Sample source"] = [None] * len(datamaf)
    datactag["Tumour origin"] = [None] * len(datamaf)
    datactag["Age"] = [None] * len(datamaf)
    datactag["PP2_prob1"] = datamaf["Polyphen2_HDIV_score"]
    datactag["PP2_prob2"] = [np.nan] * len(datamaf)
    datactag = datactag[datactag['Gene CDS length'].notna()]

#    os.chdir(DATAPATH + "/OralCancer")
#    fname = "dataTcgaCosmicformat.tsv"
#    datactag.to_csv(fname, sep="\t", index=False)
    return datactag
