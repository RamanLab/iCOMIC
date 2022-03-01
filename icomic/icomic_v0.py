#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 17:06:27 2020

@author: priyanka
"""

 # -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_v1_tabs.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QWidget, QMessageBox, QFormLayout, QGroupBox, QScrollArea
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtCore import QProcess, QBasicTimer
from PyQt5.QtGui import QPainter, QBrush, QPen
import webbrowser
import fileinput
import pandas as pd
import numpy as np
import gzip
from multiprocessing import Process
import glob
import datetime as dt
import pickle
import subprocess
import time
import shlex
import os
import logging
import string
import re
import pickle
import sys



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("iCOMIC Pipeline")
        MainWindow.resize(725, 746)
        MainWindow.setFixedSize(725, 746)
        MainWindow.setStyleSheet("background-image: url(mainwindow.);")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint);
        ## ADDed##
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        ##
        self.PipelinetabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.PipelinetabWidget.setGeometry(QtCore.QRect(10, 10, 701, 530))
        self.PipelinetabWidget.setObjectName("PipelinetabWidget")
        self.DNAseq = QtWidgets.QWidget()
        self.DNAseq.setObjectName("DNAseq")
        self.DNAtabWidget = QtWidgets.QTabWidget(self.DNAseq)
        self.DNAtabWidget.setGeometry(QtCore.QRect(0, 0, 695, 507))
        self.DNAtabWidget.setObjectName("DNAtabWidget")
        self.DNAtabWidget.setStyleSheet("background-image: url(dnatab.png);")
        

        ### Test Run Button Grey ###
        self.one_passed = False
        self.two_passed = False
        ## Make Input as first tab ##
        self.input_dna = QtWidgets.QWidget()
        self.input_dna.setObjectName("input_dna")
        self.SamplesYesradioButton = QtWidgets.QRadioButton(self.input_dna)
        self.SamplesYesradioButton.move(70, 30)
        self.SamplesYesradioButton.setObjectName("SamplesYesradioButton")
        self.SamplesYesradioButton.setChecked(True)
        self.SamplesNoradioButton = QtWidgets.QRadioButton(self.input_dna)
        self.SamplesNoradioButton.move(70, 90)
        self.SamplesNoradioButton.setObjectName("SamplesNoradioButton")
        self.SampleOrlabel = QtWidgets.QLabel(self.input_dna)
        self.SampleOrlabel.move(130, 60)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.SampleOrlabel.setFont(font)
        self.SampleOrlabel.setObjectName("SampleOrlabel")
        
        
        font_label = QtGui.QFont()
        font_label.setPointSize(8.5)
        color  = QtGui.QColor(233, 10, 150)
        self.SampleFilelabelDNA = QtWidgets.QLabel(self.input_dna)
        self.SampleFilelabelDNA.setGeometry(QtCore.QRect(20, 150, 93, 23))
        self.SampleFilelabelDNA.setObjectName("SampleFilelabelDNA")
        self.SampleFilelabelDNA.setEnabled(True)
        self.SampleslineEditDNA = QtWidgets.QLineEdit(self.input_dna)
        self.SampleslineEditDNA.setGeometry(QtCore.QRect(200, 150, 385, 23))
        self.SampleslineEditDNA.setObjectName("SampleslineEditDNA")
        self.SampleslineEditDNA.setEnabled(True)
        self.SamplesBrowseButtonDNA = QtWidgets.QPushButton(self.input_dna)
        self.SamplesBrowseButtonDNA.setGeometry(QtCore.QRect(600, 150, 30, 25))
        self.SamplesBrowseButtonDNA.setObjectName("SamplesBrowseButtonDNA")
        self.SamplesBrowseButtonDNA.setEnabled(True)
        self.SamplesErrortextDNA = QtWidgets.QLabel(self.input_dna)
        self.SamplesErrortextDNA.setGeometry(QtCore.QRect(200, 170, 385, 23))
        self.SamplesErrortextDNA.setFont(font_label)
        self.SamplesErrortextDNA.setStyleSheet("color: red")
        self.UnitsFilelabelDNA = QtWidgets.QLabel(self.input_dna)
        self.UnitsFilelabelDNA.setGeometry(QtCore.QRect(20, 210, 95, 17))
        self.UnitsFilelabelDNA.setObjectName("UnitsFilelabelDNA")
        self.UnitsFilelabelDNA.setEnabled(False)
        self.UnitslineEditDNA = QtWidgets.QLineEdit(self.input_dna)
        self.UnitslineEditDNA.setGeometry(QtCore.QRect(200, 210, 385, 23))
        self.UnitslineEditDNA.setObjectName("UnitslineEditDNA")
        self.UnitslineEditDNA.setEnabled(False)
        self.UnitsBrowseButtonDNA = QtWidgets.QPushButton(self.input_dna)
        self.UnitsBrowseButtonDNA.setGeometry(QtCore.QRect(600, 210, 30, 25))
        self.UnitsBrowseButtonDNA.setObjectName("UnitsBrowseButtonDNA")
        self.UnitsBrowseButtonDNA.setEnabled(False)
        self.UnitsErrortextDNA = QtWidgets.QLabel(self.input_dna)
        self.UnitsErrortextDNA.setGeometry(QtCore.QRect(200, 230, 385, 23))
        self.UnitsErrortextDNA.setFont(font_label)
        self.UnitsErrortextDNA.setStyleSheet("color: red")
        self.UnitsErroriconDNA = QtWidgets.QPushButton(self.input_dna)
        self.UnitsErroriconDNA.setGeometry(QtCore.QRect(635, 107, 20, 20))
        self.UnitsErroriconDNA.setToolTip("Input Units file!")
        self.UnitsErroriconDNA.setFont(font_label)
        self.UnitsErroriconDNA.hide()
        self.UnitsErroriconDNA.setIcon(QtGui.QIcon("./icons/warning.svg"))
        self.RefGenomelabelDNA = QtWidgets.QLabel(self.input_dna)
        self.RefGenomelabelDNA.setGeometry(QtCore.QRect(20, 270, 125, 17))
        self.RefGenomelabelDNA.setObjectName("RefGenomelabelDNA")
        self.RefGenomelineEditDNA = QtWidgets.QLineEdit(self.input_dna)
        self.RefGenomelineEditDNA.setGeometry(QtCore.QRect(200, 270, 385, 23))
        self.RefGenomelineEditDNA.setObjectName("RefGenomelineEditDNA")
        self.RefGenomeBrowseButtonDNA = QtWidgets.QPushButton(self.input_dna)
        self.RefGenomeBrowseButtonDNA.setGeometry(QtCore.QRect(600, 270, 30, 25))
        self.RefGenomeBrowseButtonDNA.setObjectName("RefGenomeBrowseButtonDNA")
        self.RefGenomeErrortextDNA = QtWidgets.QLabel(self.input_dna)
        self.RefGenomeErrortextDNA.setGeometry(QtCore.QRect(200, 300, 385, 23))
        self.RefGenomeErrortextDNA.setFont(font_label)
        self.RefGenomeErrortextDNA.setStyleSheet("color: red")
        self.RefVariantlabelDNA = QtWidgets.QLabel(self.input_dna)
        self.RefVariantlabelDNA.setGeometry(QtCore.QRect(20, 330, 157, 17))
        self.RefVariantlabelDNA.setObjectName("RefVariantlabelDNA")
        self.RefVariantlineEditDNA = QtWidgets.QLineEdit(self.input_dna)
        self.RefVariantlineEditDNA.setGeometry(QtCore.QRect(200, 330, 385, 23))
        self.RefVariantlineEditDNA.setObjectName("RefVariantlineEditDNA")
        self.RefVariantErrortextDNA = QtWidgets.QLabel(self.input_dna)
        self.RefVariantErrortextDNA.setGeometry(QtCore.QRect(200, 350, 385, 23))
        self.RefVariantErrortextDNA.setFont(font_label)
        self.RefVariantErrortextDNA.setStyleSheet("color: red")
        self.RefVariantpushButton = QtWidgets.QPushButton(self.input_dna)
        self.RefVariantpushButton.setGeometry(QtCore.QRect(600, 330, 30, 25))
        self.RefVariantpushButton.setObjectName("RefVariantpushButton")
        self.CorelabelDNA = QtWidgets.QLabel(self.input_dna)
        self.CorelabelDNA.setGeometry(QtCore.QRect(20, 390, 157, 17))
        self.CorelabelDNA.setObjectName("CorelabelDNA")
        self.CorelineEditDNA = QtWidgets.QLineEdit(self.input_dna)
        self.CorelineEditDNA.setGeometry(QtCore.QRect(200, 390, 250, 23))
        self.CorelineEditDNA.setObjectName("CorelineEditDNA")
        self.CoreErrortextDNA = QtWidgets.QLabel(self.input_dna)
        self.CoreErrortextDNA.setGeometry(QtCore.QRect(200, 415, 250, 23))
        self.CoreErrortextDNA.setFont(font_label)
        self.CoreErrortextDNA.setStyleSheet("color: red")

        
        self.nextbuttoninputDNA = QtWidgets.QPushButton(self.input_dna)
        self.nextbuttoninputDNA.setGeometry(QtCore.QRect(635, 400, 45, 45))
        self.nextbuttoninputDNA.setObjectName("nextbuttoninputDNA")

        
         #####info icon####
        ###dna###
        
        font_info = QtGui.QFont()
        font_info.setPointSize(8.5)

        
        self.SampleFileinfoicon_dna = QtWidgets.QPushButton(self.input_dna)
        self.SampleFileinfoicon_dna.setFlat(True)
        self.SampleFileinfoicon_dna.setGeometry(QtCore.QRect(120, 153, 20, 20))
        self.SampleFileinfoicon_dna.setToolTip("Browse for the folder containing all the relevant sample files.\n The filenames for all the fastq input data are required to be in the following format.\n (sample_name)_(condition(tumor/normal))_Rep(replicate_number)_R(1 /2 {1 for read1 and 2 for read2}).fastq.\n Example:hcc1395_normal_Rep1_R1.fastq")
        self.SampleFileinfoicon_dna.setFont(font_info)
        self.SampleFileinfoicon_dna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.SampleFileinfoicon_dna.setIconSize(QtCore.QSize(13, 13))
        
        self.UnitsFileinfoicon_dna = QtWidgets.QPushButton(self.input_dna)
        self.UnitsFileinfoicon_dna.setFlat(True)
        self.UnitsFileinfoicon_dna.setGeometry(QtCore.QRect(116, 209, 20, 20))
        self.UnitsFileinfoicon_dna.setToolTip("Browse for the tab separated text file containing the sample information. \n The table is required to be formatted as follows.\n The column names should take the order: Sample, Unit, Condition, fq1, fq2.\n (Sample- Sample name, Unit- Number of replications, \n Condition- normal/ tumor/ leave blank if the condition is not specified, \n fq1 - Path of Read 1,fq2 - Path of Read 2/ leave blank for single-end reads).\n An example table has been provided for your reference")
        self.UnitsFileinfoicon_dna.setFont(font_info)
        self.UnitsFileinfoicon_dna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.UnitsFileinfoicon_dna.setIconSize(QtCore.QSize(13, 13))
        
        self.RefGenomeinfoicon_dna = QtWidgets.QPushButton(self.input_dna)
        self.RefGenomeinfoicon_dna.setFlat(True)
        self.RefGenomeinfoicon_dna.setGeometry(QtCore.QRect(142, 270, 20, 20))
        self.RefGenomeinfoicon_dna.setToolTip("A reference genome is a digital nucleic acid database \n assembled to be a representative example of a species’ set of genes.\n It allows for fast alignment of sequences as it is less computationally intensive \n to align sequences to a known sequence map rather than to assemble it piece by piece.\n For this field, specify the path to the pre-downloaded reference genome fastq file")
        self.RefGenomeinfoicon_dna.setFont(font_info)
        self.RefGenomeinfoicon_dna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.RefGenomeinfoicon_dna.setIconSize(QtCore.QSize(13, 13))  
        
        self.RefVariantinfoicon_dna = QtWidgets.QPushButton(self.input_dna)
        self.RefVariantinfoicon_dna.setFlat(True)
        self.RefVariantinfoicon_dna.setGeometry(QtCore.QRect(177, 329, 20, 20))
        self.RefVariantinfoicon_dna.setToolTip("A vcf file specifying the known variant locations")
        self.RefVariantinfoicon_dna.setFont(font_info)
        self.RefVariantinfoicon_dna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.RefVariantinfoicon_dna.setIconSize(QtCore.QSize(13, 13))         
        
        self.SamplesYesradioinfoicon_dna = QtWidgets.QPushButton(self.input_dna)
        self.SamplesYesradioinfoicon_dna.setFlat(True)
        self.SamplesYesradioinfoicon_dna.setGeometry(QtCore.QRect(210, 32, 20, 20))
        self.SamplesYesradioinfoicon_dna.setToolTip("Specify the path to the folder containing all the relevant sample files.\n The filenames for all the fastq input data are required to be in the following format.\n (sample_name)_(condition(tumor/normal))_Rep(replicate_number)_R(1 /2 {1 for read1 and 2 for read2}).fastq. \nExample:hcc1395_normal_Rep1_R1.fastq.")
        self.SamplesYesradioinfoicon_dna.setFont(font_info)
        self.SamplesYesradioinfoicon_dna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.SamplesYesradioinfoicon_dna.setIconSize(QtCore.QSize(13, 13))       
        
        
        self.SamplesNoradioinfoicon_dna = QtWidgets.QPushButton(self.input_dna)
        self.SamplesNoradioinfoicon_dna.setFlat(True)
        self.SamplesNoradioinfoicon_dna.setGeometry(QtCore.QRect(210, 90, 20, 20))
        self.SamplesNoradioinfoicon_dna.setToolTip("Specify the tab-delimited text file containing the sample information.\n The table is required to be formatted as follows.\n The column names should take the order: Sample, Unit, Condition, fq1, fq2. \n(Sample- Sample name, Unit- Number of replications, Condition- normal/ tumor/ leave blank if the condition is not specified,\n fq1 - Path of Read 1,fq2 - Path of Read 2/ leave blank for single-end reads).\n An example table has been provided for your reference")
        self.SamplesNoradioinfoicon_dna.setFont(font_info)
        self.SamplesNoradioinfoicon_dna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.SamplesNoradioinfoicon_dna.setIconSize(QtCore.QSize(13, 13))


        self.coreinfoicon_dna = QtWidgets.QPushButton(self.input_dna)
        self.coreinfoicon_dna.setFlat(True)
        self.coreinfoicon_dna.setGeometry(QtCore.QRect(140, 390, 20, 20))
        self.coreinfoicon_dna.setToolTip("Input the number of threads to run")
        self.coreinfoicon_dna.setFont(font_info)
        self.coreinfoicon_dna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.coreinfoicon_dna.setIconSize(QtCore.QSize(13, 13))               
        
        self.DNAtabWidget.addTab(self.input_dna, "")
        ## End ##
        ## Add QC ##
        self.QC_dna = QtWidgets.QWidget()
        self.QC_dna.setObjectName("QC_dna")
#        self.QC_dna.setEnabled(False)
        ## Added from QC_Index##
        self.QCresults = QtWidgets.QPushButton(self.QC_dna)
        self.QCresults.setGeometry(QtCore.QRect(10, 30, 150, 23))
        self.QCresults.setText("Quality Control Results")
        self.QCresults.setStyleSheet("background-color: #704214")
        self.QCresultsButtonErroricon = QtWidgets.QPushButton(self.QC_dna)
        self.QCresultsButtonErroricon.setGeometry(QtCore.QRect(186, 32, 20, 20))
        self.QCresultsButtonErroricon.setToolTip("Check and Run View Quality control Results Again!")
        self.QCresultsButtonErroricon.setFont(font_label)
        self.QCresultsButtonErroricon.setIcon(QtGui.QIcon("./icons/warning.svg"))
        self.QCresultsButtonErroricon.hide()
        self.QClabel = QtWidgets.QLabel(self.QC_dna)
        self.QClabel.setGeometry(QtCore.QRect(10, 85, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.QClabel.setFont(font)
        self.QClabel.setObjectName("QClabel")
        self.QCYesradioButton = QtWidgets.QRadioButton(self.QC_dna)
        self.QCYesradioButton.setGeometry(QtCore.QRect(170, 85, 117, 22))
        self.QCYesradioButton.setObjectName("QCYesradioButton")
#        self.QCYesradioButton.setChecked(True)
        self.QCNoradioButton = QtWidgets.QRadioButton(self.QC_dna)
        self.QCNoradioButton.setGeometry(QtCore.QRect(250, 85, 117, 22))
        self.QCNoradioButton.setObjectName("QCNoradioButton")
        self.QCNoradioButton.setChecked(True)
        self.InputParamslabel = QtWidgets.QLabel(self.QC_dna)
        self.InputParamslabel.setGeometry(QtCore.QRect(10, 140, 171, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.InputParamslabel.setFont(font)
        self.InputParamslabel.setObjectName("InputParamslabel")

        self.CutadaptlineEdit = QtWidgets.QLineEdit(self.QC_dna)
        self.CutadaptlineEdit.setGeometry(QtCore.QRect(120, 200, 481, 23))
        self.CutadaptlineEdit.setObjectName("CutadaptlineEdit")
        self.Cutadaptlabel = QtWidgets.QLabel(self.QC_dna)
        self.Cutadaptlabel.setGeometry(QtCore.QRect(10, 200, 67, 17))
        self.Cutadaptlabel.setObjectName("Cutadaptlabel")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.QC_dna)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(235, 273, 240, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.RunQCpushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.RunQCpushButton.setObjectName("RunQCpushButton")
        self.horizontalLayout_4.addWidget(self.RunQCpushButton)
        self.RunQCButtonErroricon = QtWidgets.QPushButton(self.QC_dna)
        self.RunQCButtonErroricon.setGeometry(QtCore.QRect(500, 277, 20, 20))
        self.RunQCButtonErroricon.setToolTip("Check and Run Trimming Again!")
        self.RunQCButtonErroricon.setFont(font_label)
        self.RunQCButtonErroricon.setIcon(QtGui.QIcon("./icons/warning.svg"))
#        self.horizontalLayout_4.addWidget(self.RunQCButtonErroricon)
        self.RunQCButtonErroricon.hide()
        self.InputParamslabel.setEnabled(False)
        self.Cutadaptlabel.setEnabled(False)
        self.CutadaptlineEdit.setEnabled(False)
        self.RunQCpushButton.setEnabled(False)
        ##QC_Progressbar##
        self.progressBar_sub1_dna = QtWidgets.QProgressBar(self.QC_dna)
        self.progressBar_sub1_dna.setGeometry(QtCore.QRect(10, 355, 665, 17))
        self.progressBar_sub1_dna.setProperty("value", 0)
        self.progressBar_sub1_dna.setObjectName("progressBar_sub1_dna")

        ###
        self.nextbuttonqcDNA = QtWidgets.QPushButton(self.QC_dna)
        self.nextbuttonqcDNA.setGeometry(QtCore.QRect(635, 400, 45, 45))
        self.nextbuttonqcDNA.setObjectName("nextbuttonqcDNA")
        self.nextbuttonqcDNA.setEnabled(True)
        ###
        self.previousbuttonqcDNA = QtWidgets.QPushButton(self.QC_dna)
        self.previousbuttonqcDNA.setGeometry(QtCore.QRect(10, 400, 45, 45))
        self.previousbuttonqcDNA.setObjectName("previousbuttonqcDNA")
        
        
        
        font_info = QtGui.QFont()
        font_info.setPointSize(8.5)
        
        self.QCresultsinfoicon_dna = QtWidgets.QPushButton(self.QC_dna)
        self.QCresultsinfoicon_dna.setFlat(True)
        self.QCresultsinfoicon_dna.setGeometry(QtCore.QRect(166, 33, 20, 20))
        self.QCresultsinfoicon_dna.setToolTip("Generates a MultiQC report consisting of statistical metrics\n aggregated from FastQC for each sample input file.\n If the results obtained are satisfactory, you may move onto the next tab.\n If not, proceed to trim the reads to improve the quality of your data")
        self.QCresultsinfoicon_dna.setFont(font_info)
        self.QCresultsinfoicon_dna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.QCresultsinfoicon_dna.setIconSize(QtCore.QSize(13, 13))          
        
        self.QClabelinfoicon_dna = QtWidgets.QPushButton(self.QC_dna)
        self.QClabelinfoicon_dna.setFlat(True)
        self.QClabelinfoicon_dna.setGeometry(QtCore.QRect(131, 87, 20, 20))
        self.QClabelinfoicon_dna.setToolTip("Selecting 'Yes' will remove the adapter sequences from your data thereby improving data quality.\n 'No' can be selected if you are satisfied with the data quality")
        self.QClabelinfoicon_dna.setFont(font_info)
        self.QClabelinfoicon_dna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.QClabelinfoicon_dna.setIconSize(QtCore.QSize(13, 13))          
        
        self.Cutadaptlabelinfoicon_dna = QtWidgets.QPushButton(self.QC_dna)
        self.Cutadaptlabelinfoicon_dna.setFlat(True)
        self.Cutadaptlabelinfoicon_dna.setGeometry(QtCore.QRect(70, 199, 20, 20))
        self.Cutadaptlabelinfoicon_dna.setToolTip("Please input the necessary parameters for the tool cutadapt.\n It may include the adapter sequences.\n Refer https://cutadapt.readthedocs.io/en/stable/guide.html#adapter-types for details")
        self.Cutadaptlabelinfoicon_dna.setFont(font_info)
        self.Cutadaptlabelinfoicon_dna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.Cutadaptlabelinfoicon_dna.setIconSize(QtCore.QSize(13, 13))    
        
        self.RunQCpushButtoninfoicon_dna = QtWidgets.QPushButton(self.QC_dna)
        self.RunQCpushButtoninfoicon_dna.setFlat(True)
        self.RunQCpushButtoninfoicon_dna.setGeometry(QtCore.QRect(480, 277, 20, 20))
        self.RunQCpushButtoninfoicon_dna.setToolTip("Please choose yes to trim your reads if the input sequences are of poor quality.\n You may proceed to the next section if your reads are good enough for alignment")
        self.RunQCpushButtoninfoicon_dna.setFont(font_info)
        self.RunQCpushButtoninfoicon_dna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.RunQCpushButtoninfoicon_dna.setIconSize(QtCore.QSize(13, 13))           
        
        
        self.DNAtabWidget.addTab(self.QC_dna, "")
        ## End ##
        self.Tool_dna = QtWidgets.QWidget()
        self.Tool_dna.setObjectName("Tool_dna")

        self.create_aligner_groupbox()
        self.create_vc_groupbox()
        self.create_annotator_groupbox()
        self.create_group_next()
        
        
        
        self.layout = QtWidgets.QHBoxLayout(self.Tool_dna)
        self.scrollArea = QtWidgets.QScrollArea(self.Tool_dna)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layout.addWidget(self.scrollArea)
        
        self.grp_list=[self.aligner_groupbox, self.vc_groupbox, self.annotator_groupbox, self.next_groupbox]
        for i in range(4):
            self.gridLayout.addWidget(self.grp_list[i], i,0)
        
        
        self.DNAtabWidget.addTab(self.Tool_dna, "")


        

        ## End ##
        
        ##Add Run##
        self.run_dna = QtWidgets.QWidget()
        self.run_dna.setObjectName("run_dna")
        
        self.RunButton_dna = QtWidgets.QPushButton(self.run_dna)
        self.RunButton_dna.setGeometry(QtCore.QRect(300, 140, 100, 100))
        self.RunButton_dna.setObjectName("RunButton_dna")
        self.RunLabel_dna = QtWidgets.QLabel(self.run_dna)
        self.RunLabel_dna.setGeometry(QtCore.QRect(330, 255, 180, 17))
        self.RunLabel_dna.setObjectName("RunLabel_dna")
        
        
        self.RunButtonErroricon_dna = QtWidgets.QPushButton(self.run_dna)
        self.RunButtonErroricon_dna.setGeometry(QtCore.QRect(420, 172, 30, 30))
        self.RunButtonErroricon_dna.setToolTip("Click Run Button and Run Again!")
        self.RunButtonErroricon_dna.setFont(font_label)
        self.RunButtonErroricon_dna.setIcon(QtGui.QIcon("./icons/warning.svg"))
        self.RunButtonErroricon_dna.hide()            
        

        
        self.progressBar_dna = QtWidgets.QProgressBar(self.run_dna)
        self.progressBar_dna.setGeometry(QtCore.QRect(10, 340, 670, 23))
        self.progressBar_dna.setProperty("value", 0)
#        self.progressBar.setMaximum(3)
        self.progressBar_dna.setObjectName("progressBar_dna")  
        
        self.nextbuttonrunDNA = QtWidgets.QPushButton(self.run_dna)
        self.nextbuttonrunDNA.setGeometry(QtCore.QRect(635, 400, 45, 45))
        self.nextbuttonrunDNA.setObjectName("nextbuttonrunDNA")
        ###
        self.previousbuttonrunDNA = QtWidgets.QPushButton(self.run_dna)
        self.previousbuttonrunDNA.setGeometry(QtCore.QRect(10, 400,45, 45))
        self.previousbuttonrunDNA.setObjectName("previousbuttonrunDNA")
        
        font_info = QtGui.QFont()
        font_info.setPointSize(8.5)
        
        self.RunButtoninfoicon_dna = QtWidgets.QPushButton(self.run_dna)
        self.RunButtoninfoicon_dna.setFlat(True)
        self.RunButtoninfoicon_dna.setGeometry(QtCore.QRect(400, 180, 20, 20))
        self.RunButtoninfoicon_dna.setToolTip("Click to start your analysis")
        self.RunButtoninfoicon_dna.setFont(font_info)
        self.RunButtoninfoicon_dna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.RunButtoninfoicon_dna.setIconSize(QtCore.QSize(13, 13)) 
        

        
        
        self.DNAtabWidget.addTab(self.run_dna, "")
        ##End##
        ##Add Result DNA##
        self.result_dna = QtWidgets.QWidget()
        self.result_dna.setObjectName("result_dna")
        
        self.DNAtabWidget.addTab(self.result_dna, "")

        font_resulttab = QtGui.QFont()
        font_resulttab.setPointSize(16)
        self.pushbutton_result1_dna=QtWidgets.QPushButton(self.result_dna)
        self.pushbutton_result1_dna.setText("    Run statistics")
        self.pushbutton_result1_dna.setIcon(QtGui.QIcon("./icons/runstatistics.svg"))
        self.pushbutton_result1_dna.setIconSize(QtCore.QSize(40, 40))
        self.pushbutton_result1_dna.setFont(font_resulttab)
        self.pushbutton_result1_dna.setStyleSheet("background-color: #704214")
        self.pushbutton_result1_dna.setGeometry(QtCore.QRect(215, 50, 255, 48))

        self.pushbutton_result2_dna=QtWidgets.QPushButton(self.result_dna)
        self.pushbutton_result2_dna.setText("    Variants called")
        self.pushbutton_result2_dna.setIcon(QtGui.QIcon("./icons/document.svg"))
        self.pushbutton_result2_dna.setIconSize(QtCore.QSize(40, 40))
        self.pushbutton_result2_dna.setFont(font_resulttab)
        self.pushbutton_result2_dna.setStyleSheet("background-color: #704214")
        self.pushbutton_result2_dna.setGeometry(QtCore.QRect(215, 125, 255, 48))

        self.pushbutton_result3_dna=QtWidgets.QPushButton(self.result_dna)
        self.pushbutton_result3_dna.setText("Annotated variants")
        self.pushbutton_result3_dna.setIcon(QtGui.QIcon("./icons/document.svg"))
        self.pushbutton_result3_dna.setIconSize(QtCore.QSize(40, 40))
        self.pushbutton_result3_dna.setFont(font_resulttab)
        self.pushbutton_result3_dna.setStyleSheet("background-color: #704214")
        self.pushbutton_result3_dna.setGeometry(QtCore.QRect(215, 200, 255, 48))
        
        self.proceedlabel = QtWidgets.QLabel(self.result_dna)
        self.proceedlabel.setGeometry(QtCore.QRect(150, 285, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
#        font.setItalic(True)
        self.proceedlabel.setFont(font)
        self.proceedlabel.setObjectName("proceedlabel")
        self.proceedlabel.setText("Proceed with cTaG or NBDriver?")
        self.pYesradioButton = QtWidgets.QRadioButton(self.result_dna)
        self.pYesradioButton.setGeometry(QtCore.QRect(450, 285, 117, 22))
        self.pYesradioButton.setObjectName("pYesradioButton")
        self.pYesradioButton.setFont(font)
        self.pYesradioButton.setText("Yes")
#        self.SamplesNoradioButton.setText(_translate("MainWindow", "Upload from Table"))
#        self.QCYesradioButton.setChecked(True)
        self.pNoradioButton = QtWidgets.QRadioButton(self.result_dna)
        self.pNoradioButton.setGeometry(QtCore.QRect(530, 285, 117, 22))
        self.pNoradioButton.setObjectName("pNoradioButton")
        self.pNoradioButton.setFont(font)
        self.pNoradioButton.setText("No")
        self.pNoradioButton.setChecked(True)
        
        self.ctagradioButton = QtWidgets.QCheckBox(self.result_dna)
        self.ctagradioButton.setFont(font)
        self.ctagradioButton.setGeometry(QtCore.QRect(250, 345, 117, 22))
        self.ctagradioButton.setText("cTaG")
        self.nbradioButton = QtWidgets.QCheckBox(self.result_dna)
        self.nbradioButton.setFont(font)
        self.nbradioButton.setGeometry(QtCore.QRect(350, 345, 117, 22))
        self.nbradioButton.setText("NBDriver")
#        self.nbradioButton.setChecked(True)
        font_next = QtGui.QFont()
        font_next.setPointSize(12)
        self.nextbuttonresult = QtWidgets.QPushButton(self.result_dna)
        self.nextbuttonresult.setGeometry(QtCore.QRect(635, 400, 45, 45))
        self.nextbuttonresult.setIcon(QtGui.QIcon("./icons/arrow.svg"))
        self.nextbuttonresult.setStyleSheet("background-color: #704214")
#        self.nextbuttonresult.setFont(font_next)
#        self.nextbuttonresult.setText("Generate MAF file")
        self.nextbuttonresult.setIconSize(QtCore.QSize(35, 35))
        
        self.nbinfoiconradio = QtWidgets.QPushButton(self.result_dna)
        self.nbinfoiconradio.setFlat(True)
        self.nbinfoiconradio.setGeometry(QtCore.QRect(450, 347, 20, 20))
        self.nbinfoiconradio.setToolTip("NBDriver predictions has been derived using hg19 reference genome only and \n the input vcf file must be kept inside /NBDriver_ICOMIC/vcf")
        self.nbinfoiconradio.setFont(font_info)
        self.nbinfoiconradio.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.nbinfoiconradio.setIconSize(QtCore.QSize(13, 13)) 
        
        self.ctagradioButton.setEnabled(False)
        self.nbradioButton.setEnabled(False)
        self.nextbuttonresult.setEnabled(False)
        self.nbinfoiconradio.setEnabled(False)
        
        
        ##End##        
        

        ## End ##
        self.PipelinetabWidget.addTab(self.DNAseq, "")

        self.RNAseq = QtWidgets.QWidget()
        self.RNAseq.setObjectName("RNAseq")
        self.RNAtabWidget = QtWidgets.QTabWidget(self.RNAseq)
        self.RNAtabWidget.setGeometry(QtCore.QRect(0, 0, 695, 507))
        self.RNAtabWidget.setMovable(False)
        self.RNAtabWidget.setTabBarAutoHide(False)
        self.RNAtabWidget.setObjectName("RNAtabWidget")
#        self.RNAtabWidget.setStyleSheet("background-color: #F0F9EC")
        self.RNAtabWidget.setStyleSheet("background-image: url(dnatab.png);")
        ## Make Input as first tab ##
        self.input_rna = QtWidgets.QWidget()
        self.input_rna.setObjectName("input_rna")
        self.SamplesYesradioButton_rna = QtWidgets.QRadioButton(self.input_rna)
        self.SamplesYesradioButton_rna.move(70, 30)
        self.SamplesYesradioButton_rna.setObjectName("SamplesYesradioButton_rna")
        self.SamplesYesradioButton_rna.setChecked(True)
        self.SamplesNoradioButton_rna = QtWidgets.QRadioButton(self.input_rna)
        self.SamplesNoradioButton_rna.move(70, 90)
        self.SamplesNoradioButton_rna.setObjectName("SamplesNoradioButton_rna")
        self.SampleOrlabel_rna = QtWidgets.QLabel(self.input_rna)
        self.SampleOrlabel_rna.move(130, 60)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.SampleOrlabel_rna.setFont(font)
        self.SampleOrlabel_rna.setObjectName("SampleOrlabel_rna")

        self.SampleFolderlabel = QtWidgets.QLabel(self.input_rna)
        self.SampleFolderlabel.setGeometry(QtCore.QRect(20, 135, 113, 23))
        self.SampleFolderlabel.setObjectName("SampleFolderlabel")
        self.SampleFolderlabel.setEnabled(True)
        self.SampleFolderLineEdit = QtWidgets.QLineEdit(self.input_rna)
        self.SampleFolderLineEdit.setGeometry(QtCore.QRect(200, 135, 385, 23))
        self.SampleFolderLineEdit.setObjectName("SampleFolderLineEdit")
        self.SampleFolderLineEdit.setEnabled(True)
        self.SampleFolderBrowseButton = QtWidgets.QPushButton(self.input_rna)
        self.SampleFolderBrowseButton.setGeometry(QtCore.QRect(600, 135, 30, 25))
        self.SampleFolderBrowseButton.setObjectName("SampleFolderBrowseButton")
        self.SampleFolderBrowseButton.setEnabled(True)
        self.SampleFolderErrortextRNA = QtWidgets.QLabel(self.input_rna)
        self.SampleFolderErrortextRNA.setGeometry(QtCore.QRect(200, 165, 385, 15))
        self.SampleFolderErrortextRNA.setFont(font_label)
        self.SampleFolderErrortextRNA.setStyleSheet("color: red")
        self.Sampletablelabel = QtWidgets.QLabel(self.input_rna)
        self.Sampletablelabel.setGeometry(QtCore.QRect(20, 190, 113, 17))
        self.Sampletablelabel.setObjectName("Sampletablelabel")
        self.Sampletablelabel.setEnabled(False)
        self.SampletablelineEdit = QtWidgets.QLineEdit(self.input_rna)
        self.SampletablelineEdit.setGeometry(QtCore.QRect(200, 190, 385, 23))
        self.SampletablelineEdit.setObjectName("SampletablelineEdit")
        self.SampletablelineEdit.setEnabled(False)
        self.SampletableBrowseButton = QtWidgets.QPushButton(self.input_rna)
        self.SampletableBrowseButton.setGeometry(QtCore.QRect(600, 190, 30, 25))
        self.SampletableBrowseButton.setObjectName("SampletableBrowseButton")
        self.SampletableBrowseButton.setEnabled(False)
        self.SampletableErrortextRNA = QtWidgets.QLabel(self.input_rna)
        self.SampletableErrortextRNA.setGeometry(QtCore.QRect(200, 220, 385, 23))
        self.SampletableErrortextRNA.setFont(font_label)
        self.SampletableErrortextRNA.setStyleSheet("color: red")
        self.FastaFilelabel = QtWidgets.QLabel(self.input_rna)
        self.FastaFilelabel.setGeometry(QtCore.QRect(20, 240, 131, 17))
        self.FastaFilelabel.setObjectName("FastaFilelabel")
        self.FastalineEdit = QtWidgets.QLineEdit(self.input_rna)
        self.FastalineEdit.setGeometry(QtCore.QRect(200, 240, 385, 23))
        self.FastalineEdit.setObjectName("FastalineEdit")
        self.FastaBrowseButton = QtWidgets.QPushButton(self.input_rna)
        self.FastaBrowseButton.setGeometry(QtCore.QRect(600, 240, 30, 25))
        self.FastaBrowseButton.setObjectName("FastaBrowseButton")
        self.FastaErrortextRNA = QtWidgets.QLabel(self.input_rna)
        self.FastaErrortextRNA.setGeometry(QtCore.QRect(200, 265, 385, 23))
        self.FastaErrortextRNA.setFont(font_label)
        self.FastaErrortextRNA.setStyleSheet("color: red")
        self.AnnotatedFilelabelRNA = QtWidgets.QLabel(self.input_rna)
        self.AnnotatedFilelabelRNA.setGeometry(QtCore.QRect(20, 290, 171, 17))
        self.AnnotatedFilelabelRNA.setObjectName("AnnotatedFilelabelRNA")
        self.AnnotatedlineEditRNA = QtWidgets.QLineEdit(self.input_rna)
        self.AnnotatedlineEditRNA.setGeometry(QtCore.QRect(200, 290, 385, 23))
        self.AnnotatedlineEditRNA.setObjectName("AnnotatedlineEditRNA")
        self.AnnotatedBrowserButtonRNA = QtWidgets.QPushButton(self.input_rna)
        self.AnnotatedBrowserButtonRNA.setGeometry(QtCore.QRect(600, 290, 30, 25))
        self.AnnotatedBrowserButtonRNA.setObjectName("AnnotatedBrowserButtonRNA")
        self.AnnotatedErrortextRNA = QtWidgets.QLabel(self.input_rna)
        self.AnnotatedErrortextRNA.setGeometry(QtCore.QRect(200, 315, 385, 23))
        self.AnnotatedErrortextRNA.setFont(font_label)
        self.AnnotatedErrortextRNA.setStyleSheet("color: red")

        self.CorelabelRNA = QtWidgets.QLabel(self.input_rna)
        self.CorelabelRNA.setGeometry(QtCore.QRect(20, 340, 157, 17))
        self.CorelabelRNA.setObjectName("CorelabelRNA")
        self.CorelineEditRNA = QtWidgets.QLineEdit(self.input_rna)
        self.CorelineEditRNA.setGeometry(QtCore.QRect(200, 340, 250, 23))
        self.CorelineEditRNA.setObjectName("CorelineEditRNA")
        self.CoreErrortextRNA = QtWidgets.QLabel(self.input_rna)
        self.CoreErrortextRNA.setGeometry(QtCore.QRect(200, 365, 250, 23))
        self.CoreErrortextRNA.setFont(font_label)
        self.CoreErrortextRNA.setStyleSheet("color: red")
        
        ###

        ###
        
        font_label = QtGui.QFont()
        font_label.setPointSize(8.5)

               
        
        
        self.nextbuttoninputRNA = QtWidgets.QPushButton(self.input_rna)
        self.nextbuttoninputRNA.setGeometry(QtCore.QRect(635, 400, 45, 45))
        self.nextbuttoninputRNA.setObjectName("nextbuttoninputRNA")
        
        #####info icon####
        ###rna###
        font_info = QtGui.QFont()
        font_info.setPointSize(8.5)        
        

        
        self.SampleFolderinfoicon_rna = QtWidgets.QPushButton(self.input_rna)
        self.SampleFolderinfoicon_rna.setFlat(True)
        self.SampleFolderinfoicon_rna.setGeometry(QtCore.QRect(120, 139, 20, 20))
        self.SampleFolderinfoicon_rna.setToolTip("Browse for the folder containing all the relevant sample files.\n The filenames for all the fastq input data are required to be in the following format.\n (sample_name)_(condition(tumor/normal))_Rep(replicate_number)_R(1 /2 {1 for read1 and 2 for read2}).fastq.\n Example:hcc1395_normal_Rep1_R1.fastq")
        self.SampleFolderinfoicon_rna.setFont(font_info)
        self.SampleFolderinfoicon_rna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.SampleFolderinfoicon_rna.setIconSize(QtCore.QSize(13, 13))
        
        self.Sampletableinfoicon_rna = QtWidgets.QPushButton(self.input_rna)
        self.Sampletableinfoicon_rna.setFlat(True)
        self.Sampletableinfoicon_rna.setGeometry(QtCore.QRect(116, 190, 20, 20))
        self.Sampletableinfoicon_rna.setToolTip("Browse for the tab separated text file containing the sample information. \n The table is required to be formatted as follows.\n The column names should take the order: Sample, Unit, Condition, fq1, fq2.\n (Sample- Sample name, Unit- Number of replications, \n Condition- normal/ tumor/ leave blank if the condition is not specified, \n fq1 - Path of Read 1,fq2 - Path of Read 2/ leave blank for single-end reads).\n An example table has been provided for your reference")
        self.Sampletableinfoicon_rna.setFont(font_info)
        self.Sampletableinfoicon_rna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.Sampletableinfoicon_rna.setIconSize(QtCore.QSize(13, 13))
        
        self.FastaFileinfoicon_rna = QtWidgets.QPushButton(self.input_rna)
        self.FastaFileinfoicon_rna.setFlat(True)
        self.FastaFileinfoicon_rna.setGeometry(QtCore.QRect(84, 240, 20, 20))
        self.FastaFileinfoicon_rna.setToolTip("A reference genome is a digital nucleic acid database \n assembled to be a representative example of a species’ set of genes.\n It allows for fast alignment of sequences as it is less computationally intensive \n to align sequences to a known sequence map rather than to assemble it piece by piece.\n For this field, specify the path to the pre-downloaded reference genome fastq file")
        self.FastaFileinfoicon_rna.setFont(font_info)
        self.FastaFileinfoicon_rna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.FastaFileinfoicon_rna.setIconSize(QtCore.QSize(13, 13))  
        
        self.AnnotatedFileinfoicon_rna = QtWidgets.QPushButton(self.input_rna)
        self.AnnotatedFileinfoicon_rna.setFlat(True)
        self.AnnotatedFileinfoicon_rna.setGeometry(QtCore.QRect(114, 290, 20, 20))
        self.AnnotatedFileinfoicon_rna.setToolTip("An annotation file is the gene transfer format (GTF) file containing the gene structure information")
        self.AnnotatedFileinfoicon_rna.setFont(font_info)
        self.AnnotatedFileinfoicon_rna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.AnnotatedFileinfoicon_rna.setIconSize(QtCore.QSize(13, 13)) 


        
        self.SamplesYesradioinfoicon_rna = QtWidgets.QPushButton(self.input_rna)
        self.SamplesYesradioinfoicon_rna.setFlat(True)
        self.SamplesYesradioinfoicon_rna.setGeometry(QtCore.QRect(210, 32, 20, 20))
        self.SamplesYesradioinfoicon_rna.setToolTip("Specify the path to the folder containing all the relevant sample files.\n The filenames for all the fastq input data are required to be in the following format.\n (sample_name)_(condition(tumor/normal))_Rep(replicate_number)_R(1 /2 {1 for read1 and 2 for read2}).fastq. \nExample:hcc1395_normal_Rep1_R1.fastq")
        self.SamplesYesradioinfoicon_rna.setFont(font_info)
        self.SamplesYesradioinfoicon_rna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.SamplesYesradioinfoicon_rna.setIconSize(QtCore.QSize(13, 13))       
        
        
        self.SamplesNoradioinfoicon_rna = QtWidgets.QPushButton(self.input_rna)
        self.SamplesNoradioinfoicon_rna.setFlat(True)
        self.SamplesNoradioinfoicon_rna.setGeometry(QtCore.QRect(210, 90, 20, 20))
        self.SamplesNoradioinfoicon_rna.setToolTip("Specify the tab-delimited text file containing the sample information.\n The table is required to be formatted as follows.\n The column names should take the order: Sample, Unit, Condition, fq1, fq2. \n(Sample- Sample name, Unit- Number of replications, Condition- normal/ tumor/ leave blank if the condition is not specified,\n fq1 - Path of Read 1,fq2 - Path of Read 2/ leave blank for single-end reads).\n An example table has been provided for your reference")
        self.SamplesNoradioinfoicon_rna.setFont(font_info)
        self.SamplesNoradioinfoicon_rna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.SamplesNoradioinfoicon_rna.setIconSize(QtCore.QSize(13, 13))
        
        self.coreinfoicon_rna = QtWidgets.QPushButton(self.input_rna)
        self.coreinfoicon_rna.setFlat(True)
        self.coreinfoicon_rna.setGeometry(QtCore.QRect(140, 340, 20, 20))
        self.coreinfoicon_rna.setToolTip("Input the number of threads to run")
        self.coreinfoicon_rna.setFont(font_info)
        self.coreinfoicon_rna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.coreinfoicon_rna.setIconSize(QtCore.QSize(13, 13))         
        
        self.RNAtabWidget.addTab(self.input_rna, "")
        ## End ##
        
        ## Add QC ##
        self.QC_rna = QtWidgets.QWidget()
        self.QC_rna.setObjectName("QC_rna")
        ##QC_RNA Added##
        self.QCresults_rna = QtWidgets.QPushButton(self.QC_rna)
        self.QCresults_rna.setGeometry(QtCore.QRect(10, 30, 150, 23))
        self.QCresults_rna.setText("Quality Control Results")
        self.QCresults_rna.setStyleSheet("background-color: #704214")
        self.QCresultsButtonErroricon_rna = QtWidgets.QPushButton(self.QC_rna)
        self.QCresultsButtonErroricon_rna.setGeometry(QtCore.QRect(186, 32, 20, 20))
        self.QCresultsButtonErroricon_rna.setToolTip("Check and Run View Quality control Results Again!")
        self.QCresultsButtonErroricon_rna.setFont(font_label)
        self.QCresultsButtonErroricon_rna.setIcon(QtGui.QIcon("./icons/warning.svg"))
        self.QCresultsButtonErroricon_rna.hide()
        self.QClabel_rna = QtWidgets.QLabel(self.QC_rna)
        self.QClabel_rna.setGeometry(QtCore.QRect(10, 85, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.QClabel_rna.setFont(font)
        self.QClabel_rna.setObjectName("QClabel_rna")
        self.QCYesradioButton_rna = QtWidgets.QRadioButton(self.QC_rna)
        self.QCYesradioButton_rna.setGeometry(QtCore.QRect(170, 85, 117, 22))
        self.QCYesradioButton_rna.setObjectName("QCYesradioButton_rna")
#        self.QCYesradioButton_rna.setChecked(True)
        self.QCNoradioButton_rna = QtWidgets.QRadioButton(self.QC_rna)
        self.QCNoradioButton_rna.setGeometry(QtCore.QRect(250, 85, 117, 22))
        self.QCNoradioButton_rna.setObjectName("QCNoradioButton_rna")
        self.QCNoradioButton_rna.setChecked(True)
        self.InputParamslabel_rna = QtWidgets.QLabel(self.QC_rna)
        self.InputParamslabel_rna.setGeometry(QtCore.QRect(10, 140, 171, 17))
        self.InputParamslabel_rna.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.InputParamslabel_rna.setFont(font)
        self.InputParamslabel_rna.setObjectName("InputParamslabel_rna")

        self.CutadaptlineEdit_rna = QtWidgets.QLineEdit(self.QC_rna)
        self.CutadaptlineEdit_rna.setGeometry(QtCore.QRect(120, 200, 481, 23))
        self.CutadaptlineEdit_rna.setObjectName("CutadaptlineEdit_rna")
        self.Cutadaptlabel_rna = QtWidgets.QLabel(self.QC_rna)
        self.Cutadaptlabel_rna.setGeometry(QtCore.QRect(10, 200, 67, 17))
        self.Cutadaptlabel_rna.setObjectName("Cutadaptlabel_rna")
        self.Cutadaptlabel_rna.setEnabled(False)
        self.CutadaptlineEdit_rna.setEnabled(False)

        self.horizontalLayoutWidget_rna = QtWidgets.QWidget(self.QC_rna)
        self.horizontalLayoutWidget_rna.setGeometry(QtCore.QRect(235, 273, 240, 31))
        self.horizontalLayoutWidget_rna.setObjectName("horizontalLayoutWidget_rna")
        self.horizontalLayout_4_rna = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_rna)
        self.horizontalLayout_4_rna.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4_rna.setObjectName("horizontalLayout_4_rna")

        self.RunQCpushButton_rna = QtWidgets.QPushButton(self.horizontalLayoutWidget_rna)
        self.RunQCpushButton_rna.setObjectName("RunQCpushButton_rna")
        self.RunQCpushButton_rna.setEnabled(False)
        self.horizontalLayout_4_rna.addWidget(self.RunQCpushButton_rna)
        self.RunQCButtonErroricon_rna = QtWidgets.QPushButton(self.QC_rna)
        self.RunQCButtonErroricon_rna.setGeometry(QtCore.QRect(500, 277, 20, 20))
        self.RunQCButtonErroricon_rna.setToolTip("Check and Run Trimming Again!")
        self.RunQCButtonErroricon_rna.setFont(font_label)
        self.RunQCButtonErroricon_rna.setIcon(QtGui.QIcon("./icons/warning.svg"))

        self.RunQCButtonErroricon_rna.hide()
        ##QC_Progressbar##
        self.progressBar_sub1_rna = QtWidgets.QProgressBar(self.QC_rna)
        self.progressBar_sub1_rna.setGeometry(QtCore.QRect(10, 355, 665, 17))
        self.progressBar_sub1_rna.setProperty("value", 0)
        self.progressBar_sub1_rna.setObjectName("progressBar_sub1_rna")
        ###
        self.nextbuttonqcRNA = QtWidgets.QPushButton(self.QC_rna)
        self.nextbuttonqcRNA.setGeometry(QtCore.QRect(635, 400, 45, 45))
        self.nextbuttonqcRNA.setObjectName("nextbuttonqcRNA")
#        self.nextbuttonqcRNA.setEnabled(False)
        ###
        self.previousbuttonqcRNA = QtWidgets.QPushButton(self.QC_rna)
        self.previousbuttonqcRNA.setGeometry(QtCore.QRect(10, 400,45, 45))
        self.previousbuttonqcRNA.setObjectName("previousbuttonqcRNA")
        
        
        font_info = QtGui.QFont()
        font_info.setPointSize(8.5)
        
        self.QCresultsinfoicon_rna = QtWidgets.QPushButton(self.QC_rna)
        self.QCresultsinfoicon_rna.setFlat(True)
        self.QCresultsinfoicon_rna.setGeometry(QtCore.QRect(166, 33, 20, 20))
        self.QCresultsinfoicon_rna.setToolTip("Generates a MultiQC report consisting of statistical metrics\n aggregated from FastQC for each sample input file.\n If the results obtained are satisfactory, you may move onto the next tab.\n If not, proceed to trim the reads to improve the quality of your data")
        self.QCresultsinfoicon_rna.setFont(font_info)
        self.QCresultsinfoicon_rna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.QCresultsinfoicon_rna.setIconSize(QtCore.QSize(13, 13))          
        
        self.QClabelinfoicon_rna = QtWidgets.QPushButton(self.QC_rna)
        self.QClabelinfoicon_rna.setFlat(True)
        self.QClabelinfoicon_rna.setGeometry(QtCore.QRect(131, 87, 20, 20))
        self.QClabelinfoicon_rna.setToolTip("Selecting 'Yes' will remove the adapter sequences from your data thereby improving data quality.\n 'No' can be selected if you are satisfied with the data quality")
        self.QClabelinfoicon_rna.setFont(font_info)
        self.QClabelinfoicon_rna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.QClabelinfoicon_rna.setIconSize(QtCore.QSize(13, 13))          
        
        self.Cutadaptlabelinfoicon_rna = QtWidgets.QPushButton(self.QC_rna)
        self.Cutadaptlabelinfoicon_rna.setFlat(True)
        self.Cutadaptlabelinfoicon_rna.setGeometry(QtCore.QRect(70, 199, 20, 20))
        self.Cutadaptlabelinfoicon_rna.setToolTip("Please input the necessary parameters for the tool cutadapt.\n It may include the adapter sequences.\n Refer https://cutadapt.readthedocs.io/en/stable/guide.html#adapter-types for details")
        self.Cutadaptlabelinfoicon_rna.setFont(font_info)
        self.Cutadaptlabelinfoicon_rna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.Cutadaptlabelinfoicon_rna.setIconSize(QtCore.QSize(13, 13))    
        
        self.RunQCpushButtoninfoicon_rna = QtWidgets.QPushButton(self.QC_rna)
        self.RunQCpushButtoninfoicon_rna.setFlat(True)
        self.RunQCpushButtoninfoicon_rna.setGeometry(QtCore.QRect(480, 277, 20, 20))
        self.RunQCpushButtoninfoicon_rna.setToolTip("Please choose yes to trim your reads if the input sequences are of poor quality.\n You may proceed to the next section if your reads are good enough for alignment")
        self.RunQCpushButtoninfoicon_rna.setFont(font_info)
        self.RunQCpushButtoninfoicon_rna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.RunQCpushButtoninfoicon_rna.setIconSize(QtCore.QSize(13, 13))             
        
        self.RNAtabWidget.addTab(self.QC_rna, "")
        ## End ##
        self.Tool_rna = QtWidgets.QWidget()
        self.Tool_rna.setObjectName("Tool_rna")
        self.Tool_rna.setStyleSheet("background-image: url(toolstab.png);")
        
        self.create_aligner_groupbox_rna()
        self.create_em_groupbox()
        self.create_de_groupbox()
        self.create_group_next_rna()
        self.nextbuttoninputRNA
        self.layout_rna = QtWidgets.QHBoxLayout(self.Tool_rna)
        self.scrollArea_rna = QtWidgets.QScrollArea(self.Tool_rna)
        self.scrollArea_rna.setWidgetResizable(True)
        self.scrollAreaWidgetContents_rna = QtWidgets.QWidget()
        self.gridLayout_rna = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_rna)
        self.scrollArea_rna.setWidget(self.scrollAreaWidgetContents_rna)
        self.layout_rna.addWidget(self.scrollArea_rna)
        
        self.grp_list_rna=[self.aligner_groupbox_rna, self.em_groupbox, self.de_groupbox, self.next_groupbox_rna]
        for i in range(4):
            self.gridLayout_rna.addWidget(self.grp_list_rna[i], i,0)
        
        self.RNAtabWidget.addTab(self.Tool_rna, "")

        ## End ##
        
        ##Add Run##
        self.run_rna = QtWidgets.QWidget()
        self.run_rna.setObjectName("run_rna")
        
        self.RunButton = QtWidgets.QPushButton(self.run_rna)
        self.RunButton.setGeometry(QtCore.QRect(300, 140, 100, 100))
        self.RunButton.setObjectName("RunButton")
        self.RunLabel = QtWidgets.QLabel(self.run_rna)
        self.RunLabel.setGeometry(QtCore.QRect(330, 255, 180, 17))
        self.RunLabel.setObjectName("RunLabel")
        
        self.RunButtonErroricon = QtWidgets.QPushButton(self.run_rna)
        self.RunButtonErroricon.setGeometry(QtCore.QRect(420, 172, 30, 30))
        self.RunButtonErroricon.setToolTip("Click Run Button and Run Again!")
        self.RunButtonErroricon.setFont(font_label)
        self.RunButtonErroricon.setIcon(QtGui.QIcon("./icons/warning.svg"))
        self.RunButtonErroricon.hide()      
        
        
        self.progressBar = QtWidgets.QProgressBar(self.run_rna)
        self.progressBar.setGeometry(QtCore.QRect(10, 340, 670, 23))
        self.progressBar.setProperty("value", 0)
#        self.progressBar.setMaximum(3)
        self.progressBar.setObjectName("progressBar")        
        
        
        self.nextbuttonrunRNA = QtWidgets.QPushButton(self.run_rna)
        self.nextbuttonrunRNA.setGeometry(QtCore.QRect(635, 400, 45, 45))
        self.nextbuttonrunRNA.setObjectName("nextbuttonrunRNA")
        ###
        self.previousbuttonrunRNA = QtWidgets.QPushButton(self.run_rna)
        self.previousbuttonrunRNA.setGeometry(QtCore.QRect(10, 400,45, 45))
        self.previousbuttonrunRNA.setObjectName("previousbuttonrunRNA")        
        
        
        font_info = QtGui.QFont()
        font_info.setPointSize(8.5)
        
        self.RunButtoninfoicon_rna = QtWidgets.QPushButton(self.run_rna)
        self.RunButtoninfoicon_rna.setFlat(True)
        self.RunButtoninfoicon_rna.setGeometry(QtCore.QRect(400, 180, 20, 20))
        self.RunButtoninfoicon_rna.setToolTip("Click to start your analysis")
        self.RunButtoninfoicon_rna.setFont(font_info)
        self.RunButtoninfoicon_rna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.RunButtoninfoicon_rna.setIconSize(QtCore.QSize(13, 13)) 
        

        
        self.RNAtabWidget.addTab(self.run_rna, "")
        ##End##
        ##Add Result RNA##
        self.result_rna = QtWidgets.QWidget()
        self.result_rna.setObjectName("result_rna")
        font_resulttab = QtGui.QFont()
        font_resulttab.setPointSize(16)

        self.pushbutton_result1_rna=QtWidgets.QPushButton(self.result_rna)
        self.pushbutton_result1_rna.setText("Run statistics")
        self.pushbutton_result1_rna.setIcon(QtGui.QIcon("./icons/runstatistics.svg"))
        self.pushbutton_result1_rna.setIconSize(QtCore.QSize(40, 40))
        self.pushbutton_result1_rna.setFont(font_resulttab)
        self.pushbutton_result1_rna.setStyleSheet("background-color: #704214")
        self.pushbutton_result1_rna.setGeometry(QtCore.QRect(215, 145, 255, 48))

        self.pushbutton_result2_rna=QtWidgets.QPushButton(self.result_rna)
        self.pushbutton_result2_rna.setText("DE Genes")
        self.pushbutton_result2_rna.setIcon(QtGui.QIcon("./icons/document.svg"))
        self.pushbutton_result2_rna.setIconSize(QtCore.QSize(40, 40))
        self.pushbutton_result2_rna.setFont(font_resulttab)
        self.pushbutton_result2_rna.setStyleSheet("background-color: #704214")
        self.pushbutton_result2_rna.setGeometry(QtCore.QRect(215, 245, 255, 48))

        self.pushbutton_result3_rna=QtWidgets.QPushButton(self.result_rna)
        self.pushbutton_result3_rna.setText("Plots")
        self.pushbutton_result3_rna.setIcon(QtGui.QIcon("./icons/plots.svg"))
        self.pushbutton_result3_rna.setIconSize(QtCore.QSize(40, 40))
        self.pushbutton_result3_rna.setFont(font_resulttab)
        self.pushbutton_result3_rna.setStyleSheet("background-color: #704214")
        self.pushbutton_result3_rna.setGeometry(QtCore.QRect(215, 345, 255, 48))
        
        self.RNAtabWidget.addTab(self.result_rna, "")
        ##End##        
        
        ## Add Create ##

        ## End ##
        self.PipelinetabWidget.addTab(self.RNAseq, "")
        
        self.CTAG = QtWidgets.QWidget()
        self.CTAG.setObjectName("CTAG")
        self.CTAGtabWidget = QtWidgets.QTabWidget(self.CTAG)
        self.CTAGtabWidget.setGeometry(QtCore.QRect(0, 0, 695, 507))
        self.CTAGtabWidget.setMovable(False)
        self.CTAGtabWidget.setTabBarAutoHide(False)
        self.CTAGtabWidget.setObjectName("CTAGtabWidget")
        self.CTAGtabWidget.setStyleSheet("background-image: url(dnatab.png);")
        
        self.ctaglabel = QtWidgets.QLabel(self.CTAG)
        self.ctaglabel.setGeometry(QtCore.QRect(15, 25, 400, 20))
        self.ctaglabel.setObjectName("ctaglabel")
        self.ctaglabel.setEnabled(True)
        
        self.ctaglabel2 = QtWidgets.QLabel(self.CTAG)
        self.ctaglabel2.setGeometry(QtCore.QRect(20, 35, 1000, 100))
        self.ctaglabel2.setObjectName("ctaglabel2")
        self.ctaglabel2.setEnabled(True)
        
        self.ctaglabel3 = QtWidgets.QLabel(self.CTAG)
        self.ctaglabel3.setGeometry(QtCore.QRect(65, 90, 400, 100))
        self.ctaglabel3.setObjectName("ctaglabel3")
        self.ctaglabel3.setEnabled(True)
        self.ctaglabel3.setOpenExternalLinks(True)
#        urlLink = "<a href="https://github.com/.RamanLab/NBDriver"> NBDriver</a>"
        self.ctaggithubbutton = QtWidgets.QPushButton(self.CTAG)
        self.ctaggithubbutton.setGeometry(QtCore.QRect(20, 130, 30, 25))
        self.ctaggithubbutton.setObjectName("ctaggithubbutton")        
        
        self.maflineEdit = QtWidgets.QLineEdit(self.CTAG)
        self.maflineEdit.setGeometry(QtCore.QRect(160, 200, 450, 23))
        self.maflineEdit.setObjectName("maflineEdit")
        self.maflabel = QtWidgets.QLabel(self.CTAG)
        self.maflabel.setGeometry(QtCore.QRect(10, 200, 100, 17))
        self.maflabel.setObjectName("maflabel")
        self.maflabel.setEnabled(True)
        self.maflineEdit.setEnabled(True)
        self.mafBrowseButton = QtWidgets.QPushButton(self.CTAG)
        self.mafBrowseButton.setGeometry(QtCore.QRect(620, 200, 30, 25))
        self.mafBrowseButton.setObjectName("mafBrowseButton")
        
        self.mafparamlineEdit = QtWidgets.QLineEdit(self.CTAG)
        self.mafparamlineEdit.setGeometry(QtCore.QRect(200, 260, 155, 23))
        self.mafparamlineEdit.setObjectName("maflineEdit")
        self.mafparamlineEdit1 = QtWidgets.QLineEdit(self.CTAG)
        self.mafparamlineEdit1.setGeometry(QtCore.QRect(440, 260, 155, 23))
        self.mafparamlineEdit1.setObjectName("maflineEdit")
        self.mafparamlabel = QtWidgets.QLabel(self.CTAG)
        self.mafparamlabel.setGeometry(QtCore.QRect(10, 260, 100, 17))
        self.mafparamlabel.setObjectName("maflabel")
        self.mafparamlabel.setEnabled(True)
        self.mafparamlineEdit.setEnabled(True)
        self.mafparamlabel1 = QtWidgets.QLabel(self.CTAG)
        self.mafparamlabel1.setGeometry(QtCore.QRect(170, 260, 50, 17))
        self.mafparamlabel1.setObjectName("maflabel1")
        self.mafparamlabel2 = QtWidgets.QLabel(self.CTAG)
        self.mafparamlabel2.setGeometry(QtCore.QRect(410, 260, 50, 17))
        self.mafparamlabel2.setObjectName("maflabel2")
        self.runctagpushButton = QtWidgets.QPushButton(self.CTAG)
        self.runctagpushButton.setGeometry(QtCore.QRect(270, 350, 200, 30))
        self.runctagpushButton.setObjectName("runctagpushButton")
        
        self.resultctagpushButton = QtWidgets.QPushButton(self.CTAG)
        self.resultctagpushButton.setGeometry(QtCore.QRect(290, 410, 150, 50))
        self.resultctagpushButton.setObjectName("resultctagpushButton")
        
        self.ctaginfoiconmaf = QtWidgets.QPushButton(self.CTAG)
        self.ctaginfoiconmaf.setFlat(True)
        self.ctaginfoiconmaf.setGeometry(QtCore.QRect(109, 200, 20, 20))
        self.ctaginfoiconmaf.setToolTip("path to the maf file")
        self.ctaginfoiconmaf.setFont(font_info)
        self.ctaginfoiconmaf.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.ctaginfoiconmaf.setIconSize(QtCore.QSize(13, 13)) 
        
        self.ctaginfoiconparam = QtWidgets.QPushButton(self.CTAG)
        self.ctaginfoiconparam.setFlat(True)
        self.ctaginfoiconparam.setGeometry(QtCore.QRect(90, 260, 20, 20))
        self.ctaginfoiconparam.setToolTip("enter the parameters --maxmut and --percentile")
        self.ctaginfoiconparam.setFont(font_info)
        self.ctaginfoiconparam.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.ctaginfoiconparam.setIconSize(QtCore.QSize(13, 13)) 
        
        self.ctaginfoiconrun = QtWidgets.QPushButton(self.CTAG)
        self.ctaginfoiconrun.setFlat(True)
        self.ctaginfoiconrun.setGeometry(QtCore.QRect(472, 355, 20, 20))
        self.ctaginfoiconrun.setToolTip("Click Run to run the analysis")
        self.ctaginfoiconrun.setFont(font_info)
        self.ctaginfoiconrun.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.ctaginfoiconrun.setIconSize(QtCore.QSize(13, 13)) 
        
        self.ctaginfoiconres = QtWidgets.QPushButton(self.CTAG)
        self.ctaginfoiconres.setFlat(True)
        self.ctaginfoiconres.setGeometry(QtCore.QRect(447, 423, 20, 20))
        self.ctaginfoiconres.setToolTip("Click View Results to open the results")
        self.ctaginfoiconres.setFont(font_info)
        self.ctaginfoiconres.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.ctaginfoiconres.setIconSize(QtCore.QSize(13, 13))
        
        self.PipelinetabWidget.addTab(self.CTAG, "")
        
        self.NB = QtWidgets.QWidget()
        self.NB.setObjectName("NV")
        self.NBtabWidget = QtWidgets.QTabWidget(self.NB)
        self.NBtabWidget.setGeometry(QtCore.QRect(0, 0, 695, 507))
        self.NBtabWidget.setMovable(False)
        self.NBtabWidget.setTabBarAutoHide(False)
        self.NBtabWidget.setObjectName("NBtabWidget")
        self.NBtabWidget.setStyleSheet("background-image: url(dnatab.png);")
        
        self.nblabel = QtWidgets.QLabel(self.NB)
        self.nblabel.setGeometry(QtCore.QRect(15, 25, 400, 20))
        self.nblabel.setObjectName("nblabel")
        self.nblabel.setEnabled(True)
        
        self.nblabel2 = QtWidgets.QLabel(self.NB)
        self.nblabel2.setGeometry(QtCore.QRect(20, 35, 1000, 100))
        self.nblabel2.setObjectName("nblabel2")
        self.nblabel2.setEnabled(True)
        
        self.nblabel3 = QtWidgets.QLabel(self.NB)
        self.nblabel3.setGeometry(QtCore.QRect(65, 90, 400, 100))
        self.nblabel3.setObjectName("nblabel3")
        self.nblabel3.setEnabled(True)
        self.nblabel3.setOpenExternalLinks(True)
#        urlLink = "<a href="https://github.com/.RamanLab/NBDriver"> NBDriver</a>"
        self.nbgithubbutton = QtWidgets.QPushButton(self.NB)
        self.nbgithubbutton.setGeometry(QtCore.QRect(20, 130, 30, 25))
        self.nbgithubbutton.setObjectName("nbgithubbutton")
        self.nbpaperbutton = QtWidgets.QPushButton(self.NB)
        self.nbpaperbutton.setGeometry(QtCore.QRect(140, 130, 30, 25))
        self.nbpaperbutton.setObjectName("nbpaperbutton")
        
        self.nblabel5 = QtWidgets.QLabel(self.NB)
        self.nblabel5.setGeometry(QtCore.QRect(185, 90, 400, 100))
        self.nblabel5.setObjectName("nblabel5")
        self.nblabel5.setEnabled(True)
        self.nblabel5.setOpenExternalLinks(True)
        self.nblabel4 = QtWidgets.QLabel(self.NB)
        self.nblabel4.setGeometry(QtCore.QRect(10, 160, 1000, 100))
        self.nblabel4.setObjectName("nblabel4") 
        self.nblabel6 = QtWidgets.QLabel(self.NB)
        self.nblabel6.setGeometry(QtCore.QRect(151, 161, 100, 100))
        self.nblabel6.setObjectName("nblabel6")
        self.nblabel6.setEnabled(True)
        self.nblabel6.setOpenExternalLinks(True)
        
        self.vcflineEdit = QtWidgets.QLineEdit(self.NB)
        self.vcflineEdit.setGeometry(QtCore.QRect(160, 250, 450, 23))
        self.vcflineEdit.setObjectName("vcflineEdit")
        self.vcflabel = QtWidgets.QLabel(self.NB)
        self.vcflabel.setGeometry(QtCore.QRect(10, 250, 100, 17))
        self.vcflabel.setObjectName("vcflabel")
        self.vcflabel.setEnabled(True)
        self.vcflineEdit.setEnabled(True)
        self.vcfBrowseButton = QtWidgets.QPushButton(self.NB)
        self.vcfBrowseButton.setGeometry(QtCore.QRect(620, 250, 30, 25))
        self.vcfBrowseButton.setObjectName("vcfBrowseButton")
        self.runnbpushButton = QtWidgets.QPushButton(self.NB)
        self.runnbpushButton.setGeometry(QtCore.QRect(270, 350, 200, 30))
        self.runnbpushButton.setObjectName("runnbpushButton")
        
        self.resultnbpushButton = QtWidgets.QPushButton(self.NB)
        self.resultnbpushButton.setGeometry(QtCore.QRect(290, 410, 150, 50))
        self.resultnbpushButton.setObjectName("resultnbpushButton")
        
        self.nbinfoiconvcf = QtWidgets.QPushButton(self.NB)
        self.nbinfoiconvcf.setFlat(True)
        self.nbinfoiconvcf.setGeometry(QtCore.QRect(109, 250, 20, 20))
        self.nbinfoiconvcf.setToolTip("path to the vcf file")
        self.nbinfoiconvcf.setFont(font_info)
        self.nbinfoiconvcf.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.nbinfoiconvcf.setIconSize(QtCore.QSize(13, 13)) 
        
        self.nbinfoiconrun = QtWidgets.QPushButton(self.NB)
        self.nbinfoiconrun.setFlat(True)
        self.nbinfoiconrun.setGeometry(QtCore.QRect(472, 355, 20, 20))
        self.nbinfoiconrun.setToolTip("Click Run to run the analysis")
        self.nbinfoiconrun.setFont(font_info)
        self.nbinfoiconrun.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.nbinfoiconrun.setIconSize(QtCore.QSize(13, 13)) 
        
        self.nbinfoiconres = QtWidgets.QPushButton(self.NB)
        self.nbinfoiconres.setFlat(True)
        self.nbinfoiconres.setGeometry(QtCore.QRect(447, 423, 20, 20))
        self.nbinfoiconres.setToolTip("Click View Results to open the results")
        self.nbinfoiconres.setFont(font_info)
        self.nbinfoiconres.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.nbinfoiconres.setIconSize(QtCore.QSize(13, 13))
        
        self.PipelinetabWidget.addTab(self.NB, "")


        
        self.ShellTab = QtWidgets.QTabWidget(self.centralwidget)
        self.ShellTab.setGeometry(QtCore.QRect(10, 550, 701, 151))
        self.ShellTab.setObjectName("ShellTab")
#        self.ShellTab.setStyleSheet("background-color: #F0F9EC")
        self.ShellTab.setStyleSheet("background-image: url(shell1.png);")
        self.SnakemakeOutputTab = QtWidgets.QWidget()
        self.SnakemakeOutputTab.setObjectName("SnakemakeOutputTab")
        self.textBrowser = QtWidgets.QTextBrowser(self.SnakemakeOutputTab)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 695, 118))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setReadOnly(True)

        self.ShellTab.addTab(self.SnakemakeOutputTab, "")
        
        self.PipelinetabWidget.addTab(self.NB, "")


#        self.layoutWidget.raise_()
        self.PipelinetabWidget.raise_()
        self.progressBar_sub1_dna.raise_()
        self.progressBar_sub2_dna.raise_()
#        self.progressBar_sub3.raise_()
#        self.progressBar.raise_()
        self.ShellTab.raise_()
        self.RefVariantpushButton.raise_()
        self.UnitsBrowseButtonDNA.raise_()
        self.SampleslineEditDNA.raise_()
        self.RefGenomeBrowseButtonDNA.raise_()
        self.SampleFilelabelDNA.raise_()
        self.UnitsFilelabelDNA.raise_()
        self.RefVariantlabelDNA.raise_()
#        self.RefNamelineEdit.raise_()
        self.RefGenomelineEditDNA.raise_()
        self.RefGenomelabelDNA.raise_()
        self.RefNamelabelDNA.raise_()
        self.SamplesBrowseButtonDNA.raise_()
        self.UnitslineEditDNA.raise_()
        self.RefNamecomboBoxDNA.raise_()
        self.RefVariantpushButton.raise_()
        self.RefVariantlineEditDNA.raise_()
        self.UnitsBrowseButtonDNA.raise_()
        self.SampleslineEditDNA.raise_()
        self.RefGenomeBrowseButtonDNA.raise_()
        self.SampleFilelabelDNA.raise_()
        self.UnitsFilelabelDNA.raise_()
        self.RefVariantlabelDNA.raise_()
        self.RefGenomelineEditDNA.raise_()
        self.RefGenomelabelDNA.raise_()
        self.RefNamelabelDNA.raise_()
        self.SamplesBrowseButtonDNA.raise_()
        self.UnitslineEditDNA.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 619, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOption = QtWidgets.QMenu(self.menubar)
        self.menuOption.setObjectName("menuOption")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionQuick_Start = QtWidgets.QAction(MainWindow)
        self.actionQuick_Start.setObjectName("actionQuick_Start")
        self.actionAbout_2 = QtWidgets.QAction(MainWindow)
        self.actionAbout_2.setObjectName("actionAbout_2")
        self.actionSnakemake_Options = QtWidgets.QAction(MainWindow)
        self.actionSnakemake_Options.setObjectName("actionSnakemake_Options")
        self.menuFile.addAction(self.actionQuit)
        self.menuOption.addAction(self.actionSnakemake_Options)
        self.menuHelp.addAction(self.actionQuick_Start)
        self.menuHelp.addAction(self.actionAbout_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOption.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.PipelinetabWidget.setCurrentIndex(0)
        self.DNAtabWidget.setCurrentIndex(0)
        self.RNAtabWidget.setCurrentIndex(0)
        self.ShellTab.setCurrentIndex(0)
        self.actionQuit.triggered.connect(MainWindow.close)
#        QtCore.Qt.WindowMaximizeButton.hide()
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self._colors = {
            'green': QtGui.QColor(0,170,0),
            'red': QtGui.QColor(170,0,0),
            'orange': QtGui.QColor(170,150,0),
            'blue': QtGui.QColor(0,90,154),
            'black': QtGui.QColor(0,0,0),
        }
        
        ####set all tabs disabled###
# =============================================================================
        self.DNAtabWidget.setTabEnabled(1, False)
        self.DNAtabWidget.setTabEnabled(2, False)
        self.DNAtabWidget.setTabEnabled(3, False)
        self.DNAtabWidget.setTabEnabled(4, False)
        self.DNAtabWidget.setTabEnabled(5, False)
         
        self.RNAtabWidget.setTabEnabled(1, False)
        self.RNAtabWidget.setTabEnabled(2, False)
        self.RNAtabWidget.setTabEnabled(3, False)
        self.RNAtabWidget.setTabEnabled(4, False)
        self.RNAtabWidget.setTabEnabled(5, False)
# =============================================================================

                

############


############
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "iCOMIC"))
        MainWindow.setWindowIcon(QtGui.QIcon("./icons/taskbar1.png"))
        #self.PipelinetabWidget.setToolTip(_translate("MainWindow", "Performs Quality Control and Creates Mandatory files to run the pipeline"))
        ## Add Input as first tab ##
#        self.SampleOrlabel.setToolTip(_translate("MainWindow", "This option performs all the Quality Control operations like fastQC, Cutadapt and MultiQC "))
        self.SampleOrlabel.setText(_translate("MainWindow", "Or"))
#        self.SamplesYesradioButton.setToolTip(_translate("MainWindow", "Files should be in specified format"))
        self.SamplesYesradioButton.setText(_translate("MainWindow", "Upload from Folder"))
#        self.SamplesNoradioButton.setToolTip(_translate("MainWindow", "Tables should contain all the information"))
        self.SamplesNoradioButton.setText(_translate("MainWindow", "Upload from Table"))
#        self.UnitsBrowseButtonDNA.setText(_translate("MainWindow", "Browse"))
        self.UnitsBrowseButtonDNA.setIcon(QtGui.QIcon("./icons/browse.png"))
        self.UnitsBrowseButtonDNA.setIconSize(QtCore.QSize(22, 22))
        self.UnitsBrowseButtonDNA.setToolTip("Browse Samples Table")
#        self.RefGenomeBrowseButtonDNA.setText(_translate("MainWindow", "Browse"))
        self.RefGenomeBrowseButtonDNA.setIcon(QtGui.QIcon("./icons/browse.png"))
#        self.RefGenomeBrowseButtonDNA.setStyleSheet("background-color: #aeaeae")
        self.RefGenomeBrowseButtonDNA.setToolTip("Browse Reference Genome")
        self.RefGenomeBrowseButtonDNA.setIconSize(QtCore.QSize(22, 22))
        self.UnitsFilelabelDNA.setText(_translate("MainWindow", "Samples Table"))
        self.RefGenomelabelDNA.setText(_translate("MainWindow", "Reference Genome"))
        self.SampleFilelabelDNA.setText(_translate("MainWindow", "Samples Folder"))
        self.CorelabelDNA.setText(_translate("MainWindow", "Maximum threads"))
        self.CorelineEditDNA.setText(_translate("MainWindow", "10"))
#        self.SamplesBrowseButtonDNA.setText(_translate("MainWindow", "Browse"))
        self.SamplesBrowseButtonDNA.setIcon(QtGui.QIcon("./icons/browse.png"))
        self.SamplesBrowseButtonDNA.setIconSize(QtCore.QSize(22, 22))
#        self.SamplesBrowseButtonDNA.setStyleSheet("background-color: #aeaeae")
        self.SamplesBrowseButtonDNA.setToolTip("Browse Samples Folder")
        self.RefVariantlabelDNA.setText(_translate("MainWindow", "Reference Known Variant"))
#        self.RefVariantpushButton.setText(_translate("MainWindow", "Browse"))
        self.RefVariantpushButton.setIcon(QtGui.QIcon("./icons/browse.png"))
#        self.RefVariantpushButton.setStyleSheet("background-color: #aeaeae")
        self.RefVariantpushButton.setToolTip("Browse Reference Known Variant")
        self.RefVariantpushButton.setIconSize(QtCore.QSize(22, 22))
        self.RefNamelabelDNA.setText(_translate("MainWindow", "Reference Name (as in SnpEff Database)"))

        self.nextbuttoninputDNA.setIcon(QtGui.QIcon("./icons/arrow.svg"))
        self.nextbuttoninputDNA.setIconSize(QtCore.QSize(35, 35))
        self.nextbuttoninputDNA.setStyleSheet("background-color: #704214")
        self.DNAtabWidget.setTabText(self.DNAtabWidget.indexOf(self.input_dna), _translate("MainWindow", " Input Data "))
        self.DNAtabWidget.setTabIcon(self.DNAtabWidget.indexOf(self.input_dna), QtGui.QIcon('./icons/input.svg'))
#        self.DNAtabWidget.setStyleSheet(self.DNAtabWidget.indexOf(self.input_dna), ("background-color: #EBF6F5"))
        self.DNAtabWidget.setIconSize(QtCore.QSize(22, 22))
        
        ## End ###
        
        ##Label progres bar##

        
        ## Add QC ##
        self.QClabel.setToolTip(_translate("MainWindow", "This option performs all the Quality Control operations like fastQC, Cutadapt and MultiQC "))
        self.QClabel.setText(_translate("MainWindow", "Trim the reads"))
        self.QCYesradioButton.setToolTip(_translate("MainWindow", "Enables Quality Control Processing"))
        self.QCYesradioButton.setText(_translate("MainWindow", "Yes"))
        self.QCNoradioButton.setToolTip(_translate("MainWindow", "Disables Quality Control Processing"))
        self.QCNoradioButton.setText(_translate("MainWindow", "No"))
        self.InputParamslabel.setText(_translate("MainWindow", "Input Parameters:"))

        self.Cutadaptlabel.setText(_translate("MainWindow", "Cutadapt"))
        self.CutadaptlineEdit.setText(_translate("MainWindow", "-q 20"))

        self.RunQCpushButton.setText(_translate("MainWindow", "Trimming"))
        self.RunQCpushButton.setIcon(QtGui.QIcon("./icons/run1.svg"))
        self.RunQCpushButton.setIconSize(QtCore.QSize(22, 22))
        self.RunQCpushButton.setStyleSheet("background-color: #704214")
        self.nextbuttonqcDNA.setIcon(QtGui.QIcon("./icons/arrow.svg"))
        self.nextbuttonqcDNA.setStyleSheet("background-color: #704214")
        self.nextbuttonqcDNA.setIconSize(QtCore.QSize(35, 35))
        self.previousbuttonqcDNA.setIcon(QtGui.QIcon("./icons/arrow1.svg"))
        self.previousbuttonqcDNA.setStyleSheet("background-color: #704214")
        self.previousbuttonqcDNA.setIconSize(QtCore.QSize(35, 35))
        self.DNAtabWidget.setTabText(self.DNAtabWidget.indexOf(self.QC_dna), _translate("MainWindow", " Quality Control "))
        self.DNAtabWidget.setTabIcon(self.DNAtabWidget.indexOf(self.QC_dna), QtGui.QIcon('./icons/qc.svg'))
        
        
        ## End ##

        self.AlignercomboBoxDNA.setItemText(0, _translate("MainWindow", "BWA_MEM"))
        self.AlignercomboBoxDNA.setItemText(1, _translate("MainWindow", "GEM3"))
        self.AlignercomboBoxDNA.setItemText(2, _translate("MainWindow", "Bowtie2"))
# 
        self.AnnotatorcomboBoxDNA.setItemText(0, _translate("MainWindow", "SnpEff"))
        self.AnnotatorcomboBoxDNA.setItemText(1, _translate("MainWindow", "Annovar"))

        self.nextbuttontoolDNA.setIcon(QtGui.QIcon("./icons/arrow.svg"))
        self.nextbuttontoolDNA.setStyleSheet("background-color: #704214")
        self.nextbuttontoolDNA.setIconSize(QtCore.QSize(35, 35))
        self.previousbuttontoolDNA.setIcon(QtGui.QIcon("./icons/arrow1.svg"))
        self.previousbuttontoolDNA.setStyleSheet("background-color: #704214")
        self.previousbuttontoolDNA.setIconSize(QtCore.QSize(35, 35))
        self.DNAtabWidget.setTabText(self.DNAtabWidget.indexOf(self.Tool_dna), _translate("MainWindow", " Tools Selection "))
        self.Tool_dna.setStyleSheet("background-image: url(toolstab.png);")
        self.DNAtabWidget.setTabIcon(self.DNAtabWidget.indexOf(self.Tool_dna), QtGui.QIcon('./icons/tools.svg'))
        
        ## Add Index ##

        self.BWAIndexlineEdit.setToolTip(_translate("MainWindow", "Input the path of the Index for " + self.AlignercomboBoxDNA.currentText()))
        self.BWAIndexpushButton.setToolTip(_translate("MainWindow", "Click this to select one of the already available index or for a custom index"))
        self.BWAIndexpushButton.setIcon(QtGui.QIcon("./icons/browse.png"))
        self.BWAIndexpushButton.setIconSize(QtCore.QSize(22, 22))
        self.BWAIndexpushButton.setToolTip("Browse Index File")
        self.OrLabel_dna.setText(_translate("MainWindow", "Or"))

        self.RunIndexdnapushButton.setText(_translate("MainWindow", "Generate Index"))
        self.RunIndexdnapushButton.setIcon(QtGui.QIcon("./icons/run1.svg"))
        self.RunIndexdnapushButton.setStyleSheet("background-color: #704214")
        self.RunIndexdnapushButton.setIconSize(QtCore.QSize (22, 22))
        
   

        
         ## Add run DNA##
        self.DNAtabWidget.setTabText(self.DNAtabWidget.indexOf(self.run_dna), _translate("MainWindow", " Run "))
        self.DNAtabWidget.setTabIcon(self.DNAtabWidget.indexOf(self.run_dna), QtGui.QIcon('./icons/run1.svg'))

        self.DNAtabWidget.setIconSize(QtCore.QSize(22, 22))
        self.nextbuttonrunDNA.setIcon(QtGui.QIcon("./icons/arrow.svg"))
        self.nextbuttonrunDNA.setStyleSheet("background-color: #704214")
        self.nextbuttonrunDNA.setIconSize(QtCore.QSize(35, 35))
        self.previousbuttonrunDNA.setIcon(QtGui.QIcon("./icons/arrow1.svg"))
        self.previousbuttonrunDNA.setStyleSheet("background-color: #704214")
        self.previousbuttonrunDNA.setIconSize(QtCore.QSize(35, 35))
        ##End##
        ##Add Result DNA##
        self.DNAtabWidget.setTabText(self.DNAtabWidget.indexOf(self.result_dna), _translate("MainWindow", " Results "))
        self.DNAtabWidget.setTabIcon(self.DNAtabWidget.indexOf(self.result_dna), QtGui.QIcon('./icons/results.svg'))

        self.DNAtabWidget.setIconSize(QtCore.QSize(22, 22))
        ##End##
        
        ## Add run RNA##
        self.RNAtabWidget.setTabText(self.RNAtabWidget.indexOf(self.run_rna), _translate("MainWindow", " Run "))
        self.RNAtabWidget.setTabIcon(self.RNAtabWidget.indexOf(self.run_rna), QtGui.QIcon('./icons/run1.svg'))
        self.RNAtabWidget.setIconSize(QtCore.QSize(22, 22))
        self.nextbuttonrunRNA.setIcon(QtGui.QIcon("./icons/arrow.svg"))
        self.nextbuttonrunRNA.setStyleSheet("background-color: #704214")
        self.nextbuttonrunRNA.setIconSize(QtCore.QSize(35, 35))
        self.previousbuttonrunRNA.setIcon(QtGui.QIcon("./icons/arrow1.svg"))
        self.previousbuttonrunRNA.setStyleSheet("background-color: #704214")
        self.previousbuttonrunRNA.setIconSize(QtCore.QSize(35, 35))
        ##End##
        ##Add Result RNA##
        self.RNAtabWidget.setTabText(self.RNAtabWidget.indexOf(self.result_rna), _translate("MainWindow", " Results "))
        self.RNAtabWidget.setTabIcon(self.RNAtabWidget.indexOf(self.result_rna), QtGui.QIcon('./icons/results.svg'))
        self.RNAtabWidget.setIconSize(QtCore.QSize(22, 22))
        ##End##        
        
        self.RunButton.setIcon(QtGui.QIcon("./icons/run1.svg"))
        self.RunButton.setIconSize(QtCore.QSize(50, 50))
        self.RunButton.setStyleSheet("background-color:#704214")
        
        self.RunButton_dna.setIcon(QtGui.QIcon("./icons/run1.svg"))
        self.RunButton_dna.setIconSize(QtCore.QSize(50, 50))
        self.RunButton_dna.setStyleSheet("background-color:#704214")        
        

        self.RunLabel.setText(_translate("MainWindow", "Run"))
        font_label = QtGui.QFont()
        font_label.setPointSize(15)
        font_label.setBold(True)
        self.RunLabel.setFont(font_label)
        
       
        self.RunLabel_dna.setFont(font_label)
        self.RunLabel_dna.setText(_translate("MainWindow", "Run"))
        


        self.PipelinetabWidget.setTabText(self.PipelinetabWidget.indexOf(self.DNAseq), _translate("MainWindow", "DNA-Seq Pipeline"))
        self.PipelinetabWidget.setTabIcon(self.PipelinetabWidget.indexOf(self.DNAseq), QtGui.QIcon('./icons/dna.svg'))
        self.PipelinetabWidget.setIconSize(QtCore.QSize(22, 22))

        self.PipelinetabWidget.setTabToolTip(self.PipelinetabWidget.indexOf(self.DNAseq), _translate("MainWindow", "Select this pipeline to generate Annotated VCFs"))

        ## Make Input as first tab ##
        self.SampleOrlabel_rna.setText(_translate("MainWindow", "Or"))
        self.SamplesYesradioButton_rna.setText(_translate("MainWindow", "Upload from Folder"))
        self.SamplesNoradioButton_rna.setText(_translate("MainWindow", "Upload from Table"))

        self.SampleFolderlabel.setText(_translate("MainWindow", "Samples Folder"))
        self.SampleFolderBrowseButton.setIcon(QtGui.QIcon("./icons/browse.png"))
        self.SampleFolderBrowseButton.setIconSize(QtCore.QSize(22, 22))
        self.SampleFolderBrowseButton.setToolTip("Browse Samples Folder")
        self.Sampletablelabel.setText(_translate("MainWindow", "Samples Table"))
        
        self.FastaFilelabel.setText(_translate("MainWindow", "Fasta File"))
        self.AnnotatedFilelabelRNA.setText(_translate("MainWindow", "Annotated File"))
        
        self.SampletableBrowseButton.setIcon(QtGui.QIcon("./icons/browse.png"))
        self.SampletableBrowseButton.setIconSize(QtCore.QSize(22, 22))
        self.SampletableBrowseButton.setToolTip("Browse Samples Table")
        
        self.FastaBrowseButton.setIcon(QtGui.QIcon("./icons/browse.png"))
        self.FastaBrowseButton.setIconSize(QtCore.QSize(22, 22))
        self.FastaBrowseButton.setToolTip("Browse Fasta File")
        self.AnnotatedBrowserButtonRNA.setIcon(QtGui.QIcon("./icons/browse.png"))
        self.AnnotatedBrowserButtonRNA.setIconSize(QtCore.QSize(22, 22))
        self.AnnotatedBrowserButtonRNA.setToolTip("Browse Annotated File")

        self.CorelabelRNA.setText(_translate("MainWindow", "Maximum threads"))
        self.CorelineEditRNA.setText(_translate("MainWindow", "10"))
       

        self.nextbuttoninputRNA.setIcon(QtGui.QIcon("./icons/arrow.svg"))
        self.nextbuttoninputRNA.setStyleSheet("background-color: #704214")
        self.nextbuttoninputRNA.setIconSize(QtCore.QSize(35, 35))
        self.RNAtabWidget.setTabText(self.RNAtabWidget.indexOf(self.input_rna), _translate("MainWindow", " Input Data "))
        self.RNAtabWidget.setTabIcon(self.RNAtabWidget.indexOf(self.input_rna), QtGui.QIcon('./icons/input.svg'))
        self.RNAtabWidget.setIconSize(QtCore.QSize(22, 22))
        
        ## End ##
        ## Add QC ##
        self.QClabel_rna.setToolTip(_translate("MainWindow", "This option performs all the Quality Control operations like fastQC, Cutadapt and MultiQC "))
        self.QClabel_rna.setText(_translate("MainWindow", "Trim the reads"))
        self.QCYesradioButton_rna.setToolTip(_translate("MainWindow", "Enables Quality Control Processing"))
        self.QCYesradioButton_rna.setText(_translate("MainWindow", "Yes"))
        self.QCNoradioButton_rna.setToolTip(_translate("MainWindow", "Disables Quality Control Processing"))
        self.QCNoradioButton_rna.setText(_translate("MainWindow", "No"))
        self.InputParamslabel_rna.setText(_translate("MainWindow", "Input Parameters:"))

        self.Cutadaptlabel_rna.setText(_translate("MainWindow", "Cutadapt"))
        self.CutadaptlineEdit_rna.setText(_translate("MainWindow", " --adapter AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC -A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT "))

        self.RunQCpushButton_rna.setText(_translate("MainWindow", "Trimming"))
        self.RunQCpushButton_rna.setIcon(QtGui.QIcon("./icons/run1.svg"))
        self.RunQCpushButton_rna.setIconSize(QtCore.QSize(22, 22))
        self.RunQCpushButton_rna.setStyleSheet("background-color: #704214")
        self.nextbuttonqcRNA.setIcon(QtGui.QIcon("./icons/arrow.svg"))
        self.nextbuttonqcRNA.setStyleSheet("background-color: #704214")
        self.nextbuttonqcRNA.setIconSize(QtCore.QSize(35, 35))
        self.previousbuttonqcRNA.setIcon(QtGui.QIcon("./icons/arrow1.svg"))
        self.previousbuttonqcRNA.setStyleSheet("background-color: #704214")
        self.previousbuttonqcRNA.setIconSize(QtCore.QSize(35, 35))
        self.RNAtabWidget.setTabText(self.RNAtabWidget.indexOf(self.QC_rna), _translate("MainWindow", " Quality Control "))
        self.RNAtabWidget.setTabIcon(self.RNAtabWidget.indexOf(self.QC_rna), QtGui.QIcon('./icons/qc.svg'))
        

        ## End ##

        self.AlignercomboBoxRNA.setItemText(0, _translate("MainWindow", "HISAT2"))
        self.AlignercomboBoxRNA.setItemText(1, _translate("MainWindow", "STAR"))

        self.EMcomboBoxRNA.setItemText(0, _translate("MainWindow", "StringTie"))
        self.EMcomboBoxRNA.setItemText(1, _translate("MainWindow", "HTSeq"))

        self.DEcomboBoxRNA.setItemText(0, _translate("MainWindow", "ballgown"))
        self.DEcomboBoxRNA.setItemText(1, _translate("MainWindow", "DESeq2"))
        self.nextbuttontoolRNA.setIcon(QtGui.QIcon("./icons/arrow.svg"))
        self.nextbuttontoolRNA.setStyleSheet("background-color: #704214")
        self.nextbuttontoolRNA.setIconSize(QtCore.QSize(35, 35))
        self.previousbuttontoolRNA.setIcon(QtGui.QIcon("./icons/arrow1.svg"))
        self.previousbuttontoolRNA.setStyleSheet("background-color: #704214")
        self.previousbuttontoolRNA.setIconSize(QtCore.QSize(35, 35))
        self.RNAtabWidget.setTabText(self.RNAtabWidget.indexOf(self.Tool_rna), _translate("MainWindow", " Tools Selection "))
        self.RNAtabWidget.setTabIcon(self.RNAtabWidget.indexOf(self.Tool_rna), QtGui.QIcon('./icons/tools.svg'))
        ## Add Index ##
        self.StarIndexlineEdit.setToolTip(_translate("MainWindow", "Input the path of the Index for" + self.AlignercomboBoxRNA.currentText()))
        self.StarIndexpushButton.setToolTip(_translate("MainWindow", "Click this to select one of the pre-installed index or for a custom index"))
        self.StarIndexpushButton.setIcon(QtGui.QIcon("./icons/browse.png"))
        self.StarIndexpushButton.setIconSize(QtCore.QSize(22, 22))
        self.StarIndexpushButton.setToolTip("Browse Index File")
        self.OrLabel_rna.setText(_translate("MainWindow", "Or"))

        self.RunIndexrnapushButton.setText(_translate("MainWindow", "Generate Index"))
        self.RunIndexrnapushButton.setIcon(QtGui.QIcon("./icons/run1.svg"))
        self.RunIndexrnapushButton.setStyleSheet("background-color: #704214")
        self.RunIndexrnapushButton.setIconSize(QtCore.QSize(22, 22))

        self.PipelinetabWidget.setTabText(self.PipelinetabWidget.indexOf(self.RNAseq), _translate("MainWindow", "RNA-Seq Pipeline"))
        self.PipelinetabWidget.setTabIcon(self.PipelinetabWidget.indexOf(self.RNAseq), QtGui.QIcon('./icons/rna.svg'))
        self.PipelinetabWidget.setTabToolTip(self.PipelinetabWidget.indexOf(self.RNAseq), _translate("MainWindow", "Select this pipeline to generate Differentially Expressed Genes"))
        self.ShellTab.setTabText(self.ShellTab.indexOf(self.SnakemakeOutputTab), _translate("MainWindow", "Logs"))
        self.ShellTab.setTabIcon(self.ShellTab.indexOf(self.SnakemakeOutputTab), QtGui.QIcon('./icons/log.svg'))
        self.ShellTab.setIconSize(QtCore.QSize(22, 22))
        
        
        self.PipelinetabWidget.setTabText(self.PipelinetabWidget.indexOf(self.CTAG), _translate("MainWindow", "cTaG"))
        
        font_label = QtGui.QFont()
        font_label.setPointSize(12)
        font_label.setBold(True)
        
        font_label2 = QtGui.QFont()
        font_label2.setPointSize(10)
        font_label2.setBold(False)        
        
        self.maflabel.setText(_translate("MainWindow", "Path to MAF file"))
        self.mafparamlabel.setText(_translate("MainWindow", "Parameters"))
        self.mafparamlabel1.setText(_translate("MainWindow", "- m"))
        self.mafparamlabel2.setText(_translate("MainWindow", "- p"))
        self.mafparamlineEdit.setText(_translate("MainWindow", "2000"))
        self.mafparamlineEdit1.setText(_translate("MainWindow", "5"))
        
        self.ctaglabel.setText(_translate("MainWindow", "cTaG  (classify TSG and OG)"))
        self.ctaglabel.setFont(font_label)
        self.ctaglabel2.setText(_translate("MainWindow", "cTaG is a tool used to identify tumour suppressor genes (TSGs)\n and oncogenes (OGs) using somatic mutation data.The cTaG model \n returns the list of all genes labelled as TSG or OG or unlabelled\n along with predictions made by each model and whether\n the gene is among the top predictions ")) 
        self.ctaglabel2.setFont(font_label2)
        urlLink1 = "<a href=\'https://github.com/RamanLab/cTaG'>cTaG</a>"
        self.ctaglabel3.setText(_translate("MainWindow", urlLink1 ))
        self.ctaggithubbutton.setIcon(QtGui.QIcon("./icons/github.png"))
        self.ctaggithubbutton.setIconSize(QtCore.QSize(22, 22))
        self.ctaggithubbutton.setToolTip("GitHub link")
        
        self.mafBrowseButton.setIcon(QtGui.QIcon("./icons/browse.png"))
        self.mafBrowseButton.setToolTip("Browse MAF File")
        self.mafBrowseButton.setIconSize(QtCore.QSize(22, 22))
        
        self.runctagpushButton.setText(_translate("MainWindow", "cTaG"))
        self.runctagpushButton.setIcon(QtGui.QIcon("./icons/run1.svg"))
        self.runctagpushButton.setText(_translate("MainWindow", "  Run cTaG"))
        self.runctagpushButton.setIconSize(QtCore.QSize (22, 22))        
        
        self.resultctagpushButton.setText(_translate("MainWindow", "cTAG"))
        self.resultctagpushButton.setIcon(QtGui.QIcon("./icons/document.svg"))
        self.resultctagpushButton.setText(_translate("MainWindow", " View Results"))
        self.resultctagpushButton.setIconSize(QtCore.QSize (22, 22))                
        
        self.PipelinetabWidget.setTabText(self.PipelinetabWidget.indexOf(self.NB), _translate("MainWindow", "NBDriver"))
        
        font_label = QtGui.QFont()
        font_label.setPointSize(12)
        font_label.setBold(True)
        
        font_label2 = QtGui.QFont()
        font_label2.setPointSize(10)
        font_label2.setBold(False)
        
  
        self.vcflabel.setText(_translate("MainWindow", "Path to VCF file"))
        self.nblabel.setText(_translate("MainWindow", "NBDriver (NEIGHBORHOOD Driver)"))
        self.nblabel.setFont(font_label)
        self.nblabel2.setText(_translate("MainWindow", "NBDriver is a tool used to differentiate between driver \n and passenger mutations using features derived from \n the neighborhood sequences of somatic mutations.NBDriver \n returns a list of all mutations labelled as Driver or Passenger")) 
        self.nblabel2.setFont(font_label2)
        
        urlLink = "<a href=\'https://github.com/RamanLab/NBDriver'>NBDriver</a>"
        self.nblabel3.setText(_translate("MainWindow", urlLink ))
        urlLink1 = "<a href=\'https://doi.org/10.3390/cancers13102366'>Banerjee et al.</a>"
        self.nblabel5.setText(_translate("MainWindow", urlLink1 ))
        self.nbgithubbutton.setIcon(QtGui.QIcon("./icons/github.png"))
        self.nbgithubbutton.setIconSize(QtCore.QSize(22, 22))
        self.nbgithubbutton.setToolTip("GitHub link")
        self.nbpaperbutton.setIcon(QtGui.QIcon("./icons/document.svg"))
        self.nbpaperbutton.setIconSize(QtCore.QSize(22, 22))
        self.nbpaperbutton.setToolTip("GitHub link")
        urlLink2 = "<a href=\'https://doi.org/10.5281/zenodo.5759698'>link</a>"
        self.nblabel4.setText(_translate("MainWindow", " NBDriver predictions has been derived using hg19 reference genome only. The user needs to download the \n reference file from this      and put it in the /NBDriver_iCOMIC/ directory and the input vcf file must be \n kept inside /NBDriver_ICOMIC/vcf directory and renamed as NBDriver_vcf.vcf" ))
        self.nblabel6.setText(_translate("MainWindow", urlLink2 ))
        
        self.vcfBrowseButton.setIcon(QtGui.QIcon("./icons/browse.png"))
        self.vcfBrowseButton.setToolTip("Browse VCF File")
        self.vcfBrowseButton.setIconSize(QtCore.QSize(22, 22))
        
        self.runnbpushButton.setText(_translate("MainWindow", "NBDriver"))
        self.runnbpushButton.setIcon(QtGui.QIcon("./icons/run1.svg"))
        self.runnbpushButton.setText(_translate("MainWindow", "  Run NBDriver"))
        self.runnbpushButton.setIconSize(QtCore.QSize (22, 22))        
        
        self.resultnbpushButton.setText(_translate("MainWindow", "NBDriver"))
        self.resultnbpushButton.setIcon(QtGui.QIcon("./icons/document.svg"))
        self.resultnbpushButton.setText(_translate("MainWindow", " View Results"))
        self.resultnbpushButton.setIconSize(QtCore.QSize (22, 22)) 
        
        

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOption.setTitle(_translate("MainWindow", "Option"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionQuick_Start.setText(_translate("MainWindow", "Quick Start"))
        self.actionAbout_2.setText(_translate("MainWindow", "About"))
        self.actionSnakemake_Options.setText(_translate("MainWindow", "Snakemake Options"))
        ##Changelabel on choosing tools##

        
        self.nextbuttoninputDNA.clicked.connect(self.on_clicked_nextbuttoninputDNA)
        self.nextbuttonqcDNA.clicked.connect(self.on_clicked_nextbuttonqcDNA)
        self.nextbuttontoolDNA.clicked.connect(self.on_clicked_nextbuttonparamsDNA)
        self.nextbuttontoolDNA.clicked.connect(self.on_clicked_nextbuttontoolDNA)
        self.previousbuttonqcDNA.clicked.connect(self.on_clicked_previousbuttonqcDNA)
        self.previousbuttontoolDNA.clicked.connect(self.on_clicked_previousbuttontoolDNA)
        self.previousbuttonrunRNA.clicked.connect(self.on_clicked_previousbuttonrunDNA)
        self.nextbuttoninputRNA.clicked.connect(self.on_clicked_nextbuttoninputRNA)
        self.nextbuttonqcRNA.clicked.connect(self.on_clicked_nextbuttonqcRNA)
        self.nextbuttontoolRNA.clicked.connect(self.on_clicked_nextbuttonparamsRNA)
        self.nextbuttontoolRNA.clicked.connect(self.on_clicked_nextbuttontoolRNA)
        self.previousbuttonqcRNA.clicked.connect(self.on_clicked_previousbuttonqcRNA)
        self.previousbuttontoolRNA.clicked.connect(self.on_clicked_previousbuttontoolRNA)
        
        self.SamplesNoradioButton.toggled.connect(self.on_check_SamplesNo_dna)
        self.SamplesNoradioButton_rna.toggled.connect(self.on_check_SamplesNo_rna)
        self.QCresults.clicked.connect(self.show_qc_textbox)
        self.QCresults.clicked.connect(self.show_qc_results)
        
        self.QCYesradioButton.toggled.connect(self.on_check_QC_dna)
        self.QCYesradioButton_rna.toggled.connect(self.on_check_QC_rna)
        self.QCresults_rna.clicked.connect(self.show_qc_textbox)
        self.QCresults_rna.clicked.connect(self.show_qc_results_rna)
        
        self.aligner_add_dna.clicked.connect(self.advanced_aligner)
        self.vc_add_dna.clicked.connect(self.advanced_vc)
        self.annotator_add_dna.clicked.connect(self.advanced_annotator)
        self.aligner_add_rna.clicked.connect(self.advanced_aligner_rna)
        self.em_add_rna.clicked.connect(self.advanced_em)
        self.de_add_rna.clicked.connect(self.advanced_de)
        self.AnnotatorcomboBoxDNA.currentIndexChanged.connect(self.not_snpeff)
        self.AlignercomboBoxDNA.currentIndexChanged.connect(self.param_display)
        self.VCcomboBoxDNA.currentIndexChanged.connect(self.param_display)
        self.AnnotatorcomboBoxDNA.currentIndexChanged.connect(self.param_display)
        self.AlignercomboBoxRNA.currentIndexChanged.connect(self.param_display_rna)
        self.EMcomboBoxRNA.currentIndexChanged.connect(self.param_display_rna)
        self.DEcomboBoxRNA.currentIndexChanged.connect(self.param_display_rna)
    
        self.pushbutton_result1_dna.clicked.connect(self.multiqc_result)
        self.pushbutton_result2_dna.clicked.connect(self.vcf_result)
        self.pushbutton_result3_dna.clicked.connect(self.annotated_result)
        self.pushbutton_result1_rna.clicked.connect(self.multiqc_result_rna)
        self.pushbutton_result2_rna.clicked.connect(self.de_result)
        self.pushbutton_result3_rna.clicked.connect(self.plot_view)
        
        self.RunButton_dna.clicked.connect(self.run_action_textbox)
        self.RunButton_dna.clicked.connect(self.run_action_dna)
        self.RunButton.clicked.connect(self.run_action_textbox)
        self.RunButton.clicked.connect(self.run_action_rna)
        
        self.pYesradioButton.toggled.connect(self.on_check_proceed)
        self.nextbuttonresult.clicked.connect(self.on_click_nextresults)



        ##data_browse##
        self.SamplesBrowseButtonDNA.clicked.connect(self.browse_data_samples)
        self.UnitsBrowseButtonDNA.clicked.connect(self.browse_data_units)
        self.RefGenomeBrowseButtonDNA.clicked.connect(self.browse_data_ref)
        self.RefVariantpushButton.clicked.connect(self.browse_data_kv)
        ##Enable browse button for index##
        self.BWAIndexpushButton.clicked.connect(self.browse_bwaindex_dna)

        self.StarIndexpushButton.clicked.connect(self.browse_star_rna)

        self.SampletableBrowseButton.clicked.connect(self.browse_data_sampletable)
        self.FastaBrowseButton.clicked.connect(self.browse_data_fasta)
        self.AnnotatedBrowserButtonRNA.clicked.connect(self.browse_data_annotated)
        self.SampleFolderBrowseButton.clicked.connect(self.browse_samples_folder)
        ##Run_QC##

        self.RunQCpushButton.clicked.connect(self.run_qc_textbox)
        self.RunQCpushButton.clicked.connect(self.run_qc_dna)

        self.RunQCpushButton_rna.clicked.connect(self.run_qc_rna_textbox)
        self.RunQCpushButton_rna.clicked.connect(self.run_qc_rna)
        
        ##Add additional parameters##
        ##Run_indexing##

        self.RunIndexdnapushButton.clicked.connect(self.run_index_text)
        self.RunIndexdnapushButton.clicked.connect(self.run_index_dna)
        self.RunIndexrnapushButton.clicked.connect(self.run_index_text)
        self.RunIndexrnapushButton.clicked.connect(self.run_index_rna)
        ##Run_main##
        ##run cTAG##
        
        self.mafBrowseButton.clicked.connect(self.browse_data_maf)
        self.runctagpushButton.clicked.connect(self.on_click_run_ctag)
        self.resultctagpushButton.clicked.connect(self.on_click_result_ctag)
                                        
        
        self.vcfBrowseButton.clicked.connect(self.browse_data_vcf)
        self.runnbpushButton.clicked.connect(self.on_click_run_nbdriver)
        self.resultnbpushButton.clicked.connect(self.on_click_result_nbdriver)
        
        
        ##show dag##
        ##menu_popups##
        self.actionAbout_2.triggered.connect(self.about)
        self.actionQuick_Start.triggered.connect(self.quick_start)

# =============================================================================
    def on_click_nextresults(self):
        if self.ctagradioButton.isChecked() == True:
            self.PipelinetabWidget.setCurrentIndex(2)
            subprocess.run(["snakemake", "--use-conda", "-j", self.CorelineEditDNA.text(), "-s", "Snakefile_maf"])    
        elif self.nbradioButton.isChecked() == True:
            self.PipelinetabWidget.setCurrentIndex(3)
        else:
            pass
    def on_click_run_ctag(self):
        subprocess.run(["python","cTaG/code/cTaG.py","-i", self.maflineEdit.text(), "-o", (os.getcwd()+"/cTaG/results"), "-c","/cTaG", "-m", self.mafparamlineEdit.text(), "-p", self.mafparamlineEdit1.text()])
    
    def on_click_result_ctag(self):
        path='cTaG/results/CVpredictions.txt'
        self.result_dialog= ResultsDialog(path)
        self.result_dialog.show()
        
    def on_click_run_nbdriver(self):
        subprocess.run([(os.getcwd()+"/NBDriver_ICOMIC/run.sh")])
        
    def on_click_result_nbdriver(self):
        path='NBDriver_Predictions.csv'
        self.result_dialog= ResultsDialog(path)
        self.result_dialog.show()
        
    def run_results_textbox(self):
        subprocess.run(["snakemake", "--unlock", "-j", "1"])
        self.textBrowser.setTextColor(self._colors['blue'])
        self.textBrowser.append("Please be patient, while we generate MAF files \n\n")


    def multiqc_result(self):
        if os.path.exists("results_dna/multiqc/multiqc.html"):
            self.textBrowser.setTextColor(self._colors['blue'])
            filename = "results_dna/multiqc/multiqc.html"
            webbrowser.get('google-chrome').open(filename, new=0, autoraise=True)
        else:
            pass
        
    def vcf_result(self):
        path='results_dna/filtered/all.vcf.gz'
        self.result_dialog= ResultsDialog(path)

        
        self.result_dialog.show()
        
    def annotated_result(self):
        if self.AnnotatorcomboBoxDNA.currentText()=="SnpEff":
            path = "results_dna/annotated/all.vcf"
        elif self.AnnotatorcomboBoxDNA.currentText()=="Annovar":
            path = "results_dna/annotated/all.hg19_multianno.vcf"
#            path = "results_dna/annotated/all.multianno.vcf"
            self.result_dialog= ResultsDialog(path)
            self.result_dialog.show()
        else:
            pass
        self.result_dialog= ResultsDialog(path)
        self.result_dialog.show()
        
    def de_result(self):
        if self.DEcomboBoxRNA.currentText() == 'ballgown':
            path='results/de_results/SigDE.txt'
        elif self.DEcomboBoxRNA.currentText() == 'DESeq2':
            path = 'results/de_results/DESeq2_normalized_counts.txt'
            self.result_dialog= ResultsDialog(path)
            self.result_dialog.show()
        else:
            pass
            self.result_dialog= ResultsDialog(path)
            self.result_dialog.show()
        
    def plot_view(self):
        if os.path.exists("results/de_results/plot_output.pdf"):
            filename = "results/de_results/plot_output.pdf"
            webbrowser.get('google-chrome').open(filename, new=0, autoraise=True)
        elif os.path.exists("results/de_results/Rplots.pdf"):
            filename = "results/de_results/Rplots.pdf   "
            webbrowser.get('google-chrome').open(filename, new=0, autoraise=True)
        else:
            pass

        
    def multiqc_result_rna(self):
        if os.path.exists("results/multiqc/multiqc.html"):
            self.textBrowser.setTextColor(self._colors['blue'])
            filename = "results/multiqc/multiqc.html"
            webbrowser.get('google-chrome').open(filename, new=0, autoraise=True)
        else:
            pass
        
    def create_aligner_groupbox(self):
        font_label = QtGui.QFont()
        font_label.setPointSize(8.5)
        color  = QtGui.QColor(233, 10, 150)
        self.aligner_groupbox = QGroupBox("Aligner")
        self.vlayout= QtWidgets.QVBoxLayout()
        self.hlayout0_aligner = QtWidgets.QHBoxLayout()
        font_info = QtGui.QFont()
        font_info.setPointSize(8.5)
        self.Alignerninfoicon_dna = QtWidgets.QPushButton(self.aligner_groupbox)
        self.Alignerninfoicon_dna.setFlat(True)
        self.Alignerninfoicon_dna.setGeometry(QtCore.QRect(48, 0, 20, 20))
        self.Alignerninfoicon_dna.setToolTip("Software for arranging sequences to identify regions of similarity")
        self.Alignerninfoicon_dna.setFont(font_info)
        self.Alignerninfoicon_dna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.Alignerninfoicon_dna.setIconSize(QtCore.QSize(13, 13)) 
        
        self.AlignercomboBoxDNA = QtWidgets.QComboBox()
        self.AlignercomboBoxDNA.move(20, 10)
        self.AlignercomboBoxDNA.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.AlignercomboBoxDNA.setObjectName("AlignercomboBoxDNA")
        self.AlignercomboBoxDNA.addItem("")
        self.AlignercomboBoxDNA.addItem("")
        self.AlignercomboBoxDNA.addItem("")
        self.hlayout0_aligner.addWidget(self.AlignercomboBoxDNA)
        self.hlayout0_aligner.addStretch(0)
        self.vlayout.addItem(self.hlayout0_aligner)
        self.hlayout1_aligner = QtWidgets.QHBoxLayout()
        self.hlayout1_aligner.setSpacing(10)
        self.BWAIndexlabel = QtWidgets.QLabel()
        self.BWAIndexlabel.setObjectName("BWAIndexlabel")
        self.BWAIndexlineEdit = QtWidgets.QLineEdit()
        self.BWAIndexlineEdit.setObjectName("BWAIndexlineEdit")
        self.BWAIndexpushButton = QtWidgets.QPushButton()
        self.BWAIndexpushButton.setObjectName("BWAIndexpushButton")
        
        self.hlayout1_aligner.addWidget(self.BWAIndexlabel)
        self.hlayout1_aligner.addWidget(self.BWAIndexlineEdit)
        self.hlayout1_aligner.addWidget(self.BWAIndexpushButton)
        self.vlayout.addItem(self.hlayout1_aligner)
        
        self.hlayout1_error_aligner = QtWidgets.QHBoxLayout()
        self.BWAIndexErrortext = QtWidgets.QLabel()
        self.BWAIndexErrortext.setGeometry(QtCore.QRect(170, 113, 331, 22))
        self.BWAIndexErrortext.setObjectName("BWAIndexErrortext")
        self.BWAIndexErrortext.setStyleSheet("color: red")
        self.BWAIndexErrortext.setFont(font_label)
        self.BWAIndexErrortext.hide()
        self.hlayout1_error_aligner.addWidget(self.BWAIndexErrortext, 0, alignment=QtCore.Qt.AlignCenter)
        self.vlayout.addItem(self.hlayout1_error_aligner)
        
        self.hlayout0_or = QtWidgets.QHBoxLayout()
        self.OrLabel_dna = QtWidgets.QLabel()
        self.OrLabel_dna.setGeometry(QtCore.QRect(340, 130, 270, 23))
        self.OrLabel_dna.setObjectName("OrLabel_dna")
        self.hlayout0_or.addWidget(self.OrLabel_dna, 0, alignment=QtCore.Qt.AlignCenter)
        self.vlayout.addItem(self.hlayout0_or)
        
        self.hlayout0_runindex = QtWidgets.QHBoxLayout()
        self.RunIndexdnapushButton = QtWidgets.QPushButton()
        self.RunIndexdnapushButton.setObjectName("RunIndexdnapushButton")
        self.hlayout0_runindex.addWidget(self.RunIndexdnapushButton, 0, alignment=QtCore.Qt.AlignCenter)
        self.RunIndexdnaButtonErroricon = QtWidgets.QPushButton()
        self.RunIndexdnaButtonErroricon.setGeometry(QtCore.QRect(480, 175, 20, 20))
        self.RunIndexdnaButtonErroricon.setToolTip("Check and Run Index Again!")
        self.RunIndexdnaButtonErroricon.setFont(font_label)
        self.RunIndexdnaButtonErroricon.setIcon(QtGui.QIcon("./icons/warning.svg"))
        self.hlayout0_runindex.addWidget(self.RunIndexdnaButtonErroricon, 0, alignment=QtCore.Qt.AlignCenter)
        self.RunIndexdnaButtonErroricon.hide()
        self.vlayout.addItem(self.hlayout0_runindex)
        
        self.hlayout0_pb = QtWidgets.QHBoxLayout()
        self.hlayout0_pb.setGeometry(QtCore.QRect(10, 230, 665, 17))
        self.progressBar_sub2_dna = QtWidgets.QProgressBar()
        self.progressBar_sub2_dna.setProperty("value", 0)
        self.progressBar_sub2_dna.setObjectName("progressBar_sub2_dna")
        self.hlayout0_pb.addWidget(self.progressBar_sub2_dna)
        self.vlayout.addItem(self.hlayout0_pb)

        
        
        self.param1_label_dna_1 = QtWidgets.QLabel()
        self.param1_label_dna_1.setGeometry(QtCore.QRect(20, 40, 91, 18))
        self.param1_lineEdit_dna_1 = QtWidgets.QLineEdit()
        self.param1_lineEdit_dna_1.setGeometry(QtCore.QRect(120, 40, 70, 18))
        self.param1_label_dna_3 = QtWidgets.QLabel()
        self.param1_label_dna_3.setGeometry(QtCore.QRect(200, 40, 91, 18))
        self.param1_lineEdit_dna_3 = QtWidgets.QLineEdit()
        self.param1_lineEdit_dna_3.setGeometry(QtCore.QRect(280, 40, 70, 18))
        self.param1_label_dna_5 = QtWidgets.QLabel()
        self.param1_label_dna_5.setGeometry(QtCore.QRect(360, 40, 91, 18))
        self.param1_lineEdit_dna_5 = QtWidgets.QLineEdit()
        self.param1_lineEdit_dna_5.setGeometry(QtCore.QRect(440, 40, 70, 18))

        
        self.param1_label_dna_2 = QtWidgets.QLabel()
        self.param1_label_dna_2.setGeometry(QtCore.QRect(20, 65, 91, 18))
        self.param1_lineEdit_dna_2 = QtWidgets.QLineEdit()
        self.param1_lineEdit_dna_2.setGeometry(QtCore.QRect(120, 65, 70, 18))
        self.param1_label_dna_4 = QtWidgets.QLabel()
        self.param1_label_dna_4.setGeometry(QtCore.QRect(200, 65, 91, 18))
        self.param1_lineEdit_dna_4 = QtWidgets.QLineEdit()
        self.param1_lineEdit_dna_4.setGeometry(QtCore.QRect(280, 65, 70, 18))
        self.param1_label_dna_6 = QtWidgets.QLabel()
        self.param1_label_dna_6.setGeometry(QtCore.QRect(360, 65, 91, 18))
        self.param1_lineEdit_dna_6 = QtWidgets.QLineEdit()
        self.param1_lineEdit_dna_6.setGeometry(QtCore.QRect(440, 65, 70, 18))
        
        self.grid_aligner = QtWidgets.QGridLayout()
        self.grid_aligner.setSpacing(10)
        self.grid_aligner.addWidget(self.param1_label_dna_1, 0, 0)
        self.grid_aligner.addWidget(self.param1_lineEdit_dna_1, 0, 1)
        self.grid_aligner.addWidget(self.param1_label_dna_3, 0, 2)
        self.grid_aligner.addWidget(self.param1_lineEdit_dna_3, 0, 3)
        self.grid_aligner.addWidget(self.param1_label_dna_5, 0, 4)
        self.grid_aligner.addWidget(self.param1_lineEdit_dna_5, 0, 5)
        self.grid_aligner.addWidget(self.param1_label_dna_2, 1,0)
        self.grid_aligner.addWidget(self.param1_lineEdit_dna_2, 1,1)
        self.grid_aligner.addWidget(self.param1_label_dna_4, 1,2)
        self.grid_aligner.addWidget(self.param1_lineEdit_dna_4, 1, 3)
        self.grid_aligner.addWidget(self.param1_label_dna_6, 1,4)
        self.grid_aligner.addWidget(self.param1_lineEdit_dna_6, 1,5)
        
        self.vlayout.addItem(self.grid_aligner)
        
        
        self.hlayout4_aligner = QtWidgets.QHBoxLayout()
        self.hlayout4_aligner.addStretch(1)
        self.aligner_add_dna = QtWidgets.QPushButton()
        self.aligner_add_dna.setGeometry(QtCore.QRect(530, 45, 70, 30))
        self.aligner_add_dna.setText("Advanced")
        self.aligner_add_dna.setStyleSheet("background-color: #704214")
        self.hlayout4_aligner.addWidget(self.aligner_add_dna)
        self.vlayout.addItem(self.hlayout4_aligner)
        
        self.aligner_groupbox.setLayout(self.vlayout)
        
        font_param = QtGui.QFont()
        font_param.setBold(True)

        
        ##set of lbels and lineedits for params##
        
        self.param1_label_dna_1.hide()
        self.param1_label_dna_2.hide()
        self.param1_label_dna_3.hide()
        self.param1_label_dna_4.hide()
        self.param1_label_dna_5.hide()
        self.param1_label_dna_6.hide()
        self.param1_lineEdit_dna_1.hide()
        self.param1_lineEdit_dna_2.hide()
        self.param1_lineEdit_dna_3.hide()
        self.param1_lineEdit_dna_4.hide()
        self.param1_lineEdit_dna_5.hide()
        self.param1_lineEdit_dna_6.hide()
        
        
        
       
    def create_vc_groupbox(self):
        self.vc_groupbox = QGroupBox("Variant caller")
        self.vlayout_vc= QtWidgets.QVBoxLayout()
        self.hlayout0_vc = QtWidgets.QHBoxLayout()
        
        font_info = QtGui.QFont()
        font_info.setPointSize(8.5)
        self.VariantCallerninfoicon_dna = QtWidgets.QPushButton(self.vc_groupbox)
        self.VariantCallerninfoicon_dna.setFlat(True)
        self.VariantCallerninfoicon_dna.setGeometry(QtCore.QRect(84, 0, 20, 20))
        self.VariantCallerninfoicon_dna.setToolTip("Variant calling is the process by which variants are identified from \n the sample sequence data in comparison to the reference sequence.")
        self.VariantCallerninfoicon_dna.setFont(font_info)
        self.VariantCallerninfoicon_dna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.VariantCallerninfoicon_dna.setIconSize(QtCore.QSize(13, 13))         
        
        self.VCcomboBoxDNA = QtWidgets.QComboBox()
        self.VCcomboBoxDNA.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.VCcomboBoxDNA.setObjectName("VCcomboBoxDNA")
        self.VCcomboBoxDNA.addItem("")
        self.hlayout0_vc.addWidget(self.VCcomboBoxDNA)
        self.hlayout0_vc.addStretch(0)
        self.vlayout_vc.addItem(self.hlayout0_vc)
        
        
        self.param2_label_dna_1 = QtWidgets.QLabel()
        self.param2_label_dna_1.setGeometry(QtCore.QRect(20, 40, 91, 18))
        self.param2_lineEdit_dna_1 = QtWidgets.QLineEdit()
        self.param2_lineEdit_dna_1.setGeometry(QtCore.QRect(120, 40, 70, 18))
        self.param2_label_dna_3 = QtWidgets.QLabel()
        self.param2_label_dna_3.setGeometry(QtCore.QRect(200, 40, 91, 18))
        self.param2_lineEdit_dna_3 = QtWidgets.QLineEdit()
        self.param2_lineEdit_dna_3.setGeometry(QtCore.QRect(280, 40, 70, 18))
        self.param2_label_dna_5 = QtWidgets.QLabel()
        self.param2_label_dna_5.setGeometry(QtCore.QRect(360, 40, 91, 18))
        self.param2_lineEdit_dna_5 = QtWidgets.QLineEdit()
        self.param2_lineEdit_dna_5.setGeometry(QtCore.QRect(440, 40, 70, 18))
        
        self.param2_label_dna_2 = QtWidgets.QLabel()
        self.param2_label_dna_2.setGeometry(QtCore.QRect(20, 65, 91, 18))
        self.param2_lineEdit_dna_2 = QtWidgets.QLineEdit()
        self.param2_lineEdit_dna_2.setGeometry(QtCore.QRect(120, 65, 70, 18))
        self.param2_label_dna_4 = QtWidgets.QLabel()
        self.param2_label_dna_4.setGeometry(QtCore.QRect(200, 65, 91, 18))
        self.param2_lineEdit_dna_4 = QtWidgets.QLineEdit()
        self.param2_lineEdit_dna_4.setGeometry(QtCore.QRect(280, 65, 70, 18))
        self.param2_label_dna_6 = QtWidgets.QLabel()
        self.param2_label_dna_6.setGeometry(QtCore.QRect(360, 65, 91, 18))
        self.param2_lineEdit_dna_6 = QtWidgets.QLineEdit()
        self.param2_lineEdit_dna_6.setGeometry(QtCore.QRect(440, 65, 70, 18))
        
        self.grid_vc = QtWidgets.QGridLayout()
        self.grid_vc.setSpacing(10)
        self.grid_vc.addWidget(self.param2_label_dna_1, 0, 0)
        self.grid_vc.addWidget(self.param2_lineEdit_dna_1, 0, 1)
        self.grid_vc.addWidget(self.param2_label_dna_3, 0, 2)
        self.grid_vc.addWidget(self.param2_lineEdit_dna_3, 0, 3)
        self.grid_vc.addWidget(self.param2_label_dna_5, 0, 4)
        self.grid_vc.addWidget(self.param2_lineEdit_dna_5, 0, 5)
        self.grid_vc.addWidget(self.param2_label_dna_2, 1,0)
        self.grid_vc.addWidget(self.param2_lineEdit_dna_2, 1,1)
        self.grid_vc.addWidget(self.param2_label_dna_4, 1,2)
        self.grid_vc.addWidget(self.param2_lineEdit_dna_4, 1, 3)
        self.grid_vc.addWidget(self.param2_label_dna_6, 1,4)
        self.grid_vc.addWidget(self.param2_lineEdit_dna_6, 1,5)
        
        self.vlayout_vc.addItem(self.grid_vc)
        self.param2_label_dna_1.hide()
        self.param2_label_dna_2.hide()
        self.param2_label_dna_3.hide()
        self.param2_label_dna_4.hide()
        self.param2_label_dna_5.hide()
        self.param2_label_dna_6.hide()
        self.param2_lineEdit_dna_1.hide()
        self.param2_lineEdit_dna_2.hide()
        self.param2_lineEdit_dna_3.hide()
        self.param2_lineEdit_dna_4.hide()
        self.param2_lineEdit_dna_5.hide()
        self.param2_lineEdit_dna_6.hide()
        
        self.hlayout4_vc = QtWidgets.QHBoxLayout()
        self.hlayout4_vc.addStretch(1)
        self.vc_add_dna = QtWidgets.QPushButton()
        self.vc_add_dna.setGeometry(QtCore.QRect(530, 45, 70, 30))
        self.vc_add_dna.setText("Advanced")
        self.vc_add_dna.setStyleSheet("background-color: #704214")
        self.hlayout4_vc.addWidget(self.vc_add_dna)
        self.vlayout_vc.addItem(self.hlayout4_vc)
        
        self.vc_groupbox.setLayout(self.vlayout_vc)
        
    def create_annotator_groupbox(self):
        self.annotator_groupbox = QGroupBox("Annotator")
        self.vlayout_annotator= QtWidgets.QVBoxLayout()
        self.vlayout.setSpacing(20)
        self.hlayout0_annotator = QtWidgets.QHBoxLayout()
        
        self.hlayout1_warning_annotator = QtWidgets.QHBoxLayout()
        self.AnnotatorWarningtext = QtWidgets.QLabel()
        self.AnnotatorWarningtext.setGeometry(QtCore.QRect(90, 0, 331, 22))
        self.AnnotatorWarningtext.setObjectName("AnnotatorWarningtext")
        self.AnnotatorWarningtext.setStyleSheet("color: orange")
        self.AnnotatorWarningtext.setText("Choose Annovar if proceeding for cTaG or NBDriver")
        self.hlayout1_warning_annotator.addWidget(self.AnnotatorWarningtext, 0, alignment=QtCore.Qt.AlignCenter)
        self.vlayout_annotator.addItem(self.hlayout1_warning_annotator)
        
        font_info = QtGui.QFont()
        font_info.setPointSize(8.5)
        self.Annotatorninfoicon_dna = QtWidgets.QPushButton(self.annotator_groupbox)
        self.Annotatorninfoicon_dna.setFlat(True)
        self.Annotatorninfoicon_dna.setGeometry(QtCore.QRect(64, 0, 20, 20))
        self.Annotatorninfoicon_dna.setToolTip("Software for functionally annotating the identified variants")
        self.Annotatorninfoicon_dna.setFont(font_info)
        self.Annotatorninfoicon_dna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.Annotatorninfoicon_dna.setIconSize(QtCore.QSize(13, 13))         
        
        self.AnnotatorcomboBoxDNA = QtWidgets.QComboBox()
        self.AnnotatorcomboBoxDNA.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.AnnotatorcomboBoxDNA.setObjectName("AnnotatorcomboBoxDNA")
        self.AnnotatorcomboBoxDNA.addItem("")
        self.AnnotatorcomboBoxDNA.addItem("")
        self.hlayout0_annotator.addWidget(self.AnnotatorcomboBoxDNA)
        self.hlayout0_annotator.addStretch(0)
        self.vlayout_annotator.addItem(self.hlayout0_annotator)
        
        self.hlayout1_annotator = QtWidgets.QHBoxLayout()
        self.RefNamelabelDNA = QtWidgets.QLabel()
        self.RefNamelabelDNA.setObjectName("RefNamelabelDNA")
        self.RefNamecomboBoxDNA = QtWidgets.QComboBox()
        self.RefNamecomboBoxDNA.setObjectName("RefNamecomboBoxDNA")
        self.RefNamecomboBoxDNA.addItem("hg38")
        self.RefNamecomboBoxDNA.addItem("GRCh38.86")
        self.RefNamecomboBoxDNA.addItem("hg19")
        self.RefNamecomboBoxDNA.addItem("GRCh37.75")
        self.hlayout1_annotator.addWidget(self.RefNamelabelDNA)
        self.hlayout1_annotator.addWidget(self.RefNamecomboBoxDNA)
        self.vlayout_annotator.addItem(self.hlayout1_annotator)
        
        
        self.param3_label_dna_1 = QtWidgets.QLabel()
        self.param3_label_dna_1.setGeometry(QtCore.QRect(20, 40, 91, 18))
        self.param3_lineEdit_dna_1 = QtWidgets.QLineEdit()
        self.param3_lineEdit_dna_1.setGeometry(QtCore.QRect(120, 40, 70, 18))
        self.param3_label_dna_3 = QtWidgets.QLabel()
        self.param3_label_dna_3.setGeometry(QtCore.QRect(200, 40, 91, 18))
        self.param3_lineEdit_dna_3 = QtWidgets.QLineEdit()
        self.param3_lineEdit_dna_3.setGeometry(QtCore.QRect(280, 40, 70, 18))
        self.param3_label_dna_5 = QtWidgets.QLabel()
        self.param3_label_dna_5.setGeometry(QtCore.QRect(360, 40, 91, 18))
        self.param3_lineEdit_dna_5 = QtWidgets.QLineEdit()
        self.param3_lineEdit_dna_5.setGeometry(QtCore.QRect(440, 40, 70, 18))
        
        self.param3_label_dna_2 = QtWidgets.QLabel()
        self.param3_label_dna_2.setGeometry(QtCore.QRect(20, 65, 91, 18))
        self.param3_lineEdit_dna_2 = QtWidgets.QLineEdit()
        self.param3_lineEdit_dna_2.setGeometry(QtCore.QRect(120, 65, 70, 18))
        self.param3_label_dna_4 = QtWidgets.QLabel()
        self.param3_label_dna_4.setGeometry(QtCore.QRect(200, 65, 91, 18))
        self.param3_lineEdit_dna_4 = QtWidgets.QLineEdit()
        self.param3_lineEdit_dna_4.setGeometry(QtCore.QRect(280, 65, 70, 18))
        self.param3_label_dna_6 = QtWidgets.QLabel()
        self.param3_label_dna_6.setGeometry(QtCore.QRect(360, 65, 91, 18))
        self.param3_lineEdit_dna_6 = QtWidgets.QLineEdit()
        self.param3_lineEdit_dna_6.setGeometry(QtCore.QRect(440, 65, 70, 18))
        
        self.grid_annotator = QtWidgets.QGridLayout()
        self.grid_annotator.setSpacing(10)
        self.grid_annotator.addWidget(self.param3_label_dna_1, 0, 0)
        self.grid_annotator.addWidget(self.param3_lineEdit_dna_1, 0, 1)
        self.grid_annotator.addWidget(self.param3_label_dna_3, 0, 2)
        self.grid_annotator.addWidget(self.param3_lineEdit_dna_3, 0, 3)
        self.grid_annotator.addWidget(self.param3_label_dna_5, 0, 4)
        self.grid_annotator.addWidget(self.param3_lineEdit_dna_5, 0, 5)
        self.grid_annotator.addWidget(self.param3_label_dna_2, 1,0)
        self.grid_annotator.addWidget(self.param3_lineEdit_dna_2, 1,1)
        self.grid_annotator.addWidget(self.param3_label_dna_4, 1,2)
        self.grid_annotator.addWidget(self.param3_lineEdit_dna_4, 1, 3)
        self.grid_annotator.addWidget(self.param3_label_dna_6, 1,4)
        self.grid_annotator.addWidget(self.param3_lineEdit_dna_6, 1,5)
        
        self.param3_label_dna_1.hide()
        self.param3_label_dna_2.hide()
        self.param3_label_dna_3.hide()
        self.param3_label_dna_4.hide()
        self.param3_label_dna_5.hide()
        self.param3_label_dna_6.hide()
        self.param3_lineEdit_dna_1.hide()
        self.param3_lineEdit_dna_2.hide()
        self.param3_lineEdit_dna_3.hide()
        self.param3_lineEdit_dna_4.hide()
        self.param3_lineEdit_dna_5.hide()
        self.param3_lineEdit_dna_6.hide()
        
        self.vlayout_annotator.addItem(self.grid_annotator)
        
        self.hlayout4_annotator = QtWidgets.QHBoxLayout()
        self.hlayout4_annotator.addStretch(1)
        self.annotator_add_dna = QtWidgets.QPushButton()
        self.annotator_add_dna.setGeometry(QtCore.QRect(530, 45, 70, 30))
        self.annotator_add_dna.setText("Advanced")
        self.annotator_add_dna.setStyleSheet("background-color: #704214")
        self.hlayout4_annotator.addWidget(self.annotator_add_dna)
        self.vlayout_annotator.addItem(self.hlayout4_annotator)
        self.annotator_groupbox.setLayout(self.vlayout_annotator)
        
    def create_group_next(self):
        self.next_groupbox = QGroupBox()
        self.vlayout_next= QtWidgets.QVBoxLayout()
        self.nextbuttontoolDNA = QtWidgets.QPushButton()
        self.nextbuttontoolDNA.setGeometry(QtCore.QRect(635, 400, 45, 45))
        self.nextbuttontoolDNA.setObjectName("nextbuttontoolDNA")
        ###
        self.previousbuttontoolDNA = QtWidgets.QPushButton()
        self.previousbuttontoolDNA.setGeometry(QtCore.QRect(10, 400, 45, 45))
        self.previousbuttontoolDNA.setObjectName("previousbuttontoolDNA")
        
        self.hbox_next = QtWidgets.QHBoxLayout()
        self.hbox_next.addWidget(self.previousbuttontoolDNA, 0, alignment=QtCore.Qt.AlignLeft)
        self.hbox_next.addWidget(self.nextbuttontoolDNA, 0, alignment=QtCore.Qt.AlignRight)
        
        self.vlayout_next.addItem(self.hbox_next)
        self.next_groupbox.setLayout(self.vlayout_next)
        
    def create_aligner_groupbox_rna(self):
        font_label = QtGui.QFont()
        font_label.setPointSize(8.5)
        color  = QtGui.QColor(233, 10, 150)
        self.aligner_groupbox_rna = QGroupBox("Aligner")
        self.vlayout_rna= QtWidgets.QVBoxLayout()
        self.hlayout0_aligner_rna = QtWidgets.QHBoxLayout()
        
        font_info = QtGui.QFont()
        font_info.setPointSize(8.5)
        self.Alignerninfoicon_rna = QtWidgets.QPushButton(self.aligner_groupbox_rna)
        self.Alignerninfoicon_rna.setFlat(True)
        self.Alignerninfoicon_rna.setGeometry(QtCore.QRect(48, 0, 20, 20))
        self.Alignerninfoicon_rna.setToolTip("Software for arranging sequences to identify regions of similarity")
        self.Alignerninfoicon_rna.setFont(font_info)
        self.Alignerninfoicon_rna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.Alignerninfoicon_rna.setIconSize(QtCore.QSize(13, 13))         
        
        self.AlignercomboBoxRNA = QtWidgets.QComboBox()
        self.AlignercomboBoxRNA.move(20, 10)
        self.AlignercomboBoxRNA.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.AlignercomboBoxRNA.setObjectName("AlignercomboBoxRNA")
        self.AlignercomboBoxRNA.addItem("")
        self.AlignercomboBoxRNA.addItem("")
        self.hlayout0_aligner_rna.addWidget(self.AlignercomboBoxRNA)
        self.hlayout0_aligner_rna.addStretch(0)
        self.vlayout_rna.addItem(self.hlayout0_aligner_rna)
        self.hlayout1_aligner_rna = QtWidgets.QHBoxLayout()
        self.hlayout1_aligner_rna.setSpacing(10)
        self.StarIndexlabel = QtWidgets.QLabel()
        self.StarIndexlabel.setObjectName("StarIndexlabel")
        self.StarIndexlineEdit = QtWidgets.QLineEdit()
        self.StarIndexpushButton = QtWidgets.QPushButton()
        self.StarIndexpushButton.setObjectName("StarIndexpushButton")
        
        self.hlayout1_aligner_rna.addWidget(self.StarIndexlabel)
        self.hlayout1_aligner_rna.addWidget(self.StarIndexlineEdit)
        self.hlayout1_aligner_rna.addWidget(self.StarIndexpushButton)
        self.vlayout_rna.addItem(self.hlayout1_aligner_rna)
        
        self.hlayout1_error_aligner_rna = QtWidgets.QHBoxLayout()
        self.StarIndexErrortext = QtWidgets.QLabel()
        self.StarIndexErrortext.setGeometry(QtCore.QRect(170, 116, 300, 15))
        self.StarIndexErrortext.setFont(font_label)
        self.StarIndexErrortext.setStyleSheet("color: red")
        self.StarIndexErrortext.hide()
        self.hlayout1_error_aligner_rna.addWidget(self.StarIndexErrortext, 0, alignment=QtCore.Qt.AlignCenter)
        self.vlayout_rna.addItem(self.hlayout1_error_aligner_rna)
        
        self.hlayout0_or_rna = QtWidgets.QHBoxLayout()
        self.OrLabel_rna = QtWidgets.QLabel()
        self.OrLabel_rna.setGeometry(QtCore.QRect(340, 130, 270, 23))
        self.OrLabel_rna.setObjectName("OrLabel_rna")
        self.hlayout0_or_rna.addWidget(self.OrLabel_rna, 0, alignment=QtCore.Qt.AlignCenter)
        self.vlayout_rna.addItem(self.hlayout0_or_rna)
        
        self.hlayout0_runindex_rna = QtWidgets.QHBoxLayout()
        self.RunIndexrnapushButton = QtWidgets.QPushButton()
        self.RunIndexrnapushButton.setObjectName("RunIndexrnapushButton")
        self.hlayout0_runindex_rna.addWidget(self.RunIndexrnapushButton, 0, alignment=QtCore.Qt.AlignCenter)
        self.RunIndexrnaButtonErroricon = QtWidgets.QPushButton()
        self.RunIndexrnaButtonErroricon.setGeometry(QtCore.QRect(480, 175, 20, 20))
        self.RunIndexrnaButtonErroricon.setToolTip("Check and Run Index Again!")
        self.RunIndexrnaButtonErroricon.setFont(font_label)
        self.RunIndexrnaButtonErroricon.setIcon(QtGui.QIcon("./icons/warning.svg"))
        self.RunIndexrnaButtonErroricon.hide()
        self.hlayout0_runindex_rna.addWidget(self.RunIndexrnaButtonErroricon, 0, alignment=QtCore.Qt.AlignCenter)
        self.vlayout_rna.addItem(self.hlayout0_runindex_rna)
        
        self.hlayout0_pb_rna = QtWidgets.QHBoxLayout()
        self.progressBar_sub2_rna = QtWidgets.QProgressBar()
        self.progressBar_sub2_rna.setGeometry(QtCore.QRect(10, 230, 665, 17))
        self.progressBar_sub2_rna.setProperty("value", 0)
        self.progressBar_sub2_rna.setObjectName("progressBar_sub2_rna")
        self.hlayout0_pb_rna.addWidget(self.progressBar_sub2_rna)
        self.vlayout_rna.addItem(self.hlayout0_pb_rna)
        
        self.param1_label_rna_1 = QtWidgets.QLabel()
        self.param1_label_rna_1.setGeometry(QtCore.QRect(20, 40, 91, 18))
        self.param1_lineEdit_rna_1 = QtWidgets.QLineEdit()
        self.param1_lineEdit_rna_1.setGeometry(QtCore.QRect(120, 40, 70, 18))
        self.param1_label_rna_3 = QtWidgets.QLabel()
        self.param1_label_rna_3.setGeometry(QtCore.QRect(200, 40, 91, 18))
        self.param1_lineEdit_rna_3 = QtWidgets.QLineEdit()
        self.param1_lineEdit_rna_3.setGeometry(QtCore.QRect(280, 40, 70, 18))
        self.param1_label_rna_5 = QtWidgets.QLabel()
        self.param1_label_rna_5.setGeometry(QtCore.QRect(360, 40, 91, 18))
        self.param1_lineEdit_rna_5 = QtWidgets.QLineEdit()
        self.param1_lineEdit_rna_5.setGeometry(QtCore.QRect(440, 40, 70, 18))

        
        self.param1_label_rna_2 = QtWidgets.QLabel()
        self.param1_label_rna_2.setGeometry(QtCore.QRect(20, 65, 91, 18))
        self.param1_lineEdit_rna_2 = QtWidgets.QLineEdit()
        self.param1_lineEdit_rna_2.setGeometry(QtCore.QRect(120, 65, 70, 18))
        self.param1_label_rna_4 = QtWidgets.QLabel()
        self.param1_label_rna_4.setGeometry(QtCore.QRect(200, 65, 91, 18))
        self.param1_lineEdit_rna_4 = QtWidgets.QLineEdit()
        self.param1_lineEdit_rna_4.setGeometry(QtCore.QRect(280, 65, 70, 18))
        self.param1_label_rna_6 = QtWidgets.QLabel()
        self.param1_label_rna_6.setGeometry(QtCore.QRect(360, 65, 91, 18))
        self.param1_lineEdit_rna_6 = QtWidgets.QLineEdit()
        self.param1_lineEdit_rna_6.setGeometry(QtCore.QRect(440, 65, 70, 18))
        
        self.grid_aligner_rna = QtWidgets.QGridLayout()
        self.grid_aligner_rna.setSpacing(10)
        self.grid_aligner_rna.addWidget(self.param1_label_rna_1, 0, 0)
        self.grid_aligner_rna.addWidget(self.param1_lineEdit_rna_1, 0, 1)
        self.grid_aligner_rna.addWidget(self.param1_label_rna_3, 0, 2)
        self.grid_aligner_rna.addWidget(self.param1_lineEdit_rna_3, 0, 3)
        self.grid_aligner_rna.addWidget(self.param1_label_rna_5, 0, 4)
        self.grid_aligner_rna.addWidget(self.param1_lineEdit_rna_5, 0, 5)
        self.grid_aligner_rna.addWidget(self.param1_label_rna_2, 1,0)
        self.grid_aligner_rna.addWidget(self.param1_lineEdit_rna_2, 1,1)
        self.grid_aligner_rna.addWidget(self.param1_label_rna_4, 1,2)
        self.grid_aligner_rna.addWidget(self.param1_lineEdit_rna_4, 1, 3)
        self.grid_aligner_rna.addWidget(self.param1_label_rna_6, 1,4)
        self.grid_aligner_rna.addWidget(self.param1_lineEdit_rna_6, 1,5)
        
        self.vlayout_rna.addItem(self.grid_aligner_rna)
        
        
        self.hlayout4_aligner_rna = QtWidgets.QHBoxLayout()
        self.hlayout4_aligner_rna.addStretch(1)
        self.aligner_add_rna = QtWidgets.QPushButton()
        self.aligner_add_rna.setGeometry(QtCore.QRect(530, 45, 70, 30))
        self.aligner_add_rna.setText("Advanced")
        self.aligner_add_rna.setStyleSheet("background-color: #704214")
        self.hlayout4_aligner_rna.addWidget(self.aligner_add_rna)
        self.vlayout_rna.addItem(self.hlayout4_aligner_rna)
        
        self.aligner_groupbox_rna.setLayout(self.vlayout_rna)
        
        font_param = QtGui.QFont()
        font_param.setBold(True)

        
        ##set of lbels and lineedits for params##
        
        self.param1_label_rna_1.hide()
        self.param1_label_rna_2.hide()
        self.param1_label_rna_3.hide()
        self.param1_label_rna_4.hide()
        self.param1_label_rna_5.hide()
        self.param1_label_rna_6.hide()
        self.param1_lineEdit_rna_1.hide()
        self.param1_lineEdit_rna_2.hide()
        self.param1_lineEdit_rna_3.hide()
        self.param1_lineEdit_rna_4.hide()
        self.param1_lineEdit_rna_5.hide()
        self.param1_lineEdit_rna_6.hide()
        
        
        
       
    def create_em_groupbox(self):
        self.em_groupbox = QGroupBox("Expression Modeller")
        self.vlayout_em= QtWidgets.QVBoxLayout()
        self.hlayout0_em = QtWidgets.QHBoxLayout()
        
        font_info = QtGui.QFont()
        font_info.setPointSize(8.5)
        self.eminfoicon_rna = QtWidgets.QPushButton(self.em_groupbox)
        self.eminfoicon_rna.setFlat(True)
        self.eminfoicon_rna.setGeometry(QtCore.QRect(125, 0, 20, 20))
        self.eminfoicon_rna.setToolTip("Expression modelling refers to count the reads mapped \n to individual genes from the aligned the file")
        self.eminfoicon_rna.setFont(font_info)
        self.eminfoicon_rna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.eminfoicon_rna.setIconSize(QtCore.QSize(13, 13))              
        
        self.EMcomboBoxRNA = QtWidgets.QComboBox()
        self.EMcomboBoxRNA.setObjectName("EMcomboBoxRNA")
        self.EMcomboBoxRNA.addItem("")
        self.EMcomboBoxRNA.addItem("")
        self.hlayout0_em.addWidget(self.EMcomboBoxRNA)
        self.hlayout0_em.addStretch(0)
        self.vlayout_em.addItem(self.hlayout0_em)
        
        
        self.param2_label_rna_1 = QtWidgets.QLabel()
        self.param2_label_rna_1.setGeometry(QtCore.QRect(20, 40, 91, 18))
        self.param2_lineEdit_rna_1 = QtWidgets.QLineEdit()
        self.param2_lineEdit_rna_1.setGeometry(QtCore.QRect(120, 40, 70, 18))
        self.param2_label_rna_3 = QtWidgets.QLabel()
        self.param2_label_rna_3.setGeometry(QtCore.QRect(200, 40, 91, 18))
        self.param2_lineEdit_rna_3 = QtWidgets.QLineEdit()
        self.param2_lineEdit_rna_3.setGeometry(QtCore.QRect(280, 40, 70, 18))
        self.param2_label_rna_5 = QtWidgets.QLabel()
        self.param2_label_rna_5.setGeometry(QtCore.QRect(360, 40, 91, 18))
        self.param2_lineEdit_rna_5 = QtWidgets.QLineEdit()
        self.param2_lineEdit_rna_5.setGeometry(QtCore.QRect(440, 40, 70, 18))
        
        self.param2_label_rna_2 = QtWidgets.QLabel()
        self.param2_label_rna_2.setGeometry(QtCore.QRect(20, 65, 91, 18))
        self.param2_lineEdit_rna_2 = QtWidgets.QLineEdit()
        self.param2_lineEdit_rna_2.setGeometry(QtCore.QRect(120, 65, 70, 18))
        self.param2_label_rna_4 = QtWidgets.QLabel()
        self.param2_label_rna_4.setGeometry(QtCore.QRect(200, 65, 91, 18))
        self.param2_lineEdit_rna_4 = QtWidgets.QLineEdit()
        self.param2_lineEdit_rna_4.setGeometry(QtCore.QRect(280, 65, 70, 18))
        self.param2_label_rna_6 = QtWidgets.QLabel()
        self.param2_label_rna_6.setGeometry(QtCore.QRect(360, 65, 91, 18))
        self.param2_lineEdit_rna_6 = QtWidgets.QLineEdit()
        self.param2_lineEdit_rna_6.setGeometry(QtCore.QRect(440, 65, 70, 18))
        
        self.grid_em = QtWidgets.QGridLayout()
        self.grid_em.setSpacing(10)
        self.grid_em.addWidget(self.param2_label_rna_1, 0, 0)
        self.grid_em.addWidget(self.param2_lineEdit_rna_1, 0, 1)
        self.grid_em.addWidget(self.param2_label_rna_3, 0, 2)
        self.grid_em.addWidget(self.param2_lineEdit_rna_3, 0, 3)
        self.grid_em.addWidget(self.param2_label_rna_5, 0, 4)
        self.grid_em.addWidget(self.param2_lineEdit_rna_5, 0, 5)
        self.grid_em.addWidget(self.param2_label_rna_2, 1,0)
        self.grid_em.addWidget(self.param2_lineEdit_rna_2, 1,1)
        self.grid_em.addWidget(self.param2_label_rna_4, 1,2)
        self.grid_em.addWidget(self.param2_lineEdit_rna_4, 1, 3)
        self.grid_em.addWidget(self.param2_label_rna_6, 1,4)
        self.grid_em.addWidget(self.param2_lineEdit_rna_6, 1,5)
        
        self.vlayout_em.addItem(self.grid_em)
        self.param2_label_rna_1.hide()
        self.param2_label_rna_2.hide()
        self.param2_label_rna_3.hide()
        self.param2_label_rna_4.hide()
        self.param2_label_rna_5.hide()
        self.param2_label_rna_6.hide()
        self.param2_lineEdit_rna_1.hide()
        self.param2_lineEdit_rna_2.hide()
        self.param2_lineEdit_rna_3.hide()
        self.param2_lineEdit_rna_4.hide()
        self.param2_lineEdit_rna_5.hide()
        self.param2_lineEdit_rna_6.hide()
        
        self.hlayout4_em = QtWidgets.QHBoxLayout()
        self.hlayout4_em.addStretch(1)
        self.em_add_rna = QtWidgets.QPushButton()
        self.em_add_rna.setGeometry(QtCore.QRect(530, 45, 70, 30))
        self.em_add_rna.setText("Advanced")
        self.em_add_rna.setStyleSheet("background-color: #704214")
        self.hlayout4_em.addWidget(self.em_add_rna)
        self.vlayout_em.addItem(self.hlayout4_em)
        
        self.em_groupbox.setLayout(self.vlayout_em)
        
    def create_de_groupbox(self):
        self.de_groupbox = QGroupBox("Differential Expression")
        self.vlayout_de= QtWidgets.QVBoxLayout()
        self.vlayout_de.setSpacing(20)
        self.hlayout0_de = QtWidgets.QHBoxLayout()
        
        font_info = QtGui.QFont()
        font_info.setPointSize(8.5)
        self.deninfoicon_rna = QtWidgets.QPushButton(self.de_groupbox)
        self.deninfoicon_rna.setFlat(True)
        self.deninfoicon_rna.setGeometry(QtCore.QRect(140, 0, 20, 20))
        self.deninfoicon_rna.setToolTip("Differential expression analysis referes to the normalization of read count data \n and employing statistical methods to discover quantitative changes\n in expression levels between different data groups")
        self.deninfoicon_rna.setFont(font_info)
        self.deninfoicon_rna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.deninfoicon_rna.setIconSize(QtCore.QSize(13, 13))         
        
        self.DEcomboBoxRNA = QtWidgets.QComboBox()
        self.DEcomboBoxRNA.setObjectName("DEcomboBoxRNA")
        self.DEcomboBoxRNA.addItem("")
        self.DEcomboBoxRNA.addItem("")
        self.hlayout0_de.addWidget(self.DEcomboBoxRNA)
        self.hlayout0_de.addStretch(0)
        self.vlayout_de.addItem(self.hlayout0_de)
        

        
        
        self.param3_label_rna_1 = QtWidgets.QLabel()
        self.param3_label_rna_1.setGeometry(QtCore.QRect(20, 40, 91, 18))
        self.param3_lineEdit_rna_1 = QtWidgets.QLineEdit()
        self.param3_lineEdit_rna_1.setGeometry(QtCore.QRect(120, 40, 70, 18))
        self.param3_label_rna_3 = QtWidgets.QLabel()
        self.param3_label_rna_3.setGeometry(QtCore.QRect(200, 40, 91, 18))
        self.param3_lineEdit_rna_3 = QtWidgets.QLineEdit()
        self.param3_lineEdit_rna_3.setGeometry(QtCore.QRect(280, 40, 70, 18))
        self.param3_label_rna_5 = QtWidgets.QLabel()
        self.param3_label_rna_5.setGeometry(QtCore.QRect(360, 40, 91, 18))
        self.param3_lineEdit_rna_5 = QtWidgets.QLineEdit()
        self.param3_lineEdit_rna_5.setGeometry(QtCore.QRect(440, 40, 70, 18))
        
        self.param3_label_rna_2 = QtWidgets.QLabel()
        self.param3_label_rna_2.setGeometry(QtCore.QRect(20, 65, 91, 18))
        self.param3_lineEdit_rna_2 = QtWidgets.QLineEdit()
        self.param3_lineEdit_rna_2.setGeometry(QtCore.QRect(120, 65, 70, 18))
        self.param3_label_rna_4 = QtWidgets.QLabel()
        self.param3_label_rna_4.setGeometry(QtCore.QRect(200, 65, 91, 18))
        self.param3_lineEdit_rna_4 = QtWidgets.QLineEdit()
        self.param3_lineEdit_rna_4.setGeometry(QtCore.QRect(280, 65, 70, 18))
        self.param3_label_rna_6 = QtWidgets.QLabel()
        self.param3_label_rna_6.setGeometry(QtCore.QRect(360, 65, 91, 18))
        self.param3_lineEdit_rna_6 = QtWidgets.QLineEdit()
        self.param3_lineEdit_rna_6.setGeometry(QtCore.QRect(440, 65, 70, 18))
        
        self.grid_de = QtWidgets.QGridLayout()
        self.grid_de.setSpacing(10)
        self.grid_de.addWidget(self.param3_label_rna_1, 0, 0)
        self.grid_de.addWidget(self.param3_lineEdit_rna_1, 0, 1)
        self.grid_de.addWidget(self.param3_label_rna_3, 0, 2)
        self.grid_de.addWidget(self.param3_lineEdit_rna_3, 0, 3)
        self.grid_de.addWidget(self.param3_label_rna_5, 0, 4)
        self.grid_de.addWidget(self.param3_lineEdit_rna_5, 0, 5)
        self.grid_de.addWidget(self.param3_label_rna_2, 1,0)
        self.grid_de.addWidget(self.param3_lineEdit_rna_2, 1,1)
        self.grid_de.addWidget(self.param3_label_rna_4, 1,2)
        self.grid_de.addWidget(self.param3_lineEdit_rna_4, 1, 3)
        self.grid_de.addWidget(self.param3_label_rna_6, 1,4)
        self.grid_de.addWidget(self.param3_lineEdit_rna_6, 1,5)
        
        self.param3_label_rna_1.hide()
        self.param3_label_rna_2.hide()
        self.param3_label_rna_3.hide()
        self.param3_label_rna_4.hide()
        self.param3_label_rna_5.hide()
        self.param3_label_rna_6.hide()
        self.param3_lineEdit_rna_1.hide()
        self.param3_lineEdit_rna_2.hide()
        self.param3_lineEdit_rna_3.hide()
        self.param3_lineEdit_rna_4.hide()
        self.param3_lineEdit_rna_5.hide()
        self.param3_lineEdit_rna_6.hide()
        
        self.vlayout_de.addItem(self.grid_de)
        
        self.hlayout4_de = QtWidgets.QHBoxLayout()
        self.hlayout4_de.addStretch(1)
        self.de_add_rna = QtWidgets.QPushButton()
        self.de_add_rna.setGeometry(QtCore.QRect(530, 45, 70, 30))
        self.de_add_rna.setText("Advanced")
        self.de_add_rna.setStyleSheet("background-color: #704214")
        self.hlayout4_de.addWidget(self.de_add_rna)
        self.vlayout_de.addItem(self.hlayout4_de)
        self.de_groupbox.setLayout(self.vlayout_de)
        
    def create_group_next_rna(self):
        self.next_groupbox_rna = QGroupBox()
        self.vlayout_next_rna= QtWidgets.QVBoxLayout()
        self.nextbuttontoolRNA = QtWidgets.QPushButton()
        self.nextbuttontoolRNA.setGeometry(QtCore.QRect(635, 400, 45, 45))
        self.nextbuttontoolRNA.setObjectName("nextbuttontoolRNA")
        ###
        self.previousbuttontoolRNA = QtWidgets.QPushButton()
        self.previousbuttontoolRNA.setGeometry(QtCore.QRect(10, 400, 45, 45))
        self.previousbuttontoolRNA.setObjectName("previousbuttontoolRNA")
        
        self.hbox_next_rna = QtWidgets.QHBoxLayout()
        self.hbox_next_rna.addWidget(self.previousbuttontoolRNA, 0, alignment=QtCore.Qt.AlignLeft)
        self.hbox_next_rna.addWidget(self.nextbuttontoolRNA, 0, alignment=QtCore.Qt.AlignRight)
        
        self.vlayout_next_rna.addItem(self.hbox_next_rna)
        self.next_groupbox_rna.setLayout(self.vlayout_next_rna)
        
    def get_essential(self, path, essential_line_edit_array):
        dataframe = pd.read_csv(path, header =0)
        self.essential = dataframe[dataframe["Essential"] == "yes"]
        self.new_essential = [essential_line_edit_array[i].text() for i in range(len(self.essential))]
        self.essential['New_value'] = self.new_essential
        self.essential['New_value'] = self.essential['New_value'].astype('str')
        self.essential = self.essential.reset_index()
        self.essential_dict = dict()
        for row in self.essential.itertuples():
            if row[6] != row[8]:
                self.essential_dict[row[2]] = row[8]
        return self.essential_dict
    
    def get_additional_int(self, path):
        dataframe = pd.read_csv(path, header =0)
        self.additional_int = dataframe[(dataframe["Value"] == 'INT') & (dataframe["Essential"] == 'no')]
        self.new_values_int = [j.text() for j in self.adv_dialog.line_edit_list_int]
        self.additional_int['New Value'] = self.new_values_int
        self.additional_int['New Value'] = self.additional_int['New Value'].astype('str')
        self.additional_int = self.additional_int.reset_index()
        self.snakefile_dict_int = dict()
        for row in self.additional_int.itertuples():
            if row[6] != row[8]:
                self.snakefile_dict_int[row[2]] = row[8]
        return self.snakefile_dict_int
    
    def get_additional_float(self, path):
        dataframe = pd.read_csv(path, header =0)
        self.additional_float = dataframe[(dataframe["Value"] == 'FLOAT') & (dataframe["Essential"] == 'no')]
        self.new_values_float = [j.text() for j in self.adv_dialog.line_edit_list_float]
        self.additional_float['New Value'] = self.new_values_float
        self.additional_float['New Value'] = self.additional_float['New Value'].astype('str')
        self.additional_float = self.additional_float.reset_index()
        self.snakefile_dict_float = dict()
        for row in self.additional_float.itertuples():
            if row[6] != row[8]:
                self.snakefile_dict_float[row[2]] = row[8]
        return self.snakefile_dict_float
    
    def get_additional_str(self, path):
        dataframe = pd.read_csv(path, header =0)
        self.additional_str = dataframe[(dataframe["Value"] == 'STR') & (dataframe["Essential"] == 'no')]
        self.new_values_str = [j.text() for j in self.adv_dialog.line_edit_list_str]
        self.additional_str['New Value'] = self.new_values_str
        self.additional_str['New Value'] = self.additional_str['New Value'].astype('str')
        self.additional_str = self.additional_str.reset_index()
        self.snakefile_dict_str = dict()
        for j in self.adv_dialog.label_list_str:
            if j.isChecked() == True:
                self.new_values_str.append("TRUE")
            else:
                self.new_values_str.append("FALSE")
        self.additional_str['New Value'] = self.new_values_str
        self.additional_str['New Value'] = self.additional_str['New Value'].astype('str')
        self.additional_str = self.additional_str.reset_index()
        self.snakefile_dict_str = dict()
        for row in self.additional_str.itertuples():
            if row[6] != row[8]:
                self.snakefile_dict_str[row[2]] = row[8]
        return self.snakefile_dict_str
    
    def get_additional_na(self, path):
        dataframe = pd.read_csv(path, header =0)
        self.additional_na = dataframe[(dataframe["Value"] == 'na') & (dataframe["Essential"] == 'no')]
        self.new_values_na=[]
        for j in self.adv_dialog.radio_label_list_na:
            if j.isChecked() == True:
                self.new_values_na.append("yes")
            else:
                self.new_values_na.append("na")
        self.additional_na['New Value'] = self.new_values_na
        self.additional_na['New Value'] = self.additional_na['New Value'].astype('str')
        self.additional_na = self.additional_na.reset_index()
        self.snakefile_dict_na = dict()
        for row in self.additional_na.itertuples():
            if row[6] != row[8]:
                self.snakefile_dict_na[row[2]] = row[8]
        return self.snakefile_dict_na
        
    
    def on_clicked_nextbuttoninputDNA(self):
        if self.SamplesYesradioButton.isChecked() == True:
            if self.SampleslineEditDNA.text() == '':
                self.SamplesErrortextDNA.show()
                self.SamplesErrortextDNA.setText("Input Samples folder path!")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            elif not os.path.exists(self.SampleslineEditDNA.text()):
                self.SamplesErrortextDNA.show()
                self.SamplesErrortextDNA.setText("File doesn't exist! Check the path!")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            else:
                inputfile = fileinput.input("check_for_correct_filename_check.py", inplace = 1)
                for l in inputfile:
                    if "test_dir =" in l:
                        print(l.replace(l, "test_dir = '"+self.SampleslineEditDNA.text()+"/'"))
                    else:
                        print(l.rstrip())
                inputfile.close()
                subprocess.run(["python", "check_for_correct_filename_check.py"])
                if os.path.exists('name_check.txt'):
                    self.DNAtabWidget.setCurrentIndex(0)
                    self.DNAtabWidget.setTabEnabled(1, False)
                    with open('name_check.txt') as errorcheck:
                        content = errorcheck.readline()
                    self.SamplesErrortextDNA.show()
                    self.SamplesErrortextDNA.setText(content.rstrip())
                else:
                    file = fileinput.input("write_tsv.py", inplace = 1)
                    for l in file:
                        if "test_dir =" in l:
                            print(l.replace(l, "test_dir = '"+self.SampleslineEditDNA.text()+"/'"))
                        else:
                            print(l.rstrip())
                    file.close()
                    subprocess.run(["python", "write_tsv.py"])
                    unitsdf =pd.read_table('units.tsv', header=0)
                    self.UnitslineEditDNA.setText("units.tsv")
                    Row_list =[]
                    for index, rows in unitsdf.iterrows():
                        my_list =[rows.condition]
                        Row_list.append(my_list)
                    if ['tumor'] in Row_list:
                        self.VCcomboBoxDNA.setItemText(0, "Mutect2")

                    else:
                        self.VCcomboBoxDNA.addItem("")
                        self.VCcomboBoxDNA.addItem("")
                        self.VCcomboBoxDNA.setItemText(0, "GATK_HC")
                        self.VCcomboBoxDNA.setItemText(1, "bcftools_call")
                        self.VCcomboBoxDNA.setItemText(2, "freebayes")
                        
                        
                    
            if self.RefGenomelineEditDNA.text() == '':
                self.RefGenomeErrortextDNA.show()
                self.RefGenomeErrortextDNA.setText("Input reference genome file!")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            elif not os.path.exists(self.RefGenomelineEditDNA.text()):
                self.RefGenomeErrortextDNA.show()
                self.RefGenomeErrortextDNA.setText("File doesn't exist! Check the path!")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            elif os.path.splitext(self.RefGenomelineEditDNA.text())[-1] != ".fa":
                self.RefGenomeErrortextDNA.show()
                self.RefGenomeErrortextDNA.setText("File should have extension '.fa'")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)

             
            if self.RefVariantlineEditDNA.text()== '':
                self.RefVariantErrortextDNA.show()
                self.RefVariantErrortextDNA.setText("Input reference known variants file!")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            elif not os.path.exists(self.RefVariantlineEditDNA.text()):
                self.RefVariantErrortextDNA.show()
                self.RefVariantErrortextDNA.setText("File doesn't exist! Check the path!")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            elif os.path.splitext(self.RefVariantlineEditDNA.text())[-1] != ".gz":
                self.RefVariantErrortextDNA.show()
                self.RefVariantErrortextDNA.setText("File should have extension '.gz'")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            elif (self.RefVariantlineEditDNA.text()).split(".")[-2] != "vcf":
                self.RefVariantErrortextDNA.show()
                self.RefVariantErrortextDNA.setText("File should be compressed 'vcf'")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            if self.CorelineEditDNA.text()=='':
                self.CoreErrortextDNA.show()
                self.CoreErrortextDNA.setText("Input number of threads available")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            elif not self.CorelineEditDNA.text().isnumeric():
                self.CoreErrortextDNA.show()
                self.CoreErrortextDNA.setText("Number of threads should be an integer")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            elif (os.path.splitext(self.RefGenomelineEditDNA.text())[-1] == ".fa" and not os.path.exists('name_check.txt') and os.path.splitext(self.RefVariantlineEditDNA.text())[-1] == ".gz" and (self.RefVariantlineEditDNA.text().split(".")[-2]) == 'vcf' and self.CorelineEditDNA.text().isnumeric()):
                self.SamplesErrortextDNA.hide()
                self.UnitsErrortextDNA.hide()
                self.RefGenomeErrortextDNA.hide()
                self.RefVariantErrortextDNA.hide()
                self.DNAtabWidget.setCurrentIndex(1)
                self.DNAtabWidget.setTabEnabled(1, True)
                self.textBrowser.setTextColor(self._colors['blue'])
                self.textBrowser.append("Click on the 'View Quality control Results' button to view the FastQC report \n")
        else:
            if self.UnitslineEditDNA.text() == '':
                self.UnitsErrortextDNA.show()
                self.UnitsErrortextDNA.setText("Input Units table!")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            elif not os.path.exists(self.UnitslineEditDNA.text()):
                self.UnitsErrortextDNA.show()
                self.UnitsErrortextDNA.setText("File doesn't exist! Check the path!")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            elif os.path.splitext(self.UnitslineEditDNA.text())[-1] != ".tsv":
                self.UnitsErrortextDNA.show()
                self.UnitsErrortextDNA.setText("File should have extension '.tsv'")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            else:
                list_tsv_col = ['sample', 'unit', 'condition', 'fq1', 'fq2']
                unitsdf =pd.read_table(self.UnitslineEditDNA.text(), header=0)
                if list(unitsdf) != list_tsv_col:
                    self.UnitsErrortextDNA.show()
                    self.UnitsErrortextDNA.setText("Table not in given format! Check!")
                else:
                    arr = []
                    for item in unitsdf["sample"]:
                        arr.append(item)
                    sample_df = pd.DataFrame({'sample': np.unique(arr)})
                    sample_df.to_csv('samples.tsv', sep = '\t', index=False)
                    Row_list =[]
                    for index, rows in unitsdf.iterrows():
                        my_list =[rows.condition]
                        Row_list.append(my_list)
                    if ['tumor'] in Row_list:
                        self.VCcomboBoxDNA.setItemText(0, "Mutect2")

                    else:
                        self.VCcomboBoxDNA.addItem("")
                        self.VCcomboBoxDNA.addItem("")
                        self.VCcomboBoxDNA.setItemText(0, "GATK_HC")
                        self.VCcomboBoxDNA.setItemText(1, "bcftools_call")
                        self.VCcomboBoxDNA.setItemText(2, "freebayes")
            if self.RefGenomelineEditDNA.text() == '':
                self.RefGenomeErrortextDNA.show()
                self.RefGenomeErrortextDNA.setText("Input reference genome file!")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            elif not os.path.exists(self.RefGenomelineEditDNA.text()):
                self.RefGenomeErrortextDNA.show()
                self.RefGenomeErrortextDNA.setText("File doesn't exist! Check the path!")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            elif os.path.splitext(self.RefGenomelineEditDNA.text())[-1] != ".fa":
                self.RefGenomeErrortextDNA.show()
                self.RefGenomeErrortextDNA.setText("File should have extension '.fa'")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)

            if self.RefVariantlineEditDNA.text()== '':
                self.RefVariantErrortextDNA.show()
                self.RefVariantErrortextDNA.setText("Input reference known variants file!")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            elif not os.path.exists(self.RefVariantlineEditDNA.text()):
                self.RefVariantErrortextDNA.show()
                self.RefVariantErrortextDNA.setText("File doesn't exist! Check the path!")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            elif os.path.splitext(self.RefVariantlineEditDNA.text())[-1] != ".gz":
                self.RefVariantErrortextDNA.show()
                self.RefVariantErrortextDNA.setText("File should have extension '.gz'")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            elif (self.RefVariantlineEditDNA.text()).split(".")[-2] != "vcf":
                self.RefVariantErrortextDNA.show()
                self.RefVariantErrortextDNA.setText("File should be compressed 'vcf'")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            if self.CorelineEditDNA.text()=='':
                self.CoreErrortextDNA.show()
                self.CoreErrortextDNA.setText("Input number of threads available")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            elif not self.CorelineEditDNA.text().isnumeric():
                self.CoreErrortextDNA.show()
                self.CoreErrortextDNA.setText("Number of threads should be an integer")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            elif (list(unitsdf) == list_tsv_col and os.path.splitext(self.RefGenomelineEditDNA.text())[-1] == ".fa" and os.path.splitext(self.RefVariantlineEditDNA.text())[-1] == ".gz" and (self.RefVariantlineEditDNA.text().split(".")[-2]) == 'vcf' and self.CorelineEditDNA.text().isnumeric()):
                self.SamplesErrortextDNA.hide()
                self.UnitsErrortextDNA.hide()
                self.RefGenomeErrortextDNA.hide()
                self.RefVariantErrortextDNA.hide()
                self.DNAtabWidget.setCurrentIndex(1)
                self.DNAtabWidget.setTabEnabled(1, True)
                self.textBrowser.setTextColor(self._colors['blue'])
                self.textBrowser.append("Click on the 'View Quality control Results' button to view the FastQC report \n")

                
    def param_display(self):
        _translate = QtCore.QCoreApplication.translate
        path_aligner = './params/'+self.AlignercomboBoxDNA.currentText()+'.csv'
        path_vc = './params/'+self.VCcomboBoxDNA.currentText()+'.csv'
        path_annotator = './params/'+self.AnnotatorcomboBoxDNA.currentText()+'.csv'

        dataframe = pd.read_csv(path_aligner, header=0) # specifying that the table has column names
        essential = dataframe[dataframe["Essential"] == "yes"]
        
        number_of_essential = len(essential) # returns number of essential parameters
        label_array_param1 = [self.param1_label_dna_1, self.param1_label_dna_2, self.param1_label_dna_3, self.param1_label_dna_4, self.param1_label_dna_5, self.param1_label_dna_6]
        line_edit_array_param1 = [self.param1_lineEdit_dna_1,self.param1_lineEdit_dna_2, self.param1_lineEdit_dna_3, self.param1_lineEdit_dna_4, self.param1_lineEdit_dna_5, self.param1_lineEdit_dna_6]
        for i, j, k in zip(range(number_of_essential), label_array_param1, line_edit_array_param1): 
            j.show()
            j.setText(essential.iloc[i, 2])
            k.show()
            k.setText(str(essential.iloc[i, 4]))
            
        
            
        dataframe_vc = pd.read_csv(path_vc, header=0) # specifying that the table has column names
        essential_vc = dataframe_vc[dataframe_vc["Essential"] == "yes"]
        
        number_of_essential_vc = len(essential_vc) # returns number of essential parameters
        label_array_param2 = [self.param2_label_dna_1, self.param2_label_dna_2, self.param2_label_dna_3, self.param2_label_dna_4, self.param2_label_dna_5, self.param2_label_dna_6]
        line_edit_array_param2 = [self.param2_lineEdit_dna_1,self.param2_lineEdit_dna_2, self.param2_lineEdit_dna_3, self.param2_lineEdit_dna_4, self.param2_lineEdit_dna_5, self.param2_lineEdit_dna_6]
        for i, j, k in zip(range(number_of_essential_vc), label_array_param2, line_edit_array_param2): 
            j.show()
            j.setText(essential_vc.iloc[i, 2])
            k.show()
            k.setText(str(essential_vc.iloc[i, 4]))
            
        dataframe_annotator = pd.read_csv(path_annotator, header=0) # specifying that the table has column names
        essential_annotator = dataframe_annotator[dataframe_annotator["Essential"] == "yes"]
        
        number_of_essential_annotator = len(essential_annotator) # returns number of essential parameters
        label_array_param3 = [self.param3_label_dna_1, self.param3_label_dna_2, self.param3_label_dna_3, self.param3_label_dna_4, self.param3_label_dna_5, self.param3_label_dna_6]
        line_edit_array_param3 = [self.param3_lineEdit_dna_1,self.param3_lineEdit_dna_2, self.param3_lineEdit_dna_3, self.param3_lineEdit_dna_4, self.param3_lineEdit_dna_5, self.param3_lineEdit_dna_6]
        for i, j, k in zip(range(number_of_essential_annotator), label_array_param3, line_edit_array_param3): 
            j.show()
            j.setText(essential_annotator.iloc[i, 2])
            k.show()
            k.setText(str(essential_annotator.iloc[i, 4]))
            
        self.BWAIndexlabel.setText(_translate("MainWindow", "Index for " + self.AlignercomboBoxDNA.currentText()))
        self.BWAIndexlineEdit.setToolTip(_translate("MainWindow", "Input the path of the Index for" + self.AlignercomboBoxDNA.currentText()))
        
    def on_clicking_browse_samples(self):
        self.SamplesErrortextDNA.hide()
        
    def on_clicked_nextbuttonqcDNA(self):
        self.param_display()
        if os.path.exists("results_dna/qc"):
            self.DNAtabWidget.setCurrentIndex(2)
            self.DNAtabWidget.setTabEnabled(2, True)
        else:
            self.qc_warning = showQCDialog()
            if self.qc_warning.returnValue==QMessageBox.Yes:
                self.DNAtabWidget.setCurrentIndex(2)
                self.DNAtabWidget.setTabEnabled(2, True)
                                         
            if self.qc_warning.returnValue== QMessageBox.Cancel:
                self.DNAtabWidget.setCurrentIndex(1)
                self.DNAtabWidget.setTabEnabled(2, False)
        self.DNAtabWidget.setTabEnabled(2, True)
    def on_clicked_nextbuttontoolDNA(self):
        self.index_warning()
        self.DNAtabWidget.setCurrentIndex(3)
        self.DNAtabWidget.setTabEnabled(3, True)
        
        self.create_config_dna()
        self.create_snakefile_dna()
        self.if_annovar()
        self.textBrowser.setTextColor(self._colors['blue'])
        self.textBrowser.append("Click on the 'Run' button below to start your analysis \n")

    def index_warning(self):
        if self.BWAIndexlineEdit.text()=='':
            self.BWAIndexErrortext.show()
            self.BWAIndexErrortext.setText("Please input index path!")
            self.DNAtabWidget.setCurrentIndex(3)
            self.DNAtabWidget.setTabEnabled(4, False)
        else:
            self.DNAtabWidget.setCurrentIndex(4)
            self.DNAtabWidget.setTabEnabled(4, True)
            
    def on_clicked_nextbuttonparamsDNA(self):

        self.essential_dict_aligner = self.get_essential(path ='./params/'+self.AlignercomboBoxDNA.currentText()+'.csv', essential_line_edit_array= [self.param1_lineEdit_dna_1,self.param1_lineEdit_dna_2, self.param1_lineEdit_dna_3, self.param1_lineEdit_dna_4, self.param1_lineEdit_dna_5, self.param1_lineEdit_dna_6] )
        with open('aligner_params.txt', 'w') as aligner_params:
            aligner_params.write(self.AlignercomboBoxDNA.currentText() + " : '")
            for k, v in self.essential_dict_aligner.items():
                aligner_params.write(k +' '+ str(v) + " ")
            aligner_params.write("'")
            aligner_params.close()
        self.essential_dict_vc = self.get_essential(path ='./params/'+self.VCcomboBoxDNA.currentText()+'.csv', essential_line_edit_array =[self.param2_lineEdit_dna_1,self.param2_lineEdit_dna_2, self.param2_lineEdit_dna_3, self.param2_lineEdit_dna_4, self.param2_lineEdit_dna_5, self.param2_lineEdit_dna_6])
        with open('vc_params.txt', 'w') as vc_params:
            vc_params.write(self.VCcomboBoxDNA.currentText() + " : '")
            for k, v in self.essential_dict_vc.items():
                vc_params.write(k +' '+ str(v) + " ")
            vc_params.write("'")
            vc_params.close()
        self.essential_dict_annotator = self.get_essential(path ='./params/'+self.AnnotatorcomboBoxDNA.currentText()+'.csv', essential_line_edit_array=[self.param3_lineEdit_dna_1,self.param3_lineEdit_dna_2, self.param3_lineEdit_dna_3, self.param3_lineEdit_dna_4, self.param3_lineEdit_dna_5, self.param3_lineEdit_dna_6] )
        with open('annotator_params.txt', 'w') as annotator_params:
            if self.AnnotatorcomboBoxDNA.currentText() == "SnpEff":
                annotator_params.write(self.AnnotatorcomboBoxDNA.currentText() + " : '-Xmx4g ")
            else:
                annotator_params.write(self.AnnotatorcomboBoxDNA.currentText() + " : '")
            for k, v in self.essential_dict_annotator.items():
                annotator_params.write(k +' '+ str(v) + " ")
            annotator_params.write("'")
            annotator_params.close()
        

        
        
        
    def on_clicked_previousbuttonqcDNA(self):
        self.DNAtabWidget.setCurrentIndex(0)
        self.DNAtabWidget.setTabEnabled(0, True)
    def on_clicked_previousbuttontoolDNA(self):
        self.DNAtabWidget.setCurrentIndex(1)
        self.DNAtabWidget.setTabEnabled(1, True)
    def on_clicked_previousbuttonindexDNA(self):
        self.DNAtabWidget.setCurrentIndex(2)
        self.DNAtabWidget.setTabEnabled(2, True)
    def on_clicked_previousbuttonparamsDNA(self):
        self.DNAtabWidget.setCurrentIndex(3)       
        self.DNAtabWidget.setTabEnabled(3, True)
        
    def on_clicked_previousbuttonrunDNA(self):
        self.DNAtabWidget.setCurrentIndex(2)       
        self.DNAtabWidget.setTabEnabled(2, True)
    
    def on_clicked_previousbuttonresultDNA(self):
        self.DNAtabWidget.setCurrentIndex(3)       
        self.DNAtabWidget.setTabEnabled(3, True)
        
    def on_clicked_nextbuttoninputRNA(self):

        if self.SamplesYesradioButton_rna.isChecked() == True:
            if self.SampleFolderLineEdit.text() == '':
                self.SampleFolderErrortextRNA.show()
                self.SampleFolderErrortextRNA.setText("Input Samples folder path!")
                self.RNAtabWidget.setCurrentIndex(0)
                self.RNAtabWidget.setTabEnabled(1, False)
            elif not os.path.exists(self.SampleFolderLineEdit.text()):
                self.SampleFolderErrortextRNA.show()
                self.SampleFolderErrortextRNA.setText("File doesn't exist! Check the path!")
                self.RNAtabWidget.setCurrentIndex(0)
                self.RNAtabWidget.setTabEnabled(1, False)
            else :
                inputfile = fileinput.input("check_for_correct_filename_check.py", inplace = 1)
                for l in inputfile:
                    if "test_dir =" in l:
                        print(l.replace(l, "test_dir = '"+self.SampleFolderLineEdit.text()+"'"))
                    else:
                        print(l.rstrip())
                inputfile.close()
                subprocess.run(["python", "check_for_correct_filename_check.py"])
                if os.path.exists('name_check.txt'):
                    self.RNAtabWidget.setCurrentIndex(0)
                    self.RNAtabWidget.setTabEnabled(1, False)
                    with open('name_check.txt') as errorcheck:
                        content = errorcheck.readline()
                    self.SampleFolderErrortextRNA.show()
                    self.SampleFolderErrortextRNA.setText(content.rstrip())
                else:
#                    pass
                    file = fileinput.input("write_tsv_rna.py", inplace = 1)
                    for l in file:
                        if "test_dir =" in l:
                            print(l.replace(l, "test_dir = '"+self.SampleFolderLineEdit.text()+"/'"))
                        else:
                            print(l.rstrip())
                    file.close()
                    subprocess.run(["python", "write_tsv_rna.py"])
                    unitsdf =pd.read_table('units.tsv', header=0)
                    self.UnitslineEditDNA.setText("units.tsv")
                    Row_list =[]
                    for index, rows in unitsdf.iterrows():
                        my_list =[rows.condition]
                        Row_list.append(my_list)

            if self.FastalineEdit.text() == '':
                self.FastaErrortextRNA.show()
                self.FastaErrortextRNA.setText("Input Fasta file!")
                self.RNAtabWidget.setCurrentIndex(0)
                self.RNAtabWidget.setTabEnabled(1, False)
            elif not os.path.exists(self.FastalineEdit.text()):
                self.FastaErrortextRNA.show()
                self.FastaErrortextRNA.setText("File doesn't exist! Check the path!")
                self.RNAtabWidget.setCurrentIndex(0)
                self.RNAtabWidget.setTabEnabled(1, False)
            elif os.path.splitext(self.FastalineEdit.text())[-1] != ".fa":
                self.FastaErrortextRNA.show()
                self.FastaErrortextRNA.setText("File should have extension '.fa'")
                self.RNAtabWidget.setCurrentIndex(0)
                self.RNAtabWidget.setTabEnabled(1, False)

            if self.AnnotatedlineEditRNA.text()== '':
                self.AnnotatedErrortextRNA.show()
                self.AnnotatedErrortextRNA.setText("Input Annotated file!")
                self.RNAtabWidget.setCurrentIndex(0)
                self.RNAtabWidget.setTabEnabled(1, False)
            elif not os.path.exists(self.AnnotatedlineEditRNA.text()):
                self.AnnotatedErrortextRNA.show()
                self.AnnotatedErrortextRNA.setText("File doesn't exist! Check the path!")
                self.RNAtabWidget.setCurrentIndex(0)
                self.RNAtabWidget.setTabEnabled(1, False)
            elif os.path.splitext(self.AnnotatedlineEditRNA.text())[-1] != ".gtf":
                self.AnnotatedErrortextRNA.show()
                self.AnnotatedErrortextRNA.setText("File should have extension '.gtf'")
                self.RNAtabWidget.setCurrentIndex(0)
                self.RNAtabWidget.setTabEnabled(1, False)

            if self.CorelineEditRNA.text()=='':
                self.CoreErrortextRNA.show()
                self.CoreErrortextRNA.setText("Input number of threads available")
                self.RNAtabWidget.setCurrentIndex(0)
                self.RNAtabWidget.setTabEnabled(1, False)
            elif not self.CorelineEditRNA.text().isnumeric():
#                print("File doesn't exist! Check the path!")
                self.CoreErrortextRNA.show()
                self.CoreErrortextRNA.setText("Number of threads should be an integer")
                self.RNAtabWidget.setCurrentIndex(0)
                self.RNAtabWidget.setTabEnabled(1, False)
            elif (os.path.splitext(self.FastalineEdit.text())[-1] == ".fa" and not os.path.exists('name_check.txt') and os.path.splitext(self.AnnotatedlineEditRNA.text())[-1] == ".gtf" and self.CorelineEditRNA.text().isnumeric()):    
                self.FastaErrortextRNA.hide()
                self.SampleFolderErrortextRNA.hide()
                self.AnnotatedErrortextRNA.hide()
                self.RNAtabWidget.setCurrentIndex(1)
                self.RNAtabWidget.setTabEnabled(1, True)
                self.textBrowser.setTextColor(self._colors['blue'])
                self.textBrowser.append("Click on the 'View Quality control Results' button below to view the FastQC report \n")

        else:
            if self.SampleFolderLineEdit.text() == '':
                self.SampleFolderErrortextRNA.show()
                self.SampleFolderErrortextRNA.setText("Input Samples folder path!")
                self.RNAtabWidget.setCurrentIndex(0)
                self.RNAtabWidget.setTabEnabled(1, False)
            elif not os.path.exists(self.SampleFolderLineEdit.text()):
                self.SampleFolderErrortextRNA.show()
                self.SampleFolderErrortextRNA.setText("File doesn't exist! Check the path!")
                self.RNAtabWidget.setCurrentIndex(0)
                self.RNAtabWidget.setTabEnabled(1, False)

            if self.SampletablelineEdit.text() == '':
                self.SampletableErrortextRNA.show()
                self.SampletableErrortextRNA.setText("Input Sample Table!")
                self.RNAtabWidget.setCurrentIndex(0)
                self.RNAtabWidget.setTabEnabled(1, False)
            elif not os.path.exists(self.SampletablelineEdit.text()):
                self.SampletableErrortextRNA.show()
                self.SampletableErrortextRNA.setText("File doesn't exist! Check the path!")
                self.RNAtabWidget.setCurrentIndex(0)
                self.RNAtabWidget.setTabEnabled(1, False)
            elif os.path.splitext(self.SampletablelineEdit.text())[-1] != ".tsv":
                self.SampletableErrortextRNA.show()
                self.SampletableErrortextRNA.setText("File should have extension '.tsv'")
                self.RNAtabWidget.setCurrentIndex(0)
                self.RNAtabWidget.setTabEnabled(1, False)
            else:
                list_tsv_col = ['sample', 'unit', 'condition', 'fq1', 'fq2']
                unitsdf =pd.read_table(self.SampletablelineEdit.text(), header=0)
                if list(unitsdf) != list_tsv_col:
                    self.SampletableErrortextRNA.show()
                    self.SampletableErrortextRNA.setText("Table not in given format! Check!")
                else:
                    subprocess.run(["python", "rename.py"])
                    if os.path.exists("rename_check.txt"):
                        with open('rename_check.txt') as errorcheck:
                            content = errorcheck.readline()
                        self.SampletableErrortextRNA.show()
                        self.SampletableErrortextRNA.setText(content.rstrip())
                        
                    else:
                        pass

            if self.FastalineEdit.text() == '':
                self.FastaErrortextRNA.show()
                self.FastaErrortextRNA.setText("Input Fasta file!")
                self.RNAtabWidget.setCurrentIndex(0)
                self.RNAtabWidget.setTabEnabled(1, False)
            elif not os.path.exists(self.FastalineEdit.text()):
                self.FastaErrortextRNA.show()
                self.FastaErrortextRNA.setText("File doesn't exist! Check the path!")
                self.RNAtabWidget.setCurrentIndex(0)
                self.RNAtabWidget.setTabEnabled(1, False)
            elif os.path.splitext(self.FastalineEdit.text())[-1] != ".fa":
                self.FastaErrortextRNA.show()
                self.FastaErrortextRNA.setText("File should have extension '.fa'")
                self.RNAtabWidget.setCurrentIndex(0)
                self.RNAtabWidget.setTabEnabled(1, False)

            if self.AnnotatedlineEditRNA.text()== '':
                self.AnnotatedErrortextRNA.show()
                self.AnnotatedErrortextRNA.setText("Input Annotated file!")
                self.RNAtabWidget.setCurrentIndex(0)
                self.RNAtabWidget.setTabEnabled(1, False)
            elif not os.path.exists(self.AnnotatedlineEditRNA.text()):
                self.AnnotatedErrortextRNA.show()
                self.AnnotatedErrortextRNA.setText("File doesn't exist! Check the path!")
                self.RNAtabWidget.setCurrentIndex(0)
                self.RNAtabWidget.setTabEnabled(1, False)
            elif os.path.splitext(self.AnnotatedlineEditRNA.text())[-1] != ".gtf":
                self.AnnotatedErrortextRNA.show()
                self.AnnotatedErrortextRNA.setText("File should have extension '.gtf'")
                self.RNAtabWidget.setCurrentIndex(0)
                self.RNAtabWidget.setTabEnabled(1, False)

            if self.CorelineEditRNA.text()=='':
                self.CoreErrortextRNA.show()
                self.CoreErrortextRNA.setText("Input number of threads available")
                self.RNAtabWidget.setCurrentIndex(0)
                self.RNAtabWidget.setTabEnabled(1, False)
            elif not self.CorelineEditRNA.text().isnumeric():
#                print("File doesn't exist! Check the path!")
                self.CoreErrortextRNA.show()
                self.CoreErrortextRNA.setText("Number of threads should be an integer")
                self.RNAtabWidget.setCurrentIndex(0)
                self.RNAtabWidget.setTabEnabled(1, False)
            elif (os.path.splitext(self.FastalineEdit.text())[-1] == ".fa" and list(unitsdf) == list_tsv_col  and not os.path.exists('name_check.txt') and not os.path.exists('rename_check.txt') and os.path.splitext(self.AnnotatedlineEditRNA.text())[-1] == ".gtf" and self.CorelineEditDNA.text().isnumeric()):
                self.FastaErrortextRNA.hide()
                self.SampleFolderErrortextRNA.hide()
                self.SampletableErrortextRNA.hide()
                self.AnnotatedErrortextRNA.hide()
                self.RNAtabWidget.setCurrentIndex(1)
                self.RNAtabWidget.setTabEnabled(1, True)
                self.textBrowser.setTextColor(self._colors['blue'])
                self.textBrowser.append("Click on the 'View Quality control Results' button below to view the FastQC report \n")

        
    def on_clicked_nextbuttonqcRNA(self):
        self.param_display_rna()
        if os.path.exists("results/fastqc"):
            self.RNAtabWidget.setCurrentIndex(2)
            self.RNAtabWidget.setTabEnabled(2, True)
        else:
            self.qc_warning = showQCDialog()
            if self.qc_warning.returnValue==QMessageBox.Yes:
                self.RNAtabWidget.setCurrentIndex(2)
                self.RNAtabWidget.setTabEnabled(2, True)
                                         
            if self.qc_warning.returnValue== QMessageBox.Cancel:
                self.RNAtabWidget.setCurrentIndex(1)
                self.RNAtabWidget.setTabEnabled(2, False)
                
        self.RNAtabWidget.setTabEnabled(2, True)
    def on_clicked_nextbuttontoolRNA(self):
        self.index_warning_rna()
        self.create_snakefile_rna()
        self.create_config_rna()
        self.textBrowser.setTextColor(self._colors['blue'])
        self.textBrowser.append("Click on the 'Run' button below to start your analysis \n")
        
        self.RNAtabWidget.setCurrentIndex(3)
        self.RNAtabWidget.setTabEnabled(3, True)
        
    def param_display_rna(self):
        _translate = QtCore.QCoreApplication.translate
        self.StarIndexlabel.setText(_translate("MainWindow", "Index for " + self.AlignercomboBoxRNA.currentText()))
        self.StarIndexlineEdit.setToolTip(_translate("MainWindow", "Input the path of the Index for" + self.AlignercomboBoxRNA.currentText()))
        path_aligner_rna = './params/'+self.AlignercomboBoxRNA.currentText()+'.csv'
        path_em = './params/'+self.EMcomboBoxRNA.currentText()+'.csv'
        path_de = './params/'+self.DEcomboBoxRNA.currentText()+'.csv'

        dataframe = pd.read_csv(path_aligner_rna, header=0) # specifying that the table has column names
        essential = dataframe[dataframe["Essential"] == "yes"]
        
        number_of_essential = len(essential) # returns number of essential parameters
        label_array_param1 = [self.param1_label_rna_1, self.param1_label_rna_2, self.param1_label_rna_3, self.param1_label_rna_4, self.param1_label_rna_5, self.param1_label_rna_6]
        line_edit_array_param1 = [self.param1_lineEdit_rna_1,self.param1_lineEdit_rna_2, self.param1_lineEdit_rna_3, self.param1_lineEdit_rna_4, self.param1_lineEdit_rna_5, self.param1_lineEdit_rna_6]
        for i, j, k in zip(range(number_of_essential), label_array_param1, line_edit_array_param1): 
            j.show()
            j.setText(essential.iloc[i, 2])
            k.show()
            k.setText(str(essential.iloc[i, 4]))
            
        dataframe_em = pd.read_csv(path_em, header=0) # specifying that the table has column names
        essential_em = dataframe_em[dataframe_em["Essential"] == "yes"]
        
        number_of_essential_em = len(essential_em) # returns number of essential parameters
        label_array_param2 = [self.param2_label_rna_1, self.param2_label_rna_2, self.param2_label_rna_3, self.param2_label_rna_4, self.param2_label_rna_5, self.param2_label_rna_6]
        line_edit_array_param2 = [self.param2_lineEdit_rna_1,self.param2_lineEdit_rna_2, self.param2_lineEdit_rna_3, self.param2_lineEdit_rna_4, self.param2_lineEdit_rna_5, self.param2_lineEdit_rna_6]
        for i, j, k in zip(range(number_of_essential_em), label_array_param2, line_edit_array_param2): 
            j.show()
            j.setText(essential_em.iloc[i, 2])
            k.show()
            k.setText(str(essential_em.iloc[i, 4]))
            
        dataframe_de = pd.read_csv(path_de, header=0) # specifying that the table has column names
        essential_de = dataframe_de[dataframe_de["Essential"] == "yes"]
        
        number_of_essential_de = len(essential_de) # returns number of essential parameters
        label_array_param3 = [self.param3_label_rna_1, self.param3_label_rna_2, self.param3_label_rna_3, self.param3_label_rna_4, self.param3_label_rna_5, self.param3_label_rna_6]
        line_edit_array_param3 = [self.param3_lineEdit_rna_1,self.param3_lineEdit_rna_2, self.param3_lineEdit_rna_3, self.param3_lineEdit_rna_4, self.param3_lineEdit_rna_5, self.param3_lineEdit_rna_6]
        for i, j, k in zip(range(number_of_essential_de), label_array_param3, line_edit_array_param3): 
            j.show()
            j.setText(essential_de.iloc[i, 2])
            k.show()
            k.setText(str(essential_de.iloc[i, 4]))
            
        
        
    def index_warning_rna(self):
        if self.StarIndexlineEdit.text()=='':
            self.StarIndexErrortext.show()
            self.StarIndexErrortext.setText("Please input index path!")
            self.RNAtabWidget.setCurrentIndex(3)
            self.RNAtabWidget.setTabEnabled(4, False)
        elif not os.path.exists(self.StarIndexlineEdit.text()):
            self.StarIndexErrortext.show()
            self.StarIndexErrortext.setText("File doesn't exist! Please check the path!")
            self.RNAtabWidget.setCurrentIndex(3)
            self.RNAtabWidget.setTabEnabled(4, False)

        else:
            self.RNAtabWidget.setCurrentIndex(4)
            self.RNAtabWidget.setTabEnabled(4, True)

    def on_clicked_nextbuttonparamsRNA(self):

        
        self.essential_dict_aligner_rna = self.get_essential(path ='./params/'+self.AlignercomboBoxRNA.currentText()+'.csv', essential_line_edit_array= [self.param1_lineEdit_rna_1,self.param1_lineEdit_rna_2, self.param1_lineEdit_rna_3, self.param1_lineEdit_rna_4, self.param1_lineEdit_rna_5, self.param1_lineEdit_rna_6] )
        with open('aligner_params_rna.txt', 'w') as aligner_params_rna:
            aligner_params_rna.write(self.AlignercomboBoxRNA.currentText() + " : '")
            for k, v in self.essential_dict_aligner_rna.items():
                aligner_params_rna.write(k +' '+ str(v) + " ")
            aligner_params_rna.write("'")
            aligner_params_rna.close()
        self.essential_dict_em = self.get_essential(path ='./params/'+self.EMcomboBoxRNA.currentText()+'.csv', essential_line_edit_array =[self.param2_lineEdit_rna_1,self.param2_lineEdit_rna_2, self.param2_lineEdit_rna_3, self.param2_lineEdit_rna_4, self.param2_lineEdit_rna_5, self.param2_lineEdit_rna_6])
        with open('em_params.txt', 'w') as em_params:
            em_params.write(self.EMcomboBoxRNA.currentText() + " : '")
            for k, v in self.essential_dict_em.items():
                em_params.write(k +' '+ str(v) + " ")
            em_params.write("'")
            em_params.close()
        self.essential_dict_de = self.get_essential(path ='./params/'+self.DEcomboBoxRNA.currentText()+'.csv', essential_line_edit_array=[self.param3_lineEdit_rna_1,self.param3_lineEdit_rna_2, self.param3_lineEdit_rna_3, self.param3_lineEdit_rna_4, self.param3_lineEdit_rna_5, self.param3_lineEdit_rna_6] )
        with open('de_params.txt', 'w') as de_params:
            de_params.write(self.DEcomboBoxRNA.currentText() + " : '")
            for k, v in self.essential_dict_de.items():
                de_params.write(k +' '+ str(v) + " ")
            de_params.write("'")
            de_params.close()
    def on_clicked_previousbuttonqcRNA(self):
        self.RNAtabWidget.setCurrentIndex(0)
        self.RNAtabWidget.setTabEnabled(6, True)
    def on_clicked_previousbuttontoolRNA(self):
        self.RNAtabWidget.setCurrentIndex(1)
        self.RNAtabWidget.setTabEnabled(1, True)
    def on_clicked_previousbuttonindexRNA(self):
        self.RNAtabWidget.setCurrentIndex(2)
        self.RNAtabWidget.setTabEnabled(2, True)
    def on_clicked_previousbuttonparamsRNA(self):
        self.RNAtabWidget.setCurrentIndex(3)
        self.RNAtabWidget.setTabEnabled(3, True)
        
    def on_clicked_previousbuttonrunRNA(self):
        self.RNAtabWidget.setCurrentIndex(2)       
        self.RNAtabWidget.setTabEnabled(2, True)
    
    def on_clicked_previousbuttonresultRNA(self):
        self.RNAtabWidget.setCurrentIndex(3)       
        self.RNAtabWidget.setTabEnabled(3, True)
    

        
    def show_dag(self):
        with open("Snakefile", "r+") as snake:
            line= snake.readline()
            if '"rules/common_dna.smk"' in line:
                svg_filename = self.AlignercomboBoxDNA.currentText() + self.VCcomboBoxDNA.currentText() + self.AnnotatorcomboBoxDNA.currentText() + ".svg"
            else:
                svg_filename = self.AlignercomboBoxRNA.currentText() + self.EMcomboBoxRNA.currentText() + self.DEcomboBoxRNA.currentText() + ".svg"
        if os.path.exists(svg_filename):
            self.diag = SVGDialog(svg_filename)
            self.diag.show()
        else:
            self.textBrowser.setTextColor(self._colors['red'])
            self.textBrowser.append("Error creating DAG!")
        
    

    
                
    def advanced_aligner(self):
        path = './params/'+self.AlignercomboBoxDNA.currentText()+'.csv'
        self.adv_dialog = AdvancedDialog(path)
        self.adv_dialog.show()
        retval = self.adv_dialog.exec_
        self.adv_dialog.button.accepted.connect(self.close_and_write_aligner)
        
        
        
    def close_and_write_aligner(self):

        self.snakefile_dict_aligner_int = self.get_additional_int(path='./params/'+self.AlignercomboBoxDNA.currentText()+'.csv')
        self.snakefile_dict_aligner_float = self.get_additional_float(path='./params/'+self.AlignercomboBoxDNA.currentText()+'.csv')
        self.snakefile_dict_aligner_str = self.get_additional_str(path='./params/'+self.AlignercomboBoxDNA.currentText()+'.csv')
        self.snakefile_dict_aligner_na = self.get_additional_na(path='./params/'+self.AlignercomboBoxDNA.currentText()+'.csv')
        self.essential_dict_aligner = self.get_essential(path ='./params/'+self.AlignercomboBoxDNA.currentText()+'.csv', essential_line_edit_array= [self.param1_lineEdit_dna_1,self.param1_lineEdit_dna_2, self.param1_lineEdit_dna_3, self.param1_lineEdit_dna_4, self.param1_lineEdit_dna_5, self.param1_lineEdit_dna_6])
        with open('aligner_params.txt', 'w') as aligner_params:
            aligner_params.write(self.AlignercomboBoxDNA.currentText() + " : '")
            for k, v in self.snakefile_dict_aligner_int.items():
                aligner_params.write( k +''+ str(v) +" " )
            for k, v in self.snakefile_dict_aligner_float.items():
                aligner_params.write( k +''+ str(v) +" " )
            for k, v in self.snakefile_dict_aligner_str.items():
                aligner_params.write( k +''+ str(v) +" " )
            for k, v in self.snakefile_dict_aligner_na.items():
                aligner_params.write( k +' ')
            for k, v in self.essential_dict_aligner.items():
                aligner_params.write(k +''+ str(v) + " ")
            aligner_params.write("'")
            aligner_params.close()
            
        self.adv_dialog.close()
        
    def advanced_vc(self):
        path = './params/'+self.VCcomboBoxDNA.currentText()+'.csv'
        self.adv_dialog = AdvancedDialog(path)
        self.adv_dialog.show()
        retval = self.adv_dialog.exec_
        self.adv_dialog.button.accepted.connect(self.close_and_write_vc)
        
    def close_and_write_vc(self):

        self.snakefile_dict_vc_int = self.get_additional_int(path='./params/'+self.VCcomboBoxDNA.currentText()+'.csv')
        self.snakefile_dict_vc_float = self.get_additional_float(path='./params/'+self.VCcomboBoxDNA.currentText()+'.csv')
        self.snakefile_dict_vc_str = self.get_additional_str(path='./params/'+self.VCcomboBoxDNA.currentText()+'.csv')
        self.snakefile_dict_vc_na = self.get_additional_na(path='./params/'+self.VCcomboBoxDNA.currentText()+'.csv')
        self.essential_dict_vc = self.get_essential(path ='./params/'+self.VCcomboBoxDNA.currentText()+'.csv', essential_line_edit_array= [self.param2_lineEdit_dna_1,self.param2_lineEdit_dna_2, self.param2_lineEdit_dna_3, self.param2_lineEdit_dna_4, self.param2_lineEdit_dna_5, self.param2_lineEdit_dna_6])
        with open('vc_params.txt', 'w') as vc_params:
            vc_params.write(self.VCcomboBoxDNA.currentText() + " : '")
            for k, v in self.snakefile_dict_vc_int.items():
                vc_params.write( k +''+ str(v) +" " )
            for k,v in self.snakefile_dict_vc_float.items():
                vc_params.write( k +''+ str(v) +" " )
            for k,v in self.snakefile_dict_vc_str.items():
                vc_params.write( k +''+ str(v) +" " )
            for k,v in self.snakefile_dict_vc_na.items():
                vc_params.write( k +' ')
            for k, v in self.essential_dict_vc.items():
                vc_params.write(k +''+ str(v) + " ")
            vc_params.write("'")
            vc_params.close()
            
        self.adv_dialog.close()
        
    def advanced_annotator(self):
        path = './params/'+self.AnnotatorcomboBoxDNA.currentText()+'.csv'
        self.adv_dialog = AdvancedDialog(path)
        self.adv_dialog.show()
        retval = self.adv_dialog.exec_
        self.adv_dialog.button.accepted.connect(self.close_and_write_annotator)
        
    def close_and_write_annotator(self):

        self.snakefile_dict_annotator_int = self.get_additional_int(path='./params/'+self.AnnotatorcomboBoxDNA.currentText()+'.csv')
        self.snakefile_dict_annotator_float = self.get_additional_float(path='./params/'+self.AnnotatorcomboBoxDNA.currentText()+'.csv')
        self.snakefile_dict_annotator_str = self.get_additional_str(path='./params/'+self.AnnotatorcomboBoxDNA.currentText()+'.csv')
        self.snakefile_dict_annotator_na = self.get_additional_na(path='./params/'+self.AnnotatorcomboBoxDNA.currentText()+'.csv')
        self.essential_dict_annotator = self.get_essential(path ='./params/'+self.AnnotatorcomboBoxDNA.currentText()+'.csv', essential_line_edit_array= [self.param3_lineEdit_dna_1,self.param3_lineEdit_dna_2, self.param3_lineEdit_dna_3, self.param3_lineEdit_dna_4, self.param3_lineEdit_dna_5, self.param3_lineEdit_dna_6])
        with open('annotator_params.txt', 'w') as annotator_params:
            if self.AnnotatorcomboBoxDNA.currentText() == "SnpEff":
                annotator_params.write(self.AnnotatorcomboBoxDNA.currentText() + " : '-Xmx4g ")
            else:
                annotator_params.write(self.AnnotatorcomboBoxDNA.currentText() + " : '")
            for k, v in self.snakefile_dict_annotator_int.items():
                annotator_params.write( k +' '+ str(v) +" " )
            for k, v in self.snakefile_dict_annotator_float.items():
                annotator_params.write( k +' '+ str(v) +" " )
            for k, v in self.snakefile_dict_annotator_str.items():
                annotator_params.write( k +' '+ str(v) +" " )
            for k, v in self.snakefile_dict_annotator_na.items():
                annotator_params.write( k +' ' )
            for k, v in self.essential_dict_annotator.items():
                annotator_params.write(k +''+ str(v) + " ")
            annotator_params.write("'")
            annotator_params.close()
            
        self.adv_dialog.close()
        
    def advanced_aligner_rna(self):
        path = './params/'+self.AlignercomboBoxRNA.currentText()+'.csv'
        self.adv_dialog = AdvancedDialog(path)
        self.adv_dialog.show()
        retval = self.adv_dialog.exec_
        self.adv_dialog.button.accepted.connect(self.close_and_write_aligner_rna)
        
    def close_and_write_aligner_rna(self):

        self.snakefile_dict_aligner_rna_int = self.get_additional_int(path='./params/'+self.AlignercomboBoxRNA.currentText()+'.csv')
        self.snakefile_dict_aligner_rna_float = self.get_additional_float(path='./params/'+self.AlignercomboBoxRNA.currentText()+'.csv')
        self.snakefile_dict_aligner_rna_str = self.get_additional_str(path='./params/'+self.AlignercomboBoxRNA.currentText()+'.csv')
        self.snakefile_dict_aligner_rna_na = self.get_additional_na(path='./params/'+self.AlignercomboBoxRNA.currentText()+'.csv')
        self.essential_dict_aligner_rna = self.get_essential(path ='./params/'+self.AlignercomboBoxRNA.currentText()+'.csv', essential_line_edit_array= [self.param1_lineEdit_rna_1,self.param1_lineEdit_rna_2, self.param1_lineEdit_rna_3, self.param1_lineEdit_rna_4, self.param1_lineEdit_rna_5, self.param1_lineEdit_rna_6])
        with open('aligner_params_rna.txt', 'w') as aligner_params_rna:
            aligner_params_rna.write(self.AlignercomboBoxRNA.currentText() + " : '")
            for k, v in self.snakefile_dict_aligner_rna_int.items():
                aligner_params_rna.write( k +''+ str(v) +" " )
            for k, v in self.snakefile_dict_aligner_rna_float.items():
                aligner_params_rna.write( k +''+ str(v) +" " )
            for k, v in self.snakefile_dict_aligner_rna_str.items():
                aligner_params_rna.write( k +''+ str(v) +" " )
            for k, v in self.snakefile_dict_aligner_rna_na.items():
                aligner_params_rna.write( k +' ')
            for k, v in self.essential_dict_aligner_rna.items():
                aligner_params_rna.write(k +''+ str(v) + " ")
            aligner_params_rna.write("'")
            aligner_params_rna.close()
        

            
        self.adv_dialog.close()
        
    def advanced_em(self):
        path = './params/'+self.EMcomboBoxRNA.currentText()+'.csv'
        self.adv_dialog = AdvancedDialog(path)
        self.adv_dialog.show()
        retval = self.adv_dialog.exec_
        self.adv_dialog.button.accepted.connect(self.close_and_write_em)
        
    def close_and_write_em(self):

        self.snakefile_dict_em_int = self.get_additional_int(path='./params/'+self.EMcomboBoxRNA.currentText()+'.csv')
        self.snakefile_dict_em_float = self.get_additional_float(path='./params/'+self.EMcomboBoxRNA.currentText()+'.csv')
        self.snakefile_dict_em_str = self.get_additional_str(path='./params/'+self.EMcomboBoxRNA.currentText()+'.csv')
        self.snakefile_dict_em_na = self.get_additional_na(path='./params/'+self.EMcomboBoxRNA.currentText()+'.csv')
        self.essential_dict_em = self.get_essential(path ='./params/'+self.EMcomboBoxRNA.currentText()+'.csv', essential_line_edit_array= [self.param2_lineEdit_rna_1,self.param2_lineEdit_rna_2, self.param2_lineEdit_rna_3, self.param2_lineEdit_rna_4, self.param2_lineEdit_rna_5, self.param2_lineEdit_rna_6])
        with open('em_params.txt', 'w') as em_params:
            em_params.write(self.EMcomboBoxRNA.currentText() + " : '")
            for k, v in self.snakefile_dict_em_int.items():
                em_params.write( k +''+ str(v) +" " )
            for k, v in self.snakefile_dict_em_float.items():
                em_params.write( k +''+ str(v) +" " )
            for k, v in self.snakefile_dict_em_str.items():
                em_params.write( k +''+ str(v) +" " )
            for k, v in self.snakefile_dict_em_na.items():
                em_params.write( k +' ')
            for k, v in self.essential_dict_em.items():
                em_params.write(k +''+ str(v) + " ")
            em_params.write("'")
            em_params.close()
            
        self.adv_dialog.close()
        
    def advanced_de(self):
        path = './params/'+self.DEcomboBoxRNA.currentText()+'.csv'
        self.adv_dialog = AdvancedDialog(path)
        self.adv_dialog.show()
        retval = self.adv_dialog.exec_
        self.adv_dialog.button.accepted.connect(self.close_and_write_de)
        
    def close_and_write_de(self):

        self.snakefile_dict_de_int = self.get_additional_int(path='./params/'+self.DEcomboBoxRNA.currentText()+'.csv')
        self.snakefile_dict_de_float = self.get_additional_float(path='./params/'+self.DEcomboBoxRNA.currentText()+'.csv')
        self.snakefile_dict_de_str = self.get_additional_str(path='./params/'+self.DEcomboBoxRNA.currentText()+'.csv')
        self.snakefile_dict_de_na = self.get_additional_na(path='./params/'+self.DEcomboBoxRNA.currentText()+'.csv')
        self.essential_dict_de = self.get_essential(path ='./params/'+self.DEcomboBoxRNA.currentText()+'.csv', essential_line_edit_array= [self.param3_lineEdit_rna_1,self.param3_lineEdit_rna_2, self.param3_lineEdit_rna_3, self.param3_lineEdit_rna_4, self.param3_lineEdit_rna_5, self.param3_lineEdit_rna_6])
        with open('de_params.txt', 'w') as de_params:
            de_params.write(self.DEcomboBoxRNA.currentText() + " : '")
            for k, v in self.snakefile_dict_de_int.items():
                de_params.write( k +''+ str(v) +" " )
            for k, v in self.snakefile_dict_de_float.items():
                de_params.write( k +''+ str(v) +" " )
            for k, v in self.snakefile_dict_de_str.items():
                de_params.write( k +''+ str(v) +" " )
            for k, v in self.snakefile_dict_de_na.items():
                de_params.write( k +' ')
            for k, v in self.essential_dict_de.items():
                de_params.write(k +''+ str(v) + " ")
            de_params.write("'")
            de_params.close()
            
        self.adv_dialog.close()
    
    def check_run_button(self):
        if self.one_passed == self.two_passed is True:
            self.RunButton.setEnabled(True)
            self.RunLabel.setEnabled(True)
            

    def on_check_SamplesNo_dna(self,is_toggle):
        if is_toggle:
            self.UnitsFilelabelDNA.setEnabled(True)
            self.UnitslineEditDNA.setEnabled(True)
            self.UnitsBrowseButtonDNA.setEnabled(True)
            self.SampleFilelabelDNA.setEnabled(False)
            self.SampleslineEditDNA.setEnabled(False)
            self.SamplesBrowseButtonDNA.setEnabled(False)
        else:
            self.UnitsFilelabelDNA.setEnabled(False)
            self.UnitslineEditDNA.setEnabled(False)
            self.UnitsBrowseButtonDNA.setEnabled(False)
            self.SampleFilelabelDNA.setEnabled(True)
            self.SampleslineEditDNA.setEnabled(True)
            self.SamplesBrowseButtonDNA.setEnabled(True)
            
    def on_check_SamplesNo_rna(self,is_toggle):
        if is_toggle:
            self.Sampletablelabel.setEnabled(True)
            self.SampletablelineEdit.setEnabled(True)
            self.SampletableBrowseButton.setEnabled(True)
#==============================================================================
            self.SampleFolderlabel.setEnabled(False)
            self.SampleFolderLineEdit.setEnabled(False)
            self.SampleFolderBrowseButton.setEnabled(False)
#==============================================================================
        else:
            self.Sampletablelabel.setEnabled(False)
            self.SampletablelineEdit.setEnabled(False)
            self.SampletableBrowseButton.setEnabled(False)
#==============================================================================
            self.SampleFolderlabel.setEnabled(True)
            self.SampleFolderLineEdit.setEnabled(True)
            self.SampleFolderBrowseButton.setEnabled(True)
#==============================================================================

    def on_check_QC_dna(self,is_toggle):
        if is_toggle:
            self.InputParamslabel.setEnabled(True)
            self.Cutadaptlabel.setEnabled(True)
            self.CutadaptlineEdit.setEnabled(True)
            self.RunQCpushButton.setEnabled(True)
        else:
            self.InputParamslabel.setEnabled(False)
            self.Cutadaptlabel.setEnabled(False)
            self.CutadaptlineEdit.setEnabled(False)
            self.RunQCpushButton.setEnabled(False)

    def on_check_QC_rna(self,is_toggle):
        if is_toggle:
            self.InputParamslabel_rna.setEnabled(True)
            self.Cutadaptlabel_rna.setEnabled(True)            
            self.CutadaptlineEdit_rna.setEnabled(True)
            self.RunQCpushButton_rna.setEnabled(True)
        else:
            self.InputParamslabel_rna.setEnabled(False)
            self.Cutadaptlabel_rna.setEnabled(False)
            self.CutadaptlineEdit_rna.setEnabled(False)

            self.RunQCpushButton_rna.setEnabled(False)


    def browse_data_sampletable(self):
        if os.path.exists('rename_check.txt'):
            os.remove('rename_check.txt')
        else:
            pass
        self.SampletableErrortextRNA.hide()
        data_path_sampletable, _ =QtWidgets.QFileDialog.getOpenFileName(None,'Open File',r"",'*.tsv')
        self.SampletablelineEdit.setText(data_path_sampletable)
        with open('data_path_sampletable.pickle', 'wb') as handle:
            pickle.dump(data_path_sampletable,handle,protocol=pickle.HIGHEST_PROTOCOL)

    def browse_data_fasta(self):
        self.FastaErrortextRNA.hide()
        data_path_fasta, _ =QtWidgets.QFileDialog.getOpenFileName(None,'Open File',r"",'*.fa *.fa.gz')
        self.FastalineEdit.setText(data_path_fasta)
        with open('data_path_fasta.pickle', 'wb') as handle:
            pickle.dump(data_path_fasta,handle,protocol=pickle.HIGHEST_PROTOCOL)

    def browse_data_annotated(self):
        self.AnnotatedErrortextRNA.hide()
        data_path_annotated, _ =QtWidgets.QFileDialog.getOpenFileName(None,'Open File',r"",'*.gtf *.gtf.gz')
        self.AnnotatedlineEditRNA.setText(data_path_annotated)
        with open('data_path_annotated.pickle', 'wb') as handle:
            pickle.dump(data_path_annotated,handle,protocol=pickle.HIGHEST_PROTOCOL)


            
    def browse_samples_folder(self):
        self.SampleFolderErrortextRNA.hide()
        if os.path.exists("name_check.txt"):
            os.remove("name_check.txt")
        else:
            pass
        my_dir_sample = QtWidgets.QFileDialog.getExistingDirectory(
        None,
        "Open a folder")
        self.SampleFolderLineEdit.setText(my_dir_sample)
        

    def browse_data_samples(self):

        self.SamplesErrortextDNA.hide()
        if os.path.exists("name_check.txt"):
            os.remove("name_check.txt")
        else:
            pass
        my_dir_sample = QtWidgets.QFileDialog.getExistingDirectory(
        None,
        "Open a folder")
        self.SampleslineEditDNA.setText(my_dir_sample)

    def browse_data_units(self):
        self.UnitsErrortextDNA.hide()
        data_path_units, _ =QtWidgets.QFileDialog.getOpenFileName(None,'Open File',r"",'*.tsv')
        self.UnitslineEditDNA.setText(data_path_units)
        with open('data_path_units.pickle', 'wb') as handle:
            pickle.dump(data_path_units,handle,protocol=pickle.HIGHEST_PROTOCOL)


        
    def browse_data_ref(self):

        self.RefGenomeErrortextDNA.hide()
        data_path_ref, _ =QtWidgets.QFileDialog.getOpenFileName(None,'Open File',r"",'*.fa *.fa.gz')
        self.RefGenomelineEditDNA.setText(data_path_ref)
        with open('data_path_ref.pickle', 'wb') as handle:
            pickle.dump(data_path_ref,handle,protocol=pickle.HIGHEST_PROTOCOL)

    def browse_data_kv(self):
        self.RefVariantErrortextDNA.hide()
        data_path_kv, _ =QtWidgets.QFileDialog.getOpenFileName(None,'Open File',r"",'*.gz')
        self.RefVariantlineEditDNA.setText(data_path_kv)
        with open('data_path_kv.pickle', 'wb') as handle:
            pickle.dump(data_path_kv,handle,protocol=pickle.HIGHEST_PROTOCOL)

    def browse_bwaindex_dna(self):
        self.BWAIndexErrortext.hide()
        self._set_color(self._colors['blue'].name(),pb =self.progressBar_sub2_dna)
        data_path_bwadna, _ =QtWidgets.QFileDialog.getOpenFileName(None,'Open File')
        self.BWAIndexlineEdit.setText(data_path_bwadna)
        with open('data_path_bwadna.pickle', 'wb') as handle:
            pickle.dump(data_path_bwadna,handle,protocol=pickle.HIGHEST_PROTOCOL)


    def browse_data_maf(self):
        data_path_maf, _ =QtWidgets.QFileDialog.getOpenFileName(None,'Open File',r"",'*.maf *.maf.gz')
        self.maflineEdit.setText(data_path_maf)
        with open('data_path_maf.pickle', 'wb') as handle:
            pickle.dump(data_path_maf,handle,protocol=pickle.HIGHEST_PROTOCOL)

    def browse_data_vcf(self):
        data_path_vcf, _ =QtWidgets.QFileDialog.getOpenFileName(None,'Open File','./NBDriver_ICOMIC/vcf/','*.vcf *.vcf.gz')
        self.vcflineEdit.setText(data_path_vcf)
        with open('data_path_vcf.pickle', 'wb') as handle:
            pickle.dump(data_path_vcf,handle,protocol=pickle.HIGHEST_PROTOCOL)

    def browse_star_rna(self):
        self.StarIndexErrortext.hide()
        self._set_color(self._colors['blue'].name(),pb =self.progressBar_sub2_rna)
        my_dir_star = QtWidgets.QFileDialog.getExistingDirectory(
        None,
        "Open a folder")
        self.StarIndexlineEdit.setText(my_dir_star)


        
    def _set_color(self, color, pb):
        pb.setStyleSheet("""
            QProgressBar {{
                color: black;
                border: 2px solid grey;
                margin: 2px;
                border-radius: 5px;
                text-align: center;
            }}
            QProgressBar::chunk {{
                background: {};
                }}""".format(color))
    def _set_pb_color_sub(self, color, pb):
        self._set_color(self, color, pb )
    def _set_pb2_color_dna(self, color):
        self._set_color(self, color, pb = self.progressBar_sub2_dna)
    def _set_pb1_color_rna(self, color):
        self._set_color(self, color, pb=self.progressBar_sub1_rna)
    def _set_pb2_color_rna(self, color):
        self._set_color(self, color, pb=self.progressBar_sub2_rna)
        
    def func_pb_update(self, sub_pb, sub_pb_frac, initial_sub, initial_main, error_icon):
        time.sleep(2)
        files = glob.glob('.snakemake/log/*.log')
        filename_=max(files , key = os.path.getctime)
        f = open(filename_, 'r')
        while True:
            line = ''
            while len(line) == 0 or line[-1] != '\n':
                tail = f.readline()
                if tail == '':
                    break
                line += tail
                self.textBrowser.append(line)
                if '%' in line:
                    self.textBrowser.setTextColor(self._colors['black'])
                    per = line.split('(', 1)[1].split(')')[0]
                    percent = per[:-1]
                    sub_pb.setValue(initial_sub + int(percent)/sub_pb_frac)
                elif 'Error: Directory cannot be locked' in line:
                    self._set_color(self._colors['red'].name(),pb =sub_pb)
                    self.textBrowser.setTextColor(self._colors['red'])
                    self.textBrowser.append(line)
                    break
                    subprocess.run(["snakemake", "--unlock"])

                elif 'CalledProcessError' in line:
                    self._set_color(self._colors['red'].name(),pb =sub_pb)
                    self.textBrowser.setTextColor(self._colors['red'])
                    break
                elif 'WorkflowError' in line:
                    self._set_color(self._colors['red'].name(),pb =sub_pb)
                    self.textBrowser.setTextColor(self._colors['red'])
                    break
                elif 'Error' in line:
                    self._set_color(self._colors['red'].name(),pb =sub_pb)
                    self.textBrowser.setTextColor(self._colors['red'])
                    break
                elif 'Missing' in line:
                    print(line)
                    self._set_color(self._colors['red'].name(),pb =sub_pb)
                    self.textBrowser.setTextColor(self._colors['red'])
                    error_icon.show()
                    error_icon.setToolTip("Missing input file! Check the inputs")
                    break
                elif '(100%) done' in line:
                    self.textBrowser.setTextColor(self._colors['black'])
                    sub_pb.setValue(initial_sub + 100/sub_pb_frac)
                elif 'Nothing to be done' in line:
                    self.textBrowser.setTextColor(self._colors['black'])
                    sub_pb.setValue(initial_sub + 100/sub_pb_frac)
                    break
                else:
                    pass
            if ('Complete log' in line):
                break
            elif 'Missing' in line:
                self._set_color(self._colors['red'].name(),pb =sub_pb)
                break
            elif 'Exiting' in line:
                self._set_color(self._colors['red'].name(),pb =sub_pb)
                break
            
    def show_qc_textbox(self):
        subprocess.run(["snakemake", "--unlock", "-j", "1"])
        self.textBrowser.setTextColor(self._colors['black'])
        self.textBrowser.append("QC Results being generated. Please wait! \n")

    def show_qc_results(self):
        self.progressBar_sub1_dna.setValue(1)
        self.textBrowser.setTextColor(self._colors['black'])
        self.nextbuttonqcDNA.setEnabled(True)
        self._set_color(self._colors['blue'].name(),pb =self.progressBar_sub1_dna)
        conf = open('config.yaml', 'w')
        conf.write('samples: samples.tsv \n')
        conf.write('units: '+ self.UnitslineEditDNA.text() + '\n'+'ref: \n')
        conf.write('  genome: '+ self.RefGenomelineEditDNA.text() + '\n')
        conf.write("processing: \n")
        conf.write("  remove-duplicates: true\n")
        conf.write('threads: ' + self.CorelineEditDNA.text() + '\n')
        conf.close()
        time.sleep(0.1)

        
        snake = open('Snakefile', "w")
        snake.write('include: "rules/common_dna.smk"\n')
        snake.write('rule all:\n')
        snake.write('  input:\n')
        snake.write('    expand("results_dna/qc/fastqc/{u.sample}-{u.unit}-{u.condition}.html", u = units.itertuples()),\n')
        snake.write('    expand("results_dna/qc/fastqc/{u.sample}-{u.unit}-{u.condition}.zip", u = units.itertuples()),\n')
        snake.write('include: "rules/qc_dna.smk"\n')
        snake.close()
        

        
        
        def func_qc():
            subprocess.run(["snakemake", "--use-conda", "--cores", self.CorelineEditDNA.text()])
            
        def multi_qc():
            subprocess.run(["snakemake", "--use-conda", "-s", "Snakefile_multiqc", "--cores", self.CorelineEditDNA.text()])

        self.textBrowser.setTextColor(self._colors['black'])
        p1 = Process(target=func_qc)
        p1.start()
        
        p2 = Process(target=self.func_pb_update( sub_pb=self.progressBar_sub1_dna, sub_pb_frac=4, initial_sub = 0, initial_main=0, error_icon=self.QCresultsButtonErroricon))
        p2.start()
        
        if self.progressBar_sub1_dna.value()==100/4:
            p3 = Process(target=multi_qc)
            self.progressBar_sub1_dna.setValue(26)
            
            p3.start()
            
            p4 = Process(target= self.func_pb_update( sub_pb=self.progressBar_sub1_dna, sub_pb_frac=4, initial_sub = 25, initial_main=0, error_icon=self.QCresultsButtonErroricon))
            p4.start()
            
        if os.path.exists("results_dna/qc/multiqc.html"):
            self.textBrowser.setTextColor(self._colors['blue'])
            self.textBrowser.append("MultiQC results generated! Wait till the result is dispalyed and then proceed to the next tab \n\n")
            filename = "results_dna/qc/multiqc.html"
            webbrowser.get('google-chrome').open(filename, new=0, autoraise=True)
        else:
            pass


    def show_qc_results_rna(self):
        self.progressBar_sub1_rna.setValue(1)
        self.nextbuttonqcRNA.setEnabled(True)
        self._set_color(self._colors['blue'].name(),pb =self.progressBar_sub1_rna)
        self.textBrowser.setTextColor(self._colors['black'])
        self.textBrowser.append("QC Results being generated. Please wait! \n")
        time.sleep(0.1)
        conf = open('config.yaml', 'w')
        conf.write('units: units.tsv \n')
        conf.write('ref: \n')
        conf.write('  annotation: '+ self.AnnotatedlineEditRNA.text() + '\n')
        conf.write('  fasta: '+self.FastalineEdit.text() + '\n')
        conf.write('params: \n')
        conf.write("sample: " + self.SampleFolderLineEdit.text() + "\n")
        conf.write('threads: ' + self.CorelineEditRNA.text() + '\n')
        conf.close()
        time.sleep(0.1)
        self.textBrowser.setTextColor(self._colors['black'])
        self.textBrowser.append("Snakefile created for Quality Check!! \nPlease refer to the file: Snakefile in your working directory. \n\n")
        snakef = open('Snakefile', "w")
        snakef.write('include: "rules/common_rna.smk"\n')
        snakef.write('rule all:\n')
        snakef.write('  input:\n')
        snakef.write("    expand('results/fastqc/{sample}_{condition}_Rep{rep}.html', sample=samples, condition=type, rep=reps),\n")
        snakef.write("    expand('results/fastqc/{sample}_{condition}_Rep{rep}.zip', sample=samples, condition=type, rep=reps),\n")
        snakef.write('include: "rules/qc_rna.smk"\n')
        snakef.close()
        
        time.sleep(0.1)
        
        def func_qc():
            process1 = subprocess.Popen(["snakemake", "--use-conda", "--cores", self.CorelineEditRNA.text()], shell =True,  stdout=subprocess.PIPE)
            output1 = process1.communicate()

        def multi_qc():
            subprocess.run(["snakemake", "--use-conda", "-s", "Snakefile_multiqc_rna", "--cores", self.CorelineEditRNA.text()])
        self.textBrowser.setTextColor(self._colors['black'])
        p1 = Process(target=func_qc)
        p1.start()
        
        p2 = Process(target=self.func_pb_update( sub_pb=self.progressBar_sub1_rna, sub_pb_frac=4, initial_sub = 0, initial_main=0, error_icon=self.QCresultsButtonErroricon_rna))
        p2.start()
        
        if self.progressBar_sub1_rna.value()==100/4:
            p3 = Process(target=multi_qc)
            self.progressBar_sub1_rna.setValue(26)
            p3.start()
            
            p4 = Process(target= self.func_pb_update( sub_pb=self.progressBar_sub1_rna, sub_pb_frac=4, initial_sub = 25, initial_main=0, error_icon=self.QCresultsButtonErroricon_rna))
            p4.start()
        else:
            pass
            
        if os.path.exists("results/fastqc/multiqc.html"):
            self.textBrowser.setTextColor(self._colors['blue'])
            self.textBrowser.append("MultiQC results generated! Proceed to the next tab \n\n")
            filename = "results/fastqc/multiqc.html"
            webbrowser.get('google-chrome').open(filename, new=0, autoraise=True)
        else:
            pass

    def run_qc_textbox(self):
        subprocess.run(["snakemake", "--unlock", "-j", "1"])
        self.textBrowser.setTextColor(self._colors['black'])
        self.textBrowser.append("Running Quality Check!! \n\n")        
    
         
    def run_qc_dna(self, line):
        self.progressBar_sub1_dna.setValue(51)
        self._set_color(self._colors['blue'].name(),pb =self.progressBar_sub1_dna)
        self.textBrowser.setTextColor(self._colors['black'])
        self.textBrowser.append("Config file created for Quality Check!! \nPlease refer to the file: config.yaml in your working directory. \n\n")
        conf = open('config.yaml', 'w')
        conf.write('samples: ./samples.tsv \n')
        conf.write('units: '+ self.UnitslineEditDNA.text() + '\n'+'ref: \n')
        conf.write("  name: " + self.RefNamecomboBoxDNA.currentText() + "\n")
        conf.write('  genome: '+ self.RefGenomelineEditDNA.text() + '\n')
        conf.write('  genome-name: '+ os.path.basename(self.RefGenomelineEditDNA.text()) + '\n')
        conf.write('  known-variants: '+ self.RefVariantlineEditDNA.text() + '\n')
        conf.write("processing: \n")
        conf.write("  remove-duplicates: true\n")
        conf.write('threads: ' + self.CorelineEditDNA.text() + '\n')
        conf.write('params: \n')
        conf.write("  cutadapt: '" + self.CutadaptlineEdit.text() + "' \n")
        conf.close()
        
        time.sleep(0.1)
        self.textBrowser.setTextColor(self._colors['black'])
        self.textBrowser.append("Snakefile created for Quality Check!! \nPlease refer to the file: Snakefile in your working directory. \n\n")
        snake = open('Snakefile', "w")
        snake.write('include: "rules/common_dna.smk"\n')
        snake.write('rule all:\n')
        snake.write('  input:\n')
        snake.write('    expand("results_dna/trimmed/fastqc_after/{u.sample}-{u.unit}-{u.condition}.aftertrim.html", u = units.itertuples()),\n')
        snake.write('    expand("results_dna/trimmed/fastqc_after/{u.sample}-{u.unit}-{u.condition}.aftertrim.zip", u = units.itertuples()) \n')
        snake.write('include: "rules/cutadapt_dna.smk"\n')
        snake.write('include: "rules/fastqc_after_dna.smk"\n')
        snake.close()
        
        time.sleep(0.1)
        
        def func1():
            
            process1 = subprocess.run(["snakemake", "--use-conda", "--cores", self.CorelineEditDNA.text()])
        p1 = Process(target=func1)
        p1.start()
        p2 = Process(target=self.func_pb_update( sub_pb=self.progressBar_sub1_dna, sub_pb_frac=4, initial_sub = 50, initial_main=0, error_icon=self.RunQCButtonErroricon))
        p2.start()
        
        def multi_qc():
            subprocess.run(["snakemake", "--use-conda", "-s", "Snakefile_after", "--cores", self.CorelineEditDNA.text()])
        
        if self.progressBar_sub1_dna.value()==75:
            self.textBrowser.setTextColor(self._colors['black'])
            self.textBrowser.append("Running Quality Check!! \n\n")
            p3 = Process(target=multi_qc)
            self.progressBar_sub1_dna.setValue(76)
            p3.start()
            
            p4 = Process(target= self.func_pb_update( sub_pb=self.progressBar_sub1_dna, sub_pb_frac=4, initial_sub = 75, initial_main=0, error_icon=self.QCresultsButtonErroricon))
            p4.start()
        else:
            pass
            
        if os.path.exists("results_dna/qc/multiqc_after.html"):
            filename = "results_dna/qc/multiqc_after.html"
            webbrowser.get('google-chrome').open(filename, new=0, autoraise=True)
        else:
            pass
            
        

    def run_qc_rna_textbox(self):
        self.textBrowser.setTextColor(self._colors['black'])
        self.textBrowser.append("Running Quality Check!! \n\n")
        subprocess.run(["snakemake", "--unlock", "-j", "1"])

    def run_qc_rna(self, line):
        self.progressBar_sub1_rna.setValue(51)
        self._set_color(self._colors['blue'].name(),pb =self.progressBar_sub1_rna)
        self.textBrowser.setTextColor(self._colors['black'])
        self.textBrowser.append("Config file created for Quality Check!! \nPlease refer to the file: config.yaml in your working directory. \n\n")
        conf = open('config.yaml', 'w')
        conf.write('units: units.tsv \n')
        conf.write('ref: \n')
        conf.write('  annotation: '+ self.AnnotatedlineEditRNA.text() + '\n')
        conf.write('  fasta: '+self.FastalineEdit.text() + '\n')
        conf.write('threads: ' + self.CorelineEditRNA.text() + '\n')
        conf.write('params: \n')
        conf.write("  cutadapt: '" + self.CutadaptlineEdit_rna.text() + "' \n")
        conf.write("sample: " + self.SampleFolderLineEdit.text() + "\n")
        conf.close()
        time.sleep(0.1)
        self.textBrowser.setTextColor(self._colors['black'])
        self.textBrowser.append("Snakefile created for Quality Check!! \nPlease refer to the file: Snakefile in your working directory. \n\n")
        snakef = open('Snakefile', "w")
        snakef.write('include: "rules/common_rna.smk"\n')
        snakef.write('rule all:\n')
        snakef.write('  input:\n')
        snakef.write("    expand('results/cutadapt/fastqc_after/{sample}_{condition}_Rep{rep}.aftertrim.html', sample=samples, condition=type, rep=reps),\n")
        snakef.write("    expand('results/cutadapt/fastqc_after/{sample}_{condition}_Rep{rep}.aftertrim.zip', sample=samples, condition=type, rep=reps),\n")
        snakef.write('include: "rules/cutadapt_rna.smk"\n')
        snakef.write('include: "rules/fastqc_after_rna.smk"\n')
        snakef.close()
        time.sleep(0.1)
        def func_qc_rna():
            
            process2 = subprocess.run(["snakemake", "--use-conda", "--cores", self.CorelineEditRNA.text()])
            output2 = process2.communicate()
        
        p1 = Process(target=func_qc_rna)
        p1.start()
        p2 = Process(target=self.func_pb_update( sub_pb=self.progressBar_sub1_rna, sub_pb_frac=4, initial_sub = 50, initial_main=0, error_icon=self.RunQCButtonErroricon_rna))
        p2.start()  
        
        def multi_qc_rna():
            subprocess.run(["snakemake", "--use-conda", "-s", "Snakefile_after_rna", "--cores", self.CorelineEditRNA.text()])
        
        if self.progressBar_sub1_rna.value()==75:
            self.textBrowser.setTextColor(self._colors['black'])
            self.textBrowser.append("Running Quality Check!! \n\n")
            p3 = Process(target=multi_qc_rna)
            self.progressBar_sub1_rna.setValue(76)
            p3.start()
            
            p4 = Process(target= self.func_pb_update( sub_pb=self.progressBar_sub1_rna, sub_pb_frac=4, initial_sub = 75, initial_main=0, error_icon=self.QCresultsButtonErroricon_rna))
            p4.start()
        else:
            pass
            
        if os.path.exists("results/cutadapt/fastqc_after/multiqc_after.html"):
            filename = "results/cutadapt/fastqc_after/multiqc_after.html"
            webbrowser.get('google-chrome').open(filename, new=0, autoraise=True)
        else:
            pass
    
    def run_index_text(self):
        subprocess.run(["snakemake", "--unlock", "-j", "1"])
        self.textBrowser.setTextColor(self._colors['black'])
        self.textBrowser.append("Creating Index for "+self.AlignercomboBoxDNA.currentText()+ "!! \n\n")
        
    def run_index_dna(self):
        self.progressBar_sub2_dna.setValue(1)
        self._set_color(self._colors['blue'].name(),pb =self.progressBar_sub2_dna)
        conf = open('config.yaml', 'w')
        conf.write('samples: ./samples.tsv \n')
        conf.write('units: '+ self.UnitslineEditDNA.text() + '\n'+'ref: \n')
        conf.write("  name: " + self.RefNamecomboBoxDNA.currentText() + "\n")
        conf.write('  genome: '+ self.RefGenomelineEditDNA.text() + '\n')
        conf.write('  genome-name: '+ os.path.basename(self.RefGenomelineEditDNA.text()) + '\n')
        conf.write('  genome-dict: '+ os.path.splitext(self.RefGenomelineEditDNA.text())[0] + '\n')
        conf.write('  known-variants: '+ self.RefVariantlineEditDNA.text() + '\n')
        conf.write('threads: ' + self.CorelineEditRNA.text() + '\n')
        conf.write("processing: \n")
        conf.write("  remove-duplicates: true\n")
        conf.write("threads: " + self.CorelineEditDNA.text() + "\n")
        conf.write('params: \n')
        conf.write("  cutadapt: '" + self.CutadaptlineEdit.text() + "' \n")
        conf.close()
        time.sleep(0.1)
        self.textBrowser.setTextColor(self._colors['black'])
        self.textBrowser.append("Config file created for generating index!! \nPlease refer to the file: config.yaml in your working directory. \n\n")
        rule = open('rule_all_index.txt', 'r')
        snakef = open('Snakefile', "w")
        snakef.write('include: "rules/common_dna.smk"\n')
        snakef.write('rule all:\n')
        snakef.write('  input:\n')
        for line in rule:
            if self.AlignercomboBoxDNA.currentText() in line:
                snakef.write(line)
            else:
                pass
        rule.close()
        snakef.write('\ninclude: "rules/' + self.AlignercomboBoxDNA.currentText() + '_index.smk" \n')
        snakef.close()
        time.sleep(0.1)

        def func_index_dna():
            
            process3 = subprocess.run(["snakemake", "--use-conda", "-s", "Snakefile", "--cores", self.CorelineEditDNA.text()])
        p1 = Process(target=func_index_dna)
        p1.start()
        p2 = Process(target=self.func_pb_update( sub_pb=self.progressBar_sub2_dna, sub_pb_frac=1, initial_sub = 0, initial_main=0, error_icon=self.RunIndexdnaButtonErroricon))
        p2.start()
#        self.textBrowser.insertPlainText("Creating Index for "+self.AlignercomboBoxDNA.currentText()+ "!! \n\n")
        if self.AlignercomboBoxDNA.currentText() == "BWA_MEM":
            self.BWAIndexlineEdit.setText("results_dna/index/BWA_MEM/" +os.path.basename(self.RefGenomelineEditDNA.text()))
        elif self.AlignercomboBoxDNA.currentText() == 'GEM3':
            self.BWAIndexlineEdit.setText("results_dna/index/"+self.AlignercomboBoxDNA.currentText()+ "/"+os.path.basename(self.RefGenomelineEditDNA.text())+".gem")
        else:
            self.BWAIndexlineEdit.setText("results_dna/index/"+self.AlignercomboBoxDNA.currentText()+ "/"+os.path.basename(self.RefGenomelineEditDNA.text()))
#        self.BWAIndexlineEdit.setText(os.getcwd()+"/results_dna/index/"+self.AlignercomboBoxDNA.currentText()+ "/"+os.path.basename(self.RefGenomelineEditDNA.text())+".gem")
        if self.progressBar_sub2_dna.value() == 100:
            self.textBrowser.setTextColor(self._colors['black'])
            self.textBrowser.append("Index created in results_dna/index/" +self.AlignercomboBoxDNA.currentText() +"/ !! \n\n")
        else:
            pass
        
    def run_index_rna(self):
        self.progressBar_sub2_dna.setValue(1)
        self._set_color(self._colors['blue'].name(),pb =self.progressBar_sub2_dna)
        self.textBrowser.setTextColor(self._colors['black'])
        self.textBrowser.append("Config file created for generating index!! \nPlease refer to the file: config.yaml in your working directory. \n\n")
        conf = open('config.yaml', 'w')
        conf.write('units: units.tsv \n')
        conf.write('ref: \n')
        conf.write('  annotation: '+ self.AnnotatedlineEditRNA.text() + '\n')
        conf.write('  fasta: '+self.FastalineEdit.text() + '\n')
        conf.write('threads: ' + self.CorelineEditRNA.text() + '\n')
        conf.write('params: \n')
        conf.write("  cutadapt: '" + self.CutadaptlineEdit_rna.text() + "' \n")
        conf.write("sample: " + self.SampleFolderLineEdit.text() + "\n")
        conf.close()
        
        time.sleep(0.1)
        self.textBrowser.setTextColor(self._colors['black'])
        self.textBrowser.append("Snakefilefile created for generating index!! \nPlease refer to the file: Snakefile_index in your working directory. \n\n")
        rule = open('rule_all_index.txt', 'r')
        snakef = open('Snakefile', "w")
        snakef.write('configfile: "config.yaml"\n')
        snakef.write('rule all:\n')
        snakef.write('  input:\n')
        for line in rule:
            if self.AlignercomboBoxRNA.currentText() in line:
                snakef.write(line)
        snakef.write('\ninclude: "rules/' + self.AlignercomboBoxRNA.currentText() + '_index.smk" \n')
        rule.close()
        snakef.close()
        
        time.sleep(0.1)
        def func_index_rna():
            
            process4 = subprocess.run(["snakemake", "--use-conda", "-s", "Snakefile", "--cores", self.CorelineEditDNA.text()])
            output4 = process4.communicate()
        self.textBrowser.setTextColor(self._colors['black'])
        self.textBrowser.append("Creating Index for "+self.AlignercomboBoxRNA.currentText()+ "!! \n\n")
        p1 = Process(target=func_index_rna)
        p1.start()
        p2 = Process(target=self.func_pb_update( sub_pb=self.progressBar_sub2_rna, sub_pb_frac=1, initial_sub = 0, initial_main=0, error_icon=self.RunIndexrnaButtonErroricon))
        p2.start()
        self.StarIndexlineEdit.setText(os.getcwd()+"/results/index/"+self.AlignercomboBoxRNA.currentText())
        if self.progressBar_sub2_dna.value() == 100:
            self.textBrowser.setTextColor(self._colors['black'])
            self.textBrowser.append("Index created in results/index/" +self.AlignercomboBoxRNA.currentText() +"/ !! \n\n")
        else:
            pass

    def create_config_dna(self):
        conf = open('config.yaml', 'w')
        conf.write('samples: ./samples.tsv \n')
        conf.write('units: '+ self.UnitslineEditDNA.text() + '\n'+'ref: \n')
        conf.write("  name: " + self.RefNamecomboBoxDNA.currentText() + "\n")
        conf.write('  genome: '+ self.RefGenomelineEditDNA.text() + '\n')
        conf.write('  genome-name: '+ os.path.basename(self.RefGenomelineEditDNA.text()) + '\n')
        conf.write('  genome-dict: '+ os.path.splitext(self.RefGenomelineEditDNA.text())[0] + '\n')
        conf.write('  known-variants: '+ self.RefVariantlineEditDNA.text() + '\n')
        conf.write("processing: \n")
        conf.write("  remove-duplicates: true\n")
        conf.write('index: \n')
        conf.write('  '+ self.AlignercomboBoxDNA.currentText() + ': ' + self.BWAIndexlineEdit.text() + '\n')
        conf.write('threads: ' + self.CorelineEditDNA.text() + '\n')
        conf.write('params: \n')
        conf.write("  cutadapt: '" + self.CutadaptlineEdit.text() + "' \n")
        aligner_params = open("aligner_params.txt", 'r').read().replace('\n', '')
        conf.write("  " + aligner_params + '\n')
        vc_params = open("vc_params.txt", 'r').read().replace('\n', '')
        conf.write("  " + vc_params + '\n')
        annotator_params = open("annotator_params.txt", 'r').read().replace('\n', '')
        conf.write("  " + annotator_params + '\n')

        conf.write("  picard: \n")
        conf.write("    MarkDuplicates: REMOVE_DUPLICATES=true VALIDATION_STRINGENCY=SILENT \n")
        conf.write("filtering:\n")
        conf.write("  vqsr: false\n")
        conf.write("  hard:\n")
        conf.write("    snvs:\n")
        conf.write("      " + '"QD < 2.0 || FS > 60.0 || MQ < 40.0 || MQRankSum < -12.5 || ReadPosRankSum < -8.0"\n')
        conf.write("    "+"indels:\n")
        conf.write("      "+'"QD < 2.0 || FS > 200.0 || ReadPosRankSum < -20.0"\n')
        conf.close()
        self.textBrowser.setTextColor(self._colors['black'])
        self.textBrowser.append("Config file created for DNA Seq analysis!! \nPlease refer to the file: config.yaml in your working directory. \n\n")


    def create_snakefile_dna(self):
        snake = open('Snakefile', "w")
        snake.write('include: "rules/common_dna.smk"\n')
        snake.write('rule all:\n')
        snake.write('  input:\n')
        snake.write('    expand("results_dna/mapped/{u.sample}-{u.unit}-{u.condition}.sorted.bam", u = units.itertuples()),\n')
        snake.write('    expand("results_dna/dedup/{u.sample}-{u.unit}-{u.condition}.bam", u = units.itertuples()),\n')
        snake.write('    "results_dna/filtered/all.vcf.gz",\n')
        snake.write('    "results_dna/multiqc/multiqc.html",\n')
        snake.write('    config["ref"]["genome-dict"]+ ".dict",\n')
        snake.write('    config["ref"]["genome"]+ ".fai",\n')
        snake.write('\ninclude: "rules/' + self.AlignercomboBoxDNA.currentText() + '.smk" \n')
        snake.write('include: "rules/' + self.VCcomboBoxDNA.currentText() + '.smk" \n')
        snake.write('include: "rules/' + self.AnnotatorcomboBoxDNA.currentText() + '.smk" \n')
        snake.close()
        self.textBrowser.setTextColor(self._colors['black'])
        self.textBrowser.append("Snakefile created for DNA Seq analysis!! \nPlease refer to the file: Snakefile in your working directory. \n\n")

    def not_snpeff(self):
        self.param_display()
        if self.AnnotatorcomboBoxDNA.currentText() == 'SnpEff':
            self.RefNamelabelDNA.show()
            self.RefNamecomboBoxDNA.show()
        else:
            self.RefNamelabelDNA.setText("Reference name (as in Annovar database)")
            self.RefNamelabelDNA.show()
            self.RefNamecomboBoxDNA.show()

    def if_annovar(self):
        with open('Snakefile', 'r+') as fd:
            contents = fd.readlines()
            if self.AnnotatorcomboBoxDNA.currentText() == 'Annovar':
                self.RefNamelabelDNA.setText("Reference name (as in Annovar database)")
                contents.insert(7, '    "results_dna/filtered/all.avinput",\n')
                contents.insert(10, '    "results_dna/annotated/all." + config["ref"]["name"] + "_multianno.vcf", \n')
                fd.seek(0)  # readlines consumes the iterator, so we need to start over
                fd.writelines(contents)
            else:
                contents.insert(8, '    "results_dna/annotated/all.vcf", \n')
                fd.seek(0)  # readlines consumes the iterator, so we need to start over
                fd.writelines(contents)
                fd.close()

    def create_config_rna(self):
        conf = open('config.yaml', 'w')
        conf.write('units: units.tsv \n')
        conf.write('ref: \n')
        if self.AlignercomboBoxRNA.currentText() == 'HISAT2':
            conf.write('  index-'+self.AlignercomboBoxRNA.currentText() + ': ' + self.StarIndexlineEdit.text() + '/ \n')
        elif self.AlignercomboBoxRNA.currentText() == 'bowtie2':
            conf.write('  index-'+ self.AlignercomboBoxRNA.currentText() + ': ' + self.StarIndexlineEdit.text() + '/bowtie2-index \n')
        else:
            conf.write('  index-'+ self.AlignercomboBoxRNA.currentText() + ': ' + self.StarIndexlineEdit.text() + '\n')
        conf.write('  annotation: '+ self.AnnotatedlineEditRNA.text() + '\n')
        conf.write('  fasta: '+self.FastalineEdit.text() + '\n')
        conf.write('threads: ' + self.CorelineEditRNA.text() + '\n')
        conf.write('params: \n')
        conf.write("  cutadapt: '" + self.CutadaptlineEdit_rna.text() + "' \n")
        aligner_params_rna = open("aligner_params_rna.txt", 'r').read().replace('\n', '')
        conf.write("  " + aligner_params_rna + '\n')
        em_params = open("em_params.txt", 'r').read().replace('\n', '')
        conf.write("  " + em_params + '\n')
        de_params = open("de_params.txt", 'r').read().replace('\n', '')
        conf.write("  " + de_params + '\n')
        
        conf.write("sample: " + self.SampleFolderLineEdit.text() + "\n")
        conf.close()
        self.textBrowser.setTextColor(self._colors['black'])
        self.textBrowser.append("Config file created for RNA Seq analysis!! \nPlease refer to the file: config.yaml in your working directory. \n\n")


    def create_snakefile_rna(self):
        snakef = open('Snakefile', 'w')
        snakef.write('include: "rules/common_rna.smk"\n')
        snakef.write('rule all:\n')
        snakef.write('  input:\n')
        if self.AlignercomboBoxRNA.currentText() == 'HISAT2':
            snakef.write("    expand('results/aligner_results/{sample}_{condition}_Rep{rep}.sam', sample=samples, condition=type, rep=reps),\n")
            snakef.write("    expand('results/aligner_results/{sample}_{condition}_Rep{rep}.bam', sample=samples, condition=type, rep=reps),\n")
        elif self.AlignercomboBoxRNA.currentText() == 'STAR':
            snakef.write("    expand('results/aligner_results/{sample}_{condition}_Rep{rep}/Aligned.out.sam', sample=samples, condition=type, rep=reps),\n")
            snakef.write("    expand('results/aligner_results/{sample}_{condition}_Rep{rep}.bam', sample=samples, condition=type, rep=reps),\n")
        if self.EMcomboBoxRNA.currentText() == 'StringTie':
            snakef.write("    expand('results/em_results/{sample}_{condition}_Rep{rep}/{sample}_{condition}_Rep{rep}_transcript.gtf', sample=samples, condition=type, rep=reps),\n")
            snakef.write("    expand('results/em_results/{sample}_{condition}_Rep{rep}/{sample}_{condition}_Rep{rep}_gene_abundances.tsv', sample=samples, condition=type, rep=reps),\n")
            snakef.write("    expand('results/em_results/{sample}_{condition}_Rep{rep}/{sample}_{condition}_Rep{rep}_cov_ref.gtf', sample=samples, condition=type, rep=reps),\n")
        elif self.EMcomboBoxRNA.currentText() == 'HTSeq':
            snakef.write("    expand('results/em_results/{sample}_{condition}_Rep{rep}.counts', sample=samples, condition=type, rep=reps),\n")
            snakef.write('    "results/em_results/emtable.tsv",\n')
        if self.DEcomboBoxRNA.currentText() == 'ballgown':
            snakef.write("    expand('results/de_results/SigDE.txt'),\n")
        elif self.DEcomboBoxRNA.currentText() == 'DESeq2':
            snakef.write("    expand('results/de_results/DESeq2_normalized_counts.txt'),\n")
        snakef.write('    "results/multiqc/multiqc.html",\n')
        snakef.write('include: "rules/' + self.AlignercomboBoxRNA.currentText() + '.smk" \n')
        snakef.write('include: "rules/' + self.EMcomboBoxRNA.currentText() + '.smk" \n')
        snakef.write('include: "rules/' + self.DEcomboBoxRNA.currentText() + '.smk" \n')
        snakef.close()
        self.textBrowser.setTextColor(self._colors['black'])
        self.textBrowser.append("Snakefile created for RNA Seq analysis!! \nPlease refer to the file: Snakefile in your working directory. \n\n")

    def create_dag(self):
        with open("Snakefile", "r+") as snake:
            line= snake.readline()
            if '"rules/common_dna.smk"' in line:
                svg_filename = self.AlignercomboBoxDNA.currentText() + self.VCcomboBoxDNA.currentText() + self.AnnotatorcomboBoxDNA.currentText() + ".svg"
            else:
                svg_filename = self.AlignercomboBoxRNA.currentText() + self.EMcomboBoxRNA.currentText() + self.DEcomboBoxRNA.currentText() + ".svg"
        print(svg_filename)
        subprocess.run(["snakemake", "--rulegraph",  "|", "dot", "-Tsvg", "-o", '"'+ svg_filename+ '"'], shell =True,  stdout=subprocess.PIPE)


    def about(self):
        url = 'icomic.readthedocs.io'
        widget = About()
        widget.setText("iCOMIC version 0.1")
        widget.setInformativeText("""
            Online documentation on <a href="http://%(url)s">%(url)s</a>
            <br>
            <br>
            Authors:  Anjana Anilkumar Sithara, Devi Priyanka Maripuri, Keerthika Moorthy, Sai Sruthi Amirtha Ganesh, Philge Philip, Shayantan Banerjee, Malvika Sudhakar, Karthik Raman  
            """ % {"url": url})
        widget.setWindowTitle("iCOMIC")
        retval = widget.exec_()
        if retval == QtWidgets.QMessageBox.Ok:
            widget.close()

    def quick_start(self):
        url = 'iCOMIC.readthedocs.io'
        pipelines_text = "<ul>\n"
        msg = HelpDialog(pipelines=pipelines_text)
        retval = msg.exec_()
        if retval == QtWidgets.QMessageBox.Ok:
            msg.close()


                            
    def run_action_textbox(self):
        subprocess.run(["snakemake", "--unlock", "-j", "1"])
        self.textBrowser.setTextColor(self._colors['black'])
        self.textBrowser.append("Please be patient, while we analyze your data... \n\n")

    def run_action_dna(self):
        self._set_color(self._colors['blue'].name(),pb =self.progressBar_dna)
        self.progressBar_dna.setValue(1)
        
        def func_run_action():
            process5 = subprocess.run(["snakemake", "--use-conda", "-j", self.CorelineEditDNA.text()])
            
    
        p1 = Process(target=func_run_action)
        p1.start()
        p2 = Process(target=self.func_pb_update( sub_pb=self.progressBar_dna, sub_pb_frac=1, initial_sub = 0, initial_main=0, error_icon=self.RunButtonErroricon_dna))
        p2.start()
        
        if self.progressBar_dna.value() == 100:
            self._set_color(self._colors['green'].name(),pb =self.progressBar_dna)
            self.nextbuttonrunDNA.setEnabled(True)
            self.DNAtabWidget.setCurrentIndex(4)
            self.DNAtabWidget.setTabEnabled(4, True)
        else:
            pass
        

    def run_action_rna(self):
        self.progressBar.setValue(1)
        self._set_color(self._colors['blue'].name(),pb =self.progressBar)
        def func_run_action():
            process5 = subprocess.run(["snakemake", "--use-conda", "--cores", self.CorelineEditDNA.text()])
           
    
        p1 = Process(target=func_run_action)
        p1.start()
        p2 = Process(target=self.func_pb_update( sub_pb=self.progressBar, sub_pb_frac=1, initial_sub = 0, initial_main=0, error_icon=self.RunButtonErroricon))
        p2.start()
        if self.progressBar.value() == 100:
            self._set_color(self._colors['green'].name(),pb =self.progressBar)
            self.nextbuttonrunRNA.setEnabled(True)
            self.RNAtabWidget.setCurrentIndex(4)
            self.RNAtabWidget.setTabEnabled(4, True)
        else:
            pass
        
        
    def on_check_proceed(self,is_toggle):
        if is_toggle:
            self.ctagradioButton.setEnabled(True)
            self.nbradioButton.setEnabled(True)
            self.nextbuttonresult.setEnabled(True)
            self.nbinfoiconradio.setEnabled(True)
        else:
            self.ctagradioButton.setEnabled(False)
            self.nbradioButton.setEnabled(False)
            self.nextbuttonresult.setEnabled(False)
            self.nbinfoiconradio.setEnabled(False)



class About(QtWidgets.QMessageBox):
    """A resizable QMessageBox for the About dialog"""

    def __init__(self, *args, **kwargs):
        super(About, self).__init__(*args, **kwargs)
        self.setSizeGripEnabled(True)
        self.setIcon(QtWidgets.QMessageBox.Information)
        self.setWindowTitle("iCOMIC")
        self.setStandardButtons(QtWidgets.QMessageBox.Ok)

    def event(self, e):
        result = super(About, self).event(e)

        self.setMinimumHeight(0)
        self.setMaximumHeight(16777215)
        self.setMinimumWidth(500)
        self.setMaximumWidth(16777215)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        return result

class Ui_Help(object):
    def setupUi(self, Help):
        Help.setObjectName("Help")
        Help.resize(456, 582)
        self.gridLayout = QtWidgets.QGridLayout(Help)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(Help)
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.buttonBox = QtWidgets.QDialogButtonBox(Help)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Help)
        QtCore.QMetaObject.connectSlotsByName(Help)

    def retranslateUi(self, Help):
        _translate = QtCore.QCoreApplication.translate
        Help.setWindowTitle(_translate("Help", "iCOMIC Help"))

helptxt = """
<div style="fontsize:12px">
<p>
<b>iCOMIC</b> pipeline enables the ready analysis of RNA-Seq and Whole Genome Sequencing data.
	ICOMIC has an inbuilt library of tools with predefined valid combinations.
</p>
    <p>
    The user will have the freedom to choose any possible combination of tools,
    however a benchmarked list of pipelines is provided (see
<a href="http://iCOMIC.readthedocs.io">iCOMIC.readthedocs.io</a> for details).
    </p>

    <p>
    Here is a typical set of actions to run iCOMIC pipelines:
        <ol>
        <li> Select a pipeline. </li>
        <li> Input the required data files.</li>
        <li> Check 'yes' for Quality Control if you want to do quality check and
        trimming and also mention the additional parameters if required.</li>
            <ul>
           <li> Tool for Quality Control: FastQC </li>
           <li> Tool for trimming the reads: Cutadapt </li>
            </ul>
        <li> Click on 'Create snakefile for QC Analysis' button for creating
        the Snakefile and 'Create config file for QC Analysis' button for
        config file. </li>
        <li> Click on 'Run Quality Control' to perform Quality check. </li>
        <li> Select the tools for analysis. </li>
        <li> Input the index files. </li>
        <li> Enter additional parameters for each tool if required. </li>
        <li> Click on 'Create snakefile' button for creating the Snakefile and
        'Create config file' button for config file. </li>
        <li> Click 'Run' to run the pipeline.</li>
        </ol>
"""


class HelpDialog(QtWidgets.QDialog):
    """todo"""
    def __init__(self, parent=None, pipelines=""):
        super().__init__(parent=parent)
        self.ui = Ui_Help()
        self.ui.setupUi(self)
        self.ui.textBrowser.setText(helptxt % {"pipelines": pipelines})
        self.ui.buttonBox.accepted.connect(self.close)

        

class SVGDialog(QtWidgets.QDialog):
    """Dialog to show a SVG image"""
    def __init__(self, filename):
        super().__init__()
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.setWindowTitle("DAG")

        if os.path.exists(filename):
            widget = QSvgWidget(filename)
            self.main_layout.addWidget(widget)

class QCResultsDialog(QtWidgets.QWidget):
    """Dialog to show a SVG image"""
    def __init__(self, filename):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.closeButton = QtWidgets.QPushButton("Close")
        self.main_layout = QtWidgets.QHBoxLayout(self)
        self.main_layout.addStretch(1)
        self.main_layout.addWidget(self.closeButton)
        self.vbox = QtWidgets.QVBoxLayout(self)
        self.vbox.addStretch(2)
        self.vbox.addLayout(self.main_layout)
        self.setLayout(self.vbox)  
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle("FastQC Results")
        
class AdvancedDialog(QtWidgets.QDialog):
    def __init__(self, path):
        super().__init__()
        self.setWindowTitle("Advanced Options")
        self.setStyleSheet("background-color: #C3E7B5")
        self.top = 200
        self.left = 500
        self.width = 600
        self.height = 550
        self.setGeometry(self.left, self.top, self.width, self.height)
        formLayout =QFormLayout()
        groupBox = QGroupBox()
        groupBox.setStyleSheet("background-color: #F0F9EC")
        dataframe = pd.read_csv(path, header=0) # specifying that the table has column names
        add_int_param = dataframe[(dataframe["Value"] == 'INT') & (dataframe["Essential"] == 'no')]
        num_add_int_param = len(add_int_param)
        add_float_param = dataframe[(dataframe["Value"] == 'FLOAT') & (dataframe["Essential"] == 'no')]
        num_add_float_param=len(add_float_param)
        add_na_param = dataframe[(dataframe["Value"] == 'na') & (dataframe["Essential"] == 'no')]
        num_add_na_param=len(add_na_param)
        add_str_param = dataframe[(dataframe["Value"] == 'STR') & (dataframe["Essential"] == 'no')]
        num_add_str_param=len(add_str_param)
        
        self.button = QtWidgets.QDialogButtonBox(self)
        self.button.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.button.move(450,510)
        
        self.label_list_int = []
        self.line_edit_list_int = []
        self.label_list_float = []
        self.line_edit_list_float = []
        self.radio_label_list_na = []
        self.line_edit_list_str = []
        self.label_list_str = []
        for y in range(num_add_int_param):
            label_name = str(add_int_param.iloc[y, 2])
            self.label_name = QtWidgets.QLabel(label_name)
            self.label_list_int.append(self.label_name)
            default_value = str(add_int_param.iloc[y, 4])
            self.line_edit = QtWidgets.QLineEdit(default_value)
            self.line_edit_list_int.append(self.line_edit)
            formLayout.addRow(self.label_list_int[y], self.line_edit_list_int[y])
        for x in range(num_add_float_param):
            label_name = str(add_float_param.iloc[x, 2])
            self.label_name = QtWidgets.QLabel(label_name)
            self.label_list_float.append(self.label_name)
            default_value = str(add_float_param.iloc[x, 4])
            self.line_edit = QtWidgets.QLineEdit(default_value)
            self.line_edit_list_float.append(self.line_edit)
            formLayout.addRow(self.label_list_float[x], self.line_edit_list_float[x])
        for p in range(num_add_str_param):
            label_name = str(add_str_param.iloc[p, 2])
            self.label_name = QtWidgets.QLabel(label_name)
            self.label_list_str.append(self.label_name)
            default_value = str(add_str_param.iloc[p, 4])
            self.line_edit = QtWidgets.QLineEdit(default_value)
            self.line_edit_list_str.append(self.line_edit)
            formLayout.addRow(self.label_list_str[p], self.line_edit_list_str[p])
            formLayout.addRow(self.label_list_str[p])
        for z in range(num_add_na_param):
            radio_name = str(add_na_param.iloc[z, 2])
            self.radio_name = QtWidgets.QCheckBox(radio_name)
            self.radio_name.setChecked(False)
            self.radio_label_list_na.append(self.radio_name)
            formLayout.addRow(self.radio_label_list_na[z])
        

       
        groupBox.setLayout(formLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(450)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(scroll)
            
class AdvancedDialog_old(QtWidgets.QDialog):
    def __init__(self, path):
        super().__init__()
        self.setWindowTitle("Advanced Options")
        self.top = 200
        self.left = 500
        self.width = 600
        self.height = 550
        self.setGeometry(self.left, self.top, self.width, self.height)
        formLayout =QFormLayout()
        groupBox = QGroupBox()
        dataframe = pd.read_csv(path, header=0) # specifying that the table has column names
        additional = dataframe[dataframe["Essential"] == "no"]
        number_of_additional = len(additional)
        
        self.button = QtWidgets.QDialogButtonBox(self)
        self.button.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.button.move(450,510)
        self.label_list = []
        self.line_edit_list = []
        for x in range(number_of_additional):
            label_name = str(additional.iloc[x, 2])
            self.label_name = QtWidgets.QLabel(label_name)
            self.label_list.append(self.label_name)
            default_value = str(additional.iloc[x, 4])
            self.line_edit = QtWidgets.QLineEdit(default_value)
            self.line_edit_list.append(self.line_edit)
            formLayout.addRow(self.label_list[x], self.line_edit_list[x])
        groupBox.setLayout(formLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(450)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(scroll)
class showQCDialog():
    def __init__(self):
        super().__init__()
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Question)
        self.left = 700
        self.top = 450
        self.width = 320
        self.height = 400
        msgBox.setGeometry(self.left, self.top, self.width, self.height)
        msgBox.setText("Are you sure you want to proceed without Quality control of your data?")
        msgBox.setWindowTitle("WARNING")
        msgBox.resize(200,64)
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)

        self.returnValue = msgBox.exec()
            
class ResultsDialog(QtWidgets.QMainWindow):
    def __init__(self, path):
        super().__init__()     

        self.textEdit = QtWidgets.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle(os.path.basename(path))
        self.show()
        if os.path.splitext(path)[-1] == ".gz":
            with gzip.open(path, 'rb') as f:
                data = f.read()
                self.textEdit.setText(data.decode("utf-8"))
        else:
            with open(path, 'r') as f:
                data = f.read()
                self.textEdit.setText(data)

class ResultsDialog_old(QtWidgets.QMainWindow):

    def __init__(self, path):
        super().__init__()
        
        self.initUI()


    def initUI(self):      

        self.textEdit = QtWidgets.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        self.showDialog()
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("filtered vcf")
        self.show()
    def showDialog(self):
        with gzip.open(path, 'rb') as f:
            data = f.read()
            self.textEdit.setText(data.decode("utf-8"))

        




def main():
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

main()