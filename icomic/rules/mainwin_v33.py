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
# =============================================================================
# from PyQt5 import QtWebKitWidgets
# from PyQt5.QtWebKitWidgets import QWebView
# =============================================================================
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


#from tools import QPlainTextEditLogger, Tools

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("iCOMIC Pipeline")
        MainWindow.resize(725, 746)
        MainWindow.setFixedSize(725, 746)
        MainWindow.setStyleSheet("background-color: #C3E7B5")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
#        self.centralwidget.setStyleSheet("background-color: #AAC1CD")
        MainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint);
#        MainWindow.setWindowFlags()
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
        self.DNAtabWidget.setStyleSheet ("background-color: #F0F9EC")
        

        ### Test Run Button Grey ###
        self.one_passed = False
        self.two_passed = False
        # self.three_passed = False
        # self.four_passed = False
        ############################
        ## Make Input as first tab ##
        self.input_dna = QtWidgets.QWidget()
        self.input_dna.setObjectName("input_dna")
        self.SamplesYesradioButton = QtWidgets.QRadioButton(self.input_dna)
        self.SamplesYesradioButton.move(80, 30)
        self.SamplesYesradioButton.setObjectName("SamplesYesradioButton")
        self.SamplesYesradioButton.setChecked(True)
        self.SamplesNoradioButton = QtWidgets.QRadioButton(self.input_dna)
        self.SamplesNoradioButton.move(450, 30)
        self.SamplesNoradioButton.setObjectName("SamplesNoradioButton")
        self.SampleOrlabel = QtWidgets.QLabel(self.input_dna)
        self.SampleOrlabel.move(320, 30)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.SampleOrlabel.setFont(font)
        self.SampleOrlabel.setObjectName("SampleOrlabel")
# =============================================================================
#         self.SampleNolabel = QtWidgets.QLabel(self.input_dna)
#         self.SampleNolabel.setGeometry(QtCore.QRect(210, 30, 151, 21))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         font.setItalic(True)
#         self.SampleNolabel.setFont(font)
#         self.SampleNolabel.setObjectName("SampleNolabel")
# =============================================================================
        
        
        
        
        font_label = QtGui.QFont()
        font_label.setPointSize(8.5)
        color  = QtGui.QColor(233, 10, 150)
#        font_label.setStyle({color : values(r)})
#        font_label.setStyle(self._colors['red'])
#        self.SamplesErrortextDNA.setText("qwwwwwwwwwwwwwwwwwwwwww")
        
#        self.SamplesErrortextDNA.setFrameStyle("QFrame: Panel")
        
        
#        self.UnitsErroriconDNA.setStyleSheet("color: red")
        
#        self.UnitsErroriconDNA.setText("safdg")
        
#        self.UnitsErroriconDNA.
       
# =============================================================================
#         self.SamplesErroriconDNA.setIcon(QtGui.QIcon("./icons/warning.svg"))
#         self.SamplesErrortextDNA.setIconSize(QtCore.QSize(22, 22))
# =============================================================================
# =============================================================================
#         self.WDlabelDNA = QtWidgets.QLabel(self.input_dna)
#         self.WDlabelDNA.setGeometry(QtCore.QRect(20, 90, 113, 23))
#         self.WDlabelDNA.setObjectName("SampleFilelabelDNA")
#         self.WDlabelDNA.setEnabled(True)
#         self.WDlineEditDNA = QtWidgets.QLineEdit(self.input_dna)
#         self.WDlineEditDNA.setGeometry(QtCore.QRect(200, 90, 385, 23))
#         self.WDlineEditDNA.setObjectName("SampleslineEditDNA")
#         self.WDlineEditDNA.setEnabled(True)
#         self.WDBrowseButtonDNA = QtWidgets.QPushButton(self.input_dna)
#         self.WDBrowseButtonDNA.setGeometry(QtCore.QRect(600, 90, 30, 25))
#         self.WDBrowseButtonDNA.setObjectName("SamplesBrowseButtonDNA")
#         self.WDBrowseButtonDNA.setEnabled(True)
#         self.WDErrortextDNA = QtWidgets.QLabel(self.input_dna)
#         self.WDErrortextDNA.setGeometry(QtCore.QRect(200, 115, 385, 23))
#         self.WDErrortextDNA.setFont(font_label)
#         self.WDErrortextDNA.setStyleSheet("color: red")
# =============================================================================
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
        self.SamplesErrortextDNA.setGeometry(QtCore.QRect(200, 175, 385, 23))
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
        self.UnitsErrortextDNA.setGeometry(QtCore.QRect(200, 140, 385, 23))
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
# =============================================================================
#         self.RefNamelabelDNA = QtWidgets.QLabel(self.input_dna)
#         self.RefNamelabelDNA.setGeometry(QtCore.QRect(20, 220, 294, 17))
#         self.RefNamelabelDNA.setObjectName("RefNamelabelDNA")
# =============================================================================
#        self.RefNamelineEdit = QtWidgets.QLineEdit(self.input_dna)
#        self.RefNamelineEdit.setGeometry(QtCore.QRect(315, 220, 215, 23))
# =============================================================================
#         self.RefNamecomboBoxDNA = QtWidgets.QComboBox(self.input_dna)
#         self.RefNamecomboBoxDNA.setGeometry(QtCore.QRect(315, 220, 215, 23))
# #        self.RefNamecomboBoxDNA.setIconSize(QtCore.QSize(16, 16))
#         self.RefNamecomboBoxDNA.setObjectName("RefNamecomboBoxDNA")
#         self.RefNamecomboBoxDNA.addItem("GRCh38.86")
#         self.RefNamecomboBoxDNA.addItem("hg19")
#         self.RefNamecomboBoxDNA.addItem("Escherichia_coli")
#         self.RefNamecomboBoxDNA.addItem("Caenorhabditis_elegans")
# =============================================================================
        
        self.nextbuttoninputDNA = QtWidgets.QPushButton(self.input_dna)
        self.nextbuttoninputDNA.setGeometry(QtCore.QRect(635, 400, 45, 45))
        self.nextbuttoninputDNA.setObjectName("nextbuttoninputDNA")
#        self.RefNamelineEdit.setObjectName("RefNamelineEdit")
        
         #####info icon####
        ###dna###
        
        font_info = QtGui.QFont()
        font_info.setPointSize(8.5)
        
# =============================================================================
#         self.WDinfoicon_dna = QtWidgets.QPushButton(self.input_dna)
#         self.WDinfoicon_dna.setFlat(True)
#         self.WDinfoicon_dna.setGeometry(QtCore.QRect(133, 94, 20, 20))
#         self.WDinfoicon_dna.setToolTip("xxxxxxxxx!")
#         self.WDinfoicon_dna.setFont(font_info)
#         self.WDinfoicon_dna.setIcon(QtGui.QIcon("./icons/info.svg"))
#         self.WDinfoicon_dna.setIconSize(QtCore.QSize(13, 13))
# =============================================================================
        
        self.SampleFileinfoicon_dna = QtWidgets.QPushButton(self.input_dna)
        self.SampleFileinfoicon_dna.setFlat(True)
        self.SampleFileinfoicon_dna.setGeometry(QtCore.QRect(120, 153, 20, 20))
        self.SampleFileinfoicon_dna.setToolTip("xxxxxxxxx!")
        self.SampleFileinfoicon_dna.setFont(font_info)
        self.SampleFileinfoicon_dna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.SampleFileinfoicon_dna.setIconSize(QtCore.QSize(13, 13))
        
        self.UnitsFileinfoicon_dna = QtWidgets.QPushButton(self.input_dna)
        self.UnitsFileinfoicon_dna.setFlat(True)
        self.UnitsFileinfoicon_dna.setGeometry(QtCore.QRect(116, 209, 20, 20))
        self.UnitsFileinfoicon_dna.setToolTip("xxxxxxxxx!")
        self.UnitsFileinfoicon_dna.setFont(font_info)
        self.UnitsFileinfoicon_dna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.UnitsFileinfoicon_dna.setIconSize(QtCore.QSize(13, 13))
        
        self.RefGenomeinfoicon_dna = QtWidgets.QPushButton(self.input_dna)
        self.RefGenomeinfoicon_dna.setFlat(True)
        self.RefGenomeinfoicon_dna.setGeometry(QtCore.QRect(142, 270, 20, 20))
        self.RefGenomeinfoicon_dna.setToolTip("xxxxxxxxx!")
        self.RefGenomeinfoicon_dna.setFont(font_info)
        self.RefGenomeinfoicon_dna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.RefGenomeinfoicon_dna.setIconSize(QtCore.QSize(13, 13))  
        
        self.RefVariantinfoicon_dna = QtWidgets.QPushButton(self.input_dna)
        self.RefVariantinfoicon_dna.setFlat(True)
        self.RefVariantinfoicon_dna.setGeometry(QtCore.QRect(177, 329, 20, 20))
        self.RefVariantinfoicon_dna.setToolTip("xxxxxxxxx!")
        self.RefVariantinfoicon_dna.setFont(font_info)
        self.RefVariantinfoicon_dna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.RefVariantinfoicon_dna.setIconSize(QtCore.QSize(13, 13))         
        
        self.SamplesYesradioinfoicon_dna = QtWidgets.QPushButton(self.input_dna)
        self.SamplesYesradioinfoicon_dna.setFlat(True)
        self.SamplesYesradioinfoicon_dna.setGeometry(QtCore.QRect(218, 32, 20, 20))
        self.SamplesYesradioinfoicon_dna.setToolTip("xxxxxxxxx!")
        self.SamplesYesradioinfoicon_dna.setFont(font_info)
        self.SamplesYesradioinfoicon_dna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.SamplesYesradioinfoicon_dna.setIconSize(QtCore.QSize(13, 13))       
        
        
        self.SamplesNoradioinfoicon_dna = QtWidgets.QPushButton(self.input_dna)
        self.SamplesNoradioinfoicon_dna.setFlat(True)
        self.SamplesNoradioinfoicon_dna.setGeometry(QtCore.QRect(583, 32, 20, 20))
        self.SamplesNoradioinfoicon_dna.setToolTip("xxxxxxxxx!")
        self.SamplesNoradioinfoicon_dna.setFont(font_info)
        self.SamplesNoradioinfoicon_dna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.SamplesNoradioinfoicon_dna.setIconSize(QtCore.QSize(13, 13))               
        
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
        self.QCresults.setStyleSheet("background-color: #578446")
        self.QCresultsButtonErroricon = QtWidgets.QPushButton(self.QC_dna)
        self.QCresultsButtonErroricon.setGeometry(QtCore.QRect(186, 32, 20, 20))
        self.QCresultsButtonErroricon.setToolTip("Check and Run View FastQC Results Again!")
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
#==============================================================================
#         self.fastQClabel = QtWidgets.QLabel(self.QC_dna)
#         self.fastQClabel.setGeometry(QtCore.QRect(10, 100, 67, 17))
#         self.fastQClabel.setObjectName("fastQClabel")
#==============================================================================
#==============================================================================
#         self.QClineEdit = QtWidgets.QLineEdit(self.QC_dna)
#         self.QClineEdit.setGeometry(QtCore.QRect(120, 100, 481, 23))
#         self.QClineEdit.setObjectName("QClineEdit")
#==============================================================================
        self.CutadaptlineEdit = QtWidgets.QLineEdit(self.QC_dna)
        self.CutadaptlineEdit.setGeometry(QtCore.QRect(120, 200, 481, 23))
        self.CutadaptlineEdit.setObjectName("CutadaptlineEdit")
        self.Cutadaptlabel = QtWidgets.QLabel(self.QC_dna)
        self.Cutadaptlabel.setGeometry(QtCore.QRect(10, 200, 67, 17))
        self.Cutadaptlabel.setObjectName("Cutadaptlabel")
# =============================================================================
#         self.MultiQClineEdit = QtWidgets.QLineEdit(self.QC_dna)
#         self.MultiQClineEdit.setGeometry(QtCore.QRect(120, 180, 481, 23))
#         self.MultiQClineEdit.setObjectName("MultiQClineEdit")
#         self.MultiQClabel = QtWidgets.QLabel(self.QC_dna)
#         self.MultiQClabel.setGeometry(QtCore.QRect(10, 180, 67, 17))
#         self.MultiQClabel.setObjectName("MultiQClabel")
# =============================================================================
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.QC_dna)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(235, 273, 240, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
# =============================================================================
#         self.RunQCpushButton = QtWidgets.QPushButton(self.QC_dna)
#         self.RunQCpushButton.setObjectName("RunQCpushButton")
#         self.RunQCpushButton.setGeometry(QtCore.QRect(316, 172, 50, 50))
# =============================================================================
# =============================================================================
#         self.CreateSnakefilepushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
#         self.CreateSnakefilepushButton.setObjectName("CreateSnakefilepushButton")
#         self.horizontalLayout_4.addWidget(self.CreateSnakefilepushButton)
#         self.CreateConfigfilepushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
#         self.CreateConfigfilepushButton.setObjectName("CreateConfigfilepushButton")
#         self.horizontalLayout_4.addWidget(self.CreateConfigfilepushButton)
# =============================================================================
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
# =============================================================================
#         self.progressBar_sub1Label = QtWidgets.QLabel(self.centralwidget)
#         self.progressBar_sub1Label.setGeometry(QtCore.QRect(500, 570, 510, 17))
#         self.progressBar_sub1Label.setObjectName("progressBar_sub1Label")
# =============================================================================
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
        self.QCresultsinfoicon_dna.setToolTip("xxxxxxxxx!")
        self.QCresultsinfoicon_dna.setFont(font_info)
        self.QCresultsinfoicon_dna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.QCresultsinfoicon_dna.setIconSize(QtCore.QSize(13, 13))          
        
        self.QClabelinfoicon_dna = QtWidgets.QPushButton(self.QC_dna)
        self.QClabelinfoicon_dna.setFlat(True)
        self.QClabelinfoicon_dna.setGeometry(QtCore.QRect(131, 87, 20, 20))
        self.QClabelinfoicon_dna.setToolTip("xxxxxxxxx!")
        self.QClabelinfoicon_dna.setFont(font_info)
        self.QClabelinfoicon_dna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.QClabelinfoicon_dna.setIconSize(QtCore.QSize(13, 13))          
        
        self.Cutadaptlabelinfoicon_dna = QtWidgets.QPushButton(self.QC_dna)
        self.Cutadaptlabelinfoicon_dna.setFlat(True)
        self.Cutadaptlabelinfoicon_dna.setGeometry(QtCore.QRect(70, 199, 20, 20))
        self.Cutadaptlabelinfoicon_dna.setToolTip("xxxxxxxxx!")
        self.Cutadaptlabelinfoicon_dna.setFont(font_info)
        self.Cutadaptlabelinfoicon_dna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.Cutadaptlabelinfoicon_dna.setIconSize(QtCore.QSize(13, 13))    
        
        self.RunQCpushButtoninfoicon_dna = QtWidgets.QPushButton(self.QC_dna)
        self.RunQCpushButtoninfoicon_dna.setFlat(True)
        self.RunQCpushButtoninfoicon_dna.setGeometry(QtCore.QRect(480, 277, 20, 20))
        self.RunQCpushButtoninfoicon_dna.setToolTip("xxxxxxxxx!")
        self.RunQCpushButtoninfoicon_dna.setFont(font_info)
        self.RunQCpushButtoninfoicon_dna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.RunQCpushButtoninfoicon_dna.setIconSize(QtCore.QSize(13, 13))           
        
        
        self.DNAtabWidget.addTab(self.QC_dna, "")
        ## End ##
        self.Tool_dna = QtWidgets.QWidget()
        self.Tool_dna.setObjectName("Tool_dna")
# =============================================================================
#         self.layoutWidget = QtWidgets.QWidget(self.Tool_dna)
#         self.layoutWidget.setGeometry(QtCore.QRect(50, 80, 591, 29))
#         self.layoutWidget.setObjectName("layoutWidget")
# =============================================================================
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

# =============================================================================
#         for i in range(100):
#             for j in range(100):
#                 self.gridLayout.addWidget(QtWidgets.QPushButton(), i, j)
#         
#         
#         self.main_grid = QtWidgets.QGridLayout(self.Tool_dna)
# #        self.vertical = QtWidgets.QVBoxLayout(self.Tool_dna)
#         
#         
#         self.scroll = QScrollArea()
#         self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
#         self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
#         self.scroll.setWidgetResizable(True)
# #        self.scroll.setMinimumSize(400, 400)
#         self.scroll.setFixedHeight(450)
#         
#         layout = QtWidgets.QVBoxLayout(self.Tool_dna)
#         layout.addWidget(self.scroll)
# #        self.scroll.setWidget(layout)
#         self.scroll.setLayout(self.main_grid)
# #        self.scroll.setLayout(self.vertical)
#         self.grp_list=[self.aligner_groupbox, self.vc_groupbox, self.annotator_groupbox]
#         for i in range(3):
#             self.main_grid.addWidget(self.grp_list[i], i,0)
#             
#         self.Tool_dna.setLayout(self.main_grid)
# =============================================================================

#        self.setCentralWidget(self.scroll)
        
# =============================================================================
#         self.scrollArea = QScrollArea()
#         self.scrollArea.setWidgetResizable(True)
# #        self.scrollArea.move(10, 40)
#         self.scrollArea.setFixedHeight(450)
# # =============================================================================
# #         self.scrollAreaWidgetContents = QWidget(self.scrollArea)
# #         self.scrollArea.setWidget(self.scrollAreaWidgetContents)
# # =============================================================================
#         
# # =============================================================================
# #         self.scrollArea.setWidget(self.aligner_groupbox)
# #         self.scrollArea.setWidget(self.vc_groupbox)
# #         self.scrollArea.setWidget(self.annotator_groupbox)
# # =============================================================================
#         self.scrollArea.setLayout(self.vertical)
# =============================================================================
# =============================================================================
#         self.main_grid.addWidget(self.aligner_groupbox, 0,0)
#         self.main_grid.addWidget(self.vc_groupbox, 1,0)
#         self.main_grid.addWidget(self.annotator_groupbox,2,0)
# =============================================================================
# =============================================================================
#         self.vertical.addWidget(self.aligner_groupbox)
#         self.vertical.addWidget(self.vc_groupbox)
#         self.vertical.addWidget(self.annotator_groupbox)
# =============================================================================
#        self.vertical.addWidget(self.scrollArea)
        
# =============================================================================
#         scroll = QScrollArea()
#         scroll.setWidget(groupBox)
#         scroll.setWidgetResizable(True)
#         scroll.setFixedHeight(450)
# =============================================================================
        
        
       
       
    
 
# =============================================================================
#         self.button = QPushButton("Football", self)
#         self.button.setIcon(QtGui.QIcon("football.png"))
#         self.button.setIconSize(QtCore.QSize(40, 40))
#         self.button.setMinimumHeight(40)
#         hboxLayout.addWidget(self.button)
#  
#         self.button2 = QPushButton("Cricket", self)
#         self.button2.setIcon(QtGui.QIcon("cricket.png"))
#         self.button2.setIconSize(QtCore.QSize(40, 40))
#         self.button2.setMinimumHeight(40)
#         hboxLayout.addWidget(self.button2)
#  
#         self.button3 = QPushButton("Tennis", self)
#         self.button3.setIcon(QtGui.QIcon("tennis.png"))
#         self.button3.setIconSize(QtCore.QSize(40, 40))
#         self.button3.setMinimumHeight(40)
#         hboxLayout.addWidget(self.button3)
#  
#  
#         self.groupBox.setLayout(hboxLayout)
# =============================================================================
        
        
# =============================================================================
#         self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
#         self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
#         self.horizontalLayout_3.setSpacing(20)
#         self.horizontalLayout_3.setObjectName("horizontalLayout_3")
# =============================================================================
# =============================================================================
#         self.AlignerlabelDNA = QtWidgets.QLabel()
#         self.AlignerlabelDNA.setObjectName("AlignerlabelDNA")
#         self.vertical.addWidget(self.AlignerlabelDNA)
# =============================================================================
# =============================================================================
#         self.AlignercomboBoxDNA = QtWidgets.QComboBox()
#         self.AlignercomboBoxDNA.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
#         self.AlignercomboBoxDNA.setIconSize(QtCore.QSize(16, 16))
#         self.AlignercomboBoxDNA.setObjectName("AlignercomboBoxDNA")
#         self.AlignercomboBoxDNA.addItem("")
#         self.AlignercomboBoxDNA.addItem("")
# #        self.AlignercomboBoxDNA.addItem("")
#         self.vertical.addWidget(self.AlignercomboBoxDNA)
# =============================================================================
# =============================================================================
#         self.VClabelDNA = QtWidgets.QLabel()
#         self.VClabelDNA.setMinimumSize(QtCore.QSize(93, 0))
#         self.VClabelDNA.setObjectName("VClabelDNA")
#         self.vertical.addWidget(self.VClabelDNA)
# =============================================================================
# =============================================================================
#         self.VCcomboBoxDNA = QtWidgets.QComboBox()
#         self.VCcomboBoxDNA.setObjectName("VCcomboBoxDNA")
#         self.VCcomboBoxDNA.addItem("")
# =============================================================================
# =============================================================================
#         self.VCcomboBoxDNA.addItem("")
#         self.VCcomboBoxDNA.addItem("")
#         self.VCcomboBoxDNA.addItem("")
#         self.VCcomboBoxDNA.addItem("")
# =============================================================================
#        self.vertical.addWidget(self.VCcomboBoxDNA)
# =============================================================================
#         self.AnnotatorlabelDNA = QtWidgets.QLabel()
#         self.AnnotatorlabelDNA.setObjectName("AnnotatorlabelDNA")
#         self.vertical.addWidget(self.AnnotatorlabelDNA)
# =============================================================================
# =============================================================================
#         self.AnnotatorcomboBoxDNA = QtWidgets.QComboBox()
#         self.AnnotatorcomboBoxDNA.setObjectName("AnnotatorcomboBoxDNA")
#         self.AnnotatorcomboBoxDNA.addItem("")
#         self.AnnotatorcomboBoxDNA.addItem("")
# =============================================================================
#        self.AnnotatorcomboBoxDNA.addItem("")
#        self.vertical.addWidget(self.AnnotatorcomboBoxDNA)
        
        
        
#        self.layoutWidget.raise_()
    
# =============================================================================
#         self.VCcomboBoxDNA.raise_()
#         self.AlignercomboBoxDNA.raise_()
# =============================================================================
        ###
        
        ## Add Index ##
# =============================================================================
#         self.Index_dna = QtWidgets.QWidget()
#         self.Index_dna.setObjectName("Index_dna")
# =============================================================================
        ## Added from QC_Index###
# =============================================================================
#         self.InputIndexlabel_dna = QtWidgets.QLabel(self.Index_dna)
#         self.InputIndexlabel_dna.setGeometry(QtCore.QRect(10, 25, 461, 31))
#         font = QtGui.QFont()
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setItalic(False)
#         font.setWeight(75)
#         self.InputIndexlabel_dna.setFont(font)
#         self.InputIndexlabel_dna.setObjectName("InputIndexlabel_dna")
# =============================================================================
# =============================================================================
#         self.BWAIndexlabel = QtWidgets.QLabel(self.Index_dna)
#         self.BWAIndexlabel.setGeometry(QtCore.QRect(10, 90, 141, 17))
#         self.BWAIndexlabel.setObjectName("BWAIndexlabel")
#         self.BWAIndexlineEdit = QtWidgets.QLineEdit(self.Index_dna)
#         self.BWAIndexlineEdit.setGeometry(QtCore.QRect(170, 90, 331, 23))
#         self.BWAIndexlineEdit.setObjectName("BWAIndexlineEdit")
#         self.BWAIndexErrortext = QtWidgets.QLabel(self.Index_dna)
#         self.BWAIndexErrortext.setGeometry(QtCore.QRect(170, 113, 331, 22))
#         self.BWAIndexErrortext.setObjectName("BWAIndexErrortext")
#         self.BWAIndexErrortext.setStyleSheet("color: red")
#         self.BWAIndexErrortext.setFont(font_label)
#         self.BWAIndexpushButton = QtWidgets.QPushButton(self.Index_dna)
#         self.BWAIndexpushButton.setGeometry(QtCore.QRect(600, 90, 30, 25))
#         self.BWAIndexpushButton.setObjectName("BWAIndexpushButton")
# =============================================================================
       
        ##index_progressbar##
# =============================================================================
#         self.progressBar_sub2_dna = QtWidgets.QProgressBar(self.Index_dna)
#         self.progressBar_sub2_dna.setGeometry(QtCore.QRect(10, 230, 665, 17))
#         self.progressBar_sub2_dna.setProperty("value", 0)
#         self.progressBar_sub2_dna.setObjectName("progressBar_sub2_dna")
# =============================================================================
# =============================================================================
#         self.progressBar_sub2Label = QtWidgets.QLabel(self.centralwidget)
#         self.progressBar_sub2Label.setGeometry(QtCore.QRect(500, 600, 510, 17))
#         self.progressBar_sub2Label.setObjectName("progressBar_sub2Label")
# =============================================================================
# =============================================================================
#         self.CreateIndexpushButton_dna = QtWidgets.QPushButton(self.Index_dna)
#         self.CreateIndexpushButton_dna.setGeometry(QtCore.QRect(350, 210, 150, 23))
#         self.CreateIndexpushButton_dna.setObjectName("CreateIndexpushButton_dna")
#         self.CreateSnakefileforIndexpushButton_dna = QtWidgets.QPushButton(self.Index_dna)
#         self.CreateSnakefileforIndexpushButton_dna.setGeometry(QtCore.QRect(170, 210, 170, 23))
#         self.CreateSnakefileforIndexpushButton_dna.setObjectName("CreateSnakefileforIndexpushButton_dna")
# =============================================================================
# =============================================================================
#         self.Bowtie2dIndexlabel = QtWidgets.QLabel(self.Index_dna)
#         self.Bowtie2dIndexlabel.setGeometry(QtCore.QRect(10, 120, 121, 17))
#         self.Bowtie2dIndexlabel.setObjectName("Bowtie2dIndexlabel")
#         self.Bowtie2dIndexlineEdit = QtWidgets.QLineEdit(self.Index_dna)
#         self.Bowtie2dIndexlineEdit.setGeometry(QtCore.QRect(170, 120, 331, 23))
#         self.Bowtie2dIndexlineEdit.setObjectName("Bowtie2dIndexlineEdit")
#         self.Bowtie2dIndexpushButton = QtWidgets.QPushButton(self.Index_dna)
#         self.Bowtie2dIndexpushButton.setGeometry(QtCore.QRect(550, 120, 99, 23))
#         self.Bowtie2dIndexpushButton.setObjectName("Bowtie2dIndexpushButton")
# =============================================================================
# =============================================================================
#         self.SalmonIndexlabel = QtWidgets.QLabel(self.Index_dna)
#         self.SalmonIndexlabel.setGeometry(QtCore.QRect(10, 110, 121, 17))
#         self.SalmonIndexlabel.setObjectName("SalmonIndexlabel")
#         self.SalmonIndexlineEdit = QtWidgets.QLineEdit(self.Index_dna)
#         self.SalmonIndexlineEdit.setGeometry(QtCore.QRect(170, 100, 441, 27))
#         self.SalmonIndexlineEdit.setObjectName("SalmonIndexlineEdit")
#         self.Bowtie2Indexlabel = QtWidgets.QLabel(self.Index_dna)
#         self.Bowtie2Indexlabel.setGeometry(QtCore.QRect(10, 140, 121, 17))
#         self.Bowtie2Indexlabel.setObjectName("Bowtie2Indexlabel")
#         self.Bowtie2IndexlineEdit = QtWidgets.QLineEdit(self.Index_dna)
#         self.Bowtie2IndexlineEdit.setGeometry(QtCore.QRect(170, 130, 441, 27))
#         self.Bowtie2IndexlineEdit.setObjectName("Bowtie2IndexlineEdit")
# =============================================================================
# =============================================================================
#         self.SalmonIndexpushButton = QtWidgets.QPushButton(self.Index_dna)
#         self.SalmonIndexpushButton.setGeometry(QtCore.QRect(650, 100, 99, 27))
#         self.SalmonIndexpushButton.setObjectName("SalmonIndexpushButton")
#         self.Bowtie2IndexpushButton = QtWidgets.QPushButton(self.Index_dna)
#         self.Bowtie2IndexpushButton.setGeometry(QtCore.QRect(650, 130, 99, 27))
#         self.Bowtie2IndexpushButton.setObjectName("Bowtie2IndexpushButton")
# =============================================================================
        ###
# =============================================================================
#         self.nextbuttonindexDNA = QtWidgets.QPushButton(self.Index_dna)
#         self.nextbuttonindexDNA.setGeometry(QtCore.QRect(635, 400, 45, 45))
#         self.nextbuttonqcDNA.setObjectName("nextbuttonindexDNA")
#         ###
#         self.previousbuttonindexDNA = QtWidgets.QPushButton(self.Index_dna)
#         self.previousbuttonindexDNA.setGeometry(QtCore.QRect(10, 400, 45, 45))
#         self.previousbuttonindexDNA.setObjectName("previousbuttonindexDNA")
#         
#         self.DNAtabWidget.addTab(self.Index_dna, "")
#         ## End ##
#         ## Add Params ##
#         
#         self.Params_dna = QtWidgets.QWidget()
#         self.Params_dna.setObjectName("Params_dna")
# =============================================================================
# =============================================================================
#         font_param = QtGui.QFont()
#         font_param.setBold(True)
# #        self.Params_dna.setGeometry(QtCore.QRect(10, 10, 50, 17))
#         self.AlignerParamlabeldna = QtWidgets.QLabel(self.Params_dna)
#         self.AlignerParamlabeldna.setGeometry(QtCore.QRect(10, 10, 81, 17))
#         self.AlignerParamlabeldna.setObjectName('AlignerParamlabeldna')
#         self.AlignerParamlabeldna.setFont(font_param)
#         self.VCParamlabeldna = QtWidgets.QLabel(self.Params_dna)
#         self.VCParamlabeldna.setGeometry(QtCore.QRect(10, 98, 81, 17))
#         self.VCParamlabeldna.setObjectName('VCParamlabeldna')
#         self.VCParamlabeldna.setFont(font_param)
#         self.AnnotatorParamlabeldna = QtWidgets.QLabel(self.Params_dna)
#         self.AnnotatorParamlabeldna.setGeometry(QtCore.QRect(10, 186, 81, 17))
#         self.AnnotatorParamlabeldna.setObjectName('AnnotatorParamlabeldna')
#         self.AnnotatorParamlabeldna.setFont(font_param)
#         
#         ##set of lbels and lineedits for params##
#         self.param1_label_dna_1 = QtWidgets.QLabel(self.Params_dna)
#         self.param1_label_dna_1.setGeometry(QtCore.QRect(20, 40, 91, 18))
#         self.param1_lineEdit_dna_1 = QtWidgets.QLineEdit(self.Params_dna)
#         self.param1_lineEdit_dna_1.setGeometry(QtCore.QRect(120, 40, 70, 18))
#         self.param1_label_dna_2 = QtWidgets.QLabel(self.Params_dna)
#         self.param1_label_dna_2.setGeometry(QtCore.QRect(20, 65, 91, 18))
#         self.param1_lineEdit_dna_2 = QtWidgets.QLineEdit(self.Params_dna)
#         self.param1_lineEdit_dna_2.setGeometry(QtCore.QRect(120, 65, 70, 18))
#         self.param1_label_dna_3 = QtWidgets.QLabel(self.Params_dna)
#         self.param1_label_dna_3.setGeometry(QtCore.QRect(200, 40, 91, 18))
#         self.param1_lineEdit_dna_3 = QtWidgets.QLineEdit(self.Params_dna)
#         self.param1_lineEdit_dna_3.setGeometry(QtCore.QRect(280, 40, 70, 18))
#         self.param1_label_dna_4 = QtWidgets.QLabel(self.Params_dna)
#         self.param1_label_dna_4.setGeometry(QtCore.QRect(200, 65, 91, 18))
#         self.param1_lineEdit_dna_4 = QtWidgets.QLineEdit(self.Params_dna)
#         self.param1_lineEdit_dna_4.setGeometry(QtCore.QRect(280, 65, 70, 18))
#         self.param1_label_dna_5 = QtWidgets.QLabel(self.Params_dna)
#         self.param1_label_dna_5.setGeometry(QtCore.QRect(360, 40, 91, 18))
#         self.param1_lineEdit_dna_5 = QtWidgets.QLineEdit(self.Params_dna)
#         self.param1_lineEdit_dna_5.setGeometry(QtCore.QRect(440, 40, 70, 18))
#         self.param1_label_dna_6 = QtWidgets.QLabel(self.Params_dna)
#         self.param1_label_dna_6.setGeometry(QtCore.QRect(360, 65, 91, 18))
#         self.param1_lineEdit_dna_6 = QtWidgets.QLineEdit(self.Params_dna)
#         self.param1_lineEdit_dna_6.setGeometry(QtCore.QRect(440, 65, 70, 18))
#         self.aligner_add_dna = QtWidgets.QPushButton(self.Params_dna)
#         self.aligner_add_dna.setGeometry(QtCore.QRect(530, 45, 70, 30))
#         self.aligner_add_dna.setText("Advanced")
#         
#         
#         self.param2_label_dna_1 = QtWidgets.QLabel(self.Params_dna)
#         self.param2_label_dna_1.setGeometry(QtCore.QRect(20, 130, 91, 18))
#         self.param2_lineEdit_dna_1 = QtWidgets.QLineEdit(self.Params_dna)
#         self.param2_lineEdit_dna_1.setGeometry(QtCore.QRect(120, 130, 70, 18))
#         self.param2_label_dna_2 = QtWidgets.QLabel(self.Params_dna)
#         self.param2_label_dna_2.setGeometry(QtCore.QRect(20, 155, 91, 18))
#         self.param2_lineEdit_dna_2 = QtWidgets.QLineEdit(self.Params_dna)
#         self.param2_lineEdit_dna_2.setGeometry(QtCore.QRect(120, 155, 70, 18))
#         self.param2_label_dna_3 = QtWidgets.QLabel(self.Params_dna)
#         self.param2_label_dna_3.setGeometry(QtCore.QRect(200, 130, 91, 18))
#         self.param2_lineEdit_dna_3 = QtWidgets.QLineEdit(self.Params_dna)
#         self.param2_lineEdit_dna_3.setGeometry(QtCore.QRect(280, 130, 70, 18))
#         self.param2_label_dna_4 = QtWidgets.QLabel(self.Params_dna)
#         self.param2_label_dna_4.setGeometry(QtCore.QRect(200, 155, 91, 18))
#         self.param2_lineEdit_dna_4 = QtWidgets.QLineEdit(self.Params_dna)
#         self.param2_lineEdit_dna_4.setGeometry(QtCore.QRect(280, 155, 70, 18))
#         self.param2_label_dna_5 = QtWidgets.QLabel(self.Params_dna)
#         self.param2_label_dna_5.setGeometry(QtCore.QRect(360,130, 91, 18))
#         self.param2_lineEdit_dna_5 = QtWidgets.QLineEdit(self.Params_dna)
#         self.param2_lineEdit_dna_5.setGeometry(QtCore.QRect(440, 130, 70, 18))
#         self.param2_label_dna_6 = QtWidgets.QLabel(self.Params_dna)
#         self.param2_label_dna_6.setGeometry(QtCore.QRect(360, 155, 91, 18))
#         self.param2_lineEdit_dna_6 = QtWidgets.QLineEdit(self.Params_dna)
#         self.param2_lineEdit_dna_6.setGeometry(QtCore.QRect(440, 155, 70, 18))
#         self.vc_add_dna = QtWidgets.QPushButton(self.Params_dna)
#         self.vc_add_dna.setGeometry(QtCore.QRect(530, 135, 70, 30))
#         self.vc_add_dna.setText("Advanced")
#         
#         self.param3_label_dna_1 = QtWidgets.QLabel(self.Params_dna)
#         self.param3_label_dna_1.setGeometry(QtCore.QRect(20, 220, 91, 18))
#         self.param3_lineEdit_dna_1 = QtWidgets.QLineEdit(self.Params_dna)
#         self.param3_lineEdit_dna_1.setGeometry(QtCore.QRect(120, 220, 70, 18))
#         self.param3_label_dna_2 = QtWidgets.QLabel(self.Params_dna)
#         self.param3_label_dna_2.setGeometry(QtCore.QRect(20, 245, 91, 18))
#         self.param3_lineEdit_dna_2 = QtWidgets.QLineEdit(self.Params_dna)
#         self.param3_lineEdit_dna_2.setGeometry(QtCore.QRect(120, 245, 70, 18))
#         self.param3_label_dna_3 = QtWidgets.QLabel(self.Params_dna)
#         self.param3_label_dna_3.setGeometry(QtCore.QRect(200, 220, 91, 18))
#         self.param3_lineEdit_dna_3 = QtWidgets.QLineEdit(self.Params_dna)
#         self.param3_lineEdit_dna_3.setGeometry(QtCore.QRect(280, 220, 70, 18))
#         self.param3_label_dna_4 = QtWidgets.QLabel(self.Params_dna)
#         self.param3_label_dna_4.setGeometry(QtCore.QRect(200, 245, 91, 18))
#         self.param3_lineEdit_dna_4 = QtWidgets.QLineEdit(self.Params_dna)
#         self.param3_lineEdit_dna_4.setGeometry(QtCore.QRect(280, 245, 70, 18))
#         self.param3_label_dna_5 = QtWidgets.QLabel(self.Params_dna)
#         self.param3_label_dna_5.setGeometry(QtCore.QRect(360, 220, 91, 18))
#         self.param3_lineEdit_dna_5 = QtWidgets.QLineEdit(self.Params_dna)
#         self.param3_lineEdit_dna_5.setGeometry(QtCore.QRect(440, 220, 70, 18))
#         self.param3_label_dna_6 = QtWidgets.QLabel(self.Params_dna)
#         self.param3_label_dna_6.setGeometry(QtCore.QRect(360, 245, 91, 18))
#         self.param3_lineEdit_dna_6 = QtWidgets.QLineEdit(self.Params_dna)
#         self.param3_lineEdit_dna_6.setGeometry(QtCore.QRect(440, 245, 70, 18))
#         self.annotator_add_dna = QtWidgets.QPushButton(self.Params_dna)
#         self.annotator_add_dna.setGeometry(QtCore.QRect(530, 225, 70, 30))
#         self.annotator_add_dna.setText("Advanced")
#         
#         self.param1_label_dna_1.hide()
#         self.param1_label_dna_2.hide()
#         self.param1_label_dna_3.hide()
#         self.param1_label_dna_4.hide()
#         self.param1_label_dna_5.hide()
#         self.param1_label_dna_6.hide()
#         self.param1_lineEdit_dna_1.hide()
#         self.param1_lineEdit_dna_2.hide()
#         self.param1_lineEdit_dna_3.hide()
#         self.param1_lineEdit_dna_4.hide()
#         self.param1_lineEdit_dna_5.hide()
#         self.param1_lineEdit_dna_6.hide()
#         
#         self.param2_label_dna_1.hide()
#         self.param2_label_dna_2.hide()
#         self.param2_label_dna_3.hide()
#         self.param2_label_dna_4.hide()
#         self.param2_label_dna_5.hide()
#         self.param2_label_dna_6.hide()
#         self.param2_lineEdit_dna_1.hide()
#         self.param2_lineEdit_dna_2.hide()
#         self.param2_lineEdit_dna_3.hide()
#         self.param2_lineEdit_dna_4.hide()
#         self.param2_lineEdit_dna_5.hide()
#         self.param2_lineEdit_dna_6.hide()
#         
#         self.param3_label_dna_1.hide()
#         self.param3_label_dna_2.hide()
#         self.param3_label_dna_3.hide()
#         self.param3_label_dna_4.hide()
#         self.param3_label_dna_5.hide()
#         self.param3_label_dna_6.hide()
#         self.param3_lineEdit_dna_1.hide()
#         self.param3_lineEdit_dna_2.hide()
#         self.param3_lineEdit_dna_3.hide()
#         self.param3_lineEdit_dna_4.hide()
#         self.param3_lineEdit_dna_5.hide()
#         self.param3_lineEdit_dna_6.hide()
# =============================================================================
        
# =============================================================================
#         self.nextbuttonparamsDNA = QtWidgets.QPushButton(self.Params_dna)
#         self.nextbuttonparamsDNA.setGeometry(QtCore.QRect(560, 400, 110, 35))
#         self.nextbuttonparamsDNA.setObjectName("nextbuttonparamsDNA")
#         ###
#         self.previousbuttonparamsDNA = QtWidgets.QPushButton(self.Params_dna)
#         self.previousbuttonparamsDNA.setGeometry(QtCore.QRect(10, 400, 45, 45))
#         self.previousbuttonparamsDNA.setObjectName("previousbuttonparamsDNA")
# 
#         self.DNAtabWidget.addTab(self.Params_dna, "")
# =============================================================================
        ## End ##
        
        ##Add Run##
        self.run_dna = QtWidgets.QWidget()
        self.run_dna.setObjectName("run_dna")
        
        self.RunButton_dna = QtWidgets.QPushButton(self.run_dna)
        self.RunButton_dna.setGeometry(QtCore.QRect(400, 50, 170, 170))
        self.RunButton_dna.setObjectName("RunButton_dna")
        self.RunLabel_dna = QtWidgets.QLabel(self.run_dna)
        self.RunLabel_dna.setGeometry(QtCore.QRect(465, 248, 180, 17))
        self.RunLabel_dna.setObjectName("RunLabel_dna")
        
        
        self.RunButtonErroricon_dna = QtWidgets.QPushButton(self.run_dna)
        self.RunButtonErroricon_dna.setGeometry(QtCore.QRect(580, 145, 30, 30))
        self.RunButtonErroricon_dna.setToolTip("Click Run Button and Run Again!")
        self.RunButtonErroricon_dna.setFont(font_label)
        self.RunButtonErroricon_dna.setIcon(QtGui.QIcon("./icons/warning.svg"))
        self.RunButtonErroricon_dna.hide()            
        
        self.ResultsButton_dna = QtWidgets.QPushButton(self.run_dna)
        self.ResultsButton_dna.setGeometry(QtCore.QRect(100, 50, 170, 170))
        self.ResultsButton_dna.setObjectName("ResultsButton_dna")
        self.ResultsLabel_dna = QtWidgets.QLabel(self.run_dna)
        self.ResultsLabel_dna.setGeometry(QtCore.QRect(145, 248, 180, 17))
        self.ResultsLabel_dna.setObjectName("ResultsLabel_dna")          
        
        
        self.ResultsButtonErroricon_dna = QtWidgets.QPushButton(self.run_dna)
        self.ResultsButtonErroricon_dna.setGeometry(QtCore.QRect(280, 145, 30, 30))
        self.ResultsButtonErroricon_dna.setToolTip("Click Run Button and Run Again!")
        self.ResultsButtonErroricon_dna.setFont(font_label)
        self.ResultsButtonErroricon_dna.setIcon(QtGui.QIcon("./icons/warning.svg"))
        self.ResultsButtonErroricon_dna.hide()                      
        
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
        self.RunButtoninfoicon_dna.setGeometry(QtCore.QRect(580, 120, 20, 20))
        self.RunButtoninfoicon_dna.setToolTip("xxxxxxxxx!")
        self.RunButtoninfoicon_dna.setFont(font_info)
        self.RunButtoninfoicon_dna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.RunButtoninfoicon_dna.setIconSize(QtCore.QSize(13, 13)) 
        
        self.ResultsButtoninfoicon_dna = QtWidgets.QPushButton(self.run_dna)
        self.ResultsButtoninfoicon_dna.setFlat(True)
        self.ResultsButtoninfoicon_dna.setGeometry(QtCore.QRect(280, 120, 20, 20))
        self.ResultsButtoninfoicon_dna.setToolTip("xxxxxxxxx!")
        self.ResultsButtoninfoicon_dna.setFont(font_info)
        self.ResultsButtoninfoicon_dna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.ResultsButtoninfoicon_dna.setIconSize(QtCore.QSize(13, 13))        
        
        
        self.DNAtabWidget.addTab(self.run_dna, "")
        ##End##
        ##Add Result DNA##
        self.result_dna = QtWidgets.QWidget()
        self.result_dna.setObjectName("result_dna")
        
        self.DNAtabWidget.addTab(self.result_dna, "")
        self.label_result1_dna = QtWidgets.QLabel(self.result_dna)
        self.label_result1_dna.setGeometry(QtCore.QRect(150, 80, 200, 23))
        self.label_result1_dna.setText("Run statistics")
        self.pushbutton_result1_dna=QtWidgets.QPushButton(self.result_dna)
        self.pushbutton_result1_dna.setText("Click")
        self.pushbutton_result1_dna.setGeometry(QtCore.QRect(350, 80, 60, 23))
        self.label_result2_dna = QtWidgets.QLabel(self.result_dna)
        self.label_result2_dna.setGeometry(QtCore.QRect(150, 180, 200, 23))
        self.label_result2_dna.setText("Variants called")
        self.pushbutton_result2_dna=QtWidgets.QPushButton(self.result_dna)
        self.pushbutton_result2_dna.setText("Click")
        self.pushbutton_result2_dna.setGeometry(QtCore.QRect(350, 180, 60, 23))
        self.label_result3_dna = QtWidgets.QLabel(self.result_dna)
        self.label_result3_dna.setGeometry(QtCore.QRect(150, 280, 200, 23))
        self.label_result3_dna.setText("Annotated variants")
        self.pushbutton_result3_dna=QtWidgets.QPushButton(self.result_dna)
        self.pushbutton_result3_dna.setText("Click")
        self.pushbutton_result3_dna.setGeometry(QtCore.QRect(350, 280, 60, 23))
        ##End##        
        
        ## Add Create ##
#==============================================================================
#         self.Create_dna = QtWidgets.QWidget()
#         self.Create_dna.setObjectName("Create_dna")
# 
#         self.horizontalLayoutWidget_2_dna = QtWidgets.QWidget(self.Create_dna)
#         self.horizontalLayoutWidget_2_dna.setGeometry(QtCore.QRect(40, 100, 591, 31))
#         self.horizontalLayoutWidget_2_dna.setObjectName("horizontalLayoutWidget_2_dna")
#         self.horizontalLayout_7_dna = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2_dna)
#         self.horizontalLayout_7_dna.setContentsMargins(0, 0, 0, 0)
#         self.horizontalLayout_7_dna.setObjectName("horizontalLayout_7_dna")
#         self.CreateSnakefilepushButtonDNA = QtWidgets.QPushButton(self.horizontalLayoutWidget_2_dna)
#         self.CreateSnakefilepushButtonDNA.setObjectName("CreateSnakefilepushButtonDNA")
#         #self.CreateSnakefilepushButtonDNA.setEnabled(False)
#         self.horizontalLayout_7_dna.addWidget(self.CreateSnakefilepushButtonDNA)
#         self.CreateConfigpushButtonDNA = QtWidgets.QPushButton(self.horizontalLayoutWidget_2_dna)
#         self.CreateConfigpushButtonDNA.setObjectName("CreateConfigpushButtonDNA")
#         self.horizontalLayout_7_dna.addWidget(self.CreateConfigpushButtonDNA)
# 
#         self.DNAtabWidget.addTab(self.Create_dna, "")
#==============================================================================
        ## End ##
        self.PipelinetabWidget.addTab(self.DNAseq, "")

        self.RNAseq = QtWidgets.QWidget()
        self.RNAseq.setObjectName("RNAseq")
        self.RNAtabWidget = QtWidgets.QTabWidget(self.RNAseq)
        self.RNAtabWidget.setGeometry(QtCore.QRect(0, 0, 695, 507))
        self.RNAtabWidget.setMovable(False)
        self.RNAtabWidget.setTabBarAutoHide(False)
        self.RNAtabWidget.setObjectName("RNAtabWidget")
        self.RNAtabWidget.setStyleSheet("background-color: #F0F9EC")
        ## Make Input as first tab ##
        self.input_rna = QtWidgets.QWidget()
        self.input_rna.setObjectName("input_rna")
        self.SamplesYesradioButton_rna = QtWidgets.QRadioButton(self.input_rna)
        self.SamplesYesradioButton_rna.move(80, 20)
        self.SamplesYesradioButton_rna.setObjectName("SamplesYesradioButton_rna")
        self.SamplesYesradioButton_rna.setChecked(True)
        self.SamplesNoradioButton_rna = QtWidgets.QRadioButton(self.input_rna)
        self.SamplesNoradioButton_rna.move(450, 20)
        self.SamplesNoradioButton_rna.setObjectName("SamplesNoradioButton_rna")
        self.SampleOrlabel_rna = QtWidgets.QLabel(self.input_rna)
        self.SampleOrlabel_rna.move(320, 20)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.SampleOrlabel_rna.setFont(font)
        self.SampleOrlabel_rna.setObjectName("SampleOrlabel_rna")
# =============================================================================
#         self.WDlabelRNA = QtWidgets.QLabel(self.input_rna)
#         self.WDlabelRNA.setGeometry(QtCore.QRect(20, 80, 113, 23))
#         self.WDlabelRNA.setObjectName("SampleFilelabelRNA")
#         self.WDlabelRNA.setEnabled(True)
#         self.WDlineEditRNA = QtWidgets.QLineEdit(self.input_rna)
#         self.WDlineEditRNA.setGeometry(QtCore.QRect(200, 80, 385, 23))
#         self.WDlineEditRNA.setObjectName("SampleslineEditRNA")
#         self.WDlineEditRNA.setEnabled(True)
#         self.WDBrowseButtonRNA = QtWidgets.QPushButton(self.input_rna)
#         self.WDBrowseButtonRNA.setGeometry(QtCore.QRect(600, 80, 30, 25))
#         self.WDBrowseButtonRNA.setObjectName("SamplesBrowseButtonRNA")
#         self.WDBrowseButtonRNA.setEnabled(True)
#         self.WDErrortextRNA = QtWidgets.QLabel(self.input_rna)
#         self.WDErrortextRNA.setGeometry(QtCore.QRect(200, 105, 385, 23))
#         self.WDErrortextRNA.setFont(font_label)
#         self.WDErrortextRNA.setStyleSheet("color: red")
# =============================================================================
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
        self.TranscriptFilelabel = QtWidgets.QLabel(self.input_rna)
        self.TranscriptFilelabel.setGeometry(QtCore.QRect(20, 340, 201, 17))
        self.TranscriptFilelabel.setObjectName("TranscriptFilelabel")
        self.TranscriptlineEdit = QtWidgets.QLineEdit(self.input_rna)
        self.TranscriptlineEdit.setGeometry(QtCore.QRect(200, 340, 385, 23))
        self.TranscriptlineEdit.setObjectName("TranscriptlineEdit")
        self.TranscriptBrowseButton = QtWidgets.QPushButton(self.input_rna)
        self.TranscriptBrowseButton.setGeometry(QtCore.QRect(600, 340, 30, 25))
        self.TranscriptBrowseButton.setObjectName("TranscriptBrowseButton")
        self.TranscriptErrortextRNA = QtWidgets.QLabel(self.input_rna)
        self.TranscriptErrortextRNA.setGeometry(QtCore.QRect(200, 365, 385, 23))
        self.TranscriptErrortextRNA.setFont(font_label)
        self.TranscriptErrortextRNA.setStyleSheet("color: red")
        
        ###
#==============================================================================
#         self.nextbuttoninputRNA = QtWidgets.QPushButton(self.input_rna)
#         self.nextbuttoninputRNA.setGeometry(QtCore.QRect(635, 258, 45, 45))
#         self.nextbuttoninputRNA.setObjectName("nextbuttoninputRNA")
#==============================================================================
        ###
        
        font_label = QtGui.QFont()
        font_label.setPointSize(8.5)
        
#        self.FastaErrortextRNA.setText("Input Samples folder path")
        
#        self.AnnotatedErrortextRNA.setText("Input Samples folder path")
        
#        self.TranscriptErrortextRNA.setText("Input Samples folder path")
               
        
        
        self.nextbuttoninputRNA = QtWidgets.QPushButton(self.input_rna)
        self.nextbuttoninputRNA.setGeometry(QtCore.QRect(635, 400, 45, 45))
        self.nextbuttoninputRNA.setObjectName("nextbuttoninputRNA")
        
        #####info icon####
        ###rna###
        font_info = QtGui.QFont()
        font_info.setPointSize(8.5)        
        
# =============================================================================
#         self.WDinfoicon_rna = QtWidgets.QPushButton(self.input_rna)
#         self.WDinfoicon_rna.setFlat(True)
#         self.WDinfoicon_rna.setGeometry(QtCore.QRect(133, 84, 20, 20))
#         self.WDinfoicon_rna.setToolTip("xxxxxxxxx!")
#         self.WDinfoicon_rna.setFont(font_info)
#         self.WDinfoicon_rna.setIcon(QtGui.QIcon("./icons/info.svg"))
#         self.WDinfoicon_rna.setIconSize(QtCore.QSize(13, 13))
# =============================================================================
        
        self.SampleFolderinfoicon_rna = QtWidgets.QPushButton(self.input_rna)
        self.SampleFolderinfoicon_rna.setFlat(True)
        self.SampleFolderinfoicon_rna.setGeometry(QtCore.QRect(120, 139, 20, 20))
        self.SampleFolderinfoicon_rna.setToolTip("xxxxxxxxx!")
        self.SampleFolderinfoicon_rna.setFont(font_info)
        self.SampleFolderinfoicon_rna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.SampleFolderinfoicon_rna.setIconSize(QtCore.QSize(13, 13))
        
        self.Sampletableinfoicon_rna = QtWidgets.QPushButton(self.input_rna)
        self.Sampletableinfoicon_rna.setFlat(True)
        self.Sampletableinfoicon_rna.setGeometry(QtCore.QRect(116, 190, 20, 20))
        self.Sampletableinfoicon_rna.setToolTip("xxxxxxxxx!")
        self.Sampletableinfoicon_rna.setFont(font_info)
        self.Sampletableinfoicon_rna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.Sampletableinfoicon_rna.setIconSize(QtCore.QSize(13, 13))
        
        self.FastaFileinfoicon_rna = QtWidgets.QPushButton(self.input_rna)
        self.FastaFileinfoicon_rna.setFlat(True)
        self.FastaFileinfoicon_rna.setGeometry(QtCore.QRect(84, 240, 20, 20))
        self.FastaFileinfoicon_rna.setToolTip("xxxxxxxxx!")
        self.FastaFileinfoicon_rna.setFont(font_info)
        self.FastaFileinfoicon_rna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.FastaFileinfoicon_rna.setIconSize(QtCore.QSize(13, 13))  
        
        self.AnnotatedFileinfoicon_rna = QtWidgets.QPushButton(self.input_rna)
        self.AnnotatedFileinfoicon_rna.setFlat(True)
        self.AnnotatedFileinfoicon_rna.setGeometry(QtCore.QRect(114, 290, 20, 20))
        self.AnnotatedFileinfoicon_rna.setToolTip("xxxxxxxxx!")
        self.AnnotatedFileinfoicon_rna.setFont(font_info)
        self.AnnotatedFileinfoicon_rna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.AnnotatedFileinfoicon_rna.setIconSize(QtCore.QSize(13, 13)) 

        self.TranscriptFileinfoicon_rna = QtWidgets.QPushButton(self.input_rna)
        self.TranscriptFileinfoicon_rna.setFlat(True)
        self.TranscriptFileinfoicon_rna.setGeometry(QtCore.QRect(114, 339, 20, 20))
        self.TranscriptFileinfoicon_rna.setToolTip("xxxxxxxxx!")
        self.TranscriptFileinfoicon_rna.setFont(font_info)
        self.TranscriptFileinfoicon_rna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.TranscriptFileinfoicon_rna.setIconSize(QtCore.QSize(13, 13))         
        
        self.SamplesYesradioinfoicon_rna = QtWidgets.QPushButton(self.input_rna)
        self.SamplesYesradioinfoicon_rna.setFlat(True)
        self.SamplesYesradioinfoicon_rna.setGeometry(QtCore.QRect(218, 23, 20, 20))
        self.SamplesYesradioinfoicon_rna.setToolTip("xxxxxxxxx!")
        self.SamplesYesradioinfoicon_rna.setFont(font_info)
        self.SamplesYesradioinfoicon_rna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.SamplesYesradioinfoicon_rna.setIconSize(QtCore.QSize(13, 13))       
        
        
        self.SamplesNoradioinfoicon_rna = QtWidgets.QPushButton(self.input_rna)
        self.SamplesNoradioinfoicon_rna.setFlat(True)
        self.SamplesNoradioinfoicon_rna.setGeometry(QtCore.QRect(583, 23, 20, 20))
        self.SamplesNoradioinfoicon_rna.setToolTip("xxxxxxxxx!")
        self.SamplesNoradioinfoicon_rna.setFont(font_info)
        self.SamplesNoradioinfoicon_rna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.SamplesNoradioinfoicon_rna.setIconSize(QtCore.QSize(13, 13))
        
        self.RNAtabWidget.addTab(self.input_rna, "")
        ## End ##
        
        ## Add QC ##
        self.QC_rna = QtWidgets.QWidget()
        self.QC_rna.setObjectName("QC_rna")
        ##QC_RNA Added##
        self.QCresults_rna = QtWidgets.QPushButton(self.QC_rna)
        self.QCresults_rna.setGeometry(QtCore.QRect(10, 30, 150, 23))
        self.QCresults_rna.setText("Quality Control Results")
        self.QCresults_rna.setStyleSheet("background-color: #578446")
        self.QCresultsButtonErroricon_rna = QtWidgets.QPushButton(self.QC_rna)
        self.QCresultsButtonErroricon_rna.setGeometry(QtCore.QRect(186, 32, 20, 20))
        self.QCresultsButtonErroricon_rna.setToolTip("Check and Run View FastQC Results Again!")
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
#==============================================================================
#         self.fastQClabel_rna = QtWidgets.QLabel(self.QC_rna)
#         self.fastQClabel_rna.setGeometry(QtCore.QRect(10, 100, 67, 17))
#         self.fastQClabel_rna.setObjectName("fastQClabel_rna")
#==============================================================================
#==============================================================================
#         self.QClineEdit_rna = QtWidgets.QLineEdit(self.QC_rna)
#         self.QClineEdit_rna.setGeometry(QtCore.QRect(120, 100, 481, 23))
#         self.QClineEdit_rna.setObjectName("QClineEdit_rna")
#==============================================================================
        self.CutadaptlineEdit_rna = QtWidgets.QLineEdit(self.QC_rna)
        self.CutadaptlineEdit_rna.setGeometry(QtCore.QRect(120, 200, 481, 23))
        self.CutadaptlineEdit_rna.setObjectName("CutadaptlineEdit_rna")
        self.Cutadaptlabel_rna = QtWidgets.QLabel(self.QC_rna)
        self.Cutadaptlabel_rna.setGeometry(QtCore.QRect(10, 200, 67, 17))
        self.Cutadaptlabel_rna.setObjectName("Cutadaptlabel_rna")
        self.Cutadaptlabel_rna.setEnabled(False)
        self.CutadaptlineEdit_rna.setEnabled(False)
# =============================================================================
#         self.MultiQClineEdit_rna = QtWidgets.QLineEdit(self.QC_rna)
#         self.MultiQClineEdit_rna.setGeometry(QtCore.QRect(120, 180, 481, 23))
#         self.MultiQClineEdit_rna.setObjectName("MultiQClineEdit_rna")
#         self.MultiQClabel_rna = QtWidgets.QLabel(self.QC_rna)
#         self.MultiQClabel_rna.setGeometry(QtCore.QRect(10, 180, 67, 17))
#         self.MultiQClabel_rna.setObjectName("MultiQClabel_rna")
# =============================================================================
        self.horizontalLayoutWidget_rna = QtWidgets.QWidget(self.QC_rna)
        self.horizontalLayoutWidget_rna.setGeometry(QtCore.QRect(235, 273, 240, 31))
        self.horizontalLayoutWidget_rna.setObjectName("horizontalLayoutWidget_rna")
        self.horizontalLayout_4_rna = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_rna)
        self.horizontalLayout_4_rna.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4_rna.setObjectName("horizontalLayout_4_rna")
# =============================================================================
#         self.CreateSnakefilepushButton_rna = QtWidgets.QPushButton(self.horizontalLayoutWidget_rna)
#         self.CreateSnakefilepushButton_rna.setObjectName("CreateSnakefilepushButton_rna")
#         self.horizontalLayout_4_rna.addWidget(self.CreateSnakefilepushButton_rna)
#         self.CreateConfigfilepushButton_rna = QtWidgets.QPushButton(self.horizontalLayoutWidget_rna)
#         self.CreateConfigfilepushButton_rna.setObjectName("CreateConfigfilepushButton_rna")
#         self.horizontalLayout_4_rna.addWidget(self.CreateConfigfilepushButton_rna)
# =============================================================================
        self.RunQCpushButton_rna = QtWidgets.QPushButton(self.horizontalLayoutWidget_rna)
        self.RunQCpushButton_rna.setObjectName("RunQCpushButton_rna")
        self.RunQCpushButton_rna.setEnabled(False)
        self.horizontalLayout_4_rna.addWidget(self.RunQCpushButton_rna)
        self.RunQCButtonErroricon_rna = QtWidgets.QPushButton(self.QC_rna)
        self.RunQCButtonErroricon_rna.setGeometry(QtCore.QRect(500, 277, 20, 20))
        self.RunQCButtonErroricon_rna.setToolTip("Check and Run Trimming Again!")
        self.RunQCButtonErroricon_rna.setFont(font_label)
        self.RunQCButtonErroricon_rna.setIcon(QtGui.QIcon("./icons/warning.svg"))
#        self.horizontalLayout_4.addWidget(self.RunQCButtonErroricon_rna)
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
        self.QCresultsinfoicon_rna.setToolTip("xxxxxxxxx!")
        self.QCresultsinfoicon_rna.setFont(font_info)
        self.QCresultsinfoicon_rna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.QCresultsinfoicon_rna.setIconSize(QtCore.QSize(13, 13))          
        
        self.QClabelinfoicon_rna = QtWidgets.QPushButton(self.QC_rna)
        self.QClabelinfoicon_rna.setFlat(True)
        self.QClabelinfoicon_rna.setGeometry(QtCore.QRect(131, 87, 20, 20))
        self.QClabelinfoicon_rna.setToolTip("xxxxxxxxx!")
        self.QClabelinfoicon_rna.setFont(font_info)
        self.QClabelinfoicon_rna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.QClabelinfoicon_rna.setIconSize(QtCore.QSize(13, 13))          
        
        self.Cutadaptlabelinfoicon_rna = QtWidgets.QPushButton(self.QC_rna)
        self.Cutadaptlabelinfoicon_rna.setFlat(True)
        self.Cutadaptlabelinfoicon_rna.setGeometry(QtCore.QRect(70, 199, 20, 20))
        self.Cutadaptlabelinfoicon_rna.setToolTip("xxxxxxxxx!")
        self.Cutadaptlabelinfoicon_rna.setFont(font_info)
        self.Cutadaptlabelinfoicon_rna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.Cutadaptlabelinfoicon_rna.setIconSize(QtCore.QSize(13, 13))    
        
        self.RunQCpushButtoninfoicon_rna = QtWidgets.QPushButton(self.QC_rna)
        self.RunQCpushButtoninfoicon_rna.setFlat(True)
        self.RunQCpushButtoninfoicon_rna.setGeometry(QtCore.QRect(480, 277, 20, 20))
        self.RunQCpushButtoninfoicon_rna.setToolTip("xxxxxxxxx!")
        self.RunQCpushButtoninfoicon_rna.setFont(font_info)
        self.RunQCpushButtoninfoicon_rna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.RunQCpushButtoninfoicon_rna.setIconSize(QtCore.QSize(13, 13))             
        
        self.RNAtabWidget.addTab(self.QC_rna, "")
        ## End ##
        self.Tool_rna = QtWidgets.QWidget()
        self.Tool_rna.setObjectName("Tool_rna")
        
        self.create_aligner_groupbox_rna()
        self.create_em_groupbox()
        self.create_de_groupbox()
        self.create_group_next_rna()
        
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
# =============================================================================
#         
#         
#         
#         self.layoutWidget_2 = QtWidgets.QWidget(self.Tool_rna)
#         self.layoutWidget_2.setGeometry(QtCore.QRect(50, 80, 571, 29))
#         self.layoutWidget_2.setObjectName("layoutWidget_2")
#         self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
#         self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
#         self.horizontalLayout_6.setSpacing(20)
#         self.horizontalLayout_6.setObjectName("horizontalLayout_6")
#         self.AlignerlabelRNA = QtWidgets.QLabel(self.layoutWidget_2)
#         self.AlignerlabelRNA.setObjectName("AlignerlabelRNA")
#         self.horizontalLayout_6.addWidget(self.AlignerlabelRNA)
# # =============================================================================
# #         self.AlignercomboBoxRNA = QtWidgets.QComboBox(self.layoutWidget_2)
# #         self.AlignercomboBoxRNA.setObjectName("AlignercomboBoxRNA")
# # #        self.AlignercomboBoxRNA.setStyleSheet("background-color: #578446")
# #         self.AlignercomboBoxRNA.addItem("")
# #         self.AlignercomboBoxRNA.addItem("")
# #         self.AlignercomboBoxRNA.addItem("")
# #         self.AlignercomboBoxRNA.addItem("")
# #         self.horizontalLayout_6.addWidget(self.AlignercomboBoxRNA)
# # =============================================================================
#         self.EMlabelRNa = QtWidgets.QLabel(self.layoutWidget_2)
#         self.EMlabelRNa.setObjectName("EMlabelRNa")
#         self.horizontalLayout_6.addWidget(self.EMlabelRNa)
# # =============================================================================
# #         self.EMcomboBoxRNA = QtWidgets.QComboBox(self.layoutWidget_2)
# #         self.EMcomboBoxRNA.setObjectName("EMcomboBoxRNA")
# #         self.EMcomboBoxRNA.addItem("")
# #         self.EMcomboBoxRNA.addItem("")
# #         self.EMcomboBoxRNA.addItem("")
# #         self.EMcomboBoxRNA.addItem("")
# #         self.horizontalLayout_6.addWidget(self.EMcomboBoxRNA)
# # =============================================================================
#         self.DElabelRNA = QtWidgets.QLabel(self.layoutWidget_2)
#         self.DElabelRNA.setObjectName("DElabelRNA")
#         self.horizontalLayout_6.addWidget(self.DElabelRNA)
# =============================================================================
# =============================================================================
#         self.DEcomboBoxRNA = QtWidgets.QComboBox(self.layoutWidget_2)
#         self.DEcomboBoxRNA.setObjectName("DEcomboBoxRNA")
#         self.DEcomboBoxRNA.addItem("")
#         self.DEcomboBoxRNA.addItem("")
#         self.DEcomboBoxRNA.addItem("")
#         self.horizontalLayout_6.addWidget(self.DEcomboBoxRNA)
# =============================================================================
        ###
# =============================================================================
#         self.nextbuttontoolRNA = QtWidgets.QPushButton(self.Tool_rna)
#         self.nextbuttontoolRNA.setGeometry(QtCore.QRect(635, 258, 45, 45))
#         self.nextbuttontoolRNA.setObjectName("nextbuttontoolRNA")
#         ###
#         self.previousbuttontoolRNA = QtWidgets.QPushButton(self.Tool_rna)
#         self.previousbuttontoolRNA.setGeometry(QtCore.QRect(10, 258, 45, 45))
#         self.previousbuttontoolRNA.setObjectName("previousbuttontoolRNA")
#         
#         self.RNAtabWidget.addTab(self.Tool_rna, "")
# =============================================================================
        ## Add Index ##
# =============================================================================
#         self.Index_rna = QtWidgets.QWidget()
#         self.Index_rna.setObjectName("Index_rna")
# =============================================================================
#        self.RNAtabWidget.addTab(self.Index_rna, "")
        ## Added from QC_Index###
# =============================================================================
#         self.InputIndexlabel = QtWidgets.QLabel(self.Index_rna)
#         self.InputIndexlabel.setGeometry(QtCore.QRect(10, 25, 461, 31))
#         font = QtGui.QFont()
#         font.setFamily("Liberation Sans")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setItalic(False)
#         font.setWeight(75)
#         self.InputIndexlabel.setFont(font)
#         self.InputIndexlabel.setObjectName("InputIndexlabel")
#         self.StarIndexlabel = QtWidgets.QLabel(self.Index_rna)
#         self.StarIndexlabel.setGeometry(QtCore.QRect(10, 90, 331, 23))
#         self.StarIndexlabel.setObjectName("StarIndexlabel")
#         self.StarIndexlineEdit = QtWidgets.QLineEdit(self.Index_rna)
#         self.StarIndexlineEdit.setGeometry(QtCore.QRect(170, 90, 331, 23))
#         self.StarIndexlineEdit.setObjectName("StarIndexlineEdit")
#         self.StarIndexErrortext = QtWidgets.QLabel(self.Index_rna)
#         self.StarIndexErrortext.setGeometry(QtCore.QRect(170, 116, 300, 15))
#         self.StarIndexErrortext.setFont(font_label)
#         self.StarIndexErrortext.setStyleSheet("color: red")
# #        self.StarIndexErrortext.setText("Input Samples folder path")    
#         self.StarIndexpushButton = QtWidgets.QPushButton(self.Index_rna)
#         self.StarIndexpushButton.setGeometry(QtCore.QRect(600, 90, 30, 25))
#         self.StarIndexpushButton.setObjectName("StarIndexpushButton")
#         self.OrLabel_rna = QtWidgets.QLabel(self.Index_rna)
#         self.OrLabel_rna.setGeometry(QtCore.QRect(340, 130, 270, 23))
#         self.OrLabel_rna.setObjectName("OrLabel_rna")
#         self.horizontalLayoutWidget = QtWidgets.QWidget(self.Index_rna)
#         self.horizontalLayoutWidget.setGeometry(QtCore.QRect(235, 170, 240, 31))
#         self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
#         self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
#         self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
#         self.horizontalLayout_5.setObjectName("horizontalLayout_5")
# =============================================================================
# =============================================================================
#         self.CreateConfigfileforIndexrnapushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
#         self.CreateConfigfileforIndexrnapushButton.setObjectName("CreateConfigfileforIndexrnapushButton")
#         self.horizontalLayout_5.addWidget(self.CreateConfigfileforIndexrnapushButton)
#         self.CreateSnakefileforIndexrnapushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
#         self.CreateSnakefileforIndexrnapushButton.setObjectName("CreateSnakefileforIndexrnapushButton")
#         self.horizontalLayout_5.addWidget(self.CreateSnakefileforIndexrnapushButton)
# =============================================================================
# =============================================================================
#         self.RunIndexrnapushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
#         self.RunIndexrnapushButton.setObjectName("RunIndexrnapushButton")
#         self.horizontalLayout_5.addWidget(self.RunIndexrnapushButton)
#         self.RunIndexrnaButtonErroricon = QtWidgets.QPushButton(self.Index_rna)
#         self.RunIndexrnaButtonErroricon.setGeometry(QtCore.QRect(480, 175, 20, 20))
#         self.RunIndexrnaButtonErroricon.setToolTip("Check and Run Index Again!")
#         self.RunIndexrnaButtonErroricon.setFont(font_label)
#         self.RunIndexrnaButtonErroricon.setIcon(QtGui.QIcon("./icons/warning.svg"))
# #        self.horizontalLayout_4.addWidget(self.RunIndexrnaButtonErroricon)
#         self.RunIndexrnaButtonErroricon.hide()
#         ##index_progressbar##
#         self.progressBar_sub2_rna = QtWidgets.QProgressBar(self.Index_rna)
#         self.progressBar_sub2_rna.setGeometry(QtCore.QRect(10, 230, 665, 17))
#         self.progressBar_sub2_rna.setProperty("value", 0)
#         self.progressBar_sub2_rna.setObjectName("progressBar_sub2_rna")
# =============================================================================
# =============================================================================
#         self.CreateIndexpushButton_rna = QtWidgets.QPushButton(self.Index_rna)
#         self.CreateIndexpushButton_rna.setGeometry(QtCore.QRect(350, 210, 150, 23))
#         self.CreateIndexpushButton_rna.setObjectName("CreateIndexpushButton_rna")
#         self.CreateSnakefileforIndexpushButton_rna = QtWidgets.QPushButton(self.Index_rna)
#         self.CreateSnakefileforIndexpushButton_rna.setGeometry(QtCore.QRect(170, 210, 170, 23))
#         self.CreateSnakefileforIndexpushButton_rna.setObjectName("CreateSnakefileforIndexpushButton_rna")
# =============================================================================

# =============================================================================
#         self.HISAT2Indexlabel = QtWidgets.QLabel(self.Index_rna)
#         self.HISAT2Indexlabel.setGeometry(QtCore.QRect(10, 120, 121, 17))
#         self.HISAT2Indexlabel.setObjectName("HISAT2Indexlabel")
#         self.HISAT2IndexlineEdit = QtWidgets.QLineEdit(self.Index_rna)
#         self.HISAT2IndexlineEdit.setGeometry(QtCore.QRect(170, 120, 331, 23))
#         self.HISAT2IndexlineEdit.setObjectName("HISAT2IndexlineEdit")
#         self.SalmonIndexlabel = QtWidgets.QLabel(self.Index_rna)
#         self.SalmonIndexlabel.setGeometry(QtCore.QRect(10, 160, 121, 17))
#         self.SalmonIndexlabel.setObjectName("SalmonIndexlabel")
#         self.SalmonIndexlineEdit = QtWidgets.QLineEdit(self.Index_rna)
#         self.SalmonIndexlineEdit.setGeometry(QtCore.QRect(170, 160, 331, 23))
#         self.SalmonIndexlineEdit.setObjectName("SalmonIndexlineEdit")
#         self.Bowtie2Indexlabel = QtWidgets.QLabel(self.Index_rna)
#         self.Bowtie2Indexlabel.setGeometry(QtCore.QRect(10, 200, 121, 17))
#         self.Bowtie2Indexlabel.setObjectName("Bowtie2Indexlabel")
#         self.Bowtie2IndexlineEdit = QtWidgets.QLineEdit(self.Index_rna)
#         self.Bowtie2IndexlineEdit.setGeometry(QtCore.QRect(170, 200, 331, 23))
#         self.Bowtie2IndexlineEdit.setObjectName("Bowtie2IndexlineEdit")
#         self.HISAT2IndexpushButton = QtWidgets.QPushButton(self.Index_rna)
#         self.HISAT2IndexpushButton.setGeometry(QtCore.QRect(550, 120, 99, 23))
#         self.HISAT2IndexpushButton.setObjectName("HISAT2IndexpushButton")
#         self.SalmonIndexpushButton = QtWidgets.QPushButton(self.Index_rna)
#         self.SalmonIndexpushButton.setGeometry(QtCore.QRect(550, 160, 99, 23))
#         self.SalmonIndexpushButton.setObjectName("SalmonIndexpushButton")
#         self.Bowtie2IndexpushButton = QtWidgets.QPushButton(self.Index_rna)
#         self.Bowtie2IndexpushButton.setGeometry(QtCore.QRect(550, 200, 99, 23))
#         self.Bowtie2IndexpushButton.setObjectName("Bowtie2IndexpushButton")
# =============================================================================
        ###
        ###
# =============================================================================
#         self.nextbuttonindexRNA = QtWidgets.QPushButton(self.Index_rna)
#         self.nextbuttonindexRNA.setGeometry(QtCore.QRect(635, 258, 45, 45))
#         self.nextbuttonqcRNA.setObjectName("nextbuttonindexRNA")
#         ###
#         self.previousbuttonindexRNA = QtWidgets.QPushButton(self.Index_rna)
#         self.previousbuttonindexRNA.setGeometry(QtCore.QRect(10, 258, 45, 45))
#         self.previousbuttonindexRNA.setObjectName("previousbuttonindexRNA")
#         
#         self.RNAtabWidget.addTab(self.Index_rna, "")
#         ## End ##
#         ## Add Params ##
#         self.Params_rna = QtWidgets.QWidget()
#         self.Params_rna.setObjectName("Params_rna")
#         
#         self.AlignerParamlabelrna = QtWidgets.QLabel(self.Params_rna)
#         self.AlignerParamlabelrna.setGeometry(QtCore.QRect(10, 10, 81, 17))
#         self.AlignerParamlabelrna.setObjectName('AlignerParamlabelrna')
#         self.EMParamlabelrna = QtWidgets.QLabel(self.Params_rna)
#         self.EMParamlabelrna.setGeometry(QtCore.QRect(10, 98, 81, 17))
#         self.EMParamlabelrna.setObjectName('EMParamlabelrna')
#         self.DEParamlabelrna = QtWidgets.QLabel(self.Params_rna)
#         self.DEParamlabelrna.setGeometry(QtCore.QRect(10, 186, 81, 17))
#         self.DEParamlabelrna.setObjectName('DEParamlabelrna')
# =============================================================================
        
# =============================================================================
#         self.param1_label_rna_1 = QtWidgets.QLabel(self.Params_rna)
#         self.param1_label_rna_1.setGeometry(QtCore.QRect(20, 40, 91, 18))
#         self.param1_lineEdit_rna_1 = QtWidgets.QLineEdit(self.Params_rna)
#         self.param1_lineEdit_rna_1.setGeometry(QtCore.QRect(120, 40, 70, 18))
#         self.param1_label_rna_2 = QtWidgets.QLabel(self.Params_rna)
#         self.param1_label_rna_2.setGeometry(QtCore.QRect(20, 65, 91, 18))
#         self.param1_lineEdit_rna_2 = QtWidgets.QLineEdit(self.Params_rna)
#         self.param1_lineEdit_rna_2.setGeometry(QtCore.QRect(120, 65, 70, 18))
#         self.param1_label_rna_3 = QtWidgets.QLabel(self.Params_rna)
#         self.param1_label_rna_3.setGeometry(QtCore.QRect(200, 40, 91, 18))
#         self.param1_lineEdit_rna_3 = QtWidgets.QLineEdit(self.Params_rna)
#         self.param1_lineEdit_rna_3.setGeometry(QtCore.QRect(280, 40, 70, 18))
#         self.param1_label_rna_4 = QtWidgets.QLabel(self.Params_rna)
#         self.param1_label_rna_4.setGeometry(QtCore.QRect(200, 65, 91, 18))
#         self.param1_lineEdit_rna_4 = QtWidgets.QLineEdit(self.Params_rna)
#         self.param1_lineEdit_rna_4.setGeometry(QtCore.QRect(280, 65, 70, 18))
#         self.param1_label_rna_5 = QtWidgets.QLabel(self.Params_rna)
#         self.param1_label_rna_5.setGeometry(QtCore.QRect(360, 40, 91, 18))
#         self.param1_lineEdit_rna_5 = QtWidgets.QLineEdit(self.Params_rna)
#         self.param1_lineEdit_rna_5.setGeometry(QtCore.QRect(440, 40, 70, 18))
#         self.param1_label_rna_6 = QtWidgets.QLabel(self.Params_rna)
#         self.param1_label_rna_6.setGeometry(QtCore.QRect(360, 65, 91, 18))
#         self.param1_lineEdit_rna_6 = QtWidgets.QLineEdit(self.Params_rna)
#         self.param1_lineEdit_rna_6.setGeometry(QtCore.QRect(440, 65, 70, 18))
#         self.aligner_add_rna = QtWidgets.QPushButton(self.Params_rna)
#         self.aligner_add_rna.setGeometry(QtCore.QRect(530, 45, 70, 30))
#         self.aligner_add_rna.setText("Advanced")
#         
#         
#         self.param2_label_rna_1 = QtWidgets.QLabel(self.Params_rna)
#         self.param2_label_rna_1.setGeometry(QtCore.QRect(20, 130, 91, 18))
#         self.param2_lineEdit_rna_1 = QtWidgets.QLineEdit(self.Params_rna)
#         self.param2_lineEdit_rna_1.setGeometry(QtCore.QRect(120, 130, 70, 18))
#         self.param2_label_rna_2 = QtWidgets.QLabel(self.Params_rna)
#         self.param2_label_rna_2.setGeometry(QtCore.QRect(20, 155, 91, 18))
#         self.param2_lineEdit_rna_2 = QtWidgets.QLineEdit(self.Params_rna)
#         self.param2_lineEdit_rna_2.setGeometry(QtCore.QRect(120, 155, 70, 18))
#         self.param2_label_rna_3 = QtWidgets.QLabel(self.Params_rna)
#         self.param2_label_rna_3.setGeometry(QtCore.QRect(200, 130, 91, 18))
#         self.param2_lineEdit_rna_3 = QtWidgets.QLineEdit(self.Params_rna)
#         self.param2_lineEdit_rna_3.setGeometry(QtCore.QRect(280, 130, 70, 18))
#         self.param2_label_rna_4 = QtWidgets.QLabel(self.Params_rna)
#         self.param2_label_rna_4.setGeometry(QtCore.QRect(200, 155, 91, 18))
#         self.param2_lineEdit_rna_4 = QtWidgets.QLineEdit(self.Params_rna)
#         self.param2_lineEdit_rna_4.setGeometry(QtCore.QRect(280, 155, 70, 18))
#         self.param2_label_rna_5 = QtWidgets.QLabel(self.Params_rna)
#         self.param2_label_rna_5.setGeometry(QtCore.QRect(360,130, 91, 18))
#         self.param2_lineEdit_rna_5 = QtWidgets.QLineEdit(self.Params_rna)
#         self.param2_lineEdit_rna_5.setGeometry(QtCore.QRect(440, 130, 70, 18))
#         self.param2_label_rna_6 = QtWidgets.QLabel(self.Params_rna)
#         self.param2_label_rna_6.setGeometry(QtCore.QRect(360, 155, 91, 18))
#         self.param2_lineEdit_rna_6 = QtWidgets.QLineEdit(self.Params_rna)
#         self.param2_lineEdit_rna_6.setGeometry(QtCore.QRect(440, 155, 70, 18))
#         self.em_add_rna = QtWidgets.QPushButton(self.Params_rna)
#         self.em_add_rna.setGeometry(QtCore.QRect(530, 135, 70, 30))
#         self.em_add_rna.setText("Advanced")
#         
#         self.param3_label_rna_1 = QtWidgets.QLabel(self.Params_rna)
#         self.param3_label_rna_1.setGeometry(QtCore.QRect(20, 220, 91, 18))
#         self.param3_lineEdit_rna_1 = QtWidgets.QLineEdit(self.Params_rna)
#         self.param3_lineEdit_rna_1.setGeometry(QtCore.QRect(120, 220, 70, 18))
#         self.param3_label_rna_2 = QtWidgets.QLabel(self.Params_rna)
#         self.param3_label_rna_2.setGeometry(QtCore.QRect(20, 245, 91, 18))
#         self.param3_lineEdit_rna_2 = QtWidgets.QLineEdit(self.Params_rna)
#         self.param3_lineEdit_rna_2.setGeometry(QtCore.QRect(120, 245, 70, 18))
#         self.param3_label_rna_3 = QtWidgets.QLabel(self.Params_rna)
#         self.param3_label_rna_3.setGeometry(QtCore.QRect(200, 220, 91, 18))
#         self.param3_lineEdit_rna_3 = QtWidgets.QLineEdit(self.Params_rna)
#         self.param3_lineEdit_rna_3.setGeometry(QtCore.QRect(280, 220, 70, 18))
#         self.param3_label_rna_4 = QtWidgets.QLabel(self.Params_rna)
#         self.param3_label_rna_4.setGeometry(QtCore.QRect(200, 245, 91, 18))
#         self.param3_lineEdit_rna_4 = QtWidgets.QLineEdit(self.Params_rna)
#         self.param3_lineEdit_rna_4.setGeometry(QtCore.QRect(280, 245, 70, 18))
#         self.param3_label_rna_5 = QtWidgets.QLabel(self.Params_rna)
#         self.param3_label_rna_5.setGeometry(QtCore.QRect(360, 220, 91, 18))
#         self.param3_lineEdit_rna_5 = QtWidgets.QLineEdit(self.Params_rna)
#         self.param3_lineEdit_rna_5.setGeometry(QtCore.QRect(440, 220, 70, 18))
#         self.param3_label_rna_6 = QtWidgets.QLabel(self.Params_rna)
#         self.param3_label_rna_6.setGeometry(QtCore.QRect(360, 245, 91, 18))
#         self.param3_lineEdit_rna_6 = QtWidgets.QLineEdit(self.Params_rna)
#         self.param3_lineEdit_rna_6.setGeometry(QtCore.QRect(440, 245, 70, 18))
#         self.de_add_rna = QtWidgets.QPushButton(self.Params_rna)
#         self.de_add_rna.setGeometry(QtCore.QRect(530, 225, 70, 30))
#         self.de_add_rna.setText("Advanced")
#         
#         self.param1_label_rna_1.hide()
#         self.param1_label_rna_2.hide()
#         self.param1_label_rna_3.hide()
#         self.param1_label_rna_4.hide()
#         self.param1_label_rna_5.hide()
#         self.param1_label_rna_6.hide()
#         self.param1_lineEdit_rna_1.hide()
#         self.param1_lineEdit_rna_2.hide()
#         self.param1_lineEdit_rna_3.hide()
#         self.param1_lineEdit_rna_4.hide()
#         self.param1_lineEdit_rna_5.hide()
#         self.param1_lineEdit_rna_6.hide()
#         
#         self.param2_label_rna_1.hide()
#         self.param2_label_rna_2.hide()
#         self.param2_label_rna_3.hide()
#         self.param2_label_rna_4.hide()
#         self.param2_label_rna_5.hide()
#         self.param2_label_rna_6.hide()
#         self.param2_lineEdit_rna_1.hide()
#         self.param2_lineEdit_rna_2.hide()
#         self.param2_lineEdit_rna_3.hide()
#         self.param2_lineEdit_rna_4.hide()
#         self.param2_lineEdit_rna_5.hide()
#         self.param2_lineEdit_rna_6.hide()
#         
#         self.param3_label_rna_1.hide()
#         self.param3_label_rna_2.hide()
#         self.param3_label_rna_3.hide()
#         self.param3_label_rna_4.hide()
#         self.param3_label_rna_5.hide()
#         self.param3_label_rna_6.hide()
#         self.param3_lineEdit_rna_1.hide()
#         self.param3_lineEdit_rna_2.hide()
#         self.param3_lineEdit_rna_3.hide()
#         self.param3_lineEdit_rna_4.hide()
#         self.param3_lineEdit_rna_5.hide()
#         self.param3_lineEdit_rna_6.hide()
# =============================================================================

        
        ###
# =============================================================================
#         self.nextbuttonparamsRNA = QtWidgets.QPushButton(self.Params_rna)
#         self.nextbuttonparamsRNA.setGeometry(QtCore.QRect(560, 270, 110, 35))
#         self.nextbuttonparamsRNA.setObjectName("nextbuttonparamsRNA")
#         ###
#         self.previousbuttonparamsRNA = QtWidgets.QPushButton(self.Params_rna)
#         self.previousbuttonparamsRNA.setGeometry(QtCore.QRect(10, 258, 45, 45))
#         self.previousbuttonparamsRNA.setObjectName("previousbuttonparamsRNA")
# 
#         self.RNAtabWidget.addTab(self.Params_rna, "")
# =============================================================================
        ## End ##
        
        ##Add Run##
        self.run_rna = QtWidgets.QWidget()
        self.run_rna.setObjectName("run_rna")
        
        self.RunButton = QtWidgets.QPushButton(self.run_rna)
        self.RunButton.setGeometry(QtCore.QRect(400, 50, 170, 170))
        self.RunButton.setObjectName("RunButton")
        self.RunLabel = QtWidgets.QLabel(self.run_rna)
        self.RunLabel.setGeometry(QtCore.QRect(465, 248, 180, 17))
        self.RunLabel.setObjectName("RunLabel")
        
        self.RunButtonErroricon = QtWidgets.QPushButton(self.run_rna)
        self.RunButtonErroricon.setGeometry(QtCore.QRect(580, 145, 30, 30))
        self.RunButtonErroricon.setToolTip("Click Run Button and Run Again!")
        self.RunButtonErroricon.setFont(font_label)
        self.RunButtonErroricon.setIcon(QtGui.QIcon("./icons/warning.svg"))
        self.RunButtonErroricon.hide()      
        
        self.ResultsButton = QtWidgets.QPushButton(self.run_rna)
        self.ResultsButton.setGeometry(QtCore.QRect(100, 50, 170, 170))
        self.ResultsButton.setObjectName("ResultsButton")
# #        self.horizontalLayout.addWidget(self.ResultsButton)
        self.ResultsLabel = QtWidgets.QLabel(self.run_rna)
        self.ResultsLabel.setGeometry(QtCore.QRect(145, 248, 180, 17))
        self.ResultsLabel.setObjectName("ResultsLabel") 
        
        self.ResultsButtonErroricon = QtWidgets.QPushButton(self.run_rna)
        self.ResultsButtonErroricon.setGeometry(QtCore.QRect(280, 145, 30, 30))
        self.ResultsButtonErroricon.setToolTip("Click Run Button and Run Again!")
        self.ResultsButtonErroricon.setFont(font_label)
        self.ResultsButtonErroricon.setIcon(QtGui.QIcon("./icons/warning.svg"))
        self.ResultsButtonErroricon.hide()              
        
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
        self.RunButtoninfoicon_rna.setGeometry(QtCore.QRect(580, 120, 20, 20))
        self.RunButtoninfoicon_rna.setToolTip("xxxxxxxxx!")
        self.RunButtoninfoicon_rna.setFont(font_info)
        self.RunButtoninfoicon_rna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.RunButtoninfoicon_rna.setIconSize(QtCore.QSize(13, 13)) 
        
        self.ResultsButtoninfoicon_rna = QtWidgets.QPushButton(self.run_rna)
        self.ResultsButtoninfoicon_rna.setFlat(True)
        self.ResultsButtoninfoicon_rna.setGeometry(QtCore.QRect(280, 120, 20, 20))
        self.ResultsButtoninfoicon_rna.setToolTip("xxxxxxxxx!")
        self.ResultsButtoninfoicon_rna.setFont(font_info)
        self.ResultsButtoninfoicon_rna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.ResultsButtoninfoicon_rna.setIconSize(QtCore.QSize(13, 13))          
        
        self.RNAtabWidget.addTab(self.run_rna, "")
        ##End##
        ##Add Result RNA##
        self.result_rna = QtWidgets.QWidget()
        self.result_rna.setObjectName("result_rna")
        
        self.label_result1_rna = QtWidgets.QLabel(self.result_rna)
        self.label_result1_rna.setGeometry(QtCore.QRect(150, 80, 200, 23))
        self.label_result1_rna.setText("Run statistics")
        self.pushbutton_result1_rna=QtWidgets.QPushButton(self.result_rna)
        self.pushbutton_result1_rna.setText("Click")
        self.pushbutton_result1_rna.setGeometry(QtCore.QRect(350, 80, 60, 23))
        self.label_result2_rna = QtWidgets.QLabel(self.result_rna)
        self.label_result2_rna.setGeometry(QtCore.QRect(150, 180, 200, 23))
        self.label_result2_rna.setText("Differentially Expressed Genes")
        self.pushbutton_result2_rna=QtWidgets.QPushButton(self.result_rna)
        self.pushbutton_result2_rna.setText("Click")
        self.pushbutton_result2_rna.setGeometry(QtCore.QRect(350, 180, 60, 23))
        self.label_result3_rna = QtWidgets.QLabel(self.result_rna)
        self.label_result3_rna.setGeometry(QtCore.QRect(150, 280, 200, 23))
        self.label_result3_rna.setText("Plots")
        self.pushbutton_result3_rna=QtWidgets.QPushButton(self.result_rna)
        self.pushbutton_result3_rna.setText("Click")
        self.pushbutton_result3_rna.setGeometry(QtCore.QRect(350, 280, 60, 23))
        
        self.RNAtabWidget.addTab(self.result_rna, "")
        ##End##        
        
        ## Add Create ##
#==============================================================================
#         self.Create_rna = QtWidgets.QWidget()
#         self.Create_rna.setObjectName("Create_rna")
# 
#         self.horizontalLayoutWidget_2_rna = QtWidgets.QWidget(self.Create_rna)
#         self.horizontalLayoutWidget_2_rna.setGeometry(QtCore.QRect(40, 100, 591, 31))
#         self.horizontalLayoutWidget_2_rna.setObjectName("horizontalLayoutWidget_2_rna")
#         self.horizontalLayout_7_rna = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2_rna)
#         self.horizontalLayout_7_rna.setContentsMargins(0, 0, 0, 0)
#         self.horizontalLayout_7_rna.setObjectName("horizontalLayout_7_rna")
#         self.CreateSnakefilepushButtonRNA = QtWidgets.QPushButton(self.horizontalLayoutWidget_2_rna)
#         self.CreateSnakefilepushButtonRNA.setObjectName("CreateSnakefilepushButtonRNA")
#         self.horizontalLayout_7_rna.addWidget(self.CreateSnakefilepushButtonRNA)
#         self.CreateConfigpushButtonRNA = QtWidgets.QPushButton(self.horizontalLayoutWidget_2_rna)
#         self.CreateConfigpushButtonRNA.setObjectName("CreateConfigpushButtonRNA")
#         self.horizontalLayout_7_rna.addWidget(self.CreateConfigpushButtonRNA)
# 
#         self.RNAtabWidget.addTab(self.Create_rna, "")
#==============================================================================
        ## End ##
        self.PipelinetabWidget.addTab(self.RNAseq, "")

# =============================================================================
#         self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
#         self.progressBar.setGeometry(QtCore.QRect(10, 670, 701, 23))
#         self.progressBar.setProperty("value", 0)
# #        self.progressBar.setMaximum(3)
#         self.progressBar.setObjectName("progressBar")
# =============================================================================
        ##subprogressbars##
# =============================================================================
#         self.progressBar_sub1 = QtWidgets.QProgressBar(self.centralwidget)
#         self.progressBar_sub1.setGeometry(QtCore.QRect(10, 570, 465, 17))
#         self.progressBar_sub1.setProperty("value", 0)
#         self.progressBar_sub1.setObjectName("progressBar_sub1")
#         self.progressBar_sub1Label = QtWidgets.QLabel(self.centralwidget)
#         self.progressBar_sub1Label.setGeometry(QtCore.QRect(500, 570, 510, 17))
#         self.progressBar_sub1Label.setObjectName("progressBar_sub1Label")
# =============================================================================
        
# =============================================================================
#         self.progressBar_sub2 = QtWidgets.QProgressBar(self.centralwidget)
#         self.progressBar_sub2.setGeometry(QtCore.QRect(10, 600, 465, 17))
#         self.progressBar_sub2.setProperty("value", 0)
#         self.progressBar_sub2.setObjectName("progressBar_sub2")
#         self.progressBar_sub2Label = QtWidgets.QLabel(self.centralwidget)
#         self.progressBar_sub2Label.setGeometry(QtCore.QRect(500, 600, 510, 17))
#         self.progressBar_sub2Label.setObjectName("progressBar_sub2Label")
# =============================================================================
        
# =============================================================================
#         self.progressBar_sub3 = QtWidgets.QProgressBar(self.centralwidget)
#         self.progressBar_sub3.setGeometry(QtCore.QRect(10, 630, 465, 17))
#         self.progressBar_sub3.setProperty("value", 0)
#         self.progressBar_sub3.setObjectName("progressBar_sub3")
#         self.progressBar_sub3Label = QtWidgets.QLabel(self.centralwidget)
#         self.progressBar_sub3Label.setGeometry(QtCore.QRect(500, 630, 510, 17))
#         self.progressBar_sub3Label.setObjectName("progressBar_sub3Label")
# =============================================================================
        
        self.ShellTab = QtWidgets.QTabWidget(self.centralwidget)
        self.ShellTab.setGeometry(QtCore.QRect(10, 550, 701, 151))
        self.ShellTab.setObjectName("ShellTab")
        self.ShellTab.setStyleSheet("background-color: #F0F9EC") 
        self.SnakemakeOutputTab = QtWidgets.QWidget()
        self.SnakemakeOutputTab.setObjectName("SnakemakeOutputTab")
        self.textBrowser = QtWidgets.QTextBrowser(self.SnakemakeOutputTab)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 695, 118))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setReadOnly(True)
#        self.logTextBox = QPlainTextEditLogger(self)
#        self.set_level()
#        self.ui.layout_logger.addWidget(self.logTextBox.widget)
        self.ShellTab.addTab(self.SnakemakeOutputTab, "")
# =============================================================================
#         self.PythonShellTab = QtWidgets.QWidget()
#         self.PythonShellTab.setObjectName("PythonShellTab")
#         self.ShellTab.addTab(self.PythonShellTab, "")
#         self.textBrowser_PythonShellTab = QtWidgets.QTextBrowser(self.PythonShellTab)
#         self.textBrowser_PythonShellTab.setGeometry(QtCore.QRect(0, 0, 695, 118))
#         self.textBrowser_PythonShellTab.setObjectName("textBrowser_PythonShellTab")
#         self.textBrowser_PythonShellTab.setReadOnly(True)
# =============================================================================
        
        
# =============================================================================
#         self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
#         self.layoutWidget1.setGeometry(QtCore.QRect(10, 500, 701, 331))
#         self.layoutWidget1.setObjectName("layoutWidget1")
# =============================================================================
# =============================================================================
#         self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
#         self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
#         self.horizontalLayout.setObjectName("horizontalLayout")
# =============================================================================
        
        
# =============================================================================
#         self.DAGButton = QtWidgets.QPushButton(self.centralwidget)
#         self.DAGButton.setGeometry(QtCore.QRect(80, 565, 75, 75))
#         self.DAGButton.setObjectName("DAGButton")
#         self.DAGLabel = QtWidgets.QLabel(self.centralwidget)
#         self.DAGLabel.setGeometry(QtCore.QRect(90, 645, 180, 17))
#         self.DAGLabel.setObjectName("DAGLabel")
#         self.DAGLabel.setEnabled(False)
#         
# #        self.horizontalLayout.addWidget(self.DAGButton)
#         self.DAGButton.setEnabled(False)
#         self.RunButton = QtWidgets.QPushButton(self.centralwidget)
#         self.RunButton.setGeometry(QtCore.QRect(320, 565, 75, 75))
#         self.RunButton.setObjectName("RunButton")
#         self.RunLabel = QtWidgets.QLabel(self.centralwidget)
#         self.RunLabel.setGeometry(QtCore.QRect(345, 645, 180, 17))
#         self.RunLabel.setObjectName("RunLabel")
#         self.RunLabel.setEnabled(False)
# #        self.horizontalLayout.addWidget(self.RunButton)
#         self.RunButton.setEnabled(False)
#         self.RunButtonErroricon = QtWidgets.QPushButton(self.centralwidget)
#         self.RunButtonErroricon.setGeometry(QtCore.QRect(400, 593, 20, 20))
#         self.RunButtonErroricon.setToolTip("Click Run Button and Run Again!")
#         self.RunButtonErroricon.setFont(font_label)
#         self.RunButtonErroricon.setIcon(QtGui.QIcon("./icons/warning.svg"))
#         self.RunButtonErroricon.hide()
#         self.ResultsButton = QtWidgets.QPushButton(self.centralwidget)
#         self.ResultsButton.setGeometry(QtCore.QRect(540, 565, 75, 75))
#         self.ResultsButton.setObjectName("ResultsButton")
# #        self.horizontalLayout.addWidget(self.ResultsButton)
#         self.ResultsLabel = QtWidgets.QLabel(self.centralwidget)
#         self.ResultsLabel.setGeometry(QtCore.QRect(555, 645, 180, 17))
#         self.ResultsLabel.setObjectName("ResultsLabel")
#         self.ResultsLabel.setEnabled(False)
#         self.ResultsButton.setEnabled(False)
#         self.ResultsButtonErroricon = QtWidgets.QPushButton(self.centralwidget)
#         self.ResultsButtonErroricon.setGeometry(QtCore.QRect(623, 600, 20, 20))
#         self.ResultsButtonErroricon.setToolTip("Click Unlock and Run Again!")
#         self.ResultsButtonErroricon.setFont(font_label)
# #        self.ResultsButtonErroricon.setStyleSheet("color: red")
# #        self.ResultsButtonErroricon.hide()
# #        self.ResultsButtonErroricon.setText("safdg")
#         self.ResultsButtonErroricon.setIcon(QtGui.QIcon("./icons/warning.svg"))
#         self.ResultsButtonErroricon.hide()
# =============================================================================


#        self.layoutWidget.raise_()
        self.PipelinetabWidget.raise_()
        self.progressBar_sub1_dna.raise_()
        self.progressBar_sub2_dna.raise_()
#        self.progressBar_sub3.raise_()
#        self.progressBar.raise_()
        self.ShellTab.raise_()
        self.RefVariantpushButton.raise_()
        self.RefVariantlineEditDNA.raise_()
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
#         self._colors = {
#             'green': QtGui.QColor(0,170,0),
#             'red': QtGui.QColor(170,0,0),
#             'orange': QtGui.QColor(170,150,0),
#             'blue': QtGui.QColor(0,90,154),
#         }
#         self.shell = ""
#         self.shell_error = ""
#         self._step_regex = re.compile("([0-9]+) of ([0-9]+) steps")
# =============================================================================
        
        





############


############
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "iCOMIC"))
        MainWindow.setWindowIcon(QtGui.QIcon("./icons/mainwindow.png"))
        #self.PipelinetabWidget.setToolTip(_translate("MainWindow", "Performs Quality Control and Creates Mandatory files to run the pipeline"))
        ## Add Input as first tab ##
#        self.SampleOrlabel.setToolTip(_translate("MainWindow", "This option performs all the Quality Control operations like fastQC, Cutadapt and MultiQC "))
        self.SampleOrlabel.setText(_translate("MainWindow", "Or"))
        self.SamplesYesradioButton.setToolTip(_translate("MainWindow", "Files should be in specified format"))
        self.SamplesYesradioButton.setText(_translate("MainWindow", "Upload from Folder"))
        self.SamplesNoradioButton.setToolTip(_translate("MainWindow", "Tables should contain all the information"))
        self.SamplesNoradioButton.setText(_translate("MainWindow", "Upload from Table"))
#        self.UnitsBrowseButtonDNA.setText(_translate("MainWindow", "Browse"))
        self.UnitsBrowseButtonDNA.setIcon(QtGui.QIcon("./icons/browse.svg"))
        self.UnitsBrowseButtonDNA.setIconSize(QtCore.QSize(22, 22))
        self.UnitsBrowseButtonDNA.setToolTip("Browse Samples Table")
#        self.RefGenomeBrowseButtonDNA.setText(_translate("MainWindow", "Browse"))
        self.RefGenomeBrowseButtonDNA.setIcon(QtGui.QIcon("./icons/browse.svg"))
#        self.RefGenomeBrowseButtonDNA.setStyleSheet("background-color: #aeaeae")
        self.RefGenomeBrowseButtonDNA.setToolTip("Browse Reference Genome")
        self.RefGenomeBrowseButtonDNA.setIconSize(QtCore.QSize(22, 22))
        self.UnitsFilelabelDNA.setText(_translate("MainWindow", "Samples Table"))
        self.RefGenomelabelDNA.setText(_translate("MainWindow", "Reference Genome"))
        self.SampleFilelabelDNA.setText(_translate("MainWindow", "Samples Folder"))
# =============================================================================
#         self.WDlabelDNA.setText(_translate("MainWindow", "Working directory"))
#         self.WDBrowseButtonDNA.setIcon(QtGui.QIcon("./icons/browse.svg"))
#         self.WDBrowseButtonDNA.setIconSize(QtCore.QSize(22, 22))
# =============================================================================
#        self.SamplesBrowseButtonDNA.setText(_translate("MainWindow", "Browse"))
        self.SamplesBrowseButtonDNA.setIcon(QtGui.QIcon("./icons/browse.svg"))
        self.SamplesBrowseButtonDNA.setIconSize(QtCore.QSize(22, 22))
#        self.SamplesBrowseButtonDNA.setStyleSheet("background-color: #aeaeae")
        self.SamplesBrowseButtonDNA.setToolTip("Browse Samples Folder")
        self.RefVariantlabelDNA.setText(_translate("MainWindow", "Reference Known Variant"))
#        self.RefVariantpushButton.setText(_translate("MainWindow", "Browse"))
        self.RefVariantpushButton.setIcon(QtGui.QIcon("./icons/browse.svg"))
#        self.RefVariantpushButton.setStyleSheet("background-color: #aeaeae")
        self.RefVariantpushButton.setToolTip("Browse Reference Known Variant")
        self.RefVariantpushButton.setIconSize(QtCore.QSize(22, 22))
        self.RefNamelabelDNA.setText(_translate("MainWindow", "Reference Name (as in SnpEff Database)"))
# =============================================================================
# #        self.RefNamelineEdit.setText(_translate("MainWindow", "GRCh38.86"))        
#         self.UnitslineEditDNA.setText(_translate("MainWindow", "/data/Priyanka/other_pipelines/iCOMIC/Test/DNA-Seq/units.tsv"))
#         self.SampleslineEditDNA.setText(_translate("MainWindow", "/data/Priyanka/other_pipelines/iCOMIC/Test/DNA-Seq/samples.tsv"))
#         self.RefGenomelineEditDNA.setText(_translate("MainWindow", "/data/Priyanka/other_pipelines/iCOMIC/Test/DNA-Seq/ref/genome.chr21.fa"))
#         self.RefVariantlineEditDNA.setText(_translate("MainWindow", "/data/Priyanka/other_pipelines/iCOMIC/Test/DNA-Seq/ref/dbsnp.vcf.gz"))
# =============================================================================
        self.nextbuttoninputDNA.setIcon(QtGui.QIcon("./icons/arrow.svg"))
        self.nextbuttoninputDNA.setIconSize(QtCore.QSize(35, 35))
#        self.nextbuttoninputDNA.setStyleSheet("background-color: #f50057")
        self.DNAtabWidget.setTabText(self.DNAtabWidget.indexOf(self.input_dna), _translate("MainWindow", " Input Data "))
        self.DNAtabWidget.setTabIcon(self.DNAtabWidget.indexOf(self.input_dna), QtGui.QIcon('./icons/input.svg'))
#        self.DNAtabWidget.setStyleSheet(self.DNAtabWidget.indexOf(self.input_dna), ("background-color: #EBF6F5"))
        self.DNAtabWidget.setIconSize(QtCore.QSize(22, 22))
        
        ## End ###
        
        ##Label progres bar##
# =============================================================================
#         self.progressBar_sub1Label.setText(_translate("MainWindow", "Quality Check"))
#         self.progressBar_sub2Label.setText(_translate("MainWindow", "Index"))
#         self.progressBar_sub3Label.setText(_translate("MainWindow", "Analysis"))
# =============================================================================
        
        ## Add QC ##
        self.QClabel.setToolTip(_translate("MainWindow", "This option performs all the Quality Control operations like fastQC, Cutadapt and MultiQC "))
        self.QClabel.setText(_translate("MainWindow", "Trim the reads"))
        self.QCYesradioButton.setToolTip(_translate("MainWindow", "Enables Quality Control Processing"))
        self.QCYesradioButton.setText(_translate("MainWindow", "Yes"))
        self.QCNoradioButton.setToolTip(_translate("MainWindow", "Disables Quality Control Processing"))
        self.QCNoradioButton.setText(_translate("MainWindow", "No"))
        self.InputParamslabel.setText(_translate("MainWindow", "Input Parameters:"))
#        self.fastQClabel.setText(_translate("MainWindow", "fastQC"))
#        self.QClineEdit.setText(_translate("MainWindow", " --threads 1 --quiet "))
        self.Cutadaptlabel.setText(_translate("MainWindow", "Cutadapt"))
        self.CutadaptlineEdit.setText(_translate("MainWindow", "--threads 1"))
#        self.MultiQClabel.setText(_translate("MainWindow", "MultiQC"))
# =============================================================================
#         self.CreateSnakefilepushButton.setText(_translate("MainWindow", "Create Snakefile for QC Analysis"))
#         self.CreateConfigfilepushButton.setText(_translate("MainWindow", "Create Configfile for QC Analysis"))
# =============================================================================
        self.RunQCpushButton.setText(_translate("MainWindow", "Trimming"))
        self.RunQCpushButton.setIcon(QtGui.QIcon("./icons/run1.svg"))
        self.RunQCpushButton.setIconSize(QtCore.QSize(22, 22))
#        self.RunQCpushButton.setStyleSheet("background-color: #03a9f4")
        self.nextbuttonqcDNA.setIcon(QtGui.QIcon("./icons/arrow.svg"))
        self.nextbuttonqcDNA.setIconSize(QtCore.QSize(35, 35))
        self.previousbuttonqcDNA.setIcon(QtGui.QIcon("./icons/arrow1.svg"))
        self.previousbuttonqcDNA.setIconSize(QtCore.QSize(35, 35))
        self.DNAtabWidget.setTabText(self.DNAtabWidget.indexOf(self.QC_dna), _translate("MainWindow", " Quality Control "))
        self.DNAtabWidget.setTabIcon(self.DNAtabWidget.indexOf(self.QC_dna), QtGui.QIcon('./icons/qc.svg'))
        
        
#        self.DNAtabWidget.setIconSize(QtCore.QSize(20, 20))
        ## End ##
#        self.AlignerlabelDNA.setText(_translate("MainWindow", "Aligner"))
        self.AlignercomboBoxDNA.setStyleSheet("background-color: #578446")
        self.AlignercomboBoxDNA.setItemText(0, _translate("MainWindow", "BWA_MEM"))
        self.AlignercomboBoxDNA.setItemText(1, _translate("MainWindow", "GEM3"))
        self.AlignercomboBoxDNA.setItemText(2, _translate("MainWindow", "Bowtie2"))
        self.AlignercomboBoxDNA.setItemText(3, _translate("MainWindow", "None"))
#        self.VClabelDNA.setText(_translate("MainWindow", "Variant Caller"))
        self.VCcomboBoxDNA.setStyleSheet("background-color: #578446")
# =============================================================================
#         self.VCcomboBoxDNA.setItemText(0, _translate("MainWindow", "GATK_HC"))
#         self.VCcomboBoxDNA.setItemText(1, _translate("MainWindow", "bcftools_call"))
#         self.VCcomboBoxDNA.setItemText(2, _translate("MainWindow", "freebayes"))
#         self.VCcomboBoxDNA.setItemText(3, _translate("MainWindow", "Mutect2"))
#         self.VCcomboBoxDNA.setItemText(4, _translate("MainWindow", "None"))
# =============================================================================
#        self.VCcomboBoxDNA.removeItem(2)
#        self.AnnotatorlabelDNA.setText(_translate("MainWindow", "Annotator"))
        self.AnnotatorcomboBoxDNA.setStyleSheet("background-color: #578446")
        self.AnnotatorcomboBoxDNA.setItemText(0, _translate("MainWindow", "SnpEff"))
        self.AnnotatorcomboBoxDNA.setItemText(1, _translate("MainWindow", "Annovar"))
#        self.AnnotatorcomboBoxDNA.setItemText(2, _translate("MainWindow", "None"))
        self.nextbuttontoolDNA.setIcon(QtGui.QIcon("./icons/arrow.svg"))
        self.nextbuttontoolDNA.setIconSize(QtCore.QSize(35, 35))
        self.previousbuttontoolDNA.setIcon(QtGui.QIcon("./icons/arrow1.svg"))
        self.previousbuttontoolDNA.setIconSize(QtCore.QSize(35, 35))
        self.DNAtabWidget.setTabText(self.DNAtabWidget.indexOf(self.Tool_dna), _translate("MainWindow", " Tools Selection "))
        self.DNAtabWidget.setTabIcon(self.DNAtabWidget.indexOf(self.Tool_dna), QtGui.QIcon('./icons/tools.svg'))
        
        ## Add Index ##
#        self.InputIndexlabel_dna.setText(_translate("MainWindow", "Input Indexes for DNA-Seq analysis"))
#        self.BWAIndexlabel.setText(_translate("MainWindow", "Index for " + self.AlignercomboBoxDNA.currentText()))
        self.BWAIndexlineEdit.setToolTip(_translate("MainWindow", "Input the path of the Index for " + self.AlignercomboBoxDNA.currentText()))
        self.BWAIndexpushButton.setToolTip(_translate("MainWindow", "Click this to select one of the already available index or for a custom index"))
#        self.BWAIndexpushButton.setText(_translate("MainWindow", "Browse"))
        self.BWAIndexpushButton.setIcon(QtGui.QIcon("./icons/browse.svg"))
        self.BWAIndexpushButton.setIconSize(QtCore.QSize(22, 22))
#        self.BWAIndexpushButton.setStyleSheet("background-color: #aeaeae")
        self.BWAIndexpushButton.setToolTip("Browse Index File")
        self.OrLabel_dna.setText(_translate("MainWindow", "Or"))
# =============================================================================
#         self.CreateConfigfileforIndexdnapushButton.setText(_translate("MainWindow", "Create configfile for index"))
#         self.CreateSnakefileforIndexdnapushButton.setText(_translate("MainWindow", "Create Snakefile for index"))
# =============================================================================
        self.RunIndexdnapushButton.setText(_translate("MainWindow", "Generate Index"))
        self.RunIndexdnapushButton.setIcon(QtGui.QIcon("./icons/run1.svg"))
        self.RunIndexdnapushButton.setIconSize(QtCore.QSize (22, 22))
        
   
#        self.information(self, 'Notification', "Click on 'Run' below to start your analysis", QtWidgets.QMessageBox.Ok)
#        QtWidgets.QMessageBox.information(self, 'Notification', "Click on 'Run' below to start your analysis")
       
#        self.RunIndexdnapushButton.setStyleSheet("background-color: #03a9f4")
#        self.BWAIndexlineEdit.setText(_translate("MainWindow", "/data/Priyanka/other_pipelines/iCOMIC/Test/DNA-Seq/ref/genome.chr21.fa"))
# =============================================================================
#         self.SalmonIndexlabel.setText(_translate("MainWindow", "Index for Salmon"))
#         self.SalmonIndexlineEdit.setToolTip(_translate("MainWindow", "Input the path of the Salmon Index"))
#         self.Bowtie2Indexlabel.setText(_translate("MainWindow", "Index for Bowtie2"))
#         self.Bowtie2IndexlineEdit.setToolTip(_translate("MainWindow", "Input the path of the Bowtie2 Index"))
# =============================================================================
# =============================================================================
#         self.Bowtie2dIndexlabel.setText(_translate("MainWindow", "Index for Bowtie2"))
#         self.Bowtie2dIndexlineEdit.setToolTip(_translate("MainWindow", "Input the path of the Bowtie2 Index"))
#         self.Bowtie2dIndexpushButton.setToolTip(_translate("MainWindow", "Click this to select one of the pre-installed index or for a custom index"))
#         self.Bowtie2dIndexpushButton.setText(_translate("MainWindow", "Browse"))
# =============================================================================

# =============================================================================
#         self.SalmonIndexpushButton.setToolTip(_translate("MainWindow", "Click this to select one of the pre-installed index or for a custom index"))
#         self.SalmonIndexpushButton.setText(_translate("MainWindow", "Browse"))
#         self.Bowtie2IndexpushButton.setToolTip(_translate("MainWindow", "Click this to select one of the pre-installed index or for a custom index"))
#         self.Bowtie2IndexpushButton.setText(_translate("MainWindow", "Browse"))
# =============================================================================
# =============================================================================
#         self.nextbuttonindexDNA.setIcon(QtGui.QIcon("./icons/arrow.svg"))
#         self.nextbuttonindexDNA.setIconSize(QtCore.QSize(35, 35))
#         self.previousbuttonindexDNA.setIcon(QtGui.QIcon("./icons/arrow1.svg"))
#         self.previousbuttonindexDNA.setIconSize(QtCore.QSize(35, 35))
#         self.DNAtabWidget.setTabText(self.DNAtabWidget.indexOf(self.Index_dna), _translate("MainWindow", " Indexes "))
#         self.DNAtabWidget.setTabIcon(self.DNAtabWidget.indexOf(self.Index_dna), QtGui.QIcon('./icons/index.svg'))
# =============================================================================
        ## End ##
        ## Add Params ##
        

# =============================================================================
#         self.Paramstool1labelDNA.setText(_translate("MainWindow", self.AlignercomboBoxDNA.currentText()))
#         self.Mandatory1labelDNA.setText(_translate("MainWindow", "Mandatory"))
#         self.Mandatory1lineEditDNA.setToolTip(_translate("MainWindow", "Manage mandatory parameters to run the tool"))
#         self.Additional1labelDNA.setText(_translate("MainWindow", "Additional"))
#         self.Additional1lineEditDNA.setToolTip(_translate("MainWindow", "Add additional parameters to run the tool"))
#         self.Paramstool2labelDNA.setText(_translate("MainWindow", self.VCcomboBoxDNA.currentText()))
#         self.Mandatory2labelDNA.setText(_translate("MainWindow", "Mandatory"))
#         self.Mandatory2lineEditDNA.setToolTip(_translate("MainWindow", "Manage mandatory parameters to run the tool"))
#         self.Additional2labelDNA.setText(_translate("MainWindow", "Additional"))
#         self.Additional2lineEditDNA.setToolTip(_translate("MainWindow", "Add additional parameters to run the tool"))
#         self.Paramstool3labelDNA.setText(_translate("MainWindow", self.AnnotatorcomboBoxDNA.currentText()))
#         self.Mandatory3labelDNA.setText(_translate("MainWindow", "Mandatory"))
#         self.Mandatory3lineEditDNA.setToolTip(_translate("MainWindow", "Manage mandatory parameters to run the tool"))
#         self.Additional3labelDNA.setText(_translate("MainWindow", "Additional"))
#         self.Additional3lineEditDNA.setToolTip(_translate("MainWindow", "Add additional parameters to run the tool"))
# =============================================================================
#==============================================================================
#         self.nextbuttonparamsDNA.setIcon(QtGui.QIcon("./icons/arrow.svg"))
#         self.nextbuttonparamsDNA.setIconSize(QtCore.QSize(35, 35))
#==============================================================================
#        self.nextbuttonparamsDNA.setText(_translate("MainWindow", "Finish"))
# =============================================================================
#         self.previousbuttonparamsDNA.setIcon(QtGui.QIcon("./icons/arrow1.svg"))
#         self.previousbuttonparamsDNA.setIconSize(QtCore.QSize(35, 35))
# =============================================================================
# =============================================================================
#         self.DNAtabWidget.setTabText(self.DNAtabWidget.indexOf(self.Params_dna), _translate("MainWindow", " Parameters"))
#         self.DNAtabWidget.setTabIcon(self.DNAtabWidget.indexOf(self.Params_dna), QtGui.QIcon('./icons/parameter.svg'))
# =============================================================================
        ## End ##
        
         ## Add run DNA##
        self.DNAtabWidget.setTabText(self.DNAtabWidget.indexOf(self.run_dna), _translate("MainWindow", " Run "))
        self.DNAtabWidget.setTabIcon(self.DNAtabWidget.indexOf(self.run_dna), QtGui.QIcon('./icons/run1.svg'))
#        self.DNAtabWidget.setStyleSheet(self.DNAtabWidget.indexOf(self.input_dna), ("background-color: #EBF6F5"))
        self.DNAtabWidget.setIconSize(QtCore.QSize(22, 22))
        self.nextbuttonrunDNA.setIcon(QtGui.QIcon("./icons/arrow.svg"))
        self.nextbuttonrunDNA.setIconSize(QtCore.QSize(35, 35))
        self.previousbuttonrunDNA.setIcon(QtGui.QIcon("./icons/arrow1.svg"))
        self.previousbuttonrunDNA.setIconSize(QtCore.QSize(35, 35))
        ##End##
        ##Add Result DNA##
        self.DNAtabWidget.setTabText(self.DNAtabWidget.indexOf(self.result_dna), _translate("MainWindow", " Results "))
        self.DNAtabWidget.setTabIcon(self.DNAtabWidget.indexOf(self.result_dna), QtGui.QIcon('./icons/results.svg'))
#        self.DNAtabWidget.setStyleSheet(self.DNAtabWidget.indexOf(self.input_dna), ("background-color: #EBF6F5"))
        self.DNAtabWidget.setIconSize(QtCore.QSize(22, 22))
        ##End##
        
        ## Add run RNA##
        self.RNAtabWidget.setTabText(self.RNAtabWidget.indexOf(self.run_rna), _translate("MainWindow", " Run "))
        self.RNAtabWidget.setTabIcon(self.RNAtabWidget.indexOf(self.run_rna), QtGui.QIcon('./icons/run1.svg'))
#        self.RNAtabWidget.setStyleSheet(self.RNAtabWidget.indexOf(self.input_rna), ("background-color: #EBF6F5"))
        self.RNAtabWidget.setIconSize(QtCore.QSize(22, 22))
        self.nextbuttonrunRNA.setIcon(QtGui.QIcon("./icons/arrow.svg"))
        self.nextbuttonrunRNA.setIconSize(QtCore.QSize(35, 35))
        self.previousbuttonrunRNA.setIcon(QtGui.QIcon("./icons/arrow1.svg"))
        self.previousbuttonrunRNA.setIconSize(QtCore.QSize(35, 35))
        ##End##
        ##Add Result RNA##
        self.RNAtabWidget.setTabText(self.RNAtabWidget.indexOf(self.result_rna), _translate("MainWindow", " Results "))
        self.RNAtabWidget.setTabIcon(self.RNAtabWidget.indexOf(self.result_rna), QtGui.QIcon('./icons/results.svg'))
#        self.RNAtabWidget.setStyleSheet(self.RNAtabWidget.indexOf(self.input_rna), ("background-color: #EBF6F5"))
        self.RNAtabWidget.setIconSize(QtCore.QSize(22, 22))
        ##End##        
        
        self.RunButton.setIcon(QtGui.QIcon("./icons/run1.svg"))
        self.RunButton.setIconSize(QtCore.QSize(100, 100))
        self.RunButton.setStyleSheet("background-color:#C7D6C1")
        
        self.RunButton_dna.setIcon(QtGui.QIcon("./icons/run1.svg"))
        self.RunButton_dna.setIconSize(QtCore.QSize(100, 100))
        self.RunButton_dna.setStyleSheet("background-color:#C7D6C1")        
        
#        self.ResultsButton.setText(_translate("MainWindow", "Results"))
        self.ResultsButton.setIcon(QtGui.QIcon("./icons/unlock.svg"))
        self.ResultsButton.setIconSize(QtCore.QSize(100, 100))
        self.ResultsButton.setStyleSheet("background-color: #C7D6C1")
        
        self.ResultsButton_dna.setIcon(QtGui.QIcon("./icons/unlock.svg"))
        self.ResultsButton_dna.setIconSize(QtCore.QSize(100, 100))
        self.ResultsButton_dna.setStyleSheet("background-color: #C7D6C1")
#         
#         self.DAGLabel.setText(_translate("MainWindow", "Pipeline"))
        self.RunLabel.setText(_translate("MainWindow", "Run"))
        self.ResultsLabel.setText(_translate("MainWindow", "Unlock"))
        font_label = QtGui.QFont()
        font_label.setPointSize(15)
        font_label.setBold(True)
        self.RunLabel.setFont(font_label)
        self.ResultsLabel.setFont(font_label)         
        
       
        self.RunLabel_dna.setFont(font_label)
        self.ResultsLabel_dna.setFont(font_label)
        self.RunLabel_dna.setText(_translate("MainWindow", "Run"))
        self.ResultsLabel_dna.setText(_translate("MainWindow", "Unlock"))        
        
        ## Add Create ##
#==============================================================================
#         self.CreateSnakefilepushButtonDNA.setText(_translate("MainWindow", "Create Snakefile"))
#         self.CreateConfigpushButtonDNA.setText(_translate("MainWindow", "Create Configfile"))
#         self.DNAtabWidget.setTabText(self.DNAtabWidget.indexOf(self.Create_dna), _translate("MainWindow", "Create"))
#==============================================================================
        ## End ##

        self.PipelinetabWidget.setTabText(self.PipelinetabWidget.indexOf(self.DNAseq), _translate("MainWindow", "DNA-Seq Pipeline"))
        self.PipelinetabWidget.setTabIcon(self.PipelinetabWidget.indexOf(self.DNAseq), QtGui.QIcon('./icons/dna.svg'))
        self.PipelinetabWidget.setIconSize(QtCore.QSize(22, 22))
#        self.PipelinetabWidget.setStyleSheet ("background-color: #EBF6F5") #fce4ec
#        self.PipelinetabWidget.setStyleSheet("background-color: #98FB98")#212121#FFFAFA
        self.PipelinetabWidget.setTabToolTip(self.PipelinetabWidget.indexOf(self.DNAseq), _translate("MainWindow", "Select this pipeline to generate Annotated VCFs"))

        ## Make Input as first tab ##
        self.SampleOrlabel_rna.setText(_translate("MainWindow", "Or"))
        self.SamplesYesradioButton_rna.setToolTip(_translate("MainWindow", "Files should be in specified format"))
        self.SamplesYesradioButton_rna.setText(_translate("MainWindow", "Upload from Folder"))
        self.SamplesNoradioButton_rna.setToolTip(_translate("MainWindow", "Tables should contain all the information"))
        self.SamplesNoradioButton_rna.setText(_translate("MainWindow", "Upload from Table"))
# =============================================================================
#         self.WDlabelRNA.setText(_translate("MainWindow", "Working directory"))
#         self.WDBrowseButtonRNA.setIcon(QtGui.QIcon("./icons/browse.svg"))
#         self.WDBrowseButtonRNA.setIconSize(QtCore.QSize(22, 22))
#         self.WDBrowseButtonRNA.setToolTip("Browse Working Directory")
# =============================================================================
        self.SampleFolderlabel.setText(_translate("MainWindow", "Samples Folder"))
        self.SampleFolderBrowseButton.setIcon(QtGui.QIcon("./icons/browse.svg"))
        self.SampleFolderBrowseButton.setIconSize(QtCore.QSize(22, 22))
        self.SampleFolderBrowseButton.setToolTip("Browse Samples Folder")
        self.Sampletablelabel.setText(_translate("MainWindow", "Samples Table"))
        
        self.FastaFilelabel.setText(_translate("MainWindow", "Fasta File"))
        self.AnnotatedFilelabelRNA.setText(_translate("MainWindow", "Annotated File"))
        self.TranscriptFilelabel.setText(_translate("MainWindow", "Transcript File"))
        
#        self.FastaBrowseButton.setText(_translate("MainWindow", "Browse"))
        self.SampletableBrowseButton.setIcon(QtGui.QIcon("./icons/browse.svg"))
        self.SampletableBrowseButton.setIconSize(QtCore.QSize(22, 22))
        self.SampletableBrowseButton.setToolTip("Browse Samples Table")
        
        self.FastaBrowseButton.setIcon(QtGui.QIcon("./icons/browse.svg"))
        self.FastaBrowseButton.setIconSize(QtCore.QSize(22, 22))
#        self.FastaBrowseButton.setStyleSheet("background-color: #aeaeae")
        self.FastaBrowseButton.setToolTip("Browse Fasta File")
#        self.AnnotatedBrowserButtonRNA.setText(_translate("MainWindow", "Browse"))
        self.AnnotatedBrowserButtonRNA.setIcon(QtGui.QIcon("./icons/browse.svg"))
        self.AnnotatedBrowserButtonRNA.setIconSize(QtCore.QSize(22, 22))
        self.AnnotatedBrowserButtonRNA.setToolTip("Browse Annotated File")
#        self.TranscriptBrowseButton.setText(_translate("MainWindow", "Browse"))
        self.TranscriptBrowseButton.setIcon(QtGui.QIcon("./icons/browse.svg"))
        self.TranscriptBrowseButton.setIconSize(QtCore.QSize(22, 22))
#        self.TranscriptBrowseButton.setStyleSheet("background-color: #aeaeae")
        self.TranscriptBrowseButton.setToolTip("Browse Transcript File")
#        self.SampleFolderBrowseButton.setText(_translate("MainWindow", "Browse"))
        
#        self.SampleFolderBrowseButton.setStyleSheet("background-color: #aeaeae")
        
        
# =============================================================================
#         self.FastalineEdit.setText(_translate("MainWindow", "/data/Priyanka/other_pipelines/iCOMIC/Test/gencode_input-RNA/GRCh38.primary_assembly.genome.fa"))
#         self.AnnotatedlineEditRNA.setText(_translate("MainWindow", "/data/Priyanka/other_pipelines/iCOMIC/Test/gencode_input-RNA/gencode.v29.annotation.gtf"))
#         self.TranscriptlineEdit.setText(_translate("MainWindow", "/data/Priyanka/other_pipelines/iCOMIC/Test/gencode_input-RNA/gencode.v29.transcripts.fa"))
#         self.SampleFolderLineEdit.setText(_translate("MainWindow", "/data/Priyanka/other_pipelines/iCOMIC"))
# =============================================================================
        self.nextbuttoninputRNA.setIcon(QtGui.QIcon("./icons/arrow.svg"))
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
#        self.fastQClabel_rna.setText(_translate("MainWindow", "fastQC"))
#        self.QClineEdit_rna.setText(_translate("MainWindow", " --threads 1 --quiet "))
        self.Cutadaptlabel_rna.setText(_translate("MainWindow", "Cutadapt"))
        self.CutadaptlineEdit_rna.setText(_translate("MainWindow", " --adapter AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC -A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT "))
#        self.MultiQClabel_rna.setText(_translate("MainWindow", "MultiQC"))
# =============================================================================
#         self.CreateSnakefilepushButton_rna.setText(_translate("MainWindow", "Create Snakefile for QC"))
#         self.CreateConfigfilepushButton_rna.setText(_translate("MainWindow", "Create Configfile for QC"))
# =============================================================================
        self.RunQCpushButton_rna.setText(_translate("MainWindow", "Trimming"))
        self.RunQCpushButton_rna.setIcon(QtGui.QIcon("./icons/run1.svg"))
        self.RunQCpushButton_rna.setIconSize(QtCore.QSize(22, 22))
#        self.RunQCpushButton_rna.setStyleSheet("background-color: #03a9f4")
        self.nextbuttonqcRNA.setIcon(QtGui.QIcon("./icons/arrow.svg"))
        self.nextbuttonqcRNA.setIconSize(QtCore.QSize(35, 35))
        self.previousbuttonqcRNA.setIcon(QtGui.QIcon("./icons/arrow1.svg"))
        self.previousbuttonqcRNA.setIconSize(QtCore.QSize(35, 35))
        self.RNAtabWidget.setTabText(self.RNAtabWidget.indexOf(self.QC_rna), _translate("MainWindow", " Quality Control "))
        self.RNAtabWidget.setTabIcon(self.RNAtabWidget.indexOf(self.QC_rna), QtGui.QIcon('./icons/qc.svg'))
        

        ## End ##
#        self.AlignerlabelRNA.setText(_translate("MainWindow", "Aligner"))
        self.AlignercomboBoxRNA.setStyleSheet("background-color: #578446")
        self.AlignercomboBoxRNA.setItemText(0, _translate("MainWindow", "hisat2"))
        self.AlignercomboBoxRNA.setItemText(1, _translate("MainWindow", "star"))
        self.AlignercomboBoxRNA.setItemText(2, _translate("MainWindow", "salmon"))
        self.AlignercomboBoxRNA.setItemText(3, _translate("MainWindow", "None"))
#        self.EMlabelRNa.setText(_translate("MainWindow", "EM Tools"))
        self.EMcomboBoxRNA.setStyleSheet("background-color: #578446")
        self.EMcomboBoxRNA.setItemText(0, _translate("MainWindow", "stringtie"))
        self.EMcomboBoxRNA.setItemText(1, _translate("MainWindow", "HTseq"))
        self.EMcomboBoxRNA.setItemText(2, _translate("MainWindow", "salmon"))
        self.EMcomboBoxRNA.setItemText(3, _translate("MainWindow", "None"))
#        self.DElabelRNA.setText(_translate("MainWindow", "DE Tools"))
        self.DEcomboBoxRNA.setStyleSheet("background-color: #578446")
        self.DEcomboBoxRNA.setItemText(0, _translate("MainWindow", "ballgown"))
        self.DEcomboBoxRNA.setItemText(1, _translate("MainWindow", "deseq2"))
        self.DEcomboBoxRNA.setItemText(2, _translate("MainWindow", "None"))
        self.nextbuttontoolRNA.setIcon(QtGui.QIcon("./icons/arrow.svg"))
        self.nextbuttontoolRNA.setIconSize(QtCore.QSize(35, 35))
        self.previousbuttontoolRNA.setIcon(QtGui.QIcon("./icons/arrow1.svg"))
        self.previousbuttontoolRNA.setIconSize(QtCore.QSize(35, 35))
        self.RNAtabWidget.setTabText(self.RNAtabWidget.indexOf(self.Tool_rna), _translate("MainWindow", " Tools Selection "))
        self.RNAtabWidget.setTabIcon(self.RNAtabWidget.indexOf(self.Tool_rna), QtGui.QIcon('./icons/tools.svg'))
        ## Add Index ##
#        self.InputIndexlabel.setText(_translate("MainWindow", "Input Indexes for RNA-Seq analysis"))
#        self.StarIndexlabel.setText(_translate("MainWindow", "Index for " + self.AlignercomboBoxRNA.currentText()))
        self.StarIndexlineEdit.setToolTip(_translate("MainWindow", "Input the path of the Index for" + self.AlignercomboBoxRNA.currentText()))
        self.StarIndexpushButton.setToolTip(_translate("MainWindow", "Click this to select one of the pre-installed index or for a custom index"))
#        self.StarIndexpushButton.setText(_translate("MainWindow", "Browse"))
        self.StarIndexpushButton.setIcon(QtGui.QIcon("./icons/browse.svg"))
        self.StarIndexpushButton.setIconSize(QtCore.QSize(22, 22))
#        self.StarIndexpushButton.setStyleSheet("background-color: #aeaeae")
        self.StarIndexpushButton.setToolTip("Browse Index File")
        self.OrLabel_rna.setText(_translate("MainWindow", "Or"))
#        self.StarIndexlineEdit.setText(_translate("MainWindow", "/data/Priyanka/other_pipelines/iCOMIC/Test/gencode_input-RNA/Ref/hisat2-index"))
#        self.StarIndexlineEdit.setText(_translate("MainWindow", "results/index/" +self.AlignercomboBoxRNA.currentText()))
# =============================================================================
#         self.CreateConfigfileforIndexrnapushButton.setText(_translate("MainWindow", "Create configfile for index"))
#         self.CreateSnakefileforIndexrnapushButton.setText(_translate("MainWindow", "Create Snakefile for index"))
# =============================================================================
        self.RunIndexrnapushButton.setText(_translate("MainWindow", "Generate Index"))
        self.RunIndexrnapushButton.setIcon(QtGui.QIcon("./icons/run1.svg"))
        self.RunIndexrnapushButton.setIconSize(QtCore.QSize(22, 22))
#        self.RunIndexrnapushButton.setStyleSheet("background-color: #03a9f4")
# =============================================================================
#         self.HISAT2Indexlabel.setText(_translate("MainWindow", "Index for HISAT2"))
#         self.HISAT2IndexlineEdit.setToolTip(_translate("MainWindow", "Input the path of the HISAT2 Index"))
#         self.SalmonIndexlabel.setText(_translate("MainWindow", "Index for Salmon"))
#         self.SalmonIndexlineEdit.setToolTip(_translate("MainWindow", "Input the path of the Salmon Index"))
#         self.Bowtie2Indexlabel.setText(_translate("MainWindow", "Index for Bowtie2"))
#         self.Bowtie2IndexlineEdit.setToolTip(_translate("MainWindow", "Input the path of the Bowtie2 Index"))
#         self.HISAT2IndexpushButton.setToolTip(_translate("MainWindow", "Click this to select one of the pre-installed index or for a custom index"))
#         self.HISAT2IndexpushButton.setText(_translate("MainWindow", "Browse"))
#         self.SalmonIndexpushButton.setToolTip(_translate("MainWindow", "Click this to select one of the pre-installed index or for a custom index"))
#         self.SalmonIndexpushButton.setText(_translate("MainWindow", "Browse"))
#         self.Bowtie2IndexpushButton.setToolTip(_translate("MainWindow", "Click this to select one of the pre-installed index or for a custom index"))
#         self.Bowtie2IndexpushButton.setText(_translate("MainWindow", "Browse"))
# =============================================================================
# =============================================================================
#         self.nextbuttonindexRNA.setIcon(QtGui.QIcon("./icons/arrow.svg"))
#         self.nextbuttonindexRNA.setIconSize(QtCore.QSize(35, 35))
#         self.previousbuttonindexRNA.setIcon(QtGui.QIcon("./icons/arrow1.svg"))
#         self.previousbuttonindexRNA.setIconSize(QtCore.QSize(35, 35))
#         self.RNAtabWidget.setTabText(self.RNAtabWidget.indexOf(self.Index_rna), _translate("MainWindow", " Indexes "))
#         self.RNAtabWidget.setTabIcon(self.RNAtabWidget.indexOf(self.Index_rna), QtGui.QIcon('./icons/index.svg'))
# =============================================================================
        ## End ##
        ## Add Params ##
# =============================================================================
#         self.Paramstool1labelRNA.setText(_translate("MainWindow", self.AlignercomboBoxRNA.currentText()))
#         self.Mandatory1labelRNA.setText(_translate("MainWindow", "Mandatory"))
#         self.Mandatory1lineEditRNA.setToolTip(_translate("MainWindow", "Manage mandatory parameters to run the tool"))
#         self.Additional1labelRNA.setText(_translate("MainWindow", "Additional"))
#         self.Additional1lineEditRNA.setToolTip(_translate("MainWindow", "Add additional parameters to run the tool"))
#         self.Paramstool2labelRNA.setText(_translate("MainWindow", self.EMcomboBoxRNA.currentText()))
#         self.Mandatory2labelRNA.setText(_translate("MainWindow", "Mandatory"))
#         self.Mandatory2lineEditRNA.setToolTip(_translate("MainWindow", "Manage mandatory parameters to run the tool"))
#         self.Additional2labelRNA.setText(_translate("MainWindow", "Additional"))
#         self.Additional2lineEditRNA.setToolTip(_translate("MainWindow", "Add additional parameters to run the tool"))
#         self.Paramstool3labelRNA.setText(_translate("MainWindow", self.DEcomboBoxRNA.currentText()))
#         self.Mandatory3labelRNA.setText(_translate("MainWindow", "Mandatory"))
#         self.Mandatory3lineEditRNA.setToolTip(_translate("MainWindow", "Manage mandatory parameters to run the tool"))
#         self.Additional3labelRNA.setText(_translate("MainWindow", "Additional"))
#         self.Additional3lineEditRNA.setToolTip(_translate("MainWindow", "Add additional parameters to run the tool"))
# =============================================================================
#==============================================================================
#         self.nextbuttonparamsRNA.setIcon(QtGui.QIcon("./icons/arrow.svg"))
#         self.nextbuttonparamsRNA.setIconSize(QtCore.QSize(35, 35))
#==============================================================================
# =============================================================================
#         self.nextbuttonparamsRNA.setText(_translate("MainWindow", "Finish"))
#         self.previousbuttonparamsRNA.setIcon(QtGui.QIcon("./icons/arrow1.svg"))
#         self.previousbuttonparamsRNA.setIconSize(QtCore.QSize(35, 35))
# =============================================================================
# =============================================================================
#         self.RNAtabWidget.setTabText(self.RNAtabWidget.indexOf(self.Params_rna), _translate("MainWindow", " Parameters"))
#         self.RNAtabWidget.setTabIcon(self.RNAtabWidget.indexOf(self.Params_rna), QtGui.QIcon('./icons/parameter.svg'))
# =============================================================================
        ## End ##
        ## Add Create ##
#==============================================================================
#         self.CreateSnakefilepushButtonRNA.setText(_translate("MainWindow", "Create Snakefile"))
#         self.CreateConfigpushButtonRNA.setText(_translate("MainWindow", "Create Configfile"))
#         self.RNAtabWidget.setTabText(self.RNAtabWidget.indexOf(self.Create_rna), _translate("MainWindow", "Create"))
#==============================================================================
        ## End ##
        self.PipelinetabWidget.setTabText(self.PipelinetabWidget.indexOf(self.RNAseq), _translate("MainWindow", "RNA-Seq Pipeline"))
        self.PipelinetabWidget.setTabIcon(self.PipelinetabWidget.indexOf(self.RNAseq), QtGui.QIcon('./icons/rna.svg'))
        self.PipelinetabWidget.setTabToolTip(self.PipelinetabWidget.indexOf(self.RNAseq), _translate("MainWindow", "Select this pipeline to generate Differentially Expressed Genes"))
        self.ShellTab.setTabText(self.ShellTab.indexOf(self.SnakemakeOutputTab), _translate("MainWindow", "Logs"))
        self.ShellTab.setTabIcon(self.ShellTab.indexOf(self.SnakemakeOutputTab), QtGui.QIcon('./icons/log.svg'))
        self.ShellTab.setIconSize(QtCore.QSize(22, 22))
# =============================================================================
#         self.ShellTab.setTabText(self.ShellTab.indexOf(self.PythonShellTab), _translate("MainWindow", "Snakemake Output"))
#         self.ShellTab.setTabIcon(self.ShellTab.indexOf(self.PythonShellTab), QtGui.QIcon('./icons/output.svg'))
# =============================================================================
        
#        self.DAGButton.setTextAlignment(QtCore.Qt.AlignBottom)
# =============================================================================
#         self.DAGButton.setIcon(QtGui.QIcon("./icons/dag.svg"))
#         self.DAGButton.setIconSize(QtCore.QSize(50, 50))
#         self.DAGButton.setStyleSheet("background-color:#C7D6C1")
# #        self.DAGButton.setStyleSheet("background-position: bottom;")
# #        self.RunButton.setText(_translate("MainWindow", "Run"))
#         self.RunButton.setIcon(QtGui.QIcon("./icons/run1.svg"))
#         self.RunButton.setIconSize(QtCore.QSize(50, 50))
#         self.RunButton.setStyleSheet("background-color:#C7D6C1")
# #        self.ResultsButton.setText(_translate("MainWindow", "Results"))
#         self.ResultsButton.setIcon(QtGui.QIcon("./icons/unlock.svg"))
#         self.ResultsButton.setIconSize(QtCore.QSize(50, 50))
#         self.ResultsButton.setStyleSheet("background-color: #C7D6C1")
#         
#         self.DAGLabel.setText(_translate("MainWindow", "Pipeline"))
#         self.RunLabel.setText(_translate("MainWindow", "Run"))
#         self.ResultsLabel.setText(_translate("MainWindow", "Unlock"))
# =============================================================================

        self.menuFile.setTitle(_translate("MainWindow", "File"))
#        self.menuFile.setIcon(QtGui.QIcon("./icons/file.svg"))
        self.menuOption.setTitle(_translate("MainWindow", "Option"))
#        self.menuOption.setIcon(QtGui.QIcon("./icons/option.svg"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
#        self.menuHelp.setIcon(QtGui.QIcon("./icons/help.svg"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionQuick_Start.setText(_translate("MainWindow", "Quick Start"))
        self.actionAbout_2.setText(_translate("MainWindow", "About"))
        self.actionSnakemake_Options.setText(_translate("MainWindow", "Snakemake Options"))
        ##Changelabel on choosing tools##
# =============================================================================
#         self.AlignercomboBoxDNA.activated[str].connect(self.on_changed_AlignerDNA)
#         self.VCcomboBoxDNA.activated[str].connect(self.on_changed_VC)
#         self.AnnotatorcomboBoxDNA.activated[str].connect(self.on_changed_Annotator)
#         self.AlignercomboBoxRNA.activated[str].connect(self.on_changed_AlignerRNA)
#         self.EMcomboBoxRNA.activated[str].connect(self.on_changed_EM)
#         self.DEcomboBoxRNA.activated[str].connect(self.on_changed_DE)
# =============================================================================
        ##Set Mandatory Parameters on tool selection##
# =============================================================================
#         params = open('params_dna.txt', 'r')
#         for line in params:
#             if self.AlignercomboBoxDNA.currentText() in line:
#                 mod_line = ' '.join(line.split()[1:])
#             if self.VCcomboBoxDNA.currentText() in line:
#                 mod_line_VC = ' '.join(line.split()[1:])
#             if self.AnnotatorcomboBoxDNA.currentText() in line:
#                 mod_line_annotator = ' '.join(line.split()[1:])
# 
# 
#         params = open('params_rna.txt', 'r')
#         for line in params:
#             if self.AlignercomboBoxRNA.currentText() in line:
#                 mod_line_aligner_rna = ' '.join(line.split()[1:])
#             if self.EMcomboBoxRNA.currentText() in line:
#                 mod_line_EM = ' '.join(line.split()[1:])
#             if self.DEcomboBoxRNA.currentText() in line:
#                 mod_line_DE = ' '.join(line.split()[1:])
# 
#         self.Mandatory1lineEditDNA.setText(_translate("MainWindow",mod_line))
#         self.Mandatory2lineEditDNA.setText(_translate("MainWindow",mod_line_VC))
#         self.Mandatory3lineEditDNA.setText(_translate("MainWindow",mod_line_annotator))
#         self.Mandatory1lineEditRNA.setText(_translate("MainWindow",mod_line_aligner_rna))
#         self.Mandatory2lineEditRNA.setText(_translate("MainWindow",mod_line_EM))
#         self.Mandatory3lineEditRNA.setText(_translate("MainWindow",mod_line_DE))
# =============================================================================
        
        self.nextbuttoninputDNA.clicked.connect(self.on_clicked_nextbuttoninputDNA)
        self.nextbuttonqcDNA.clicked.connect(self.on_clicked_nextbuttonqcDNA)
        self.nextbuttontoolDNA.clicked.connect(self.on_clicked_nextbuttonparamsDNA)
        self.nextbuttontoolDNA.clicked.connect(self.on_clicked_nextbuttontoolDNA)
#        self.nextbuttonindexDNA.clicked.connect(self.on_clicked_nextbuttonindexDNA)
#        self.nextbuttonparamsDNA.clicked.connect(self.on_clicked_nextbuttonparamsDNA)
        self.previousbuttonqcDNA.clicked.connect(self.on_clicked_previousbuttonqcDNA)
        self.previousbuttontoolDNA.clicked.connect(self.on_clicked_previousbuttontoolDNA)
        self.previousbuttonrunRNA.clicked.connect(self.on_clicked_previousbuttonrunDNA)
#        self.previousbuttonresultDNA.clicked.connect(self.on_clicked_previousbuttonrunDNA)
#        self.previousbuttonindexDNA.clicked.connect(self.on_clicked_previousbuttonindexDNA)
#        self.previousbuttonparamsDNA.clicked.connect(self.on_clicked_previousbuttonparamsDNA)
        self.nextbuttoninputRNA.clicked.connect(self.on_clicked_nextbuttoninputRNA)
        self.nextbuttonqcRNA.clicked.connect(self.on_clicked_nextbuttonqcRNA)
        self.nextbuttontoolRNA.clicked.connect(self.on_clicked_nextbuttonparamsRNA)
        self.nextbuttontoolRNA.clicked.connect(self.on_clicked_nextbuttontoolRNA)
#        self.nextbuttonindexRNA.clicked.connect(self.on_clicked_nextbuttonindexRNA)
        self.previousbuttonqcRNA.clicked.connect(self.on_clicked_previousbuttonqcRNA)
        self.previousbuttontoolRNA.clicked.connect(self.on_clicked_previousbuttontoolRNA)
#        self.previousbuttonindexRNA.clicked.connect(self.on_clicked_previousbuttonindexRNA)
#        self.previousbuttonparamsRNA.clicked.connect(self.on_clicked_previousbuttonparamsRNA)
        
#        self.ResultsButton.clicked.connect(self.on_clicked_ResultsButton)
        
#        self.SamplesYesradioButton.toggled.connect(self.on_check_SamplesYes_dna)
        self.SamplesNoradioButton.toggled.connect(self.on_check_SamplesNo_dna)
        self.SamplesNoradioButton_rna.toggled.connect(self.on_check_SamplesNo_rna)
        self.QCresults.clicked.connect(self.show_qc_textbox)
        self.QCresults.clicked.connect(self.show_qc_results)
        
        self.QCYesradioButton.toggled.connect(self.on_check_QC_dna)
        self.QCYesradioButton_rna.toggled.connect(self.on_check_QC_rna)
        self.QCresults_rna.clicked.connect(self.show_qc_textbox)
        self.QCresults_rna.clicked.connect(self.show_qc_results_rna)
        
#        self.QCYesradioButton.toggled.connect(self.on_check_QC_dna)
#        self.QCYesradioButton_rna.toggled.connect(self.on_check_QC_rna)
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
        



# =============================================================================
#         self.AlignercomboBoxDNA.activated[str].connect(self.mandatoryParams_AlignerDna)
#         self.VCcomboBoxDNA.activated[str].connect(self.mandatoryParams_VC)
#         self.AnnotatorcomboBoxDNA.activated[str].connect(self.mandatoryParams_Annotator)
#         self.AnnotatorcomboBoxDNA.currentIndexChanged.connect(self.not_snpeff)
#         self.AlignercomboBoxRNA.activated[str].connect(self.mandatoryParams_AlignerRna)
#         self.EMcomboBoxRNA.activated[str].connect(self.mandatoryParams_EM)
#         self.DEcomboBoxRNA.activated[str].connect(self.mandatoryParams_DE)
# =============================================================================


        ### To connect Create snakefile and Create Configfile to RUN ####
#==============================================================================
#         self.CreateSnakefilepushButtonDNA.clicked.connect(self.BP_one)
#         self.CreateConfigpushButtonDNA.clicked.connect(self.BP_two)
# 
#         self.CreateSnakefilepushButtonRNA.clicked.connect(self.BP_one)
#         self.CreateConfigpushButtonRNA.clicked.connect(self.BP_two)
#==============================================================================
        ###################################################################

        ##snakemake_options##
# =============================================================================
#         self.RunButton.clicked.connect(self.run_action_textbox)
#         self.RunButton.clicked.connect(self.run_action)
# =============================================================================
#        self.UnlockButton.clicked.connect(self.unlock_action)
#        self.DAGButton.clicked.connect(self.dag_action)
        ##data_browse##
        self.SamplesBrowseButtonDNA.clicked.connect(self.browse_data_samples)
#        self.SamplesBrowseButtonDNA.toggled.connect(self.toggle_samples)
        self.UnitsBrowseButtonDNA.clicked.connect(self.browse_data_units)
#        self.UnitsBrowseButtonDNA.toggled.connect(self.toggle_units)
        self.RefGenomeBrowseButtonDNA.clicked.connect(self.browse_data_ref)
        self.RefVariantpushButton.clicked.connect(self.browse_data_kv)
        ##Enable browse button for index##
        self.BWAIndexpushButton.clicked.connect(self.browse_bwaindex_dna)
# =============================================================================
#         self.Bowtie2dIndexpushButton.clicked.connect(self.browse_bowtie_dna)
        self.StarIndexpushButton.clicked.connect(self.browse_star_rna)
#         self.HISAT2IndexpushButton.clicked.connect(self.browse_hisat2_rna)
#         self.SalmonIndexpushButton.clicked.connect(self.browse_salmon_rna)
#         self.Bowtie2IndexpushButton.clicked.connect(self.browse_bowtie_rna)
# =============================================================================
        self.SampletableBrowseButton.clicked.connect(self.browse_data_sampletable)
        self.FastaBrowseButton.clicked.connect(self.browse_data_fasta)
        self.AnnotatedBrowserButtonRNA.clicked.connect(self.browse_data_annotated)
        self.TranscriptBrowseButton.clicked.connect(self.browse_data_transcript)
        self.SampleFolderBrowseButton.clicked.connect(self.browse_samples_folder)
#        self.CreateConfigpushButtonDNA.clicked.connect(self.create_config_dna)
        ##Run_QC##
#        self.CreateConfigfilepushButton.clicked.connect(self.config_qc_dna)
#        self.CreateSnakefilepushButton.clicked.connect(self.snakefile_qc_dna)
#        self.RunQCpushButton.clicked.connect(self.run_qc_dna_textbox)
        self.RunQCpushButton.clicked.connect(self.run_qc_textbox)
        self.RunQCpushButton.clicked.connect(self.run_qc_dna)
        
#        self.CreateConfigfilepushButton_rna.clicked.connect(self.config_qc_rna)
#        self.CreateSnakefilepushButton_rna.clicked.connect(self.snakefile_qc_rna)
#        self.RunQCpushButton_rna.clicked.connect(self.run_qc_rna_textbox)
        self.RunQCpushButton_rna.clicked.connect(self.run_qc_rna_textbox)
        self.RunQCpushButton_rna.clicked.connect(self.run_qc_rna)
        
        ##Add additional parameters##
#        self.CreateConfigpushButtonDNA.clicked.connect(self.add_params_dna)
        ##Run_indexing##
#        self.CreateSnakefileforIndexdnapushButton.clicked.connect(self.create_snakefile_for_index_dna)
#        self.CreateSnakefileforIndexrnapushButton.clicked.connect(self.create_snakefile_for_index_rna)
#        self.CreateConfigfileforIndexdnapushButton.clicked.connect(self.create_config_for_index_dna)
#        self.CreateConfigfileforIndexrnapushButton.clicked.connect(self.create_config_for_index_rna)
#        self.RunIndexdnapushButton.clicked.connect(self.run_index_dna_textbox)
        self.RunIndexdnapushButton.clicked.connect(self.run_index_text)
        self.RunIndexdnapushButton.clicked.connect(self.run_index_dna)
#        self.RunIndexrnapushButton.clicked.connect(self.run_index_rna_textbox)
        self.RunIndexrnapushButton.clicked.connect(self.run_index_text)
        self.RunIndexrnapushButton.clicked.connect(self.run_index_rna)
        ##Run_main##
#==============================================================================
#         self.CreateConfigpushButtonDNA.clicked.connect(self.create_config_dna)
#         self.CreateSnakefilepushButtonDNA.clicked.connect(self.create_snakefile_dna)
#         self.CreateSnakefilepushButtonDNA.clicked.connect(self.if_annovar)
#         self.CreateConfigpushButtonRNA.clicked.connect(self.create_config_rna)
#         self.CreateSnakefilepushButtonRNA.clicked.connect(self.create_snakefile_rna)
#==============================================================================
        ##show dag##
#        self.DAGButton.clicked.connect(self.show_dag)
        ##menu_popups##
        self.actionAbout_2.triggered.connect(self.about)
        self.actionQuick_Start.triggered.connect(self.quick_start)
# =============================================================================
#         self.SampleslineEditDNA.setText("/sysroot/home/anjana/Documents/iCOMIC-20200402T102703Z-001/iCOMIC/sample_demo")
#         self.RefGenomelineEditDNA.setText("/sysroot/home/anjana/Documents/iCOMIC-20200402T102703Z-001/iCOMIC/ref/hg38.fa")
#         self.RefVariantlineEditDNA.setText("/sysroot/home/anjana/Documents/iCOMIC-20200402T102703Z-001/iCOMIC/ref/dbsnp.vcf.gz")
# =============================================================================
        self.SampleslineEditDNA.setText("/data/Priyanka/other_pipelines/iCOMIC/sample_demo")
        self.RefGenomelineEditDNA.setText("/data/Priyanka/other_pipelines/iCOMIC/ref/hg38.fa")
        self.RefVariantlineEditDNA.setText("/data/Priyanka/other_pipelines/iCOMIC/ref/clinvar_20191231.vcf.gz")
        self.SampleFolderLineEdit.setText("/data/Priyanka/other_pipelines/iCOMIC/Test/Demo_rna/samples")
#        self.SampletablelineEdit.setText("")
        self.FastalineEdit.setText("/data/Priyanka/other_pipelines/iCOMIC/Test/Demo_rna/hg38.chr22.fa")
        self.AnnotatedlineEditRNA.setText("/data/Priyanka/other_pipelines/iCOMIC/Test/Demo_rna/chr22_refGene.gtf")
        self.TranscriptlineEdit.setText("/data/Priyanka/other_pipelines/iCOMIC/Test/Demo_rna/gencode.v29.transcripts.fa")
        self.BWAIndexlineEdit.setText("/data/Priyanka/other_pipelines/iCOMIC/ref/hg38.fa")
#        self.SampleFolderLineEdit.setText(_translate("MainWindow", "/data/Priyanka/other_pipelines/iCOMIC"))

        
        ##snakemake_output##
 #       self.RunButton.clicked.connect(self.progress)
# =============================================================================
#     def __init__(self):
#         
# #        self.ui = ui
# #        self.ui.setupUi(self)
#         
#         self.process = QtCore.QProcess()
#         self.process.started.connect(self.start_progress)
#         self.process.finished.connect(self.end_run)
#         self.process.readyReadStandardOutput.connect(self.snakemake_data_stdout)
#         self.process.readyReadStandardError.connect(self.snakemake_data_error)
#         
#         self.shell = ""
#         self.shell_error = ""
#         self._colors = {
#             'green': QtGui.QColor(0,170,0),
#             'red': QtGui.QColor(170,0,0),
#             'orange': QtGui.QColor(170,150,0),
#             'blue': QtGui.QColor(0,90,154),
#         }
#         
#         self._step_regex = re.compile("([0-9]+) of ([0-9]+) steps")
# =============================================================================

        
# =============================================================================
#         self.process.readyReadStandardOutput.connect(self.snakemake_data_stdout)
#         self.process.readyReadStandardError.connect(self.snakemake_data_error)
# =============================================================================
        
# =============================================================================
#         self.timer = QBasicTimer()
#         self.step = 0
#         self.RunQCpushButton.clicked.connect(self.doAction)
# ============================================================================
# =============================================================================
#     def my_function():
#         # """Do nothing, but document it.
#         #
#         # No, really, it doesn't do anything.
#         # """
#         pass
# 
#         print(my_function.__doc__)
#         #Do nothing, but document it.
# =============================================================================
# =============================================================================
#     def start_progress(self):
#         self.progressBar.setRange(0,1)
#
#     def timerEvent(self, e):
#
#         if self.step >= 100:
#
#             self.timer.stop()
#             self.btn.setText('Finished')
#             return
#
#         self.step = self.step + 1
#         self.pbar.setValue(self.step)
#
#
#     def doAction(self):
#
#         if self.timer.isActive():
#             self.timer.stop()
#             self.btn.setText('Start')
#         else:
#             self.timer.start(100, self)
#             self.btn.setText('Stop')
# =============================================================================
# =============================================================================
#         self.SamplesBrowseButtonDNA.clicked.connect(self.editor)
#         self.FastaBrowseButton.clicked.connect(self.editor)
# =============================================================================
#        self.RunButton.clicked.connect(self.on_runbutton_clicked)


# =============================================================================
#     def on_runbutton_clicked(self):
#         output = subprocess.check_output("snakemake", "--use-conda", "--unlock", shell = True )
#         print(output)
# =============================================================================

# =============================================================================
#     def progress(self):
#         self.completed = 0
#
#         while self.completed < 100:
#             self.completed += 0.0001
#             self.progressBar.setValue(self.completed)
# =============================================================================

    # --------------------------------------------------------------------
    # Running snakemake
    # --------------------------------------------------------------------

# =============================================================================
#     def _clean_line(self, line):
#         # TODO: surely there is a better way to do that and not overlap
#         # with tools.py ...
#         line = line.replace("b'\\r'", "")
#         line = line.replace("b'\r'", "")
#         line = line.replace("b'\\r '", "")
#         line = line.replace("b'\r '", "")
#         line = line.replace("b' '", "")
#         line = line.replace("\\t", "&nbsp;"*4)
#         line = line.replace("'b'", "")
#         for this in ["b'", 'b"', "\r"]:
#             if line.startswith(this):
#                 line = line.replace(this, "")
#         if line.startswith('b"'):
#             line = line.replace('b"', "")
#         line = line.rstrip("\\x1b[0m")
#         line = line.replace("\\x1b[33m", "")
#         return line
#     
#     def update_progress_bar(self, line):
#         """ Parse with a regex to retrieve current step and total step.
#         """
#         grouprex = self._step_regex.findall(line)
#         # Use last "x of y" (not the first item at position 0)
#         if grouprex:
#             step = int(grouprex[-1][0]) / float(grouprex[-1][1]) * 100
#             self.progressBar.setValue(step)
#         if "Nothing to be done" in line:
#             self.progressBar.setValue(100)
#             
#     def _set_pb_color(self, color):
#         self.progressBar.setStyleSheet("""
#             QProgressBar {{
#                 color: black;
#                 border: 2px solid grey;
#                 margin: 2px;
#                 border-radius: 5px;
#                 text-align: center;
#             }}
#             QProgressBar::chunk {{
#                 background: {};
#                 }}""".format(color))
# 
#     def snakemake_data_stdout(self):
#         """ Read standard output of snakemake process """
#         data = str(self.process.readAllStandardOutput())
# #        print(data)
#         self.shell += data
#         self.update_progress_bar(data)
# 
#         for this in data.split("\\n"):
#             line = this.strip()
#             print(line)
#             if line and len(line) > 3 and "complete in" not in line: # prevent all b'' strings
#                 line = self._clean_line(line)
#                 if len(line.strip()) == 0:
#                     continue
#                 return line, data
# #                self.textBrowser_PythonShellTab.append('<font style="color:blue">' + line +'</font>')
# 
#     def snakemake_data_error(self):
#         """ Read error output of snakemake process """
#         error = str(self.process.readAllStandardError())
#         self.shell_error += error
#         self.update_progress_bar(error)
#         for this in error.split("\\n"):
#             line = this.strip()
#             if line and len(line) > 3 and "complete in" not in line: # prevent all b'' strings
#                 line = self._clean_line(line)
#                 if line.startswith("b'"):
#                     line = line[2:]
#                     line.rstrip("'")
#                 grouprex = self._step_regex.findall(line)
#                 if grouprex:
#                     self.textBrowser_PythonShellTab.append('<font style="color:orange">' + line +'</font>')
#                 elif "Error" in line:
#                     self.textBrowser_PythonShellTab.append('<font style="color:red">' + line +'</font>')
#                 else:
#                     self.textBrowser_PythonShellTab.append('<font style="color:green">' + line +'</font>')
#                     
# 
# 
#     def start_progress(self):
#         self.progressBar.setRange(0,1)
# 
#     def end_run(self):
#         pal = self.progressBar.palette()
#         if self.progressBar.value() >= 100 :
#             self._set_pb_color(self._colors['green'].name())
#             self.info('Run done. Status: successful')
#         else:
#             self._set_pb_color(self._colors['red'].name())
#             text = 'Run manually to check the exact error or check the log.'
#             if "--unlock" in self.shell_error:
#                 text += "<br>You may need to unlock the directory. "
#                 text += "click on Unlock button"
#                 self.critical(text)
#             return
# 
# =============================================================================
    def multiqc_result(self):
        if os.path.exists("results_dna/multiqc/multiqc.html"):
            self.textBrowser.setTextColor(self._colors['blue'])
            filename = "results_dna/multiqc/multiqc.html"
            webbrowser.get('firefox').open(filename, new=0, autoraise=True)
        else:
            pass
        
    def vcf_result(self):
        path='results_dna/filtered/all.vcf.gz'
        self.result_dialog= ResultsDialog(path)
# =============================================================================
#         if os.path.splitext(path)[-1] == ".gz":
#             print('zipped')
#             with gzip.open(path, 'rb') as f:
#                 data = f.read()
#                 self.result_dialog.textEdit.setText(data.decode("utf-8"))
#         else:
#             print('not zipped')
#             with open(path, 'r') as f:
#                 data = f.read()
#                 self.result_dialog.textEdit.setText(data)
# =============================================================================
        
        self.result_dialog.show()
        
    def annotated_result(self):
        if self.AnnotatorcomboBoxDNA.currentText()=="SnpEff":
            path = "results_dna/annotated/all.vcf"
        elif self.AnnotatorcomboBoxDNA.currentText()=="Annovar":
            path = "results_dna/annotated/all.hg19_multianno.vcf"
            self.result_dialog= ResultsDialog(path)
            self.result_dialog.show()
        else:
            pass
        self.result_dialog= ResultsDialog(path)
        self.result_dialog.show()
        
    def de_result(self):
        path='results/de_results/SigDE.txt'
        self.result_dialog= ResultsDialog(path)
        self.result_dialog.show()
        
    def plot_view(self):
        if os.path.exists("results/de_results/plot_output.pdf"):
            filename = "results/de_results/plot_output.pdf"
            webbrowser.get('firefox').open(filename, new=0, autoraise=True)
        else:
            pass
# =============================================================================
#         result_name = "VCF file"
#         path="/data/Priyanka/other_pipelines/iCOMIC/Snakefile"
# =============================================================================
        
#        ResultsDialog.showDialog(self,path ='results_dna/filtered/all.vcf.gz')
#        self.result_dialog= ResultsDialog()
#        ResultsDialog().showDialog(path='results_dna/filtered/all.vcf.gz')
#        self.result_dialog.show()
# =============================================================================
#     def showDialog(self):
#         f = open('/data/Priyanka/other_pipelines/iCOMIC/Snakefile', 'r')
#         with f:
#             data = f.read()
#             self.result_dialog.textEdit.setText(data)    
# =============================================================================
        
    def multiqc_result_rna(self):
        if os.path.exists("results/multiqc/multiqc.html"):
            self.textBrowser.setTextColor(self._colors['blue'])
            filename = "results/multiqc/multiqc.html"
            webbrowser.get('firefox').open(filename, new=0, autoraise=True)
        else:
            pass
        
    def create_aligner_groupbox(self):
        font_label = QtGui.QFont()
        font_label.setPointSize(8.5)
        color  = QtGui.QColor(233, 10, 150)
        self.aligner_groupbox = QGroupBox("Aligner")
        self.vlayout= QtWidgets.QVBoxLayout()
#        self.vlayout.setSpacing
        self.hlayout0_aligner = QtWidgets.QHBoxLayout()
        font_info = QtGui.QFont()
        font_info.setPointSize(8.5)
        self.Alignerninfoicon_dna = QtWidgets.QPushButton(self.aligner_groupbox)
        self.Alignerninfoicon_dna.setFlat(True)
        self.Alignerninfoicon_dna.setGeometry(QtCore.QRect(48, 0, 20, 20))
        self.Alignerninfoicon_dna.setToolTip("xxxxxxxxx!")
        self.Alignerninfoicon_dna.setFont(font_info)
        self.Alignerninfoicon_dna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.Alignerninfoicon_dna.setIconSize(QtCore.QSize(13, 13)) 
        
        self.AlignercomboBoxDNA = QtWidgets.QComboBox()
        self.AlignercomboBoxDNA.move(20, 10)
        self.AlignercomboBoxDNA.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
#        self.AlignercomboBoxDNA.setIconSize(QtCore.QSize(16, 16))
        self.AlignercomboBoxDNA.setObjectName("AlignercomboBoxDNA")
        self.AlignercomboBoxDNA.addItem("")
        self.AlignercomboBoxDNA.addItem("")
        self.AlignercomboBoxDNA.addItem("")
        self.AlignercomboBoxDNA.addItem("")
        self.hlayout0_aligner.addWidget(self.AlignercomboBoxDNA)
        self.hlayout0_aligner.addStretch(0)
        self.vlayout.addItem(self.hlayout0_aligner)
        self.hlayout1_aligner = QtWidgets.QHBoxLayout()
        self.hlayout1_aligner.setSpacing(10)
        self.BWAIndexlabel = QtWidgets.QLabel()
#        self.BWAIndexlabel.setGeometry(QtCore.QRect(10, 90, 141, 17))
        self.BWAIndexlabel.setObjectName("BWAIndexlabel")
        self.BWAIndexlineEdit = QtWidgets.QLineEdit()
#        self.BWAIndexlineEdit.setGeometry(QtCore.QRect(170, 90, 331, 23))
        self.BWAIndexlineEdit.setObjectName("BWAIndexlineEdit")
        self.BWAIndexpushButton = QtWidgets.QPushButton()
#        self.BWAIndexpushButton.setGeometry(QtCore.QRect(600, 90, 30, 25))
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
#        self.progressBar_sub2_dna.setGeometry(QtCore.QRect(10, 230, 665, 17))
        self.progressBar_sub2_dna.setProperty("value", 0)
        self.progressBar_sub2_dna.setObjectName("progressBar_sub2_dna")
        self.hlayout0_pb.addWidget(self.progressBar_sub2_dna)
        self.vlayout.addItem(self.hlayout0_pb)
#        self.horizontalLayout_4.addWidget(self.RunIndexdnaButtonErroricon)

        
#        self.hlayout2 = QtWidgets.QHBoxLayout()
        
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
# =============================================================================
#         self.hlayout2.addWidget(self.param1_label_dna_1)
#         self.hlayout2.addWidget(self.param1_lineEdit_dna_1)
#         self.hlayout2.addWidget(self.param1_label_dna_3)
#         self.hlayout2.addWidget(self.param1_lineEdit_dna_3)
#         self.hlayout2.addWidget(self.param1_label_dna_5)
#         self.hlayout2.addWidget(self.param1_lineEdit_dna_5)
# =============================================================================
#        self.vlayout.addItem(self.hlayout2)
        
        
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
        self.hlayout4_aligner.addWidget(self.aligner_add_dna)
        self.vlayout.addItem(self.hlayout4_aligner)
        
        self.aligner_groupbox.setLayout(self.vlayout)
        
        font_param = QtGui.QFont()
        font_param.setBold(True)
#        self.Params_dna.setGeometry(QtCore.QRect(10, 10, 50, 17))
# =============================================================================
#         self.AlignerParamlabeldna = QtWidgets.QLabel()
#         self.AlignerParamlabeldna.setGeometry(QtCore.QRect(10, 10, 81, 17))
#         self.AlignerParamlabeldna.setObjectName('AlignerParamlabeldna')
#         self.AlignerParamlabeldna.setFont(font_param)
#         self.VCParamlabeldna = QtWidgets.QLabel()
#         self.VCParamlabeldna.setGeometry(QtCore.QRect(10, 98, 81, 17))
#         self.VCParamlabeldna.setObjectName('VCParamlabeldna')
#         self.VCParamlabeldna.setFont(font_param)
#         self.AnnotatorParamlabeldna = QtWidgets.QLabel()
#         self.AnnotatorParamlabeldna.setGeometry(QtCore.QRect(10, 186, 81, 17))
#         self.AnnotatorParamlabeldna.setObjectName('AnnotatorParamlabeldna')
#         self.AnnotatorParamlabeldna.setFont(font_param)
# =============================================================================
        
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
#        self.vlayout.setSpacing
        self.hlayout0_vc = QtWidgets.QHBoxLayout()
        
        font_info = QtGui.QFont()
        font_info.setPointSize(8.5)
        self.VariantCallerninfoicon_dna = QtWidgets.QPushButton(self.vc_groupbox)
        self.VariantCallerninfoicon_dna.setFlat(True)
        self.VariantCallerninfoicon_dna.setGeometry(QtCore.QRect(84, 0, 20, 20))
        self.VariantCallerninfoicon_dna.setToolTip("xxxxxxxxx!")
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
        self.hlayout4_vc.addWidget(self.vc_add_dna)
        self.vlayout_vc.addItem(self.hlayout4_vc)
        
        self.vc_groupbox.setLayout(self.vlayout_vc)
        
    def create_annotator_groupbox(self):
        self.annotator_groupbox = QGroupBox("Annotator")
        self.vlayout_annotator= QtWidgets.QVBoxLayout()
        self.vlayout.setSpacing(20)
        self.hlayout0_annotator = QtWidgets.QHBoxLayout()
        
        font_info = QtGui.QFont()
        font_info.setPointSize(8.5)
        self.VariantCallerninfoicon_dna = QtWidgets.QPushButton(self.annotator_groupbox)
        self.VariantCallerninfoicon_dna.setFlat(True)
        self.VariantCallerninfoicon_dna.setGeometry(QtCore.QRect(64, 0, 20, 20))
        self.VariantCallerninfoicon_dna.setToolTip("xxxxxxxxx!")
        self.VariantCallerninfoicon_dna.setFont(font_info)
        self.VariantCallerninfoicon_dna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.VariantCallerninfoicon_dna.setIconSize(QtCore.QSize(13, 13))         
        
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
#        self.RefNamelabelDNA.setGeometry(QtCore.QRect(50, 150, 294, 17))
        self.RefNamelabelDNA.setObjectName("RefNamelabelDNA")
        self.RefNamecomboBoxDNA = QtWidgets.QComboBox()
#        self.RefNamecomboBoxDNA.setGeometry(QtCore.QRect(345, 150, 215, 23))
        self.RefNamecomboBoxDNA.setStyleSheet ("background-color: #578446")
#        self.RefNamecomboBoxDNA.setIconSize(QtCore.QSize(16, 16))
        self.RefNamecomboBoxDNA.setObjectName("RefNamecomboBoxDNA")
        self.RefNamecomboBoxDNA.addItem("GRCh38.86")
        self.RefNamecomboBoxDNA.addItem("hg19")
        self.RefNamecomboBoxDNA.addItem("GRCh37.75")
        self.hlayout1_annotator.addWidget(self.RefNamelabelDNA)
        self.hlayout1_annotator.addWidget(self.RefNamecomboBoxDNA)
        self.vlayout_annotator.addItem(self.hlayout1_annotator)
#        self.RefNamecomboBoxDNA.addItem("hg38")
        
        
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
        self.hlayout4_annotator.addWidget(self.annotator_add_dna)
        self.vlayout_annotator.addItem(self.hlayout4_annotator)
        self.annotator_groupbox.setLayout(self.vlayout_annotator)
        
    def create_group_next(self):
        self.next_groupbox = QGroupBox()
#        self.next_groupbox.setFlat(True)
        self.vlayout_next= QtWidgets.QVBoxLayout()
        self.nextbuttontoolDNA = QtWidgets.QPushButton()
        self.nextbuttontoolDNA.setGeometry(QtCore.QRect(635, 400, 45, 45))
#        self.nextbuttontoolDNA.move(635, 500)
        self.nextbuttontoolDNA.setObjectName("nextbuttontoolDNA")
        ###
        self.previousbuttontoolDNA = QtWidgets.QPushButton()
        self.previousbuttontoolDNA.setGeometry(QtCore.QRect(10, 400, 45, 45))
#        self.previousbuttontoolDNA.move(10, 500)
        self.previousbuttontoolDNA.setObjectName("previousbuttontoolDNA")
        
        self.hbox_next = QtWidgets.QHBoxLayout()
        self.hbox_next.addWidget(self.previousbuttontoolDNA, 0, alignment=QtCore.Qt.AlignLeft)
        self.hbox_next.addWidget(self.nextbuttontoolDNA, 0, alignment=QtCore.Qt.AlignRight)
        
#        self.hbox_next.addStretch()
        self.vlayout_next.addItem(self.hbox_next)
        self.next_groupbox.setLayout(self.vlayout_next)
        
    def create_aligner_groupbox_rna(self):
        font_label = QtGui.QFont()
        font_label.setPointSize(8.5)
        color  = QtGui.QColor(233, 10, 150)
        self.aligner_groupbox_rna = QGroupBox("Aligner")
        self.vlayout_rna= QtWidgets.QVBoxLayout()
#        self.vlayout.setSpacing
        self.hlayout0_aligner_rna = QtWidgets.QHBoxLayout()
        
        font_info = QtGui.QFont()
        font_info.setPointSize(8.5)
        self.Alignerninfoicon_rna = QtWidgets.QPushButton(self.aligner_groupbox_rna)
        self.Alignerninfoicon_rna.setFlat(True)
        self.Alignerninfoicon_rna.setGeometry(QtCore.QRect(48, 0, 20, 20))
        self.Alignerninfoicon_rna.setToolTip("xxxxxxxxx!")
        self.Alignerninfoicon_rna.setFont(font_info)
        self.Alignerninfoicon_rna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.Alignerninfoicon_rna.setIconSize(QtCore.QSize(13, 13))         
        
        self.AlignercomboBoxRNA = QtWidgets.QComboBox()
        self.AlignercomboBoxRNA.move(20, 10)
        self.AlignercomboBoxRNA.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
#        self.AlignercomboBoxDNA.setIconSize(QtCore.QSize(16, 16))
        self.AlignercomboBoxRNA.setObjectName("AlignercomboBoxRNA")
        self.AlignercomboBoxRNA.addItem("")
        self.AlignercomboBoxRNA.addItem("")
        self.AlignercomboBoxRNA.addItem("")
        self.AlignercomboBoxRNA.addItem("")
        self.hlayout0_aligner_rna.addWidget(self.AlignercomboBoxRNA)
        self.hlayout0_aligner_rna.addStretch(0)
        self.vlayout_rna.addItem(self.hlayout0_aligner_rna)
        self.hlayout1_aligner_rna = QtWidgets.QHBoxLayout()
        self.hlayout1_aligner_rna.setSpacing(10)
        self.StarIndexlabel = QtWidgets.QLabel()
#        self.BWAIndexlabel.setGeometry(QtCore.QRect(10, 90, 141, 17))
        self.StarIndexlabel.setObjectName("StarIndexlabel")
        self.StarIndexlineEdit = QtWidgets.QLineEdit()
#        self.BWAIndexlineEdit.setGeometry(QtCore.QRect(170, 90, 331, 23))
        self.StarIndexpushButton = QtWidgets.QPushButton()
#        self.StarIndexpushButton.setGeometry(QtCore.QRect(600, 90, 30, 25))
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
#        self.horizontalLayout_4.addWidget(self.RunIndexrnaButtonErroricon)
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
#        self.horizontalLayout_4.addWidget(self.RunIndexdnaButtonErroricon)

        
#        self.hlayout2 = QtWidgets.QHBoxLayout()
        
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
# =============================================================================
#         self.hlayout2.addWidget(self.param1_label_dna_1)
#         self.hlayout2.addWidget(self.param1_lineEdit_dna_1)
#         self.hlayout2.addWidget(self.param1_label_dna_3)
#         self.hlayout2.addWidget(self.param1_lineEdit_dna_3)
#         self.hlayout2.addWidget(self.param1_label_dna_5)
#         self.hlayout2.addWidget(self.param1_lineEdit_dna_5)
# =============================================================================
#        self.vlayout.addItem(self.hlayout2)
        
        
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
        self.hlayout4_aligner_rna.addWidget(self.aligner_add_rna)
        self.vlayout_rna.addItem(self.hlayout4_aligner_rna)
        
        self.aligner_groupbox_rna.setLayout(self.vlayout_rna)
        
        font_param = QtGui.QFont()
        font_param.setBold(True)
#        self.Params_dna.setGeometry(QtCore.QRect(10, 10, 50, 17))
# =============================================================================
#         self.AlignerParamlabelrna = QtWidgets.QLabel()
#         self.AlignerParamlabelrna.setGeometry(QtCore.QRect(10, 10, 81, 17))
#         self.AlignerParamlabelrna.setObjectName('AlignerParamlabelrna')
#         self.EMParamlabelrna = QtWidgets.QLabel()
#         self.EMParamlabelrna.setGeometry(QtCore.QRect(10, 98, 81, 17))
#         self.EMParamlabelrna.setObjectName('EMParamlabelrna')
#         self.DEParamlabelrna = QtWidgets.QLabel()
#         self.DEParamlabelrna.setGeometry(QtCore.QRect(10, 186, 81, 17))
#         self.DEParamlabelrna.setObjectName('DEParamlabelrna')
# =============================================================================
        
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
#        self.vlayout.setSpacing
        self.hlayout0_em = QtWidgets.QHBoxLayout()
        
        font_info = QtGui.QFont()
        font_info.setPointSize(8.5)
        self.VariantCallerninfoicon_rna = QtWidgets.QPushButton(self.em_groupbox)
        self.VariantCallerninfoicon_rna.setFlat(True)
        self.VariantCallerninfoicon_rna.setGeometry(QtCore.QRect(125, 0, 20, 20))
        self.VariantCallerninfoicon_rna.setToolTip("xxxxxxxxx!")
        self.VariantCallerninfoicon_rna.setFont(font_info)
        self.VariantCallerninfoicon_rna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.VariantCallerninfoicon_rna.setIconSize(QtCore.QSize(13, 13))              
        
        self.EMcomboBoxRNA = QtWidgets.QComboBox()
        self.EMcomboBoxRNA.setObjectName("EMcomboBoxRNA")
        self.EMcomboBoxRNA.addItem("")
        self.EMcomboBoxRNA.addItem("")
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
        self.VariantCallerninfoicon_rna = QtWidgets.QPushButton(self.de_groupbox)
        self.VariantCallerninfoicon_rna.setFlat(True)
        self.VariantCallerninfoicon_rna.setGeometry(QtCore.QRect(140, 0, 20, 20))
        self.VariantCallerninfoicon_rna.setToolTip("xxxxxxxxx!")
        self.VariantCallerninfoicon_rna.setFont(font_info)
        self.VariantCallerninfoicon_rna.setIcon(QtGui.QIcon("./icons/info.svg"))
        self.VariantCallerninfoicon_rna.setIconSize(QtCore.QSize(13, 13))         
        
        self.DEcomboBoxRNA = QtWidgets.QComboBox()
        self.DEcomboBoxRNA.setObjectName("DEcomboBoxRNA")
        self.DEcomboBoxRNA.addItem("")
        self.DEcomboBoxRNA.addItem("")
        self.DEcomboBoxRNA.addItem("")
        self.hlayout0_de.addWidget(self.DEcomboBoxRNA)
        self.hlayout0_de.addStretch(0)
        self.vlayout_de.addItem(self.hlayout0_de)
        
# =============================================================================
#         self.hlayout1_de = QtWidgets.QHBoxLayout()
#         self.RefNamelabelDNA = QtWidgets.QLabel()
# #        self.RefNamelabelDNA.setGeometry(QtCore.QRect(50, 150, 294, 17))
#         self.RefNamelabelDNA.setObjectName("RefNamelabelDNA")
#         self.RefNamecomboBoxDNA = QtWidgets.QComboBox()
# #        self.RefNamecomboBoxDNA.setGeometry(QtCore.QRect(345, 150, 215, 23))
#         self.RefNamecomboBoxDNA.setStyleSheet ("background-color: #578446")
# #        self.RefNamecomboBoxDNA.setIconSize(QtCore.QSize(16, 16))
#         self.RefNamecomboBoxDNA.setObjectName("RefNamecomboBoxDNA")
#         self.RefNamecomboBoxDNA.addItem("GRCh38.86")
#         self.RefNamecomboBoxDNA.addItem("hg19")
#         self.RefNamecomboBoxDNA.addItem("GRCh37.75")
#         self.hlayout1_annotator.addWidget(self.RefNamelabelDNA)
#         self.hlayout1_annotator.addWidget(self.RefNamecomboBoxDNA)
#         self.vlayout_annotator.addItem(self.hlayout1_annotator)
# =============================================================================
#        self.RefNamecomboBoxDNA.addItem("hg38")
        
        
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
        self.hlayout4_de.addWidget(self.de_add_rna)
        self.vlayout_de.addItem(self.hlayout4_de)
        self.de_groupbox.setLayout(self.vlayout_de)
        
    def create_group_next_rna(self):
        self.next_groupbox_rna = QGroupBox()
#        self.next_groupbox.setFlat(True)
        self.vlayout_next_rna= QtWidgets.QVBoxLayout()
        self.nextbuttontoolRNA = QtWidgets.QPushButton()
        self.nextbuttontoolRNA.setGeometry(QtCore.QRect(635, 400, 45, 45))
#        self.nextbuttontoolDNA.move(635, 500)
        self.nextbuttontoolRNA.setObjectName("nextbuttontoolRNA")
        ###
        self.previousbuttontoolRNA = QtWidgets.QPushButton()
        self.previousbuttontoolRNA.setGeometry(QtCore.QRect(10, 400, 45, 45))
#        self.previousbuttontoolDNA.move(10, 500)
        self.previousbuttontoolRNA.setObjectName("previousbuttontoolRNA")
        
        self.hbox_next_rna = QtWidgets.QHBoxLayout()
        self.hbox_next_rna.addWidget(self.previousbuttontoolRNA, 0, alignment=QtCore.Qt.AlignLeft)
        self.hbox_next_rna.addWidget(self.nextbuttontoolRNA, 0, alignment=QtCore.Qt.AlignRight)
        
#        self.hbox_next.addStretch()
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
        self.new_values_str=[]
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
# =============================================================================
#                 print(self.DNAtabWidget.currentIndex())
#                 print("Input Samples table!")
# =============================================================================
            elif not os.path.exists(self.SampleslineEditDNA.text()):
#                print("File doesn't exist! Check the path!")
                self.SamplesErrortextDNA.show()
                self.SamplesErrortextDNA.setText("File doesn't exist! Check the path!")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
#                print(self.DNAtabWidget.currentIndex())
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
#                    print(self.DNAtabWidget.currentIndex())
                    with open('name_check.txt') as errorcheck:
                        content = errorcheck.readline()
#                        print(content)
#                    print(content.rstrip())
                    self.SamplesErrortextDNA.show()
                    self.SamplesErrortextDNA.setText(content.rstrip())
                else:
#                    print("ok")
# =============================================================================
#                     self.DNAtabWidget.setCurrentIndex(1)
#                     self.DNAtabWidget.setTabEnabled(1, True)
# =============================================================================
#                    print(self.DNAtabWidget.currentIndex())
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
                        self.VCcomboBoxDNA.addItem("")
                        self.VCcomboBoxDNA.setItemText(1, "MuSE")
# =============================================================================
#                         self.VCcomboBoxDNA.setCurrentIndex(3)
#                         self.VCcomboBoxDNA.findText('bcftools_call')
#                         self.VCcomboBoxDNA.removeItem(0)
#                         self.VCcomboBoxDNA.removeItem(1)
#                         self.VCcomboBoxDNA.removeItem(2)
#                         self.VCcomboBoxDNA.removeItem(4)                        
# =============================================================================
                    else:
                        self.VCcomboBoxDNA.addItem("")
                        self.VCcomboBoxDNA.addItem("")
                        self.VCcomboBoxDNA.setItemText(0, "GATK_HC")
                        self.VCcomboBoxDNA.setItemText(1, "bcftools_call")
                        self.VCcomboBoxDNA.setItemText(2, "freebayes")
                        
                        
                    
            if self.RefGenomelineEditDNA.text() == '':
#                print("Input reference genome file!")
                self.RefGenomeErrortextDNA.show()
                self.RefGenomeErrortextDNA.setText("Input reference genome file!")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            elif not os.path.exists(self.RefGenomelineEditDNA.text()):
#                print("File doesn't exist! Check the path!")
                self.RefGenomeErrortextDNA.show()
                self.RefGenomeErrortextDNA.setText("File doesn't exist! Check the path!")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            elif os.path.splitext(self.RefGenomelineEditDNA.text())[-1] != ".fa":
#                print("File should have extension '.fa'")
                self.RefGenomeErrortextDNA.show()
                self.RefGenomeErrortextDNA.setText("File should have extension '.fa'")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
# =============================================================================
#             else:
#                 print("ok")
#                 self.DNAtabWidget.setCurrentIndex(1)
#                 self.DNAtabWidget.setTabEnabled(1, True)
# =============================================================================
             
            if self.RefVariantlineEditDNA.text()== '':
#                print("Input reference known variants file!")
                self.RefVariantErrortextDNA.show()
                self.RefVariantErrortextDNA.setText("Input reference known variants file!")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            elif not os.path.exists(self.RefVariantlineEditDNA.text()):
#                print("File doesn't exist! Check the path!")
                self.RefVariantErrortextDNA.show()
                self.RefVariantErrortextDNA.setText("File doesn't exist! Check the path!")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            elif os.path.splitext(self.RefVariantlineEditDNA.text())[-1] != ".gz":
#                print("File should have extension '.gz'")
                self.RefVariantErrortextDNA.show()
                self.RefVariantErrortextDNA.setText("File should have extension '.gz'")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            elif (self.RefVariantlineEditDNA.text()).split(".")[-2] != "vcf":
#                print("File should have extension '.gz'")
                self.RefVariantErrortextDNA.show()
                self.RefVariantErrortextDNA.setText("File should be compressed 'vcf'")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            elif (os.path.splitext(self.RefGenomelineEditDNA.text())[-1] == ".fa" and not os.path.exists('name_check.txt') and os.path.splitext(self.RefVariantlineEditDNA.text())[-1] == ".gz" and (self.RefVariantlineEditDNA.text().split(".")[-2]) == 'vcf'):
#                print("ok")
                self.SamplesErrortextDNA.hide()
                self.UnitsErrortextDNA.hide()
                self.RefGenomeErrortextDNA.hide()
                self.RefVariantErrortextDNA.hide()
                self.DNAtabWidget.setCurrentIndex(1)
                self.DNAtabWidget.setTabEnabled(1, True)
                self.textBrowser.setTextColor(self._colors['blue'])
                self.textBrowser.append("Click on the 'View FastQC Results' button to view the FastQC report \n")
#                process=subprocess.Popen(["snakemake", "--unlock"])
        else:
            if self.UnitslineEditDNA.text() == '':
                self.UnitsErrortextDNA.show()
                self.UnitsErrortextDNA.setText("Input Units table!")
#                print("Input Units table!")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            elif not os.path.exists(self.UnitslineEditDNA.text()):
                self.UnitsErrortextDNA.show()
                self.UnitsErrortextDNA.setText("File doesn't exist! Check the path!")
#                print("File doesn't exist! Check the path!")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            elif os.path.splitext(self.UnitslineEditDNA.text())[-1] != ".tsv":
#                print("File should have extension '.tsv'")
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
                        self.VCcomboBoxDNA.addItem("")
                        self.VCcomboBoxDNA.setItemText(1, "MuSE")
# =============================================================================
#                         self.VCcomboBoxDNA.setCurrentIndex(3)
#                         self.VCcomboBoxDNA.removeItem(0)
#                         self.VCcomboBoxDNA.removeItem(1)
#                         self.VCcomboBoxDNA.removeItem(2)
#                         self.VCcomboBoxDNA.removeItem(4)
# =============================================================================
                    else:
                        self.VCcomboBoxDNA.addItem("")
                        self.VCcomboBoxDNA.addItem("")
                        self.VCcomboBoxDNA.setItemText(0, "GATK_HC")
                        self.VCcomboBoxDNA.setItemText(1, "bcftools_call")
                        self.VCcomboBoxDNA.setItemText(2, "freebayes")
#                        self.VCcomboBoxDNA.removeItem(3)
            if self.RefGenomelineEditDNA.text() == '':
#                print("Input Units table!")
                self.RefGenomeErrortextDNA.show()
                self.RefGenomeErrortextDNA.setText("Input reference genome file!")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            elif not os.path.exists(self.RefGenomelineEditDNA.text()):
#                print("File doesn't exist! Check the path!")
                self.RefGenomeErrortextDNA.show()
                self.RefGenomeErrortextDNA.setText("File doesn't exist! Check the path!")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            elif os.path.splitext(self.RefGenomelineEditDNA.text())[-1] != ".fa":
#                print("File should have extension '.fa'")
                self.RefGenomeErrortextDNA.show()
                self.RefGenomeErrortextDNA.setText("File should have extension '.fa'")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
# =============================================================================
#                 self.DNAtabWidget.setCurrentIndex(1)
#                 self.DNAtabWidget.setTabEnabled(1, True)
# =============================================================================
#                print("ok")
            if self.RefVariantlineEditDNA.text()== '':
#                print("Input Units table!")
                self.RefVariantErrortextDNA.show()
                self.RefVariantErrortextDNA.setText("Input reference known variants file!")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            elif not os.path.exists(self.RefVariantlineEditDNA.text()):
#                print("File doesn't exist! Check the path!")
                self.RefVariantErrortextDNA.show()
                self.RefVariantErrortextDNA.setText("File doesn't exist! Check the path!")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            elif os.path.splitext(self.RefVariantlineEditDNA.text())[-1] != ".gz":
#                print("File should have extension '.gz'")
                self.RefVariantErrortextDNA.show()
                self.RefVariantErrortextDNA.setText("File should have extension '.gz'")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            elif (self.RefVariantlineEditDNA.text()).split(".")[-2] != "vcf":
#                print("File should have extension '.gz'")
                self.RefVariantErrortextDNA.show()
                self.RefVariantErrortextDNA.setText("File should be compressed 'vcf'")
                self.DNAtabWidget.setCurrentIndex(0)
                self.DNAtabWidget.setTabEnabled(1, False)
            elif (list(unitsdf) == list_tsv_col and os.path.splitext(self.RefGenomelineEditDNA.text())[-1] == ".fa" and os.path.splitext(self.RefVariantlineEditDNA.text())[-1] == ".gz" and (self.RefVariantlineEditDNA.text().split(".")[-2]) == 'vcf'):
                self.SamplesErrortextDNA.hide()
                self.UnitsErrortextDNA.hide()
                self.RefGenomeErrortextDNA.hide()
                self.RefVariantErrortextDNA.hide()
                self.DNAtabWidget.setCurrentIndex(1)
                self.DNAtabWidget.setTabEnabled(1, True)
                self.textBrowser.setTextColor(self._colors['blue'])
                self.textBrowser.append("Click on the 'View FastQC Results' button to view the FastQC report \n")
#                subprocess.run(["snakemake", "--unlock"])
#                print("ok")    
    
# =============================================================================
#     def on_clicked_nextbuttoninputDNA(self):
#         if self.SamplesYesradioButton.isChecked() == True:
#             if self.SampleslineEditDNA.text() == '':
#                 self.DNAtabWidget.setCurrentIndex(0)
#                 self.DNAtabWidget.setTabEnabled(1, False)
#                 self.SamplesErrortextDNA.setText("Input Samples folder path!")
#             
#             elif self.RefGenomelineEditDNA.text() == '':
#                 self.RefGenomeErrortextDNA.setText("Input reference genome file!")
#                 self.DNAtabWidget.setCurrentIndex(0)
#                 self.DNAtabWidget.setTabEnabled(1, False)
#             elif self.RefVariantlineEditDNA.text()== '':
#                 self.RefVariantErrortextDNA.setText("Input reference known variants file!")
#                 self.DNAtabWidget.setCurrentIndex(0)
#                 self.DNAtabWidget.setTabEnabled(1, False)
#             elif not os.path.exists(self.SampleslineEditDNA.text()):
#                 self.SamplesErrortextDNA.setText("File doesn't exist! Check the path!")
#                 self.DNAtabWidget.setCurrentIndex(0)
#                 self.DNAtabWidget.setTabEnabled(1, False)
#             elif not os.path.exists(self.RefGenomelineEditDNA.text()):
#                 self.RefGenomeErrortextDNA.setText("File doesn't exist! Check the path!")
#                 self.DNAtabWidget.setCurrentIndex(0)
#                 self.DNAtabWidget.setTabEnabled(1, False)
#             elif not os.path.exists(self.RefVariantlineEditDNA.text()):
#                 self.RefVariantErrortextDNA.setText("File doesn't exist! Check the path!")
#                 self.DNAtabWidget.setCurrentIndex(0)
#                 self.DNAtabWidget.setTabEnabled(1, False)
#             elif os.path.exists(self.SampleslineEditDNA.text()):
#                 inputfile = fileinput.input("check_for_correct_filename_check.py", inplace = 1)
#                 for l in inputfile:
#                     if "test_dir =" in l:
#                         print(l.replace(l, "test_dir = '"+self.SampleslineEditDNA.text()+"'"))
#                     else:
#                         print(l.rstrip())
#                 inputfile.close()
#                 subprocess.run(["python", "check_for_correct_filename.py"])
#                 if os.path.exists('name_check.txt'):
#                     with open('name_check.txt') as errorcheck:
#                         self.SamplesErrortextDNA.setText(errorcheck.readline())
#                 else:
#                     file = fileinput.input("write_tsv.py", inplace = 1)
#                     for l in file:
#                         if "test_dir =" in l:
#                             print(l.replace(l, "test_dir = '"+self.SampleslineEditDNA.text()+"'"))
#                         else:
#                             print(l.rstrip())
#                     file.close()
#                     subprocess.run(["python", "write_tsv.py"])
#                     unitsdf =pd.read_table(self.UnitslineEditDNA.text(), header=0)
#                     if pd.isnull(unitsdf["condition"][0]) == False:
#                         self.VCcomboBoxDNA.setCurrentIndex(3)
#                         self.VCcomboBoxDNA.removeItem(0)
#                         self.VCcomboBoxDNA.removeItem(1)
#                         self.VCcomboBoxDNA.removeItem(2)
#                         self.VCcomboBoxDNA.removeItem(4)
#                     else:
#                         self.VCcomboBoxDNA.removeItem(3)
#                     self.DNAtabWidget.setCurrentIndex(1)
#                     self.DNAtabWidget.setTabEnabled(1, True)
#             elif os.path.exists(self.RefGenomelineEditDNA.text()):
#                 if os.path.splitext(self.RefGenomelineEditDNA.text())[-1] != ".fa":
#                     self.RefGenomeErrortextDNA.setText("File should have extension '.fa'")
#                 else:
#                     self.DNAtabWidget.setCurrentIndex(1)
#                     self.DNAtabWidget.setTabEnabled(1, True)
#             elif os.path.exists(self.RefVariantlineEditDNA.text()):
#                 if os.path.splitext(self.RefGenomelineEditDNA.text())[-1] != ".vcf.gz":
#                     self.RefVariantErrortextDNA.setText("File should have extension '.vcf.gz'")
#                 else:
#                     self.DNAtabWidget.setCurrentIndex(1)
#                     self.DNAtabWidget.setTabEnabled(1, True)
#         else:
#             if self.UnitslineEditDNA.text() == '':
#                 self.UnitsErrortextDNA.setText("Input Units table!")
#                 self.DNAtabWidget.setCurrentIndex(0)
#                 self.DNAtabWidget.setTabEnabled(1, False)
#             elif self.RefGenomelineEditDNA.text() == '':
#                 self.RefGenomeErrortextDNA.setText("Input reference genome file!")
#                 self.DNAtabWidget.setCurrentIndex(0)
#                 self.DNAtabWidget.setTabEnabled(1, False)
#             elif self.RefVariantlineEditDNA.text()== '':
#                 self.RefVariantErrortextDNA.setText("Input reference known variants file!")
#                 self.DNAtabWidget.setCurrentIndex(0)
#                 self.DNAtabWidget.setTabEnabled(1, False)
#             elif not os.path.exists(self.UnitslineEditDNA.text()):
#                 self.UnitsErrortextDNA.setText("File doesn't exist! Check the path!")
#                 self.DNAtabWidget.setCurrentIndex(0)
#                 self.DNAtabWidget.setTabEnabled(1, False)
#             elif not os.path.exists(self.RefGenomelineEditDNA.text()):
#                 self.RefGenomeErrortextDNA.setText("File doesn't exist! Check the path!")
#                 self.DNAtabWidget.setCurrentIndex(0)
#                 self.DNAtabWidget.setTabEnabled(1, False)
#             elif not os.path.exists(self.RefVariantlineEditDNA.text()):
#                 self.RefVariantErrortextDNA.setText("File doesn't exist! Check the path!")
#                 self.DNAtabWidget.setCurrentIndex(0)
#                 self.DNAtabWidget.setTabEnabled(1, False)
#             elif os.path.exists(self.UnitslineEditDNA.text()):
#                 if os.path.splitext(self.UnitslineEditDNA.text())[-1] != ".tsv":
#                     self.UnitsErrortextDNA.setText("File should have extension '.tsv'")
#                 else:
#                     unitsdf =pd.read_table(self.UnitslineEditDNA.text(), header=0)
#                     arr = []
#                     for item in unitsdf["sample"]:
#                         arr.append(item)
#                     sample_df = pd.DataFrame({'sample': np.unique(arr)})
#                     sample_df.to_csv('samples.tsv', sep = '\t', index=False)
#                     if pd.isnull(unitsdf["condition"][0]) == False:
#                         self.VCcomboBoxDNA.setCurrentIndex(3)
#                         self.VCcomboBoxDNA.removeItem(0)
#                         self.VCcomboBoxDNA.removeItem(1)
#                         self.VCcomboBoxDNA.removeItem(2)
#                         self.VCcomboBoxDNA.removeItem(4)
#                     else:
#                         self.VCcomboBoxDNA.removeItem(3)
#                     self.DNAtabWidget.setCurrentIndex(1)
#                     self.DNAtabWidget.setTabEnabled(1, True)
#             elif os.path.exists(self.RefGenomelineEditDNA.text()):
#                 if os.path.splitext(self.RefGenomelineEditDNA.text())[-1] != ".fa":
#                     self.RefGenomeErrortextDNA.setText("File should have extension '.fa'")
#                 else:
#                     self.DNAtabWidget.setCurrentIndex(1)
#                     self.DNAtabWidget.setTabEnabled(1, True)
#             elif os.path.exists(self.RefVariantlineEditDNA.text()):
#                 if os.path.splitext(self.RefGenomelineEditDNA.text())[-1] != ".vcf.gz":
#                     self.RefVariantErrortextDNA.setText("File should have extension '.vcf.gz'")
#                 else:
#                     self.DNAtabWidget.setCurrentIndex(1)
#                     self.DNAtabWidget.setTabEnabled(1, True)
# =============================================================================
            
# =============================================================================
#     def on_clicked_nextbuttoninputDNA(self):
#         if self.SamplesYesradioButton.isChecked() == True:
#             if self.SampleslineEditDNA.text() == '':
#                 self.DNAtabWidget.setCurrentIndex(0)
#                 self.DNAtabWidget.setTabEnabled(1, False)
#                 self.SamplesErrortextDNA.setText("Input Samples folder path")
#             else:
#                 inputfile = fileinput.input("check_for_correct_filename.py", inplace = 1)
#                 for l in inputfile:
#                     if "test_dir =" in l:
#                         print(l.replace(l, "test_dir = '"+self.SampleslineEditDNA.text()+"'"))
#                     else:
#                         print(l.rstrip())
#                 inputfile.close()
#                 subprocess.run(["python", "check_for_correct_filename.py"])
#                 if os.path.exists('name_check.txt'):
#                     self.DNAtabWidget.setCurrentIndex(0)
#                     self.DNAtabWidget.setTabEnabled(1, False)
#                     with open('name_check.txt') as errorcheck:
#                         self.SamplesErrortextDNA.setText(errorcheck.readline())
#                 else:
#                     file = fileinput.input("write_tsv.py", inplace = 1)
#                     for l in file:
#                         if "test_dir =" in l:
#                             print(l.replace(l, "test_dir = '"+self.SampleslineEditDNA.text()+"'"))
#                         else:
#                             print(l.rstrip())
#                     file.close()
#                     subprocess.run(["python", "write_tsv.py"])
#                     unitsdf =pd.read_table(self.UnitslineEditDNA.text(), header=0)
#                     if pd.isnull(unitsdf["condition"][0]) == False:
#                         self.VCcomboBoxDNA.setCurrentIndex(3)
#                         self.VCcomboBoxDNA.removeItem(0)
#                         self.VCcomboBoxDNA.removeItem(1)
#                         self.VCcomboBoxDNA.removeItem(2)
#                         self.VCcomboBoxDNA.removeItem(4)
#                     else:
#                         self.VCcomboBoxDNA.removeItem(3)
#                     
#                     self.DNAtabWidget.setCurrentIndex(1)
#                     self.DNAtabWidget.setTabEnabled(1, True)
#         elif self.SamplesNoradioButton.isChecked() == True:
#             if self.UnitslineEditDNA.text() == '':
#                 self.DNAtabWidget.setCurrentIndex(0)
#                 self.DNAtabWidget.setTabEnabled(1, False)
#                 self.UnitsErrortextDNA.setText("Input units file")
#             else:
#                 if os.path.splitext(self.UnitslineEditDNA.text())[-1] != ".tsv":
#                     self.UnitsErrortextDNA.setText("Table should be in .tsv format")
#                     self.DNAtabWidget.setCurrentIndex(0)
#                     self.DNAtabWidget.setTabEnabled(1, False)
#                 else:
#                     unitsdf =pd.read_table(self.UnitslineEditDNA.text(), header=0)
#                     arr = []
#                     for item in unitsdf["sample"]:
#                         arr.append(item)
#                     sample_df = pd.DataFrame({'sample': np.unique(arr)})
#                     sample_df.to_csv('samples.tsv', sep = '\t', index=False)
#                     if pd.isnull(unitsdf["condition"][0]) == False:
#                         self.VCcomboBoxDNA.setCurrentIndex(3)
#                         self.VCcomboBoxDNA.removeItem(0)
#                         self.VCcomboBoxDNA.removeItem(1)
#                         self.VCcomboBoxDNA.removeItem(2)
#                         self.VCcomboBoxDNA.removeItem(4)
#                     else:
#                         self.VCcomboBoxDNA.removeItem(3)
#                     self.DNAtabWidget.setCurrentIndex(1)
#                     self.DNAtabWidget.setTabEnabled(1, True)
# =============================================================================
# =============================================================================
#                     df =pd.read_table(self.UnitslineEditDNA.text(), header=0)
#                     if pd.isnull(df["condition"][0]) == "false":
#                         self.VCcomboBoxDNA.item(0).setEnabled(False)
#                         self.VCcomboBoxDNA.item(1).setEnabled(False)
#                         self.VCcomboBoxDNA.item(2).setEnabled(False)
#                         self.VCcomboBoxDNA.item(4).setEnabled(False)
#                     else:
#                         self.VCcomboBoxDNA.item(3).setEnabled(False)
# =============================================================================
            
# =============================================================================
#         elif self.RefGenomelineEditDNA.text() == '':
#             self.DNAtabWidget.setCurrentIndex(0)
#             self.DNAtabWidget.setTabEnabled(1, False)
#             self.RefGenomeErrortextDNA.setText("Input reference genome file")
#         else:
#             if os.path.splitext(self.RefGenomelineEditDNA.text())[-1] != ".fa":
#                 self.DNAtabWidget.setCurrentIndex(0)
#                 self.DNAtabWidget.setTabEnabled(1, False)
#                 self.RefGenomeErrortextDNA.setText("File should have extension .fa")
#             else:
#                 self.DNAtabWidget.setCurrentIndex(1)
#                 self.DNAtabWidget.setTabEnabled(1, True)
# =============================================================================
        
            
                
         
# =============================================================================
#             msg= QMessageBox()
#             msg.setText("upload samples file!")
#             msg.show()
#             msg.exec_()
# =============================================================================           
# =============================================================================
#         else:
#             self.DNAtabWidget.setCurrentIndex(1)
#             self.DNAtabWidget.setTabEnabled(1, True)
# =============================================================================
#        self.QC_dna.setEnabled(True)
                
    def param_display(self):
        _translate = QtCore.QCoreApplication.translate
        path_aligner = './params/'+self.AlignercomboBoxDNA.currentText()+'.csv'
        path_vc = './params/'+self.VCcomboBoxDNA.currentText()+'.csv'
        path_annotator = './params/'+self.AnnotatorcomboBoxDNA.currentText()+'.csv'
# =============================================================================
#         self.AlignerParamlabeldna.setText(_translate("MainWindow", self.AlignercomboBoxDNA.currentText()))
#         self.VCParamlabeldna.setText(_translate("MainWindow", self.VCcomboBoxDNA.currentText()))
#         self.AnnotatorParamlabeldna.setText(_translate("MainWindow", self.AnnotatorcomboBoxDNA.currentText()))
# =============================================================================
        dataframe = pd.read_csv(path_aligner, header=0) # specifying that the table has column names
        essential = dataframe[dataframe["Essential"] == "yes"]
#        print(essential.iloc[1, 2])
        
        number_of_essential = len(essential) # returns number of essential parameters
#        print(number_of_essential)
        label_array_param1 = [self.param1_label_dna_1, self.param1_label_dna_2, self.param1_label_dna_3, self.param1_label_dna_4, self.param1_label_dna_5, self.param1_label_dna_6]
        line_edit_array_param1 = [self.param1_lineEdit_dna_1,self.param1_lineEdit_dna_2, self.param1_lineEdit_dna_3, self.param1_lineEdit_dna_4, self.param1_lineEdit_dna_5, self.param1_lineEdit_dna_6]
        for i, j, k in zip(range(number_of_essential), label_array_param1, line_edit_array_param1): 
            j.show()
            j.setText(essential.iloc[i, 2])
            k.show()
            k.setText(str(essential.iloc[i, 4]))
            
        
            
        dataframe_vc = pd.read_csv(path_vc, header=0) # specifying that the table has column names
        essential_vc = dataframe_vc[dataframe_vc["Essential"] == "yes"]
#        print(essential.iloc[1, 2])
        
        number_of_essential_vc = len(essential_vc) # returns number of essential parameters
#        print(number_of_essential)
        label_array_param2 = [self.param2_label_dna_1, self.param2_label_dna_2, self.param2_label_dna_3, self.param2_label_dna_4, self.param2_label_dna_5, self.param2_label_dna_6]
        line_edit_array_param2 = [self.param2_lineEdit_dna_1,self.param2_lineEdit_dna_2, self.param2_lineEdit_dna_3, self.param2_lineEdit_dna_4, self.param2_lineEdit_dna_5, self.param2_lineEdit_dna_6]
        for i, j, k in zip(range(number_of_essential_vc), label_array_param2, line_edit_array_param2): 
            j.show()
            j.setText(essential_vc.iloc[i, 2])
            k.show()
            k.setText(str(essential_vc.iloc[i, 4]))
            
        dataframe_annotator = pd.read_csv(path_annotator, header=0) # specifying that the table has column names
        essential_annotator = dataframe_annotator[dataframe_annotator["Essential"] == "yes"]
#        print(essential.iloc[1, 2])
        
        number_of_essential_annotator = len(essential_annotator) # returns number of essential parameters
#        print(number_of_essential)
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
#            print("yes")
            self.DNAtabWidget.setCurrentIndex(2)
            self.DNAtabWidget.setTabEnabled(2, True)
        else:
#            print("no")
            self.qc_warning = showQCDialog()
#            if self.qc_warning.initUI== QMessageBox.Yes:
            if self.qc_warning.returnValue==QMessageBox.Yes:
                self.DNAtabWidget.setCurrentIndex(2)
                self.DNAtabWidget.setTabEnabled(2, True)
#                print('Yes clicked')
                                         
            if self.qc_warning.returnValue== QMessageBox.Cancel:
#                print('not')
                self.DNAtabWidget.setCurrentIndex(1)
                self.DNAtabWidget.setTabEnabled(2, False)
#        self.Tool_dna.setEnabled(True)
        self.DNAtabWidget.setTabEnabled(2, True)
#        subprocess.run(["snakemake", "--unlock"])
    def on_clicked_nextbuttontoolDNA(self):
#        _translate = QtCore.QCoreApplication.translate
#        self.on_clicked_nextbuttonparamsDNA()
        self.index_warning()
        self.DNAtabWidget.setCurrentIndex(3)
#        self.Index_dna.setEnabled(True)
        self.DNAtabWidget.setTabEnabled(3, True)
        
        self.create_config_dna()
        self.create_snakefile_dna()
        self.if_annovar()
        self.textBrowser.setTextColor(self._colors['blue'])
        self.textBrowser.append("Click on the 'Run' button below to start your analysis \n")
#        subprocess.run(["snakemake", "--unlock"])
        
# =============================================================================
#         path_aligner = './params/'+self.AlignercomboBoxDNA.currentText()+'.csv'
#         path_vc = './params/'+self.VCcomboBoxDNA.currentText()+'.csv'
#         path_annotator = './params/'+self.AnnotatorcomboBoxDNA.currentText()+'.csv'
#         self.AlignerParamlabeldna.setText(_translate("MainWindow", self.AlignercomboBoxDNA.currentText()))
#         self.VCParamlabeldna.setText(_translate("MainWindow", self.VCcomboBoxDNA.currentText()))
#         self.AnnotatorParamlabeldna.setText(_translate("MainWindow", self.AnnotatorcomboBoxDNA.currentText()))
#         dataframe = pd.read_csv(path_aligner, header=0) # specifying that the table has column names
#         essential = dataframe[dataframe["Essential"] == "yes"]
# #        print(essential.iloc[1, 2])
#         
#         number_of_essential = len(essential) # returns number of essential parameters
# #        print(number_of_essential)
#         label_array_param1 = [self.param1_label_dna_1, self.param1_label_dna_2, self.param1_label_dna_3, self.param1_label_dna_4, self.param1_label_dna_5, self.param1_label_dna_6]
#         line_edit_array_param1 = [self.param1_lineEdit_dna_1,self.param1_lineEdit_dna_2, self.param1_lineEdit_dna_3, self.param1_lineEdit_dna_4, self.param1_lineEdit_dna_5, self.param1_lineEdit_dna_6]
#         for i, j, k in zip(range(number_of_essential), label_array_param1, line_edit_array_param1): 
#             j.show()
#             j.setText(essential.iloc[i, 2])
#             k.show()
#             k.setText(str(essential.iloc[i, 4]))
#             
#         
#             
#         dataframe_vc = pd.read_csv(path_vc, header=0) # specifying that the table has column names
#         essential_vc = dataframe_vc[dataframe_vc["Essential"] == "yes"]
# #        print(essential.iloc[1, 2])
#         
#         number_of_essential_vc = len(essential_vc) # returns number of essential parameters
# #        print(number_of_essential)
#         label_array_param2 = [self.param2_label_dna_1, self.param2_label_dna_2, self.param2_label_dna_3, self.param2_label_dna_4, self.param2_label_dna_5, self.param2_label_dna_6]
#         line_edit_array_param2 = [self.param2_lineEdit_dna_1,self.param2_lineEdit_dna_2, self.param2_lineEdit_dna_3, self.param2_lineEdit_dna_4, self.param2_lineEdit_dna_5, self.param2_lineEdit_dna_6]
#         for i, j, k in zip(range(number_of_essential_vc), label_array_param2, line_edit_array_param2): 
#             j.show()
#             j.setText(essential_vc.iloc[i, 2])
#             k.show()
#             k.setText(str(essential_vc.iloc[i, 4]))
#             
#         dataframe_annotator = pd.read_csv(path_annotator, header=0) # specifying that the table has column names
#         essential_annotator = dataframe_annotator[dataframe_annotator["Essential"] == "yes"]
# #        print(essential.iloc[1, 2])
#         
#         number_of_essential_annotator = len(essential_annotator) # returns number of essential parameters
# #        print(number_of_essential)
#         label_array_param3 = [self.param3_label_dna_1, self.param3_label_dna_2, self.param3_label_dna_3, self.param3_label_dna_4, self.param3_label_dna_5, self.param3_label_dna_6]
#         line_edit_array_param3 = [self.param3_lineEdit_dna_1,self.param3_lineEdit_dna_2, self.param3_lineEdit_dna_3, self.param3_lineEdit_dna_4, self.param3_lineEdit_dna_5, self.param3_lineEdit_dna_6]
#         for i, j, k in zip(range(number_of_essential_annotator), label_array_param3, line_edit_array_param3): 
#             j.show()
#             j.setText(essential_annotator.iloc[i, 2])
#             k.show()
#             k.setText(str(essential_annotator.iloc[i, 4]))
#             
#         self.BWAIndexlabel.setText(_translate("MainWindow", "Index for " + self.AlignercomboBoxDNA.currentText()))
#         self.BWAIndexlineEdit.setToolTip(_translate("MainWindow", "Input the path of the Index for" + self.AlignercomboBoxDNA.currentText()))
# =============================================================================
# =============================================================================
#         with open('aligner_params.txt', 'w') as aligner_params:
#             aligner_params.write(self.AlignercomboBoxDNA.currentText() + " : ' '")
#         with open('vc_params.txt', 'w') as vc_params:
#             vc_params.write(self.VCcomboBoxDNA.currentText() + " : '")
#         with open('annotator_params.txt', 'w') as annotator_params:
#             annotator_params.write(self.AnnotatorcomboBoxDNA.currentText() + " : '")
# =============================================================================
# =============================================================================
#     def on_clicked_nextbuttonindexDNA(self):
#         if self.BWAIndexlineEdit.text()=='':
#             self.BWAIndexErrortext.show()
#             self.BWAIndexErrortext.setText("Please input index path!")
#             self.DNAtabWidget.setCurrentIndex(3)
#             self.DNAtabWidget.setTabEnabled(4, False)
#         elif not os.path.exists(self.BWAIndexlineEdit.text()):
#             self.BWAIndexErrortext.setText("Filed doesn't exist! Please check the path!")
#             self.BWAIndexErrortext.show()
#             self.DNAtabWidget.setCurrentIndex(3)
#             self.DNAtabWidget.setTabEnabled(4, False)
#         elif os.path.exists(self.BWAIndexlineEdit.text()):
#             if os.path.splitext(self.BWAIndexlineEdit.text())[-1] != ".fa":
#                 self.BWAIndexErrortext.show()
#                 self.BWAIndexErrortext.setText("File should have extension '.fa'")
#             else:
#                 self.DNAtabWidget.setCurrentIndex(4)
#                 self.DNAtabWidget.setTabEnabled(4, True)
# =============================================================================
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
#        self.DNAtabWidget.setCurrentIndex(5)
#        self.DNAtabWidget.setTabEnabled(5, True)
# =============================================================================
#         self.RunButton.setEnabled(True)
#         self.RunLabel.setEnabled(True)
# #        self.Create_dna.setEnabled(True)
#         self.RunButtonErroricon.hide()
#         self._set_color(self._colors['blue'].name(), pb = self.progressBar)
# =============================================================================
        
#        self.message = WarningMessage()
#        self.message.show()
# =============================================================================
#         self.message..connect(self.close_message)
#         
#     def close_message(self):
#         self.message.close()
# =============================================================================
        self.essential_dict_aligner = self.get_essential(path ='./params/'+self.AlignercomboBoxDNA.currentText()+'.csv', essential_line_edit_array= [self.param1_lineEdit_dna_1,self.param1_lineEdit_dna_2, self.param1_lineEdit_dna_3, self.param1_lineEdit_dna_4, self.param1_lineEdit_dna_5, self.param1_lineEdit_dna_6] )
        with open('aligner_params.txt', 'w') as aligner_params:
            aligner_params.write(self.AlignercomboBoxDNA.currentText() + " : '")
            for k, v in self.essential_dict_aligner.items():
                aligner_params.write(k +''+ str(v) + " ")
            aligner_params.write("'")
            aligner_params.close()
        self.essential_dict_vc = self.get_essential(path ='./params/'+self.VCcomboBoxDNA.currentText()+'.csv', essential_line_edit_array =[self.param2_lineEdit_dna_1,self.param2_lineEdit_dna_2, self.param2_lineEdit_dna_3, self.param2_lineEdit_dna_4, self.param2_lineEdit_dna_5, self.param2_lineEdit_dna_6])
        with open('vc_params.txt', 'w') as vc_params:
            vc_params.write(self.VCcomboBoxDNA.currentText() + " : '")
            for k, v in self.essential_dict_vc.items():
                vc_params.write(k +''+ str(v) + " ")
            vc_params.write("'")
            vc_params.close()
        self.essential_dict_annotator = self.get_essential(path ='./params/'+self.AnnotatorcomboBoxDNA.currentText()+'.csv', essential_line_edit_array=[self.param3_lineEdit_dna_1,self.param3_lineEdit_dna_2, self.param3_lineEdit_dna_3, self.param3_lineEdit_dna_4, self.param3_lineEdit_dna_5, self.param3_lineEdit_dna_6] )
        with open('annotator_params.txt', 'w') as annotator_params:
            if self.AnnotatorcomboBoxDNA.currentText() == "SnpEff":
                annotator_params.write(self.AnnotatorcomboBoxDNA.currentText() + " : '-Xmx4g ")
            else:
                annotator_params.write(self.AnnotatorcomboBoxDNA.currentText() + " : '")
            for k, v in self.essential_dict_annotator.items():
                annotator_params.write(k +''+ str(v) + " ")
            annotator_params.write("'")
            annotator_params.close()
            
        
        
        
    def on_clicked_previousbuttonqcDNA(self):
        self.DNAtabWidget.setCurrentIndex(0)
#        self.input_dna.setEnabled(True)
        self.DNAtabWidget.setTabEnabled(0, True)
    def on_clicked_previousbuttontoolDNA(self):
        self.DNAtabWidget.setCurrentIndex(1)
#        self.QC_dna.setEnabled(True)
        self.DNAtabWidget.setTabEnabled(1, True)
    def on_clicked_previousbuttonindexDNA(self):
        self.DNAtabWidget.setCurrentIndex(2)
#        self.Tool_dna.setEnabled(True)
        self.DNAtabWidget.setTabEnabled(2, True)
    def on_clicked_previousbuttonparamsDNA(self):
        self.DNAtabWidget.setCurrentIndex(3)       
#        self.Index_dna.setEnabled(True)
        self.DNAtabWidget.setTabEnabled(3, True)
        
    def on_clicked_previousbuttonrunDNA(self):
        self.DNAtabWidget.setCurrentIndex(2)       
        self.DNAtabWidget.setTabEnabled(2, True)
    
    def on_clicked_previousbuttonresultDNA(self):
        self.DNAtabWidget.setCurrentIndex(3)       
        self.DNAtabWidget.setTabEnabled(3, True)
        
    def on_clicked_nextbuttoninputRNA(self):
# =============================================================================
#         self.RNAtabWidget.setCurrentIndex(1)
# #        self.QC_rna.setEnabled(True)
#         self.RNAtabWidget.setTabEnabled(1, True)
#         if self.SamplesNoradioButton_rna.isChecked()==True:
#             subprocess.run(["python", "rename.py"])
# =============================================================================
#==============================================================================
#             print("checked")
#         else:
#             print("not")
#==============================================================================
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
                    pass
# =============================================================================
#                 else:
#                     self.RNAtabWidget.setCurrentIndex(1)
#                     self.RNAtabWidget.setTabEnabled(1, True)
# =============================================================================
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
# =============================================================================
#             else:
#                 self.RNAtabWidget.setCurrentIndex(1)
#                 self.RNAtabWidget.setTabEnabled(1, True)
# =============================================================================
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
# =============================================================================
#             else:
#                 self.RNAtabWidget.setCurrentIndex(1)
#                 self.RNAtabWidget.setTabEnabled(1, True)
# =============================================================================
            if self.TranscriptlineEdit.text()== '':
                self.TranscriptErrortextRNA.show()
                self.TranscriptErrortextRNA.setText("Input Transcript file!")
                self.RNAtabWidget.setCurrentIndex(0)
                self.RNAtabWidget.setTabEnabled(1, False)
            elif not os.path.exists(self.TranscriptlineEdit.text()):
                self.TranscriptErrortextRNA.show()
                self.TranscriptErrortextRNA.setText("File doesn't exist! Check the path!")
                self.RNAtabWidget.setCurrentIndex(0)
                self.RNAtabWidget.setTabEnabled(1, False)
            elif os.path.splitext(self.TranscriptlineEdit.text())[-1] != ".fa":
                self.TranscriptErrortextRNA.show()
                self.TranscriptErrortextRNA.setText("File should have extension '.fa'")
                self.RNAtabWidget.setCurrentIndex(0)
                self.RNAtabWidget.setTabEnabled(1, False)
            elif (os.path.splitext(self.FastalineEdit.text())[-1] == ".fa" and not os.path.exists('name_check.txt') and os.path.splitext(self.AnnotatedlineEditRNA.text())[-1] == ".gtf" and os.path.splitext(self.TranscriptlineEdit.text())[-1] == ".fa"):
#                print("ok")
                self.FastaErrortextRNA.hide()
                self.SampleFolderErrortextRNA.hide()
                self.AnnotatedErrortextRNA.hide()
                self.TranscriptErrortextRNA.hide()
                self.RNAtabWidget.setCurrentIndex(1)
                self.RNAtabWidget.setTabEnabled(1, True)
                self.textBrowser.setTextColor(self._colors['blue'])
                self.textBrowser.append("Click on the 'View FastQC Results' button below to view the FastQC report \n")
# =============================================================================
#             else:
#                 self.RNAtabWidget.setCurrentIndex(1)
#                 self.RNAtabWidget.setTabEnabled(1, True)
# =============================================================================
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
# =============================================================================
#             else :
#                 inputfile = fileinput.input("check_for_correct_filename_rna.py", inplace = 1)
#                 for l in inputfile:
#                     if "test_dir =" in l:
#                         print(l.replace(l, "test_dir = '"+self.SampleFolderLineEdit.text()+"'"))
#                     else:
#                         print(l.rstrip())
#                 inputfile.close()
#                 subprocess.run(["python", "check_for_correct_filename_rna.py"])
#                 if os.path.exists('name_check.txt'):
#                     self.RNAtabWidget.setCurrentIndex(0)
#                     self.RNAtabWidget.setTabEnabled(1, False)
#                     with open('name_check.txt') as errorcheck:
#                         content = errorcheck.readline()
#                     self.SampleFolderErrortextRNA.show()
#                     self.SampleFolderErrortextRNA.setText(content.rstrip())
# =============================================================================
# =============================================================================
#                 else:
#                     self.RNAtabWidget.setCurrentIndex(1)
#                     self.RNAtabWidget.setTabEnabled(1, True)
# =============================================================================
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
# =============================================================================
#                 self.RNAtabWidget.setCurrentIndex(1)
#                 self.RNAtabWidget.setTabEnabled(1, True)
# =============================================================================
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
# =============================================================================
#             else:
#                 self.RNAtabWidget.setCurrentIndex(1)
#                 self.RNAtabWidget.setTabEnabled(1, True)
# =============================================================================
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
# =============================================================================
#             else:
#                 self.RNAtabWidget.setCurrentIndex(1)
#                 self.RNAtabWidget.setTabEnabled(1, True)
# =============================================================================
            if self.TranscriptlineEdit.text()== '':
                self.TranscriptErrortextRNA.show()
                self.TranscriptErrortextRNA.setText("Input Transcript file!")
                self.RNAtabWidget.setCurrentIndex(0)
                self.RNAtabWidget.setTabEnabled(1, False)
            elif not os.path.exists(self.TranscriptlineEdit.text()):
                self.TranscriptErrortextRNA.show()
                self.TranscriptErrortextRNA.setText("File doesn't exist! Check the path!")
                self.RNAtabWidget.setCurrentIndex(0)
                self.RNAtabWidget.setTabEnabled(1, False)
            elif os.path.splitext(self.TranscriptlineEdit.text())[-1] != ".fa":
                self.TranscriptErrortextRNA.show()
                self.TranscriptErrortextRNA.setText("File should have extension '.fa'")
                self.RNAtabWidget.setCurrentIndex(0)
                self.RNAtabWidget.setTabEnabled(1, False)
            elif (os.path.splitext(self.FastalineEdit.text())[-1] == ".fa" and list(unitsdf) == list_tsv_col  and not os.path.exists('name_check.txt') and not os.path.exists('rename_check.txt') and os.path.splitext(self.AnnotatedlineEditRNA.text())[-1] == ".gtf" and os.path.splitext(self.TranscriptlineEdit.text())[-1] == ".fa"):
#                print("ok")
                self.FastaErrortextRNA.hide()
                self.SampleFolderErrortextRNA.hide()
                self.SampletableErrortextRNA.hide()
                self.AnnotatedErrortextRNA.hide()
                self.TranscriptErrortextRNA.hide()
                self.RNAtabWidget.setCurrentIndex(1)
                self.RNAtabWidget.setTabEnabled(1, True)
                self.textBrowser.setTextColor(self._colors['blue'])
                self.textBrowser.append("Click on the 'View FastQC Results' button below to view the FastQC report \n")
# =============================================================================
#             if self.SampleFolderLineEdit.text() == '':
#                 self.RNAtabWidget.setCurrentIndex(0)
#                 self.RNAtabWidget.setTabEnabled(1, False)
#                 self.SampleFolderErrortextRNA.setText("Input Samples folder path!")
#             elif not os.path.exists(self.SampleFolderLineEdit.text()):
#                 self.SampleFolderErrortextRNA.setText("File doesn't exist! Check the path!")
#                 self.RNAtabWidget.setCurrentIndex(0)
#                 self.RNAtabWidget.setTabEnabled(1, False)
#             else :
#                 inputfile = fileinput.input("check_for_correct_filename_rna.py", inplace = 1)
#                 for l in inputfile:
#                     if "test_dir =" in l:
#                         print(l.replace(l, "test_dir = '"+self.SampleFolderLineEdit.text()+"'"))
#                     else:
#                         print(l.rstrip())
#                 inputfile.close()
#                 subprocess.run(["python", "check_for_correct_filename_rna.py"])
#                 if os.path.exists('name_check.txt'):
#                     with open('name_check.txt') as errorcheck:
#                         self.SampleFolderErrortextRNA.setText(errorcheck.readline())
#                 else:
#                     self.RNAtabWidget.setCurrentIndex(1)
#                     self.RNAtabWidget.setTabEnabled(1, True)
#             if self.SampletablelineEdit.text() == '':
#                 self.SampletableErrortextRNA.setText("Input Sample Table!")
#                 self.RNAtabWidget.setCurrentIndex(0)
#                 self.RNAtabWidget.setTabEnabled(1, False)
#             elif not os.path.exists(self.SampletablelineEdit.text()):
#                 self.SampletableErrortextRNA.setText("File doesn't exist! Check the path!")
#                 self.RNAtabWidget.setCurrentIndex(0)
#                 self.RNAtabWidget.setTabEnabled(1, False)
#             elif os.path.splitext(self.SampletablelineEdit.text())[-1] != ".tsv":
#                 self.SampletableErrortextRNA.setText("File should have extension '.tsv'")
#                 self.RNAtabWidget.setCurrentIndex(0)
#                 self.RNAtabWidget.setTabEnabled(1, False)
#             else:
#                 subprocess.run(["python", "rename.py"])
#                 self.RNAtabWidget.setCurrentIndex(1)
#                 self.RNAtabWidget.setTabEnabled(1, True)
#             if self.FastalineEdit.text() == '':
#                 self.FastaErrortextRNA.setText("Input Fasta file!")
#                 self.RNAtabWidget.setCurrentIndex(0)
#                 self.RNAtabWidget.setTabEnabled(1, False)
#             elif not os.path.exists(self.FastalineEdit.text()):
#                 self.FastaErrortextRNA.setText("File doesn't exist! Check the path!")
#                 self.RNAtabWidget.setCurrentIndex(0)
#                 self.RNAtabWidget.setTabEnabled(1, False)
#             elif os.path.splitext(self.FastalineEdit.text())[-1] != ".fa":
#                 self.FastaErrortextRNA.setText("File should have extension '.fa'")
#                 self.RNAtabWidget.setCurrentIndex(0)
#                 self.RNAtabWidget.setTabEnabled(1, False)
#             else:
#                 self.RNAtabWidget.setCurrentIndex(1)
#                 self.RNAtabWidget.setTabEnabled(1, True)
#             if self.AnnotatedlineEditRNA.text()== '':
#                 self.AnnotatedErrortextRNA.setText("Input Annotated file!")
#                 self.RNAtabWidget.setCurrentIndex(0)
#                 self.RNAtabWidget.setTabEnabled(1, False)
#             elif not os.path.exists(self.AnnotatedlineEditRNA.text()):
#                 self.AnnotatedErrortextRNA.setText("File doesn't exist! Check the path!")
#                 self.RNAtabWidget.setCurrentIndex(0)
#                 self.RNAtabWidget.setTabEnabled(1, False)
#             elif os.path.splitext(self.AnnotatedlineEditRNA.text())[-1] != ".gtf":
#                 self.AnnotatedErrortextRNA.setText("File should have extension '.gtf'")
#                 self.RNAtabWidget.setCurrentIndex(0)
#                 self.RNAtabWidget.setTabEnabled(1, False)
#             else:
#                 self.RNAtabWidget.setCurrentIndex(1)
#                 self.RNAtabWidget.setTabEnabled(1, True)
#             if self.TranscriptlineEdit.text()== '':
#                 self.TranscriptErrortextRNA.setText("Input Transcript file!")
#                 self.RNAtabWidget.setCurrentIndex(0)
#                 self.RNAtabWidget.setTabEnabled(1, False)
#             elif not os.path.exists(self.TranscriptlineEdit.text()):
#                 self.TranscriptErrortextRNA.setText("File doesn't exist! Check the path!")
#                 self.RNAtabWidget.setCurrentIndex(0)
#                 self.RNAtabWidget.setTabEnabled(1, False)
#             elif os.path.splitext(self.TranscriptlineEdit.text())[-1] != ".fa":
#                 self.TranscriptErrortextRNA.setText("File should have extension '.fa'")
#                 self.RNAtabWidget.setCurrentIndex(0)
#                 self.RNAtabWidget.setTabEnabled(1, False)
#             else:
#                 self.RNAtabWidget.setCurrentIndex(1)
#                 self.RNAtabWidget.setTabEnabled(1, True) 
# =============================================================================
        
    def on_clicked_nextbuttonqcRNA(self):
        self.param_display_rna()
        if os.path.exists("results/fastqc"):
#            print("yes")
            self.RNAtabWidget.setCurrentIndex(2)
            self.RNAtabWidget.setTabEnabled(2, True)
        else:
#            print("no")
            self.qc_warning = showQCDialog()
#            if self.qc_warning.initUI== QMessageBox.Yes:
            if self.qc_warning.returnValue==QMessageBox.Yes:
                self.RNAtabWidget.setCurrentIndex(2)
                self.RNAtabWidget.setTabEnabled(2, True)
#                print('Yes clicked')
                                         
            if self.qc_warning.returnValue== QMessageBox.Cancel:
#                print('not')
                self.RNAtabWidget.setCurrentIndex(1)
                self.RNAtabWidget.setTabEnabled(2, False)
                
        self.RNAtabWidget.setTabEnabled(2, True)
    def on_clicked_nextbuttontoolRNA(self):
#        _translate = QtCore.QCoreApplication.translate
        self.index_warning_rna()
        self.create_snakefile_rna()
        self.create_config_rna()
        self.textBrowser.setTextColor(self._colors['blue'])
        self.textBrowser.append("Click on the 'Run' button below to start your analysis \n")
        
#        self.on_clicked_nextbuttonparamsRNA()
        self.RNAtabWidget.setCurrentIndex(3)
#        self.Index_rna.setEnabled(True)
        self.RNAtabWidget.setTabEnabled(3, True)
#        self.StarIndexlabel.setText(_translate("MainWindow", "kjhjg"))
        
    def param_display_rna(self):
        _translate = QtCore.QCoreApplication.translate
        self.StarIndexlabel.setText(_translate("MainWindow", "Index for " + self.AlignercomboBoxRNA.currentText()))
        self.StarIndexlineEdit.setToolTip(_translate("MainWindow", "Input the path of the Index for" + self.AlignercomboBoxRNA.currentText()))
        path_aligner_rna = './params/'+self.AlignercomboBoxRNA.currentText()+'.csv'
        path_em = './params/'+self.EMcomboBoxRNA.currentText()+'.csv'
        path_de = './params/'+self.DEcomboBoxRNA.currentText()+'.csv'
# =============================================================================
#         self.AlignerParamlabelrna.setText(_translate("MainWindow", self.AlignercomboBoxRNA.currentText()))
#         self.EMParamlabelrna.setText(_translate("MainWindow", self.EMcomboBoxRNA.currentText()))
#         self.DEParamlabelrna.setText(_translate("MainWindow", self.DEcomboBoxRNA.currentText()))
# =============================================================================
        dataframe = pd.read_csv(path_aligner_rna, header=0) # specifying that the table has column names
        essential = dataframe[dataframe["Essential"] == "yes"]
#        print(essential.iloc[1, 2])
        
        number_of_essential = len(essential) # returns number of essential parameters
#        print(number_of_essential)
        label_array_param1 = [self.param1_label_rna_1, self.param1_label_rna_2, self.param1_label_rna_3, self.param1_label_rna_4, self.param1_label_rna_5, self.param1_label_rna_6]
        line_edit_array_param1 = [self.param1_lineEdit_rna_1,self.param1_lineEdit_rna_2, self.param1_lineEdit_rna_3, self.param1_lineEdit_rna_4, self.param1_lineEdit_rna_5, self.param1_lineEdit_rna_6]
        for i, j, k in zip(range(number_of_essential), label_array_param1, line_edit_array_param1): 
            j.show()
            j.setText(essential.iloc[i, 2])
            k.show()
            k.setText(str(essential.iloc[i, 4]))
            
        dataframe_em = pd.read_csv(path_em, header=0) # specifying that the table has column names
        essential_em = dataframe_em[dataframe_em["Essential"] == "yes"]
#        print(essential.iloc[1, 2])
        
        number_of_essential_em = len(essential_em) # returns number of essential parameters
#        print(number_of_essential)
        label_array_param2 = [self.param2_label_rna_1, self.param2_label_rna_2, self.param2_label_rna_3, self.param2_label_rna_4, self.param2_label_rna_5, self.param2_label_rna_6]
        line_edit_array_param2 = [self.param2_lineEdit_rna_1,self.param2_lineEdit_rna_2, self.param2_lineEdit_rna_3, self.param2_lineEdit_rna_4, self.param2_lineEdit_rna_5, self.param2_lineEdit_rna_6]
        for i, j, k in zip(range(number_of_essential_em), label_array_param2, line_edit_array_param2): 
            j.show()
            j.setText(essential_em.iloc[i, 2])
            k.show()
            k.setText(str(essential_em.iloc[i, 4]))
            
        dataframe_de = pd.read_csv(path_de, header=0) # specifying that the table has column names
        essential_de = dataframe_de[dataframe_de["Essential"] == "yes"]
#        print(essential.iloc[1, 2])
        
        number_of_essential_de = len(essential_de) # returns number of essential parameters
#        print(number_of_essential)
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
# =============================================================================
#         elif os.path.exists(self.StarIndexlineEdit.text()):
#             if os.path.splitext(self.StarIndexlineEdit.text())[-1] != ".fa":
#                 self.StarIndexErrortext.setText("File should have extension '.fa'")
# =============================================================================
        else:
            self.RNAtabWidget.setCurrentIndex(4)
            self.RNAtabWidget.setTabEnabled(4, True)
# =============================================================================
#         self.RNAtabWidget.setCurrentIndex(4)
# #        self.Params_rna.setEnabled(True)
#         self.RNAtabWidget.setTabEnabled(4, True)
# =============================================================================
    def on_clicked_nextbuttonparamsRNA(self):
#        self.RNAtabWidget.setCurrentIndex(5)
# =============================================================================
#         self.RunButton.setEnabled(True)
#         self.RunLabel.setEnabled(True)
# #        self.Create_rna.setEnabled(True)
#         self.RunButtonErroricon.hide()
#         self._set_color(self._colors['blue'].name(), pb = self.progressBar)
# =============================================================================
#        self.RNAtabWidget.setTabEnabled(5, True)
# =============================================================================
#         self.create_snakefile_rna()
#         self.create_config_rna()
#         self.textBrowser.setTextColor(self._colors['blue'])
#         self.textBrowser.append("Click on the 'Run' button below to start your analysis \n")
# =============================================================================
        
        self.essential_dict_aligner_rna = self.get_essential(path ='./params/'+self.AlignercomboBoxRNA.currentText()+'.csv', essential_line_edit_array= [self.param1_lineEdit_rna_1,self.param1_lineEdit_rna_2, self.param1_lineEdit_rna_3, self.param1_lineEdit_rna_4, self.param1_lineEdit_rna_5, self.param1_lineEdit_rna_6] )
        with open('aligner_params_rna.txt', 'w') as aligner_params_rna:
            aligner_params_rna.write(self.AlignercomboBoxRNA.currentText() + " : '")
            for k, v in self.essential_dict_aligner_rna.items():
                aligner_params_rna.write(k +''+ str(v) + " ")
            aligner_params_rna.write("'")
            aligner_params_rna.close()
        self.essential_dict_em = self.get_essential(path ='./params/'+self.EMcomboBoxRNA.currentText()+'.csv', essential_line_edit_array =[self.param2_lineEdit_rna_1,self.param2_lineEdit_rna_2, self.param2_lineEdit_rna_3, self.param2_lineEdit_rna_4, self.param2_lineEdit_rna_5, self.param2_lineEdit_rna_6])
        with open('em_params.txt', 'w') as em_params:
            em_params.write(self.EMcomboBoxRNA.currentText() + " : '")
            for k, v in self.essential_dict_em.items():
                em_params.write(k +''+ str(v) + " ")
            em_params.write("'")
            em_params.close()
        self.essential_dict_de = self.get_essential(path ='./params/'+self.DEcomboBoxRNA.currentText()+'.csv', essential_line_edit_array=[self.param3_lineEdit_rna_1,self.param3_lineEdit_rna_2, self.param3_lineEdit_rna_3, self.param3_lineEdit_rna_4, self.param3_lineEdit_rna_5, self.param3_lineEdit_rna_6] )
        with open('de_params.txt', 'w') as de_params:
            de_params.write(self.DEcomboBoxRNA.currentText() + " : '")
            for k, v in self.essential_dict_de.items():
                de_params.write(k +''+ str(v) + " ")
            de_params.write("'")
            de_params.close()
    def on_clicked_previousbuttonqcRNA(self):
        self.RNAtabWidget.setCurrentIndex(0)
#        self.input_rna.setEnabled(True)
        self.RNAtabWidget.setTabEnabled(6, True)
    def on_clicked_previousbuttontoolRNA(self):
        self.RNAtabWidget.setCurrentIndex(1)
#        self.QC_rna.setEnabled(True)
        self.RNAtabWidget.setTabEnabled(1, True)
    def on_clicked_previousbuttonindexRNA(self):
        self.RNAtabWidget.setCurrentIndex(2)
#        self.Tool_rna.setEnabled(True)
        self.RNAtabWidget.setTabEnabled(2, True)
    def on_clicked_previousbuttonparamsRNA(self):
        self.RNAtabWidget.setCurrentIndex(3)
#        self.Index_rna.setEnabled(True)
        self.RNAtabWidget.setTabEnabled(3, True)
        
    def on_clicked_previousbuttonrunRNA(self):
        self.RNAtabWidget.setCurrentIndex(2)       
        self.RNAtabWidget.setTabEnabled(2, True)
    
    def on_clicked_previousbuttonresultRNA(self):
        self.RNAtabWidget.setCurrentIndex(3)       
        self.RNAtabWidget.setTabEnabled(3, True)
    
    def on_clicked_ResultsButton(self):
        self.ResultsButton.setEnabled(False)
        subprocess.run(["snakemake", "--unlock"])
# =============================================================================
#         with open("Snakefile", "r+") as snake:
#             line= snake.readline()
#             if '"rules/common_dna.smk"' in line:
#                 path = "./results_dna"
#             else:
#                 path = "./results"
#         self.results_widget = ResultsDialog(path)
#         self.results_widget.show()
# =============================================================================
# =============================================================================
#             lines = snake.readlines()
#             if 'include: "rules/common_dna.smk"' in lines:
#                 path = "/data/Priyanka/other_pipelines/iCOMIC/results_dna"
#             else:
#                 path = "/data/Priyanka/other_pipelines/iCOMIC/results"
#             
#         print(path)
# =============================================================================
# =============================================================================
#         self.results_widget = ResultsDialog(results_path)
#         self.results_widget.show()
# =============================================================================
        
#        subprocess.Popen( "./results_dna")
#        os.start('/data/Priyanka/other_pipelines/iCOMIC/results')
#        subprocess.Popen(['xdg-open', '/data/Priyanka/other_pipelines/iCOMIC/results'])
#        subprocess.Popen(["open", "./results_dna"])
#        os.system('explorer.exe "/data/Priyanka/other_pipelines/iCOMIC/"')
#==============================================================================
#         data_path=QtWidgets.QFileDialog.getOpenFileName(self,'Open File',"/data/Priyanka/other_pipelines/iCOMIC/",)
#         with open('data_path.pickle', 'wb') as handle:
#             _pickle.dump(data_path,handle,protocol=_pickle.HIGHEST_PROTOCOL)
#==============================================================================
        
    def show_dag(self):
        with open("Snakefile", "r+") as snake:
            line= snake.readline()
            if '"rules/common_dna.smk"' in line:
                svg_filename = self.AlignercomboBoxDNA.currentText() + self.VCcomboBoxDNA.currentText() + self.AnnotatorcomboBoxDNA.currentText() + ".svg"
            else:
                svg_filename = self.AlignercomboBoxRNA.currentText() + self.EMcomboBoxRNA.currentText() + self.DEcomboBoxRNA.currentText() + ".svg"
#        self.textBrowser.insertPlainText("Please find your DAG in your working Directory... \n\n")
        if os.path.exists(svg_filename):
            self.diag = SVGDialog(svg_filename)
            self.diag.show()
        else:
            self.textBrowser.setTextColor(self._colors['red'])
            self.textBrowser.append("Error creating DAG!")
        
    

#==============================================================================
#     def BP_one(self):
#          self.one_passed = True
#          self.check_run_button()
#     # #
#     def BP_two(self):
#          self.two_passed = True
#          self.check_run_button()
#==============================================================================
    
                
    def advanced_aligner(self):
        path = './params/'+self.AlignercomboBoxDNA.currentText()+'.csv'
        self.adv_dialog = AdvancedDialog(path)
        self.adv_dialog.show()
        retval = self.adv_dialog.exec_
        self.adv_dialog.button.accepted.connect(self.close_and_write_aligner)
        
        
        
    def close_and_write_aligner(self):
# =============================================================================
#         path = '/data/Priyanka/other_pipelines/iCOMIC/'+self.AlignercomboBoxDNA.currentText()+'.csv'
#         dataframe = pd.read_csv(path, header =0)
#         additional = dataframe[dataframe["Essential"] == "no"]
#         new_values = [j.text() for j in self.adv_dialog.line_edit_list]
#         additional['New Value'] = new_values
#         additional['New Value'] = additional['New Value'].astype('float64')
#         additional = additional.reset_index()
#         essential_line_edit_array = [self.param1_lineEdit_dna_1,self.param1_lineEdit_dna_2, self.param1_lineEdit_dna_3, self.param1_lineEdit_dna_4, self.param1_lineEdit_dna_5, self.param1_lineEdit_dna_6]
#         self.essential = dataframe[dataframe["Essential"] == "yes"]
#         self.new_essential = [essential_line_edit_array[i].text() for i in range(len(self.essential))]
#         
#         self.essential['New_value'] = self.new_essential
#         self.essential['New_value'] = self.essential['New_value'].astype('float64')
#         self.essential = self.essential.reset_index()
#         
#         snakefile_dict = dict()
#         for row in additional.itertuples():
#             if row[6] != row[8]:
#                 snakefile_dict[row[2]] = row[8]
#         self.essential_dict = dict()
#         for row in self.essential.itertuples():
#             if row[6] != row[8]:
#                 self.essential_dict[row[2]] = row[8]
# =============================================================================
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
# =============================================================================
#         path = '/data/Priyanka/other_pipelines/iCOMIC/'+self.VCcomboBoxDNA.currentText()+'.csv'
#         dataframe = pd.read_csv(path, header =0)
#         additional = dataframe[dataframe["Essential"] == "no"]
#         new_values = [j.text() for j in self.adv_dialog.line_edit_list]
#         additional['New Value'] = new_values
#         additional['New Value'] = additional['New Value'].astype('float64')
#         additional = additional.reset_index()
#         essential_line_edit_array = [self.param2_lineEdit_dna_1,self.param2_lineEdit_dna_2, self.param2_lineEdit_dna_3, self.param2_lineEdit_dna_4, self.param2_lineEdit_dna_5, self.param2_lineEdit_dna_6]
#         essential = dataframe[dataframe["Essential"] == "yes"]
#         new_essential = [essential_line_edit_array[i].text() for i in range(len(essential))]
#         
#         essential['New_value'] = new_essential
#         essential['New_value'] = essential['New_value'].astype('float64')
#         essential = essential.reset_index()
#         
#         snakefile_dict_vc = dict()
#         for row in additional.itertuples():
#             if row[6] != row[8]:
#                 snakefile_dict_vc[row[2]] = row[8]
#         essential_dict_vc = dict()
#         for row in essential.itertuples():
#             if row[6] != row[8]:
#                 essential_dict_vc[row[2]] = row[8]
# =============================================================================
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
# =============================================================================
#         path = '/data/Priyanka/other_pipelines/iCOMIC/'+self.AnnotatorcomboBoxDNA.currentText()+'.csv'
#         dataframe = pd.read_csv(path, header =0)
#         additional = dataframe[dataframe["Essential"] == "no"]
#         new_values = [j.text() for j in self.adv_dialog.line_edit_list]
#         additional['New Value'] = new_values
#         additional['New Value'] = additional['New Value'].astype('float64')
#         additional = additional.reset_index()
#         essential_line_edit_array = [self.param3_lineEdit_dna_1,self.param3_lineEdit_dna_2, self.param3_lineEdit_dna_3, self.param3_lineEdit_dna_4, self.param3_lineEdit_dna_5, self.param3_lineEdit_dna_6]
#         essential = dataframe[dataframe["Essential"] == "yes"]
#         new_essential = [essential_line_edit_array[i].text() for i in range(len(essential))]
#         
#         essential['New_value'] = new_essential
#         essential['New_value'] = essential['New_value'].astype('float64')
#         essential = essential.reset_index()
#         
#         snakefile_dict_annotator = dict()
#         for row in additional.itertuples():
#             if row[6] != row[8]:
#                 snakefile_dict_annotator[row[2]] = row[8]
#         essential_dict_annotator = dict()
#         for row in essential.itertuples():
#             if row[6] != row[8]:
#                 essential_dict_annotator[row[2]] = row[8]
# =============================================================================
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
# =============================================================================
#         path = '/data/Priyanka/other_pipelines/iCOMIC/'+self.AlignercomboBoxRNA.currentText()+'.csv'
#         dataframe = pd.read_csv(path, header =0)
#         additional = dataframe[dataframe["Essential"] == "no"]
#         new_values = [j.text() for j in self.adv_dialog.line_edit_list]
#         additional['New Value'] = new_values
#         additional['New Value'] = additional['New Value'].astype('float64')
#         additional = additional.reset_index()
#         essential_line_edit_array = [self.param1_lineEdit_rna_1,self.param1_lineEdit_rna_2, self.param1_lineEdit_rna_3, self.param1_lineEdit_rna_4, self.param1_lineEdit_rna_5, self.param1_lineEdit_rna_6]
#         essential = dataframe[dataframe["Essential"] == "yes"]
#         new_essential = [essential_line_edit_array[i].text() for i in range(len(essential))]
#         
#         essential['New_value'] = new_essential
#         essential['New_value'] = essential['New_value'].astype('float64')
#         essential = essential.reset_index()
#         
#         snakefile_dict_aligner_rna = dict()
#         for row in additional.itertuples():
#             if row[6] != row[8]:
#                 snakefile_dict_aligner_rna[row[2]] = row[8]
#         essential_dict_aligner_rna = dict()
#         for row in essential.itertuples():
#             if row[6] != row[8]:
#                 essential_dict_aligner_rna[row[2]] = row[8]
# =============================================================================
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
        
#==============================================================================
#         with open('aligner_params_rna.txt', 'w') as aligner_params_rna:
#             aligner_params_rna.write(self.AlignercomboBoxRNA.currentText() + " : '")
#             for k, v in self.snakefile_dict_aligner_rna.items():
#                 aligner_params_rna.write( k +''+ str(v) +" " )
#             for k, v in self.essential_dict_aligner_rna.items():
#                 aligner_params_rna.write(k +''+ str(v) + " ")
#             aligner_params_rna.write("'")
#             aligner_params_rna.close()
#==============================================================================
            
        self.adv_dialog.close()
        
    def advanced_em(self):
        path = './params/'+self.EMcomboBoxRNA.currentText()+'.csv'
        self.adv_dialog = AdvancedDialog(path)
        self.adv_dialog.show()
        retval = self.adv_dialog.exec_
        self.adv_dialog.button.accepted.connect(self.close_and_write_em)
        
    def close_and_write_em(self):
# =============================================================================
#         path = '/data/Priyanka/other_pipelines/iCOMIC/'+self.EMcomboBoxRNA.currentText()+'.csv'
#         dataframe = pd.read_csv(path, header =0)
#         additional = dataframe[dataframe["Essential"] == "no"]
#         new_values = [j.text() for j in self.adv_dialog.line_edit_list]
#         additional['New Value'] = new_values
#         additional['New Value'] = additional['New Value'].astype('float64')
#         additional = additional.reset_index()
#         essential_line_edit_array = [self.param2_lineEdit_rna_1,self.param2_lineEdit_rna_2, self.param2_lineEdit_rna_3, self.param2_lineEdit_rna_4, self.param2_lineEdit_rna_5, self.param2_lineEdit_rna_6]
#         essential = dataframe[dataframe["Essential"] == "yes"]
#         new_essential = [essential_line_edit_array[i].text() for i in range(len(essential))]
#         
#         essential['New_value'] = new_essential
#         essential['New_value'] = essential['New_value'].astype('float64')
#         essential = essential.reset_index()
#         
#         snakefile_dict_em = dict()
#         for row in additional.itertuples():
#             if row[6] != row[8]:
#                 snakefile_dict_em[row[2]] = row[8]
#         essential_dict_em = dict()
#         for row in essential.itertuples():
#             if row[6] != row[8]:
#                 essential_dict_em[row[2]] = row[8]
# =============================================================================
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
# =============================================================================
#         path = '/data/Priyanka/other_pipelines/iCOMIC/'+self.DEcomboBoxRNA.currentText()+'.csv'
#         dataframe = pd.read_csv(path, header =0)
#         additional = dataframe[dataframe["Essential"] == "no"]
#         new_values = [j.text() for j in self.adv_dialog.line_edit_list]
#         additional['New Value'] = new_values
#         additional['New Value'] = additional['New Value'].astype('float64')
#         additional = additional.reset_index()
#         essential_line_edit_array = [self.param3_lineEdit_rna_1,self.param3_lineEdit_rna_2, self.param3_lineEdit_rna_3, self.param3_lineEdit_rna_4, self.param3_lineEdit_rna_5, self.param3_lineEdit_rna_6]
#         essential = dataframe[dataframe["Essential"] == "yes"]
#         new_essential = [essential_line_edit_array[i].text() for i in range(len(essential))]
#         
#         essential['New_value'] = new_essential
#         essential['New_value'] = essential['New_value'].astype('float64')
#         essential = essential.reset_index()
#         
#         snakefile_dict_de = dict()
#         for row in additional.itertuples():
#             if row[6] != row[8]:
#                 snakefile_dict_de[row[2]] = row[8]
#         essential_dict_de = dict()
#         for row in essential.itertuples():
#             if row[6] != row[8]:
#                 essential_dict_de[row[2]] = row[8]
# =============================================================================
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
            
    def check_dag_and_results_button(self):
#        if self.progressBar.value() == 100:
        self.DAGButton.setEnabled(True)
        self.ResultsButton.setEnabled(True)
        self.DAGLabel.setEnabled(True)
        self.ResultsLabel.setEnabled(True)
    
# =============================================================================
#     def on_check_SamplesYes_dna(self,is_toggle):
#         if is_toggle:
#             self.SampleFilelabelDNA.setEnabled(True)
#             self.SampleslineEditDNA.setEnabled(True)
#             self.SamplesBrowseButtonDNA.setEnabled(True)
#         else:
#             self.UnitsFilelabelDNA.setEnabled(False)
#             self.UnitslineEditDNA.setEnabled(False)
#             self.UnitsBrowseButtonDNA.setEnabled(False)
# =============================================================================
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
#            self.QClineEdit.setEnabled(True)
            self.InputParamslabel.setEnabled(True)
            self.Cutadaptlabel.setEnabled(True)
            self.CutadaptlineEdit.setEnabled(True)
# =============================================================================
#             self.CreateSnakefilepushButton.setEnabled(True)
#             self.CreateConfigfilepushButton.setEnabled(True)
# =============================================================================
            self.RunQCpushButton.setEnabled(True)
        else:
#            self.QClineEdit.setEnabled(False)
            self.InputParamslabel.setEnabled(False)
            self.Cutadaptlabel.setEnabled(False)
            self.CutadaptlineEdit.setEnabled(False)
# =============================================================================
#             self.CreateSnakefilepushButton.setEnabled(False)
#             self.CreateConfigfilepushButton.setEnabled(False)
# =============================================================================
            self.RunQCpushButton.setEnabled(False)

    def on_check_QC_rna(self,is_toggle):
        if is_toggle:
#            self.QClineEdit_rna.setEnabled(True)
            self.InputParamslabel_rna.setEnabled(True)
            self.Cutadaptlabel_rna.setEnabled(True)            
            self.CutadaptlineEdit_rna.setEnabled(True)
# =============================================================================
#             self.CreateSnakefilepushButton_rna.setEnabled(True)
#             self.CreateConfigfilepushButton_rna.setEnabled(True)
# =============================================================================
            self.RunQCpushButton_rna.setEnabled(True)
        else:
#            self.QClineEdit_rna.setEnabled(False)
            self.InputParamslabel_rna.setEnabled(False)
            self.Cutadaptlabel_rna.setEnabled(False)
            self.CutadaptlineEdit_rna.setEnabled(False)
# =============================================================================
#             self.CreateSnakefilepushButton_rna.setEnabled(False)
#             self.CreateConfigfilepushButton_rna.setEnabled(False)
# =============================================================================
            self.RunQCpushButton_rna.setEnabled(False)

# =============================================================================
#     def on_changed_AlignerDNA(self, text):
#         _translate = QtCore.QCoreApplication.translate
#         self.BWAIndexlabel.setText(_translate("MainWindow", "Index for " + self.AlignercomboBoxDNA.currentText()))
#         self.BWAIndexlineEdit.setToolTip(_translate("MainWindow", "Input the path of the Index for" + self.AlignercomboBoxDNA.currentText()))
# 
#     def on_changed_VC(self, text):
#         _translate = QtCore.QCoreApplication.translate
#         self.Paramstool2labelDNA.setText(_translate("MainWindow", text))
# 
#     def on_changed_Annotator(self, text):
#         _translate = QtCore.QCoreApplication.translate
#         self.Paramstool3labelDNA.setText(_translate("MainWindow", text))
# 
# =============================================================================
# =============================================================================
#     def on_changed_AlignerRNA(self, text):
#         _translate = QtCore.QCoreApplication.translate
#         self.Paramstool1labelRNA.setText(_translate("MainWindow", text))
#         self.StarIndexlabel.setText(_translate("MainWindow", "Index for " + self.AlignercomboBoxRNA.currentText()))
#         self.StarIndexlineEdit.setToolTip(_translate("MainWindow", "Input the path of the Index for" + self.AlignercomboBoxRNA.currentText()))
# 
#     def on_changed_EM(self, text):
#         _translate = QtCore.QCoreApplication.translate
#         self.Paramstool2labelRNA.setText(_translate("MainWindow", text))
# 
#     def on_changed_DE(self, text):
#         _translate = QtCore.QCoreApplication.translate
#         self.Paramstool3labelRNA.setText(_translate("MainWindow", text))
# 
#     def mandatoryParams_AlignerDna(self):
#         params = open('params_dna.txt', 'r')
#         for line in params:
#             if self.AlignercomboBoxDNA.currentText() in line:
#                 mod_line = ' '.join(line.split()[1:])
#                 self.Mandatory1lineEditDNA.setText(mod_line)
# 
#     def mandatoryParams_VC(self):
#         params = open('params_dna.txt', 'r')
#         for line in params:
#             if self.VCcomboBoxDNA.currentText() in line:
#                 mod_line = ' '.join(line.split()[1:])
#                 self.Mandatory2lineEditDNA.setText(mod_line)
# 
#     def mandatoryParams_Annotator(self):
#         params = open('params_dna.txt', 'r')
#         for line in params:
#             if self.AnnotatorcomboBoxDNA.currentText() in line:
#                 mod_line = ' '.join(line.split()[1:])
#                 self.Mandatory3lineEditDNA.setText(mod_line)
# 
#     def mandatoryParams_AlignerRna(self):
#         params = open('params_rna.txt', 'r')
#         for line in params:
#             if self.AlignercomboBoxRNA.currentText() in line:
#                 mod_line = ' '.join(line.split()[1:])
#                 self.Mandatory1lineEditRNA.setText(mod_line)
# 
#     def mandatoryParams_EM(self):
#         params = open('params_rna.txt', 'r')
#         for line in params:
#             if self.EMcomboBoxRNA.currentText() in line:
#                 mod_line = ' '.join(line.split()[1:])
#                 self.Mandatory2lineEditRNA.setText(mod_line)
# 
#     def mandatoryParams_DE(self):
#         params = open('params_rna.txt', 'r')
#         for line in params:
#             if self.DEcomboBoxRNA.currentText() in line:
#                 mod_line = ' '.join(line.split()[1:])
#                 self.Mandatory3lineEditRNA.setText(mod_line)
# =============================================================================
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
        #print(data_path)
        self.AnnotatedlineEditRNA.setText(data_path_annotated)
        with open('data_path_annotated.pickle', 'wb') as handle:
            pickle.dump(data_path_annotated,handle,protocol=pickle.HIGHEST_PROTOCOL)

    def browse_data_transcript(self):
        self.TranscriptErrortextRNA.hide()
        data_path_transcipt, _ =QtWidgets.QFileDialog.getOpenFileName(None,'Open File',r"",'*.fa *.fa.gz')
        #print(data_path)
        self.TranscriptlineEdit.setText(data_path_transcipt)
        with open('data_path_transcript.pickle', 'wb') as handle:
            pickle.dump(data_path_transcipt,handle,protocol=pickle.HIGHEST_PROTOCOL)
            
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
# =============================================================================
#         self.SamplesErrortextDNA.hide()
#         data_path_samples, _ =QtWidgets.QFileDialog.getOpenFileName(None,'Open File',r"",'*.tsv')
#         self.SampleslineEditDNA.setText(data_path_samples)
#         with open('data_path_samples.pickle', 'wb') as handle:
#             pickle.dump(data_path_samples,handle,protocol=pickle.HIGHEST_PROTOCOL)
# =============================================================================
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

# =============================================================================
#     def toggle_samples(self):
#         self.SamplesErrortextDNA.hide()
#         
#     def toggle_units(self):
#         self.UnitsErroriconDNA.hide()
# =============================================================================
        
    def browse_data_ref(self):
# =============================================================================
#         if self.SampleslineEditDNA.text() == '':
#             self.SamplesErrortextDNA.setText("")
# =============================================================================
        self.RefGenomeErrortextDNA.hide()
        data_path_ref, _ =QtWidgets.QFileDialog.getOpenFileName(None,'Open File',r"",'*.fa *.fa.gz')
        self.RefGenomelineEditDNA.setText(data_path_ref)
        with open('data_path_ref.pickle', 'wb') as handle:
            pickle.dump(data_path_ref,handle,protocol=pickle.HIGHEST_PROTOCOL)

    def browse_data_kv(self):
        self.RefVariantErrortextDNA.hide()
        data_path_kv, _ =QtWidgets.QFileDialog.getOpenFileName(None,'Open File',r"",'*.gz')
        self.RefVariantlineEditDNA.setText(data_path_kv)
#        print("  name: " + self.RefNamelineEdit.text + "\n")
        with open('data_path_kv.pickle', 'wb') as handle:
            pickle.dump(data_path_kv,handle,protocol=pickle.HIGHEST_PROTOCOL)

    def browse_bwaindex_dna(self):
        self.BWAIndexErrortext.hide()
        self._set_color(self._colors['blue'].name(),pb =self.progressBar_sub2_dna)
#        self._set_color(self._colors['blue'].name(),pb =self.progressBar)
        data_path_bwadna, _ =QtWidgets.QFileDialog.getOpenFileName(None,'Open File')
#        data_path_bwadna, _ =QtWidgets.QFileDialog.getOpenFileName(None,'Open File',r"",'*.fa', '*.gem')
        self.BWAIndexlineEdit.setText(data_path_bwadna)
#        print("  name: " + self.RefNamelineEdit.text + "\n")
        with open('data_path_bwadna.pickle', 'wb') as handle:
            pickle.dump(data_path_bwadna,handle,protocol=pickle.HIGHEST_PROTOCOL)

#    def browse_bowtie_dna(self):
#        data_path_bowtiedna, _ =QtWidgets.QFileDialog.getOpenFileName(None,'Open File',r"")
#        self.Bowtie2dIndexlineEdit.setText(data_path_bowtiedna)
##        print("  name: " + self.RefNamelineEdit.text + "\n")
#        with open('data_path_bowtiedna.pickle', 'wb') as handle:
#            pickle.dump(data_path_bowtiedna,handle,protocol=pickle.HIGHEST_PROTOCOL)

    def browse_star_rna(self):
        self.StarIndexErrortext.hide()
        self._set_color(self._colors['blue'].name(),pb =self.progressBar_sub2_rna)
#        self._set_color(self._colors['blue'].name(),pb =self.progressBar)
        my_dir_star = QtWidgets.QFileDialog.getExistingDirectory(
        None,
        "Open a folder")
        self.StarIndexlineEdit.setText(my_dir_star)


#    def browse_hisat2_rna(self):
#        my_dir_hisat2 = QtWidgets.QFileDialog.getExistingDirectory(
#        None,
#        "Open a folder")
#        self.HISAT2IndexlineEdit.setText(my_dir_hisat2)
#
#    def browse_salmon_rna(self):
#        my_dir_salmon = QtWidgets.QFileDialog.getExistingDirectory(
#        None,
#        "Open a folder")
#        self.SalmonIndexlineEdit.setText(my_dir_salmon)
#
#    def browse_bowtie_rna(self):
#        my_dir_bowtie2 = QtWidgets.QFileDialog.getExistingDirectory(
#        None,
#        "Open a folder")
#        self.Bowtie2IndexlineEdit.setText(my_dir_bowtie2)

# =============================================================================
#     def browse_star_rna(self):
#         data_path_starrna, _ =QtWidgets.QFileDialog.getExistingDirectory(None, 'Select Directory')
#         self.StarIndexlineEdit.setText(data_path_starrna)
# #        print("  name: " + self.RefNamelineEdit.text + "\n")
#         with open('data_path_starrna.pickle', 'wb') as handle:
#             pickle.dump(data_path_starrna,handle,protocol=pickle.HIGHEST_PROTOCOL)
# =============================================================================


#    def config_qc_dna(self):
# =============================================================================
#         conf = open('config.yaml', 'w')
#         conf.write('samples: '+ self.SampleslineEditDNA.text() + '\n')
#         conf.write('units: '+ self.UnitslineEditDNA.text() + '\n'+'ref: \n')
#         conf.write("  name: " + self.RefNamelineEdit.text() + "\n")
#         conf.write('  genome: '+ self.RefGenomelineEditDNA.text() + '\n')
#         conf.write('  genome-name: '+ os.path.basename(self.RefGenomelineEditDNA.text()) + '\n')
#         conf.write('  known-variants: '+ self.RefVariantlineEditDNA.text() + '\n')
#         conf.write("processing: \n")
#         conf.write("  remove-duplicates: true\n")
# #        conf.write('index: \n')
# #        conf.write('  '+ self.AlignercomboBoxDNA.currentText() + ': ' + self.BWAIndexlineEdit.text() + '\n')
#         conf.write('params: \n')
#         conf.write("  fastqc: '" + self.QClineEdit.text() + "' \n")
#         conf.write("  cutadapt: '" + self.CutadaptlineEdit.text() + "' \n")
#         conf.close()
#         self.textBrowser.insertPlainText("Config file created for Quality Check!! \nPlease refer to the file: config.yaml in your working directory. \n\n")
# =============================================================================


#    def snakefile_qc_dna(self):
# =============================================================================
#         snake = open('Snakefile', "w")
#         snake.write('include: "rules/common_dna.smk"\n')
#         snake.write('rule all:\n')
#         snake.write('  input:\n')
#         snake.write('    expand("results_dna/qc/fastqc/{u.sample}-{u.unit}.html", u = units.itertuples()),\n')
#         snake.write('    expand("results_dna/qc/fastqc/{u.sample}-{u.unit}.zip", u = units.itertuples()),\n')
#         snake.write('    expand("results_dna/trimmed/{u.sample}-{u.unit}.fastq.gz", u = units.itertuples()),\n')
#         snake.write('    expand("results_dna/qc/fastqc/{u.sample}-{u.unit}.aftertrim.html", u = units.itertuples()),\n')
#         snake.write('    expand("results_dna/qc/fastqc/{u.sample}-{u.unit}.aftertrim.zip", u = units.itertuples()),\n')
#         snake.write('\ninclude: "rules/qc_dna.smk"\n')
#         snake.write('include: "rules/cutadapt_dna.smk"\n')
#         snake.write('include: "rules/fastqc_after_dna.smk"\n')
#         snake.close()
#         self.textBrowser.insertPlainText("Snakefile created for Quality Check!! \nPlease refer to the file: Snakefile in your working directory. \n\n")
# =============================================================================
        
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
# =============================================================================
#     def _set_pb_color(self, color, pb):
#         self._set_color(self, color, pb = self.progressBar)
# =============================================================================
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
#        print(filename_)
        f = open(filename_, 'r')
        while True:
            line = ''
            while len(line) == 0 or line[-1] != '\n':
                tail = f.readline()
                if tail == '':
                    break
#                    print('empty')
#                    time.sleep(0.1)          # avoid busy waiting
                    # f.seek(0, io.SEEK_CUR) # appears to be unneccessary
#                    pass
#                    continue
                line += tail
#                line.rstrip("\n")
                self.textBrowser.append(line)
#                self.textBrowser.insertPlainText(line)
#                print(line)
#                                self.textBrowser_PythonShellTab.insertPlainText(line)
                if '%' in line:
                    self.textBrowser.setTextColor(self._colors['black'])
                    per = line.split('(', 1)[1].split(')')[0]
                    percent = per[:-1]
                    sub_pb.setValue(initial_sub + int(percent)/sub_pb_frac)
#                    main_pb.setValue(initial_main + int(percent))
                elif 'Error: Directory cannot be locked' in line:
#                    print(line) 
                    self._set_color(self._colors['red'].name(),pb =sub_pb)
#                    self._set_color(self._colors['red'].name(), pb = main_pb)
                    self.textBrowser.setTextColor(self._colors['red'])
                    self.textBrowser.append(line)
                    break
                    subprocess.run(["snakemake", "--unlock"])
# =============================================================================
#                     self.ResultsButton.setEnabled(True)
#                     self.ResultsButtonErroricon.show()
#                     self.ResultsButtonErroricon.setToolTip("Directory locked! Click unlock and then run!")
# =============================================================================
                    
# =============================================================================
#                     self._set_color(self._colors['red'].name(),pb =sub_pb)
#                     self._set_color(self._colors['red'].name(), pb = self.progressBar)
#                     self.textBrowser.setTextColor(self._colors['red'])
# =============================================================================
                elif 'CalledProcessError' in line:
                    self._set_color(self._colors['red'].name(),pb =sub_pb)
#                    self._set_color(self._colors['red'].name(), pb = main_pb)
                    self.textBrowser.setTextColor(self._colors['red'])
# =============================================================================
#                     self._set_color(self._colors['red'].name(),pb =sub_pb)
#                     self._set_color(self._colors['red'].name(), pb = self.progressBar)
#                     self.textBrowser.setTextColor(self._colors['red'])
# =============================================================================
# =============================================================================
#                     error_icon.show()
#                     self.RunButton.setEnabled(False)
#                     self.RunLabel.setEnabled(False)
#                     error_icon.setToolTip("Error in parameters! Check the parameters click finish and then run")
# =============================================================================
                    break
                elif 'WorkflowError' in line:
                    self._set_color(self._colors['red'].name(),pb =sub_pb)
#                    self._set_color(self._colors['red'].name(), pb = main_pb)
                    self.textBrowser.setTextColor(self._colors['red'])
# =============================================================================
#                     error_icon.show()
#                     error_icon.setToolTip("Workflow error!")
# =============================================================================
                    break
                elif 'Error' in line:
                    self._set_color(self._colors['red'].name(),pb =sub_pb)
#                    self._set_color(self._colors['red'].name(), pb = main_pb)
                    self.textBrowser.setTextColor(self._colors['red'])
                    break
                elif 'Missing' in line:
                    print(line)
                    self._set_color(self._colors['red'].name(),pb =sub_pb)
#                    self._set_color(self._colors['red'].name(), pb = main_pb)
                    self.textBrowser.setTextColor(self._colors['red'])
                    error_icon.show()
                    error_icon.setToolTip("Missing input file! Check the inputs")
                    break
                elif '(100%) done' in line:
                    self.textBrowser.setTextColor(self._colors['black'])
                    sub_pb.setValue(initial_sub + 100/sub_pb_frac)
#                    main_pb.setValue(initial_main + 100)
#                    self.DAGButton.setEnabled(True)
# =============================================================================
#                             if os.path.exists("results_dna/qc/fastqc_after"):
#                                 for file in os.listdir("results_dna/qc/fastqc_after"):
#                                     if file.endswith(".html"):
#                                         filename = os.path.join("results_dna/qc/fastqc_after", file)
#                                         webbrowser.get('google-chrome').open(filename, new=0, autoraise=True)  # open in new tab
#                             else:
#                                 continue
# =============================================================================
                elif 'Nothing to be done' in line:
                    self.textBrowser.setTextColor(self._colors['black'])
                    sub_pb.setValue(initial_sub + 100/sub_pb_frac)
                    break
#                    main_pb.setValue(initial_main + 100)
#                    self.DAGButton.setEnabled(True)
                else:
                    pass
# =============================================================================
#                             if os.path.exists("results_dna/qc/fastqc_after"):
#                                 for file in os.listdir("results_dna/qc/fastqc_after"):
#                                     if file.endswith(".html"):
#                                         filename = os.path.join("results_dna/qc/fastqc_after", file)
#                                         webbrowser.get('google-chrome').open(filename, new=0, autoraise=True)  # open in new tab
#                             else:
#                                 continue
# =============================================================================
# =============================================================================
#             if line != "":
#                 self.textBrowser.insertPlainText(line)
#             else:
#                 break
# =============================================================================
            if ('Complete log' in line):
                break
            elif 'Missing' in line:
                self._set_color(self._colors['red'].name(),pb =sub_pb)
#                self._set_color(self._colors['red'].name(), pb = main_pb)
                break
            elif 'Exiting' in line:
                self._set_color(self._colors['red'].name(),pb =sub_pb)
#                self._set_color(self._colors['red'].name(), pb = main_pb)
                break
            
                
        
# =============================================================================
#     def func_pb_update(self, sub_pb, main_pb_frac, sub_pb_frac, initial_sub, initial_main, error_icon):
#         time.sleep(0.9)
#         files = glob.glob('.snakemake/log/*.log')
#         filename_=max(files , key = os.path.getctime)
#         print(filename_)
#         f = open(filename_, 'r')
#         while True:
#             line = ''
#             while len(line) == 0 or line[-1] != '\n':
#                 tail = f.readline()
#                 if tail == '':
#                     time.sleep(0.1)          # avoid busy waiting
#                     # f.seek(0, io.SEEK_CUR) # appears to be unneccessary
#                     continue
#                 line += tail
# #                self.textBrowser.append(line)
#                 self.textBrowser.insertPlainText(line)
# #                                self.textBrowser_PythonShellTab.insertPlainText(line)
#                 if '%' in line:
#                     self.textBrowser.setTextColor(self._colors['black'])
#                     per = line.split('(', 1)[1].split(')')[0]
#                     percent = per[:-1]
#                     sub_pb.setValue(initial_sub + int(percent)/sub_pb_frac)
#                     self.progressBar.setValue(initial_main + int(percent)/main_pb_frac)
#                 elif 'Error' in line:
#                     self._set_color(self._colors['red'].name(),pb =sub_pb)
#                     self._set_color(self._colors['red'].name(), pb = self.progressBar)
#                     self.textBrowser.setTextColor(self._colors['red'])
#                     break
#                 elif '(100%) done' in line:
#                     self.textBrowser.setTextColor(self._colors['black'])
#                     sub_pb.setValue(initial_sub + 100/sub_pb_frac)
#                     self.progressBar.setValue(initial_main + 100/main_pb_frac)
# #                    self.DAGButton.setEnabled(True)
# # =============================================================================
# #                             if os.path.exists("results_dna/qc/fastqc_after"):
# #                                 for file in os.listdir("results_dna/qc/fastqc_after"):
# #                                     if file.endswith(".html"):
# #                                         filename = os.path.join("results_dna/qc/fastqc_after", file)
# #                                         webbrowser.get('google-chrome').open(filename, new=0, autoraise=True)  # open in new tab
# #                             else:
# #                                 continue
# # =============================================================================
#                 elif 'MissingInputException' in line:
#                     self._set_color(self._colors['red'].name(),pb =sub_pb)
#                     self._set_color(self._colors['red'].name(), pb = self.progressBar)
#                     self.textBrowser.setTextColor(self._colors['red'])
#                     error_icon.show()
#                     error_icon.setToolTip("Missing input file! Check the inputs")
#                     break
#                 elif 'Error: Directory cannot be locked' in line:
#                     self._set_color(self._colors['red'].name(),pb =sub_pb)
#                     self._set_color(self._colors['red'].name(), pb = self.progressBar)
#                     self.ResultsButtonErroricon.show()
#                     self.ResultsButtonErroricon.setToolTip("Directory locked! Click unlock and then run!")
#                     self.textBrowser.setTextColor(self._colors['red'])
#                     break
#                 elif 'Nothing to be done' in line:
#                     self.textBrowser.setTextColor(self._colors['black'])
#                     sub_pb.setValue(initial_sub + 100/sub_pb_frac)
#                     self.progressBar.setValue(initial_main + 100/main_pb_frac)
# #                    self.DAGButton.setEnabled(True)
#                 else:
#                     pass
# # =============================================================================
# #                             if os.path.exists("results_dna/qc/fastqc_after"):
# #                                 for file in os.listdir("results_dna/qc/fastqc_after"):
# #                                     if file.endswith(".html"):
# #                                         filename = os.path.join("results_dna/qc/fastqc_after", file)
# #                                         webbrowser.get('google-chrome').open(filename, new=0, autoraise=True)  # open in new tab
# #                             else:
# #                                 continue
# # =============================================================================
#                 
#             if ('Complete log' in line):
#                 break 
# =============================================================================
    def show_qc_textbox(self):
        self.textBrowser.setTextColor(self._colors['black'])
        self.textBrowser.append("QC Results being generated. Please wait! \n")

    def show_qc_results(self):
#        self.spinner.start()
        self.progressBar_sub1_dna.setValue(1)
#        self.progressBar.setValue(1)
        self.textBrowser.setTextColor(self._colors['black'])
#        self.textBrowser.append("QC Results being generated. Please wait! \n")
        self.nextbuttonqcDNA.setEnabled(True)
        self._set_color(self._colors['blue'].name(),pb =self.progressBar_sub1_dna)
#        self._set_color(self._colors['blue'].name(),pb =self.progressBar)
        conf = open('config.yaml', 'w')
        conf.write('samples: samples.tsv \n')
        conf.write('units: '+ self.UnitslineEditDNA.text() + '\n'+'ref: \n')
        conf.write('  genome: '+ self.RefGenomelineEditDNA.text() + '\n')
        conf.write("processing: \n")
        conf.write("  remove-duplicates: true\n")
        conf.close()
        time.sleep(0.1)

        
#        self.textBrowser.insertPlainText("Snakefile created for Quality Check!! \nPlease refer to the file: Snakefile in your working directory. \n\n")
        snake = open('Snakefile', "w")
        snake.write('include: "rules/common_dna.smk"\n')
        snake.write('rule all:\n')
        snake.write('  input:\n')
        snake.write('    expand("results_dna/qc/fastqc/{u.sample}-{u.unit}-{u.condition}.html", u = units.itertuples()),\n')
        snake.write('    expand("results_dna/qc/fastqc/{u.sample}-{u.unit}-{u.condition}.zip", u = units.itertuples()),\n')
        snake.write('include: "rules/qc_dna.smk"\n')
        snake.close()
        
# =============================================================================
#         self.textBrowser.setTextColor(self._colors['black'])
#         self.textBrowser.append("QC Results being generated. Please wait! \n")
# =============================================================================
        
        
        def func_qc():
            subprocess.run(["snakemake", "--use-conda", "-j", "1"])
#            process1 = subprocess.Popen(["snakemake", "--use-conda", "&&", "snakemake", "--use-conda" ], shell =True,  stdout=subprocess.PIPE)
#            output1 = process1.communicate()
            
        def multi_qc():
            subprocess.run(["snakemake", "--use-conda", "-s", "Snakefile_multiqc", "-j", "1"])
#            print("started func1")
#            self.progressBar.setValue(1)
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
            webbrowser.get('firefox').open(filename, new=0, autoraise=True)
        else:
            pass
#        subprocess.run(["snakemake", "--use-conda", "&>>", "show_qc_results_out.txt"], shell =True)
        
#        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
#        print(webbrowser._browsers)
# =============================================================================
#         self.textBrowser.setTextColor(self._colors['blue'])
#         self.textBrowser.append("Wait till the QC results popup! \n\n")
# =============================================================================
# =============================================================================
#         if os.path.exists("results_dna/qc/fastqc"):
#             for file in os.listdir("results_dna/qc/fastqc"):
#                 if file.endswith(".html"):
#                     filename = os.path.join("results_dna/qc/fastqc", file)
# #                    print(filename)
#                     webbrowser.get('firefox').open(filename, new=0, autoraise=True)
# # =============================================================================
# #                     chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
# #                     webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
# #                     webbrowser.get('chrome').open(filename, new=0, autoraise=True)
# # =============================================================================
# #                    webbrowser.get('google-chrome').open(filename, new=0, autoraise=True)  # open in new tab
#                 else:
#                     pass
#         else:
#             pass
# =============================================================================
                


    def show_qc_results_rna(self):
        self.progressBar_sub1_rna.setValue(1)
#        self.progressBar.setValue(1)
        self.nextbuttonqcRNA.setEnabled(True)
        self._set_color(self._colors['blue'].name(),pb =self.progressBar_sub1_rna)
#        self._set_color(self._colors['blue'].name(),pb =self.progressBar)
        self.textBrowser.setTextColor(self._colors['black'])
        self.textBrowser.append("QC Results being generated. Please wait! \n")
        time.sleep(0.1)
        conf = open('config.yaml', 'w')
        conf.write('ref: \n')
#        if self.AlignercomboBoxRNA.currentText() == 'hisat2':
#            conf.write('  index-'+self.AlignercomboBoxRNA.currentText() + ': ' + self.StarIndexlineEdit.text() + '/hisat2-index \n')
#        elif self.AlignercomboBoxRNA.currentText() == 'bowtie2':
#            conf.write('  index-'+ self.AlignercomboBoxRNA.currentText() + ': ' + self.StarIndexlineEdit.text() + '/bowtie2-index \n')
#        else:
#            conf.write('  index-'+ self.AlignercomboBoxRNA.currentText() + ': ' + self.StarIndexlineEdit.text() + '\n')
        conf.write('  annotation: '+ self.AnnotatedlineEditRNA.text() + '\n')
        conf.write('  fasta: '+self.FastalineEdit.text() + '\n')
        conf.write('  transcript: '+self.TranscriptlineEdit.text() + '\n')
        conf.write('params: \n')
#        conf.write("  fastqc: '" + self.QClineEdit_rna.text() + "' \n")
        conf.write("  cutadapt: '" + self.CutadaptlineEdit.text() + "' \n")
        conf.write("sample: " + self.SampleFolderLineEdit.text() + "\n")
        conf.close()
        time.sleep(0.1)
        self.textBrowser.setTextColor(self._colors['black'])
        self.textBrowser.append("Snakefile created for Quality Check!! \nPlease refer to the file: Snakefile in your working directory. \n\n")
        snakef = open('Snakefile', "w")
        snakef.write('include: "rules/common_rna.smk"\n')
        snakef.write('rule all:\n')
        snakef.write('  input:\n')
        snakef.write("    expand('results/fastqc/{sample}_{condition}_Rep{rep}_R1_fastqc.zip', sample=samples, condition=type, rep=reps),\n")
        snakef.write("    expand('results/fastqc/{sample}_{condition}_Rep{rep}_R2_fastqc.zip', sample=samples, condition=type, rep=reps),\n")
        snakef.write('include: "rules/qc_rna.smk"\n')
        snakef.close()
        
        time.sleep(0.1)
        
        def func_qc():
            process1 = subprocess.Popen(["snakemake", "--use-conda", "-j", "1"], shell =True,  stdout=subprocess.PIPE)
            output1 = process1.communicate()
            
#            print("started func1")
#            self.progressBar.setValue(1)
        def multi_qc():
            subprocess.run(["snakemake", "--use-conda", "-s", "Snakefile_multiqc_rna", "-j", "1"])
#            print("started func1")
#            self.progressBar.setValue(1)
#        self.textBrowser.append("Running Quality Check!! \n\n")
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
            webbrowser.get('firefox').open(filename, new=0, autoraise=True)
        else:
            pass
# =============================================================================
#     def func2(self):
#         
#         time.sleep(1)
# #            print("started func2")
#         
#         now = dt.datetime.now()
#         ago = now-dt.timedelta(minutes=1)
# #           self.textBrowser_PythonShellTab.clear()
# #            self.progressBar.setValue(1)
#     
#         for root, dirs,files in os.walk('.snakemake/log/'):  
#             for fname in files:
#                 path = os.path.join(root, fname)
#                 st = os.stat(path)    
#                 mtime = dt.datetime.fromtimestamp(st.st_mtime)
#                 if mtime > ago:
# #                        print(path)
# #                        self.progressBar.setValue(1)
#                     f = open(path, 'r')
#                     while True:
#                         line = ''
#                         while len(line) == 0 or line[-1] != '\n':
#                             tail = f.readline()
#                             if tail == '':
#                                 time.sleep(0.1)          # avoid busy waiting
#                                 # f.seek(0, io.SEEK_CUR) # appears to be unneccessary
#                                 continue
#                             line += tail
# #                                self.textBrowser_PythonShellTab.insertPlainText(line)
#                             if '%' in line:
# #                                    print(line)
#                                 per = line.split('(', 1)[1].split(')')[0]
#                                 percent = per[:-1]
#                                 self.progressBar_sub1_dna.setValue(int(percent))
#                                 self.progressBar.setValue(int(percent)/3)
# # =============================================================================
# # #                                    print(percent)
# #                                 if percent == '10':
# #                                     self.progressBar_sub1.setValue(100)
# #                                     self.progressBar.setValue(1)
# # #                                    self.progressBar.setValue(100/3)
# #                                 else:
# # =============================================================================
#                                     
# #                                    self.progressBar.setValue(int(percent)/3)
#                             elif 'Error' in line:
#                                 self._set_pb1_color_dna(self._colors['red'].name())
#                                 self._set_pb_color(self._colors['red'].name())
#                             elif '(100%) done' in line:
#                                 self.progressBar_sub1_dna.setValue(100)
#                                 self.progressBar.setValue(100/3)
#                                 if os.path.exists("results_dna/qc/fastqc_after"):
#                                     for file in os.listdir("results_dna/qc/fastqc_after"):
#                                         if file.endswith(".html"):
#                                             filename = os.path.join("results_dna/qc/fastqc_after", file)
#                                             webbrowser.get('google-chrome').open(filename, new=0, autoraise=True)  # open in new tab
#                                 else:
#                                     continue
# # =============================================================================
# #                                 self._set_pb1_color(self._colors['green'].name())
# #                                 self._set_pb_color(self._colors['green'].name())
# # =============================================================================
# #                                self.progressBar.setValue(100/3)
#  #                            self.progressBar.setValue(1)
#                             elif 'Nothing to be done' in line:
#                                 self.progressBar_sub1_dna.setValue(100)
#                                 self.progressBar.setValue(100/3)
#                                 if os.path.exists("results_dna/qc/fastqc_after"):
#                                     for file in os.listdir("results_dna/qc/fastqc_after"):
#                                         if file.endswith(".html"):
#                                             filename = os.path.join("results_dna/qc/fastqc_after", file)
#                                             webbrowser.get('google-chrome').open(filename, new=0, autoraise=True)  # open in new tab
#                                 else:
#                                     continue
#                             
# #                                self.progressBar.setValue(100/3)
# #                        except IOError:
#                         if ('Complete log' in line):
#                             break
# =============================================================================
                        
                    
    
# =============================================================================
#         p1 = Process(target=func1)
#         p1.start()
#         p2 = Process(target=func2)
#         p2.start()
# =============================================================================
    def run_qc_textbox(self):
        self.textBrowser.setTextColor(self._colors['black'])
        self.textBrowser.append("Running Quality Check!! \n\n")        
    
         
    def run_qc_dna(self, line):
        self.progressBar_sub1_dna.setValue(51)
#        self.progressBar.setValue(26)
        self._set_color(self._colors['blue'].name(),pb =self.progressBar_sub1_dna)
#        self._set_color(self._colors['blue'].name(),pb =self.progressBar)
        self.textBrowser.setTextColor(self._colors['black'])
        self.textBrowser.append("Config file created for Quality Check!! \nPlease refer to the file: config.yaml in your working directory. \n\n")
        conf = open('config.yaml', 'w')
        conf.write('samples: ./samples.tsv \n')
        conf.write('units: '+ self.UnitslineEditDNA.text() + '\n'+'ref: \n')
        conf.write("  name: " + self.RefNamecomboBoxDNA.currentText() + "\n")
        conf.write('  genome: '+ self.WDlineEditDNA.text() + "/" +self.RefGenomelineEditDNA.text() + '\n')
        conf.write('  genome-name: '+ os.path.basename(self.RefGenomelineEditDNA.text()) + '\n')
        conf.write('  known-variants: '+ self.RefVariantlineEditDNA.text() + '\n')
        conf.write("processing: \n")
        conf.write("  remove-duplicates: true\n")
#        conf.write('index: \n')
#        conf.write('  '+ self.AlignercomboBoxDNA.currentText() + ': ' + self.BWAIndexlineEdit.text() + '\n')
        conf.write('params: \n')
#        conf.write("  fastqc: '" + self.QClineEdit.text() + "' \n")
        conf.write("  cutadapt: '" + self.CutadaptlineEdit.text() + "' \n")
        conf.close()
        
        time.sleep(0.1)
        self.textBrowser.setTextColor(self._colors['black'])
        self.textBrowser.append("Snakefile created for Quality Check!! \nPlease refer to the file: Snakefile in your working directory. \n\n")
        snake = open('Snakefile', "w")
        snake.write('include: "rules/common_dna.smk"\n')
        snake.write('rule all:\n')
        snake.write('  input:\n')
#        snake.write('    expand("results_dna/qc/fastqc/{u.sample}-{u.unit}.html", u = units.itertuples()),\n')
#        snake.write('    expand("results_dna/qc/fastqc/{u.sample}-{u.unit}.zip", u = units.itertuples()),\n')
        snake.write('    expand("results_dna/trimmed/{u.sample}-{u.unit}-{u.condition}.qc.txt", u = units.itertuples()),\n')
        snake.write('    expand("results_dna/qc/fastqc_after/{u.sample}-{u.unit}-{u.condition}.aftertrim.html", u = units.itertuples()),\n')
        snake.write('    expand("results_dna/qc/fastqc_after/{u.sample}-{u.unit}-{u.condition}.aftertrim.zip", u = units.itertuples()) \n')
#        snake.write('\ninclude: "rules/qc_dna.smk"\n')
        snake.write('include: "rules/cutadapt_dna.smk"\n')
        snake.write('include: "rules/fastqc_after_dna.smk"\n')
        snake.close()
        
        time.sleep(0.1)
        
        def func1():
            
            process1 = subprocess.Popen(["snakemake", "--use-conda", "-j", "1"], shell =True,  stdout=subprocess.PIPE)
            output1 = process1.communicate()
#            print("started func1")
#            self.progressBar.setValue(1)
#        self.textBrowser.setTextColor(self._colors['black'])
#        self.textBrowser.append("Running Quality Check!! \n\n")
        p1 = Process(target=func1)
#        QtWidgets.QApplication.instance().processEvents()
        p1.start()
        p2 = Process(target=self.func_pb_update( sub_pb=self.progressBar_sub1_dna, sub_pb_frac=4, initial_sub = 50, initial_main=0, error_icon=self.RunQCButtonErroricon))
#        QtWidgets.QApplication.instance().processEvents()
        p2.start()
        
        def multi_qc():
            subprocess.run(["snakemake", "--use-conda", "-s", "Snakefile_after", "-j", "1"])
        
        if self.progressBar_sub1_dna.value()==50:
            self.textBrowser.setTextColor(self._colors['black'])
            self.textBrowser.append("Running Quality Check!! \n\n")
            p3 = Process(target=multi_qc)
            self.progressBar_sub1_dna.setValue(51)
            p3.start()
            
            p4 = Process(target= self.func_pb_update( sub_pb=self.progressBar_sub1_dna, sub_pb_frac=4, initial_sub = 50, initial_main=0, error_icon=self.QCresultsButtonErroricon))
            p4.start()
        else:
            pass
            
        if os.path.exists("results_dna/qc/multiqc_after.html"):
            filename = "results_dna/qc/multiqc_after.html"
            webbrowser.get('firefox').open(filename, new=0, autoraise=True)
        else:
            pass
            
        
        
# =============================================================================
#         def func1():
#             print("started func1")
# #            self.progressBar.setValue(1)
#             process = subprocess.Popen(["snakemake", "--use-conda"], shell =True,  stdout=subprocess.PIPE)
#             output = process.communicate()
#             print("ended func1")
#         
#         def func2(self):
#             time.sleep(1)
#             print("started func2")
#             
#             now = dt.datetime.now()
#             ago = now-dt.timedelta(minutes=2)
#         #           self.textBrowser_PythonShellTab.clear()
#         #            self.progressBar.setValue(1)
#         
#             for root, dirs,files in os.walk('.snakemake/log/'):  
#                 for fname in files:
#                     path = os.path.join(root, fname)
#                     st = os.stat(path)    
#                     mtime = dt.datetime.fromtimestamp(st.st_mtime)
#                     if mtime > ago:
#         #                        print(path)
#         #                        self.progressBar.setValue(1)
#                         f = open(path, 'r')
#                         while True:
#                             line = ''
#                             while len(line) == 0 or line[-1] != '\n':
#                                 tail = f.readline()
#                                 if tail == '':
#                                     time.sleep(0.1)          # avoid busy waiting
#                                     # f.seek(0, io.SEEK_CUR) # appears to be unneccessary
#                                     continue
#                                 line += tail
#         #                                self.textBrowser_PythonShellTab.insertPlainText(line)
#                                 if '%' in line:
#         #                                    print(line)
#                                     percent = line[14:16]
#         #                                    print(percent)
#                                     if percent == '10':
#                                         self.progressBar_sub1.setValue(100)
#                                         self.progressBar.setValue(100/3)
#                                     else:
#                                         self.progressBar_sub1.setValue(int(percent))
#                                         self.progressBar.setValue(int(percent)/3)
#                                 elif 'Finished job' in line:
#                                     self.progressBar_sub1.setValue(100)
#                                     self.progressBar.setValue(100/3)
#          #                            self.progressBar.setValue(1)
#                                 elif 'Nothing to be done' in line:
#                                     self.progressBar_sub1.setValue(100)
#                                     self.progressBar.setValue(100/3)
#                                 print("ended func2")
# =============================================================================
# =============================================================================
#         p1 = Process(target=func1)
#         p1.start()
#         p2 = Process(target=func2)
#         p2.start()
# =============================================================================
#        return True
        
# =============================================================================
#         def func1():
# #            print("started func1")
# #            self.progressBar.setValue(1)
#             process = subprocess.Popen(["snakemake", "--use-conda"], shell =True,  stdout=subprocess.PIPE)
#             output = process.communicate()
# =============================================================================
            
           
#        self.textBrowser.insertPlainText("Running Quality Check!! \n\n")
#        subprocess.run(["snakemake", "--use-conda"])
#        subprocess.run(["snakemake", "--use-conda"])
# =============================================================================
#         def func2():
#             now = dt.datetime.now()
#             ago = now-dt.timedelta(minutes=10)
#             self.textBrowser_PythonShellTab.clear()
#             self.progressBar.setValue(0)
#             
#             for root, dirs,files in os.walk('.snakemake/log/'):  
#                 for fname in files:
#                     path = os.path.join(root, fname)
#                     st = os.stat(path)    
#                     mtime = dt.datetime.fromtimestamp(st.st_mtime)
#                     if mtime > ago:
#                         print(path)
#                         
#                         with open(path, 'r') as testout:
#                             content = testout.readlines()
#                             for line in content:
#                                 self.textBrowser_PythonShellTab.insertPlainText(line)
#                                 if '%' in line:
#                                     print(line)
#                                     percent = line[14:16]
#                                     print(percent)
#                                     if percent == (10):
#                                         self.progressBar.setValue(100)
#                                     else:
#                                         self.progressBar.setValue(int(percent))
#                                         
#     #                            self.progressBar.setValue(1)
#                                 elif 'Complete log' in line:
#                                     self.progressBar.setValue(100)
#                             
#                                                             
#         self.textBrowser.insertPlainText("Quality Check completed!! Please view results in /results_dna/QC \n\n")                    
# =============================================================================
# =============================================================================
#         self.shell_error = ""
#         self.shell = ""
# =============================================================================
        
#        self.textBrowser.setText(str(subprocess.check_output(["snakemake", "--use-conda"])))
        
# =============================================================================
#         self._set_pb_color(self._colors['blue'].name())
#         self.textBrowser_PythonShellTab.clear()
# #        line, data = self.snakemake_data_stdout()
#         data = str(self.process.readAllStandardOutput())
# 
#         grouprex = self._step_regex.findall(str(line))
#         print(data)
# #        print(line)
# #        print(grouprex)
#         self.progressBar.setValue(1)
#         if grouprex:
#             step = int(grouprex[-1][0]) / float(grouprex[-1][1]) * 100
#             self.progressBar.setValue(step)
#         to_find = "Nothing to be done."
# #        if(line.contains(to_find)):
# =============================================================================
#            self.progressBar.setValue(100)
        
        
# =============================================================================
#         proc = subprocess.Popen(["snakemake", "--use-conda"], shell=True, stdout=subprocess.PIPE)
#         for line in proc.stdout.readlines():
#             print(line)
# =============================================================================
# =============================================================================
#        file_ = open("output_qc.txt", "w")
#        subprocess.Popen("snakemake", "--use-conda", stdout=file_)
        
    
        
#    def run_qc_dna_textbox(self):
        
#        sys.stdout = port(self.textBrowser)



#    def config_qc_rna(self):
# =============================================================================
#         conf = open('config.yaml', 'w')
#         conf.write('ref: \n')
# #        if self.AlignercomboBoxRNA.currentText() == 'hisat2':
# #            conf.write('  index-'+self.AlignercomboBoxRNA.currentText() + ': ' + self.StarIndexlineEdit.text() + '/hisat2-index \n')
# #        elif self.AlignercomboBoxRNA.currentText() == 'bowtie2':
# #            conf.write('  index-'+ self.AlignercomboBoxRNA.currentText() + ': ' + self.StarIndexlineEdit.text() + '/bowtie2-index \n')
# #        else:
# #            conf.write('  index-'+ self.AlignercomboBoxRNA.currentText() + ': ' + self.StarIndexlineEdit.text() + '\n')
#         conf.write('  annotation: '+ self.AnnotatedlineEditRNA.text() + '\n')
#         conf.write('  fasta: '+self.FastalineEdit.text() + '\n')
#         conf.write('  transcript: '+self.TranscriptlineEdit.text() + '\n')
#         conf.write('params: \n')
#         conf.write("  fastqc: '" + self.QClineEdit_rna.text() + "' \n")
#         conf.write("  cutadapt: '" + self.CutadaptlineEdit.text() + "' \n")
#         conf.write("sample: " + self.SampleFolderLineEdit.text() + "\n")
#         conf.close()
#         self.textBrowser.insertPlainText("Config file created for Quality Check!! \nPlease refer to the file: config.yaml in your working directory. \n\n")
# =============================================================================
#==============================================================================
#         with open('rules/common_rna.smk', 'r+') as common:
#             contents = common.readlines()
#             contents.insert(29, 'test_data_dir = "'+self.SampleFolderLineEdit.text() +'" \n')  # new_string should end in a newline
#             common.seek(0)  # readlines consumes the iterator, so we need to start over
#             common.writelines(contents)
#==============================================================================
        
# =============================================================================
#         with open('rules/common_rna.smk', 'r') as common:
#             data = common.read()
#         data = data.replace('os.getcwd()', '"' + self.SampleFolderLineEdit.text() + '"')
#         with open('rules/common_rna.smk', 'w') as cr:
#             cr.write(data)
# =============================================================================
            
        
#    def snakefile_qc_rna(self):
# =============================================================================
#         snakef = open('Snakefile', "w")
#         snakef.write('include: "rules/common_rna.smk"\n')
#         snakef.write('rule all:\n')
#         snakef.write('  input:\n')
#         snakef.write("    expand('results/fastqc/{sample}_{condition}_Rep{rep}_R1_fastqc.zip', sample=samples, condition=type, rep=reps),\n")
#         snakef.write("    expand('results/fastqc/{sample}_{condition}_Rep{rep}_R2_fastqc.zip', sample=samples, condition=type, rep=reps),\n")
#         snakef.write("    expand('results/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R1.fastq', sample=samples, condition=type, rep=reps),\n")
#         snakef.write("    expand('results/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R2.fastq', sample=samples, condition=type, rep=reps),\n")
#         snakef.write("    expand('results/summary_stats/{sample}_{condition}_Rep{rep}_cutadapt_summary.txt', sample=samples, condition=type, rep=reps),\n")
#         snakef.write("    expand('results/fastqc_after/{sample}_{condition}_Rep{rep}_cutadapt_R1_fastqc.zip', sample=samples, condition=type, rep=reps),\n")
#         snakef.write('include: "rules/qc_rna.smk"\n')
#         snakef.write('include: "rules/cutadapt_rna.smk"\n')
#         snakef.write('include: "rules/fastqc_after_rna.smk"\n')
#         snakef.close()
#         self.textBrowser.insertPlainText("Snakefile created for Quality Check!! \nPlease refer to the file: Snakefile in your working directory. \n\n")
# =============================================================================
        
# =============================================================================
#     def func2_rna(self):
#         
#         time.sleep(1)
# #            print("started func2")
#         
#         now = dt.datetime.now()
#         ago = now-dt.timedelta(minutes=1)
# #           self.textBrowser_PythonShellTab.clear()
# #            self.progressBar.setValue(1)
#     
#         for root, dirs,files in os.walk('.snakemake/log/'):  
#             for fname in files:
#                 path = os.path.join(root, fname)
#                 st = os.stat(path)    
#                 mtime = dt.datetime.fromtimestamp(st.st_mtime)
#                 if mtime > ago:
# #                        print(path)
# #                        self.progressBar.setValue(1)
#                     f = open(path, 'r')
#                     while True:
#                         line = ''
#                         while len(line) == 0 or line[-1] != '\n':
#                             tail = f.readline()
#                             if tail == '':
#                                 time.sleep(0.1)          # avoid busy waiting
#                                 # f.seek(0, io.SEEK_CUR) # appears to be unneccessary
#                                 continue
#                             line += tail
# #                                self.textBrowser_PythonShellTab.insertPlainText(line)
#                             if '%' in line:
# #                                    print(line)
#                                 per = line.split('(', 1)[1].split(')')[0]
#                                 percent = per[:-1]
#                                 self.progressBar_sub1_rna.setValue(int(percent))
#                                 self.progressBar.setValue(int(percent)/3)
# # =============================================================================
# # #                                    print(percent)
# #                                 if percent == '10':
# #                                     self.progressBar_sub1.setValue(100)
# #                                     self.progressBar.setValue(1)
# # #                                    self.progressBar.setValue(100/3)
# #                                 else:
# # =============================================================================
#                                     
# #                                    self.progressBar.setValue(int(percent)/3)
#                             elif 'Error' in line:
#                                 self._set_pb1_color_rna(self._colors['red'].name())
#                                 self._set_pb_color(self._colors['red'].name())
#                             elif '(100%) done' in line:
#                                 self.progressBar_sub1_rna.setValue(100)
#                                 self.progressBar.setValue(100/3)
#                                 
#                                 if os.path.exists("results/qc/fastqc_after"):
#                                     for file in os.listdir("results/qc/fastqc_after"):
#                                         if file.endswith(".html"):
#                                             filename = os.path.join("results/qc/fastqc_after", file)
#                                             webbrowser.get('google-chrome').open(filename, new=0, autoraise=True)  # open in new tab
#                                 else:
#                                     continue
# # =============================================================================
# #                                 self._set_pb1_color(self._colors['green'].name())
# #                                 self._set_pb_color(self._colors['green'].name())
# # =============================================================================
# #                                self.progressBar.setValue(100/3)
#  #                            self.progressBar.setValue(1)
#                             elif 'Nothing to be done' in line:
#                                 self.progressBar_sub1_rna.setValue(100)
#                                 self.progressBar.setValue(100/3)
#                                 if os.path.exists("results/qc/fastqc_after"):
#                                     for file in os.listdir("results/qc/fastqc_after"):
#                                         if file.endswith(".html"):
#                                             filename = os.path.join("results/qc/fastqc_after", file)
#                                             webbrowser.get('google-chrome').open(filename, new=0, autoraise=True)  # open in new tab
#                                 else:
#                                     continue
# #                                self.progressBar.setValue(100/3)
# #                        except IOError:
#                         if ('Complete log' in line):
#                             break
# =============================================================================
    def run_qc_rna_textbox(self):
        self.textBrowser.setTextColor(self._colors['black'])
        self.textBrowser.append("Running Quality Check!! \n\n")

    def run_qc_rna(self, line):
        self.progressBar_sub1_rna.setValue(51)
#        self.progressBar.setValue(26)
        self._set_color(self._colors['blue'].name(),pb =self.progressBar_sub1_rna)
#        self._set_color(self._colors['blue'].name(),pb =self.progressBar)
        self.textBrowser.setTextColor(self._colors['black'])
        self.textBrowser.append("Config file created for Quality Check!! \nPlease refer to the file: config.yaml in your working directory. \n\n")
        conf = open('config.yaml', 'w')
        conf.write('ref: \n')
#        if self.AlignercomboBoxRNA.currentText() == 'hisat2':
#            conf.write('  index-'+self.AlignercomboBoxRNA.currentText() + ': ' + self.StarIndexlineEdit.text() + '/hisat2-index \n')
#        elif self.AlignercomboBoxRNA.currentText() == 'bowtie2':
#            conf.write('  index-'+ self.AlignercomboBoxRNA.currentText() + ': ' + self.StarIndexlineEdit.text() + '/bowtie2-index \n')
#        else:
#            conf.write('  index-'+ self.AlignercomboBoxRNA.currentText() + ': ' + self.StarIndexlineEdit.text() + '\n')
        conf.write('  annotation: '+ self.AnnotatedlineEditRNA.text() + '\n')
        conf.write('  fasta: '+self.FastalineEdit.text() + '\n')
        conf.write('  transcript: '+self.TranscriptlineEdit.text() + '\n')
        conf.write('params: \n')
#        conf.write("  fastqc: '" + self.QClineEdit_rna.text() + "' \n")
        conf.write("  cutadapt: '" + self.CutadaptlineEdit.text() + "' \n")
        conf.write("sample: " + self.SampleFolderLineEdit.text() + "\n")
        conf.close()
        time.sleep(0.1)
        self.textBrowser.setTextColor(self._colors['black'])
        self.textBrowser.append("Snakefile created for Quality Check!! \nPlease refer to the file: Snakefile in your working directory. \n\n")
        snakef = open('Snakefile', "w")
        snakef.write('include: "rules/common_rna.smk"\n')
        snakef.write('rule all:\n')
        snakef.write('  input:\n')
#        snakef.write("    expand('results/fastqc/{sample}_{condition}_Rep{rep}_R1_fastqc.zip', sample=samples, condition=type, rep=reps),\n")
#        snakef.write("    expand('results/fastqc/{sample}_{condition}_Rep{rep}_R2_fastqc.zip', sample=samples, condition=type, rep=reps),\n")
        snakef.write("    expand('results/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R1.fastq', sample=samples, condition=type, rep=reps),\n")
        snakef.write("    expand('results/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R2.fastq', sample=samples, condition=type, rep=reps),\n")
        snakef.write("    expand('results/summary_stats/{sample}_{condition}_Rep{rep}_cutadapt_summary.txt', sample=samples, condition=type, rep=reps),\n")
        snakef.write("    expand('results/fastqc_after/{sample}_{condition}_Rep{rep}_cutadapt_R1_fastqc.zip', sample=samples, condition=type, rep=reps),\n")
#        snakef.write('include: "rules/qc_rna.smk"\n')
        snakef.write('include: "rules/cutadapt_rna.smk"\n')
        snakef.write('include: "rules/fastqc_after_rna.smk"\n')
        snakef.close()
        time.sleep(0.1)
        def func_qc_rna():
            
            process2 = subprocess.Popen(["snakemake", "--use-conda", "-j", "1"], shell =True,  stdout=subprocess.PIPE)
            output2 = process2.communicate()
#            print("started func1")
#            self.progressBar.setValue(1)
        
        p1 = Process(target=func_qc_rna)
        p1.start()
        p2 = Process(target=self.func_pb_update( sub_pb=self.progressBar_sub1_rna, sub_pb_frac=2, initial_sub = 50, initial_main=0, error_icon=self.RunQCButtonErroricon_rna))
        p2.start()  
        
        def multi_qc():
            subprocess.run(["snakemake", "--use-conda", "-s", "Snakefile_after_rna", "-j", "1"])
        
        if self.progressBar_sub1_rna.value()==50:
            self.textBrowser.setTextColor(self._colors['black'])
            self.textBrowser.append("Running Quality Check!! \n\n")
            p3 = Process(target=multi_qc)
            self.progressBar_sub1_rna.setValue(51)
            p3.start()
            
            p4 = Process(target= self.func_pb_update( sub_pb=self.progressBar_sub1_rna, sub_pb_frac=4, initial_sub = 50, initial_main=0, error_icon=self.QCresultsButtonErroricon_rna))
            p4.start()
        else:
            pass
            
        if os.path.exists("results/fastqc_after/multiqc_after.html"):
            filename = "results/fastqc_after/multiqc_after.html"
            webbrowser.get('firefox').open(filename, new=0, autoraise=True)
        else:
            pass
# =============================================================================
#         cmd = str(subprocess.run(["snakemake", "--use-conda"]))
#         stdouterr = os.popen(cmd)[1].read()
#         self.textBrowser.setText(stdouterr)
# =============================================================================
# =============================================================================
#         p = subprocess.Popen(["snakemake", "--use-conda"],stdout=subprocess.PIPE)
#         
#         output = str(p.stdout.readline())
#         print(output)
#         
#         if('%' in output):
#             value = int(output[13:-2])
#             self.textBrowser.insertPlainText("{}% completed".format(value))
# =============================================================================
        

#    def run_qc_rna_textbox(self):
#        self.textBrowser.insertPlainText("Running Quality Check!! \n\n")

#    def create_config_for_index_dna(self):
# =============================================================================
#         conf = open('config.yaml', 'w')
#         conf.write('samples: '+ self.SampleslineEditDNA.text() + '\n')
#         conf.write('units: '+ self.UnitslineEditDNA.text() + '\n'+'ref: \n')
#         conf.write("  name: " + self.RefNamelineEdit.text() + "\n")
#         conf.write('  genome: '+ self.RefGenomelineEditDNA.text() + '\n')
#         conf.write('  genome-name: '+ os.path.basename(self.RefGenomelineEditDNA.text()) + '\n')
#         conf.write('  known-variants: '+ self.RefVariantlineEditDNA.text() + '\n')
#         conf.write("processing: \n")
#         conf.write("  remove-duplicates: true\n")
# #        conf.write('index: \n')
# #        conf.write('  '+ self.AlignercomboBoxDNA.currentText() + ': ' + self.BWAIndexlineEdit.text() + '\n')
#         conf.write('params: \n')
#         conf.write("  fastqc: '" + self.QClineEdit.text() + "' \n")
#         conf.write("  cutadapt: '" + self.CutadaptlineEdit.text() + "' \n")
#         conf.close()
#         self.textBrowser.insertPlainText("Config file created for generating index!! \nPlease refer to the file: config.yaml in your working directory. \n\n")
# =============================================================================

#    def create_snakefile_for_index_dna(self):
# =============================================================================
#         rule = open('rule_all_index.txt', 'r')
#         snakef = open('Snakefile_index', "w")
#         snakef.write('include: "rules/common_dna.smk"\n')
#         snakef.write('rule all:\n')
#         snakef.write('  input:\n')
#         for line in rule:
#             if self.AlignercomboBoxDNA.currentText() in line:
#                 snakef.write(line)
#                 snakef.write('\ninclude: "rules/' + self.AlignercomboBoxDNA.currentText() + '_index.smk" \n')
#         rule.close()
#         snakef.close()
#         self.textBrowser.insertPlainText("Snakefilefile created for generating index!! \nPlease refer to the file: Snakefile_index in your working directory. \n\n")
# =============================================================================

# =============================================================================
#     def func3(self):
#         time.sleep(1)
# #            print("started func2")
#         
#         now = dt.datetime.now()
#         ago = now-dt.timedelta(minutes=1)
# #           self.textBrowser_PythonShellTab.clear()
# #            self.progressBar.setValue(1)
#     
#         for root, dirs,files in os.walk('.snakemake/log/'):  
#             for fname in files:
#                 path = os.path.join(root, fname)
#                 st = os.stat(path)    
#                 mtime = dt.datetime.fromtimestamp(st.st_mtime)
#                 if mtime > ago:
# #                        print(path)
# #                        self.progressBar.setValue(1)
#                     f = open(path, 'r')
#                     while True:
#                         line = ''
#                         while len(line) == 0 or line[-1] != '\n':
#                             tail = f.readline()
#                             if tail == '':
#                                 time.sleep(0.1)          # avoid busy waiting
#                                 # f.seek(0, io.SEEK_CUR) # appears to be unneccessary
#                                 continue
#                             line += tail
# #                                self.textBrowser_PythonShellTab.insertPlainText(line)
#                             if '%' in line:
# #                                    print(line)
#                                 per = line.split('(', 1)[1].split(')')[0]
#                                 percent = per[:-1]
#                                 self.progressBar_sub2_dna.setValue(int(percent))
#                                 self.progressBar.setValue(100/3 + int(percent)/3)
# #                                    print(percent)
# # =============================================================================
# #                                 if percent == '10':
# #                                     self.progressBar_sub2.setValue(100)
# #                                     self.progressBar.setValue(2)
# # #                                    self.progressBar.setValue(100/3)
# #                                 else:
# # =============================================================================
# #                                    self.progressBar_sub2.setValue(int(percent))
# #                                    self.progressBar.setValue(int(percent)/3)
#                             elif 'Error' in line:
#                                 self._set_pb2_color_dna(self._colors['red'].name())
#                                 self._set_pb_color(self._colors['red'].name())
#                             elif '(100%) done' in line:
#                                 self.progressBar_sub2_dna.setValue(100)
#                                 self.progressBar.setValue(200/3)
# # =============================================================================
# #                                 self._set_pb2_color(self._colors['green'].name())
# #                                 self._set_pb_color(self._colors['green'].name())
# # =============================================================================
# #                                self.progressBar.setValue(100/3)
#  #                            self.progressBar.setValue(1)
#                             elif 'Nothing to be done' in line:
#                                 self.progressBar_sub2_dna.setValue(100)
#                                 self.progressBar.setValue(200/3)
#                         if ('Complete log' in line):
#                             break
# =============================================================================
    def run_index_text(self):
        self.textBrowser.setTextColor(self._colors['black'])
        self.textBrowser.append("Creating Index for "+self.AlignercomboBoxDNA.currentText()+ "!! \n\n")
        
    def run_index_dna(self):
        self.progressBar_sub2_dna.setValue(1)
#        self.progressBar.setValue(51)
        self._set_color(self._colors['blue'].name(),pb =self.progressBar_sub2_dna)
#        self._set_color(self._colors['blue'].name(),pb =self.progressBar)
        conf = open('config.yaml', 'w')
        conf.write('samples: ./samples.tsv \n')
        conf.write('units: '+ self.UnitslineEditDNA.text() + '\n'+'ref: \n')
        conf.write("  name: " + self.RefNamecomboBoxDNA.currentText() + "\n")
        conf.write('  genome: '+ self.RefGenomelineEditDNA.text() + '\n')
        conf.write('  genome-name: '+ os.path.basename(self.RefGenomelineEditDNA.text()) + '\n')
        conf.write('  known-variants: '+ self.RefVariantlineEditDNA.text() + '\n')
        conf.write("processing: \n")
        conf.write("  remove-duplicates: true\n")
#        conf.write('index: \n')
#        conf.write('  '+ self.AlignercomboBoxDNA.currentText() + ': ' + self.BWAIndexlineEdit.text() + '\n')
        conf.write('params: \n')
#        conf.write("  fastqc: '" + self.QClineEdit.text() + "' \n")
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
# =============================================================================
#         if self.AlignercomboBoxDNA.currentText() == "BWA_MEM":
#             snakef.write("    'results_dna/index/BWA_MEM/' +config['ref']['genome-name'] + '.fai'")
#         else:
#             for line in rule:
#                 if self.AlignercomboBoxDNA.currentText() in line:
#                     snakef.write(line)
#                 else:
#                     pass
# =============================================================================
        rule.close()
        if self.AlignercomboBoxDNA.currentText() == "BWA_MEM":
            snakef.write("    config['ref']['genome'] + '.fai',\n")
            snakef.write("    config['ref']['genome'].split('.')[0] + '.dict'")
            snakef.write('\ninclude: "rules/faidx.smk"')
        else:
            pass
        snakef.write('\ninclude: "rules/' + self.AlignercomboBoxDNA.currentText() + '_index.smk" \n')
        snakef.close()
        time.sleep(0.1)
#        self.textBrowser.insertPlainText("Creating Index for "+self.AlignercomboBoxDNA.currentText()+ "!! \n\n")
# =============================================================================
#         subprocess.run(["snakemake", "--use-conda", "--unlock", "-s", "Snakefile_index"])
#         subprocess.run(["snakemake", "--use-conda", "-s", "Snakefile_index"])
# =============================================================================
        def func_index_dna():
            
#            process3 = subprocess.Popen(["snakemake", "--use-conda", "-s", "Snakefile", "-j", "1"], shell =True,  stdout=subprocess.PIPE)
            process3 =subprocess.run(["snakemake", "--use-conda", "-j", "1"])
            output3 = process3.communicate()
#            print("started func1")
#            self.progressBar.setValue(1)
            
        
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
    
# =============================================================================
#     def run_index_dna_textbox(self):
#         self.textBrowser.insertPlainText("Creating Index for "+self.AlignercomboBoxDNA.currentText()+ "!! \n\n")
# =============================================================================

#    def create_config_for_index_rna(self):
# =============================================================================
#         conf = open('config.yaml', 'w')
#         conf.write('ref: \n')
# #        if self.AlignercomboBoxRNA.currentText() == 'hisat2':
# #            conf.write('  index-'+self.AlignercomboBoxRNA.currentText() + ': ' + self.StarIndexlineEdit.text() + '/hisat2-index \n')
# #        elif self.AlignercomboBoxRNA.currentText() == 'bowtie2':
# #            conf.write('  index-'+ self.AlignercomboBoxRNA.currentText() + ': ' + self.StarIndexlineEdit.text() + '/bowtie2-index \n')
# #        else:
# #            conf.write('  index-'+ self.AlignercomboBoxRNA.currentText() + ': ' + self.StarIndexlineEdit.text() + '\n')
#         conf.write('  annotation: '+ self.AnnotatedlineEditRNA.text() + '\n')
#         conf.write('  fasta: '+self.FastalineEdit.text() + '\n')
#         conf.write('  transcript: '+self.TranscriptlineEdit.text() + '\n')
#         conf.write('params: \n')
#         conf.write("  fastqc: '" + self.QClineEdit_rna.text() + "' \n")
#         conf.write("  cutadapt: '" + self.CutadaptlineEdit.text() + "' \n")
#         conf.write("sample: " + self.SampleFolderLineEdit.text() + "\n")
#         conf.close()
#         self.textBrowser.insertPlainText("Config file created for generating index!! \nPlease refer to the file: config.yaml in your working directory. \n\n")
# =============================================================================
#==============================================================================
#         with open('rules/common_rna.smk', 'r+') as common:
#             contents = common.readlines()
#             contents.insert(29, 'test_data_dir = "'+self.SampleFolderLineEdit.text() +'" \n')  # new_string should end in a newline
#             common.seek(0)  # readlines consumes the iterator, so we need to start over
#             common.writelines(contents)
#==============================================================================

#    def create_snakefile_for_index_rna(self):
# =============================================================================
#         rule = open('rule_all_index.txt', 'r')
#         snakef = open('Snakefile_index', "w")
#         snakef.write('configfile: "config.yaml"\n')
#         snakef.write('rule all:\n')
#         snakef.write('  input:\n')
#         for line in rule:
#             if self.AlignercomboBoxRNA.currentText() in line:
#                 snakef.write(line)
#         snakef.write('\ninclude: "rules/' + self.AlignercomboBoxRNA.currentText() + '_index.smk" \n')
#         rule.close()
#         snakef.close()
#         self.textBrowser.insertPlainText("Snakefilefile created for generating index!! \nPlease refer to the file: Snakefile_index in your working directory. \n\n")
# =============================================================================
        
# =============================================================================
#     def func3_rna(self):
#         time.sleep(1)
# #            print("started func2")
#         
#         now = dt.datetime.now()
#         ago = now-dt.timedelta(minutes=1)
# #           self.textBrowser_PythonShellTab.clear()
# #            self.progressBar.setValue(1)
#     
#         for root, dirs,files in os.walk('.snakemake/log/'):  
#             for fname in files:
#                 path = os.path.join(root, fname)
#                 st = os.stat(path)    
#                 mtime = dt.datetime.fromtimestamp(st.st_mtime)
#                 if mtime > ago:
# #                        print(path)
# #                        self.progressBar.setValue(1)
#                     f = open(path, 'r')
#                     while True:
#                         line = ''
#                         while len(line) == 0 or line[-1] != '\n':
#                             tail = f.readline()
#                             if tail == '':
#                                 time.sleep(0.1)          # avoid busy waiting
#                                 # f.seek(0, io.SEEK_CUR) # appears to be unneccessary
#                                 continue
#                             line += tail
# #                                self.textBrowser_PythonShellTab.insertPlainText(line)
#                             if '%' in line:
# #                                    print(line)
#                                 per = line.split('(', 1)[1].split(')')[0]
#                                 percent = per[:-1]
#                                 self.progressBar_sub2_rna.setValue(int(percent))
#                                 self.progressBar.setValue(100/3 + int(percent)/3)
# #                                    print(percent)
# # =============================================================================
# #                                 if percent == '10':
# #                                     self.progressBar_sub2.setValue(100)
# #                                     self.progressBar.setValue(2)
# # #                                    self.progressBar.setValue(100/3)
# #                                 else:
# # =============================================================================
# #                                    self.progressBar_sub2.setValue(int(percent))
# #                                    self.progressBar.setValue(int(percent)/3)
#                             elif 'Error' in line:
#                                 self._set_pb2_color_rna(self._colors['red'].name())
#                                 self._set_pb_color(self._colors['red'].name())
#                             elif '(100%) done' in line:
#                                 self.progressBar_sub2_rna.setValue(100)
#                                 self.progressBar.setValue(200/3)
# # =============================================================================
# #                                 self._set_pb2_color(self._colors['green'].name())
# #                                 self._set_pb_color(self._colors['green'].name())
# # =============================================================================
# #                                self.progressBar.setValue(100/3)
#  #                            self.progressBar.setValue(1)
#                             elif 'Nothing to be done' in line:
#                                 self.progressBar_sub2_rna.setValue(100)
#                                 self.progressBar.setValue(200/3)
#                         if ('Complete log' in line):
#                             break
# =============================================================================
        
    def run_index_rna(self):
        self.progressBar_sub2_dna.setValue(1)
#        self.progressBar.setValue(51)
        self._set_color(self._colors['blue'].name(),pb =self.progressBar_sub2_dna)
#        self._set_color(self._colors['blue'].name(),pb =self.progressBar)
        self.textBrowser.setTextColor(self._colors['black'])
        self.textBrowser.append("Config file created for generating index!! \nPlease refer to the file: config.yaml in your working directory. \n\n")
        conf = open('config.yaml', 'w')
        conf.write('ref: \n')
#        if self.AlignercomboBoxRNA.currentText() == 'hisat2':
#            conf.write('  index-'+self.AlignercomboBoxRNA.currentText() + ': ' + self.StarIndexlineEdit.text() + '/hisat2-index \n')
#        elif self.AlignercomboBoxRNA.currentText() == 'bowtie2':
#            conf.write('  index-'+ self.AlignercomboBoxRNA.currentText() + ': ' + self.StarIndexlineEdit.text() + '/bowtie2-index \n')
#        else:
#            conf.write('  index-'+ self.AlignercomboBoxRNA.currentText() + ': ' + self.StarIndexlineEdit.text() + '\n')
        conf.write('  annotation: '+ self.AnnotatedlineEditRNA.text() + '\n')
        conf.write('  fasta: '+self.FastalineEdit.text() + '\n')
        conf.write('  transcript: '+self.TranscriptlineEdit.text() + '\n')
        conf.write('params: \n')
#        conf.write("  fastqc: '" + self.QClineEdit_rna.text() + "' \n")
        conf.write("  cutadapt: '" + self.CutadaptlineEdit.text() + "' \n")
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
            
#            process4 = subprocess.Popen(["snakemake", "--use-conda", "-s", "Snakefile", "-j", "1"], shell =True,  stdout=subprocess.PIPE)
            process4 =subprocess.run(["snakemake", "--use-conda", "-j", "1"])
            output4 = process4.communicate()
#            print("started func1")
#            self.progressBar.setValue(1)
        self.textBrowser.setTextColor(self._colors['black'])
        self.textBrowser.append("Creating Index for "+self.AlignercomboBoxRNA.currentText()+ "!! \n\n")
        p1 = Process(target=func_index_rna)
        p1.start()
        p2 = Process(target=self.func_pb_update( sub_pb=self.progressBar_sub2_rna, sub_pb_frac=1, initial_sub = 0, initial_main=0, error_icon=self.RunIndexrnaButtonErroricon))
        p2.start()
#        self.textBrowser.insertPlainText("Creating Index for "+self.AlignercomboBoxRNA.currentText()+ "!! \n\n")
# =============================================================================
#         subprocess.run(["snakemake", "--use-conda", "--unlock", "-s", "Snakefile_index"])
#         subprocess.run(["snakemake", "--use-conda", "-s", "Snakefile_index"])
# =============================================================================
        self.StarIndexlineEdit.setText(os.getcwd()+"/results/index/"+self.AlignercomboBoxRNA.currentText())
        if self.progressBar_sub2_dna.value() == 100:
            self.textBrowser.setTextColor(self._colors['black'])
            self.textBrowser.append("Index created in results/index/" +self.AlignercomboBoxRNA.currentText() +"/ !! \n\n")
        else:
            pass

# =============================================================================
#     def run_index_rna_textbox(self):
#         self.textBrowser.insertPlainText("Creating Index for "+self.AlignercomboBoxRNA.currentText()+ "!! \n\n")
# =============================================================================

    def create_config_dna(self):
        conf = open('config.yaml', 'w')
        conf.write('samples: ./samples.tsv \n')
        conf.write('units: '+ self.UnitslineEditDNA.text() + '\n'+'ref: \n')
        conf.write("  name: " + self.RefNamecomboBoxDNA.currentText() + "\n")
        conf.write('  genome: '+ self.RefGenomelineEditDNA.text() + '\n')
        conf.write('  genome-name: '+ os.path.basename(self.RefGenomelineEditDNA.text()) + '\n')
        conf.write('  known-variants: '+ self.RefVariantlineEditDNA.text() + '\n')
        conf.write("processing: \n")
        conf.write("  remove-duplicates: true\n")
        conf.write('index: \n')
        conf.write('  '+ self.AlignercomboBoxDNA.currentText() + ': ' + self.BWAIndexlineEdit.text() + '\n')
        conf.write('params: \n')
        conf.write("  cutadapt: '" + self.CutadaptlineEdit.text() + "' \n")
#        conf.write('  ' + self.AlignercomboBoxDNA.currentText() + ": '" + self.Additional1lineEditDNA.text() +"' \n")
#        conf.write("  bcftools_call: '" +self.Additional1lineEditDNA.text() +"' \n" )
        aligner_params = open("aligner_params.txt", 'r').read().replace('\n', '')
        conf.write("  " + aligner_params + '\n')
        vc_params = open("vc_params.txt", 'r').read().replace('\n', '')
        conf.write("  " + vc_params + '\n')
        annotator_params = open("annotator_params.txt", 'r').read().replace('\n', '')
        conf.write("  " + annotator_params + '\n')
# =============================================================================
# =============================================================================
#         conf.write("  GATK_HC: \n")
# #==============================================================================
#         conf.write("    HaplotypeCaller: '" +"' \n")
#         conf.write("    GenotypeGVCFs: '" +"' \n")
#         conf.write("    BaseRecalibrator: '"+"' \n")
#         conf.write("    VariantRecalibrator: '"+ "' \n")
# #==============================================================================
# # =============================================================================
# #        conf.write('  ' + self.VCcomboBoxDNA.currentText() + ": '"+ self.Additional2lineEditDNA.text() +"' \n")
#         conf.write("  bcftools_call: '' \n")
#         conf.write("  BWA_MEM: '' \n")
#         conf.write("  GEM3: '' \n")
#         conf.write("  SnpEff: '-Xmx4g' \n")
#         conf.write("  freebayes: '' \n")
# =============================================================================
#        conf.write("  Annovar: '"+ self.Additional3lineEditDNA.text() +"' \n")
        conf.write("  picard: \n")
        conf.write("    MarkDuplicates: REMOVE_DUPLICATES=true \n")
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
#        snake.write('include: "rules/cutadapt_dna.smk"\n')
        snake.write('rule all:\n')
        snake.write('  input:\n')
#        snake.write('    expand("results_dna/trimmed/{u.sample}-{u.unit}.fastq.gz", u = units.itertuples()),\n')
        snake.write('    expand("results_dna/mapped/{u.sample}-{u.unit}-{u.condition}.sorted.bam", u = units.itertuples()),\n')
        snake.write('    expand("results_dna/dedup/{u.sample}-{u.unit}-{u.condition}.bam", u = units.itertuples()),\n')
#        snake.write('    expand("results_dna/qc/dedup/{u.sample}-{u.unit}.metrics.txt", u = units.itertuples()),\n')
#        snake.write('    expand("results_dna/recal/{u.sample}-{u.unit}.bam", u = units.itertuples()),\n')
        snake.write('    "results_dna/qc/multiqc.html",\n')
        snake.write('    "results_dna/merged/all.vcf.gz", \n')
        snake.write('    "results_dna/filtered/all.vcf.gz",\n')
        snake.write('    "results_dna/multiqc/multiqc.html",\n')
        snake.write('\ninclude: "rules/' + self.AlignercomboBoxDNA.currentText() + '.smk" \n')
        snake.write('include: "rules/' + self.VCcomboBoxDNA.currentText() + '.smk" \n')
#        snake.write('include: "rules/bqsr.smk"\n')
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
            self.RefNamelabelDNA.hide()
            self.RefNamecomboBoxDNA.hide()

    def if_annovar(self):
        with open('Snakefile', 'r+') as fd:
            contents = fd.readlines()
            if self.AnnotatorcomboBoxDNA.currentText() == 'Annovar':
                contents.insert(8, '    "results_dna/annotated/all.hg19_multianno.vcf", \n')  # new_string should end in a newline
                fd.seek(0)  # readlines consumes the iterator, so we need to start over
                fd.writelines(contents)
            else:
                contents.insert(8, '    "results_dna/annotated/all.vcf", \n')
                fd.seek(0)  # readlines consumes the iterator, so we need to start over
                fd.writelines(contents)
                fd.close()

    def create_config_rna(self):
        conf = open('config.yaml', 'w')
        conf.write('ref: \n')
        if self.AlignercomboBoxRNA.currentText() == 'hisat2':
            conf.write('  index-'+self.AlignercomboBoxRNA.currentText() + ': ' + self.StarIndexlineEdit.text() + '/ \n')
        elif self.AlignercomboBoxRNA.currentText() == 'bowtie2':
            conf.write('  index-'+ self.AlignercomboBoxRNA.currentText() + ': ' + self.StarIndexlineEdit.text() + '/bowtie2-index \n')
        else:
            conf.write('  index-'+ self.AlignercomboBoxRNA.currentText() + ': ' + self.StarIndexlineEdit.text() + '\n')
        conf.write('  annotation: '+ self.AnnotatedlineEditRNA.text() + '\n')
        conf.write('  fasta: '+self.FastalineEdit.text() + '\n')
        conf.write('  transcript: '+self.TranscriptlineEdit.text() + '\n')
        conf.write('params: \n')
        conf.write("  cutadapt: '" + self.CutadaptlineEdit.text() + "' \n")
        conf.write('  star: "--quantMode GeneCounts --limitBAMsortRAM 10000000000 --outSAMattrIHstart 0" #--sjdbOverhang 150 \n')
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
#==============================================================================
#         with open('rules/common_rna.smk', 'r+') as common:
#             contents = common.readlines()
#             contents.insert(29, 'test_data_dir = "'+self.SampleFolderLineEdit.text() +'" \n')  # new_string should end in a newline
#             common.seek(0)  # readlines consumes the iterator, so we need to start over
#             common.writelines(contents)
#==============================================================================
# =============================================================================
#         with open('rules/common_rna.smk', 'r') as commonrna:
#             datarna = commonrna.read()
#         datarna = datarna.replace('os.getcwd()', '"' + self.SampleFolderLineEdit.text() + '"')
#         with open('rules/common_rna.smk', 'w') as crna:
#             crna.write(datarna)
# =============================================================================



    def create_snakefile_rna(self):
#        rule = open('rule_all.txt', 'r')
        snakef = open('Snakefile', 'w')
        snakef.write('include: "rules/common_rna.smk"\n')
#        snakef.write('include: "rules/cutadapt_rna.smk"\n')
        snakef.write('rule all:\n')
        snakef.write('  input:\n')
#        snakef.write("    expand('results/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R1.fastq', sample=samples, condition=type, rep=reps),\n")
#        snakef.write("    expand('results/cutadapt/{sample}_{condition}_Rep{rep}_cutadapt_R2.fastq', sample=samples, condition=type, rep=reps),\n")
        if self.AlignercomboBoxRNA.currentText() == 'hisat2':
            snakef.write("    expand('results/aligner_results/{sample}_{condition}_Rep{rep}_cutadapt.sam', sample=samples, condition=type, rep=reps),\n")
            snakef.write("    expand('results/aligner_results/{sample}_{condition}_Rep{rep}_cutadapt.bam', sample=samples, condition=type, rep=reps),\n")
        elif self.AlignercomboBoxRNA.currentText() == 'star':
            snakef.write("    expand('results/aligner_results/{sample}_{condition}_Rep{rep}/Aligned.sortedByCoord.out.bam', sample=samples, condition=type, rep=reps),\n")
            #snakef.write("    expand('results/aligner_results/{sample}_{condition}_Rep{rep}/ReadsPerGene.out.tab', sample=samples, condition=type, rep=reps),\n")
            #snakef.write("    expand('results/aligner_results/{sample}_{condition}_Rep{rep}/Aligned.out.sam', sample=samples, condition=type, rep=reps),\n")
            #snakef.write("    expand('results/aligner_results/{sample}_{condition}_Rep{rep}/ReadsPerGene.out.tab', sample=samples, condition=type, rep=reps),\n")
        if self.EMcomboBoxRNA.currentText() == 'stringtie':
            snakef.write("    expand('results/em_results/{sample}_{condition}_Rep{rep}/{sample}_{condition}_Rep{rep}_transcript.gtf', sample=samples, condition=type, rep=reps),\n")
            snakef.write("    expand('results/em_results/{sample}_{condition}_Rep{rep}/{sample}_{condition}_Rep{rep}_gene_abundances.tsv', sample=samples, condition=type, rep=reps),\n")
            snakef.write("    expand('results/em_results/{sample}_{condition}_Rep{rep}/{sample}_{condition}_Rep{rep}_cov_ref.gtf', sample=samples, condition=type, rep=reps),\n")
        elif self.EMcomboBoxRNA.currentText() == 'HTseq':
            snakef.write("    expand(''results/em_results/{sample}_{condition}_Rep{rep}/{sample}_{condition}_Rep{rep}.counts', sample=samples, condition=type, rep=reps),\n")
        if self.DEcomboBoxRNA.currentText() == 'ballgown':
            snakef.write("    expand('results/de_results/SigDE.txt',)\n")         
#==============================================================================
#         if self.AlignercomboBoxRNA.currentText() == 'hisat2':
#             snakef.write("    expand('results/aligner_results/{sample}_{condition}_Rep{rep}_cutadapt.sam', sample=samples, condition=type, rep=reps),\n")
#             snakef.write("    expand('results/aligner_results/{sample}_{condition}_Rep{rep}_cutadapt.bam', sample=samples, condition=type, rep=reps),\n")
#         elif self.AlignercomboBoxRNA.currentText() == 'star':
#             snakef.write("    expand('results/aligner_results/{sample}_{condition}_Rep{rep}/Aligned.out.bam', sample=samples, condition=type, rep=reps),\n")
#             snakef.write("    expand('results/aligner_results/{sample}_{condition}_Rep{rep}/ReadsPerGene.out.tab', sample=samples, condition=type, rep=reps),\n")
#         if self.EMcomboBoxRNA.currentText() == 'stringtie':
#             snakef.write("    expand('results/em_results/{sample}_{condition}_Rep{rep}/{sample}_{condition}_Rep{rep}_transcript.gtf', sample=samples, condition=type, rep=reps),\n")
#             snakef.write("    expand('results/em_results/{sample}_{condition}_Rep{rep}/{sample}_{condition}_Rep{rep}_gene_abundances.tsv', sample=samples, condition=type, rep=reps),\n")
#             snakef.write("    expand('results/em_results/{sample}_{condition}_Rep{rep}/{sample}_{condition}_Rep{rep}_cov_ref.gtf', sample=samples, condition=type, rep=reps),\n")
#         if self.DEcomboBoxRNA.currentText() == 'ballgown':
#             snakef.write("    expand('results/de_results/SigDE.txt')\n")         
# #==============================================================================
#==============================================================================
#          for line in rule:
#              if self.AlignercomboBoxRNA.currentText() in line:
#                 snakef.write(line)
#              if self.EMcomboBoxRNA.currentText() in line:
#                  snakef.write(line)
#              if self.DEcomboBoxRNA.currentText() in line:
#                  snakef.write(line)
#         rule.close()
#==============================================================================
        snakef.write("    results/multiqc/multiqc.html" + "\n")
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
#        subprocess.run(["snakemake", "--rulegraph",  "|", "dot", "-Tsvg", "-o", svg_filename], shell =True,  stdout=subprocess.PIPE)
        subprocess.run(["snakemake", "--rulegraph",  "|", "dot", "-Tsvg", "-o", '"'+ svg_filename+ '"'], shell =True,  stdout=subprocess.PIPE)

# =============================================================================
#
# =============================================================================

    def about(self):
        url = 'icomic.readthedocs.io'
        widget = About()
        widget.setText("iCOMIC version 0.1")
        widget.setInformativeText("""
            Online documentation on <a href="http://%(url)s">%(url)s</a>
            <br>
            <br>
            Authors:  Priyanka Maripuri,  Anjana A S
            """ % {"url": url})
        widget.setWindowTitle("iCOMIC")
        #widget.setStandardButtons(QW.QMessageBox.Ok)
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

# =============================================================================
#     def func4(self):
#         time.sleep(1)
# #            print("started func2")
#         
#         now = dt.datetime.now()
#         ago = now-dt.timedelta(minutes=1)
# #           self.textBrowser_PythonShellTab.clear()
# #            self.progressBar.setValue(1)
#     
#         for root, dirs,files in os.walk('.snakemake/log/'):  
#             for fname in files:
#                 path = os.path.join(root, fname)
#                 st = os.stat(path)    
#                 mtime = dt.datetime.fromtimestamp(st.st_mtime)
#                 if mtime > ago:
# #                        print(path)
# #                        self.progressBar.setValue(1)
#                     f = open(path, 'r')
#                     while True:
#                         line = ''
#                         while len(line) == 0 or line[-1] != '\n':
#                             tail = f.readline()
#                             if tail == '':
#                                 time.sleep(0.1)          # avoid busy waiting
#                                 # f.seek(0, io.SEEK_CUR) # appears to be unneccessary
#                                 continue
#                             line += tail
# #                                self.textBrowser_PythonShellTab.insertPlainText(line)
#                             if '%' in line:
# #                                    print(line)
#                                 per = line.split('(', 1)[1].split(')')[0]
#                                 percent = per[:-1]
# #                                self.progressBar_sub3.setValue(int(percent))
#                                 self.progressBar.setValue(200/3 + int(percent)/3)
# #                                    print(percent)
# # =============================================================================
# #                                 if percent == '10':
# #                                     self.progressBar_sub2.setValue(100)
# #                                     self.progressBar.setValue(3)
# # #                                    self.progressBar.setValue(100/3)
# #                                 else:
# #                                     self.progressBar_sub2.setValue(int(percent))
# # =============================================================================
# #                                    self.progressBar.setValue(int(percent)/3)
#                             elif 'Error' in line:
# #                                self._set_pb3_color(self._colors['red'].name())
#                                 self._set_pb_color(self._colors['red'].name())
# #                                self.progressBar.setColor('red')
#                             
#                             elif '(100%) done' in line:
#                                 self.check_dag_and_results_button()
#                                 self.progressBar.setValue(100)
#                                 
# #                                self.progressBar_sub3.setValue(100)
# # =============================================================================
# #                                 self.progressBar.setValue(100)
# #                                 self.DAGButton.setEnabled(True)
# #                                 self.ResultsButton.setEnabled(True)
# #                                 self.DAGLabel.setEnabled(True)
# #                                 self.ResultsLabel.setEnabled(True)
# # =============================================================================
# # =============================================================================
# #                                 self._set_pb2_color(self._colors['green'].name())
# #                                 self._set_pb_color(self._colors['green'].name())
# # =============================================================================
# #                                self.progressBar.setValue(100/3)
#  #                            self.progressBar.setValue(1)
#                             elif 'Nothing to be done' in line:
#                                 self.check_dag_and_results_button()
#                                 self.progressBar.setValue(100)
# #                                self.progressBar_sub3.setValue(100)
# # =============================================================================
# #                                 self.progressBar.setValue(100)
# #                                 self.DAGButton.setEnabled(True)
# #                                 self.ResultsButton.setEnabled(True)
# #                                 self.DAGLabel.setEnabled(True)
# #                                 self.ResultsLabel.setEnabled(True)
# # =============================================================================
#                         if ('Complete log' in line):
#                             self.check_dag_and_results_button()
#                             break
# # =============================================================================
# #                             self.DAGButton.setEnabled(True)
# #                             self.ResultsButton.setEnabled(True)
# #                             self.DAGLabel.setEnabled(True)
# #                             self.ResultsLabel.setEnabled(True)
# # =============================================================================
# =============================================================================
                            
    def run_action_textbox(self):
        self.textBrowser.setTextColor(self._colors['black'])
        self.textBrowser.append("Please be patient, while we analyze your data... \n\n")

    def run_action_dna(self):
        self._set_color(self._colors['blue'].name(),pb =self.progressBar_dna)
        self.progressBar_dna.setValue(1)
        
        def func_run_action():
#            process5 = subprocess.Popen(["snakemake", "--use-conda"], shell =True,  stdout=subprocess.PIPE)
            process5 = subprocess.run(["snakemake", "--use-conda", "-j", "1"])
#            output5 = process5.communicate()
#            print("started func1")
#            self.progressBar.setValue(1)
            
    
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
#            process5 = subprocess.Popen(["snakemake", "--use-conda"], shell =True,  stdout=subprocess.PIPE)
            process5 = subprocess.run(["snakemake", "--use-conda", "-j", "1"])
#            output5 = process5.communicate()
#            print("started func1")
#            self.progressBar.setValue(1)
            
    
        p1 = Process(target=func_run_action)
        p1.start()
        p2 = Process(target=self.func_pb_update( sub_pb=self.progressBar, sub_pb_frac=1, initial_sub = 0, initial_main=0, error_icon=self.RunButtonErroricon))
        p2.start()
        self.run_action()
        if self.progressBar.value() == 100:
            self._set_color(self._colors['green'].name(),pb =self.progressBar)
            self.nextbuttonrunrNA.setEnabled(True)
            self.RNAtabWidget.setCurrentIndex(4)
            self.RNAtabWidget.setTabEnabled(4, True)
        else:
            pass
        
        
# =============================================================================
#         self.completed = 0
#         while self.completed < 100:
#             self.completed += 0.00001
#             self.progressBar.setValue(self.completed)
# =============================================================================
#        self.textBrowser.insertPlainText("Please be patient, while we analyze your data... \n\n")
# =============================================================================
#         subprocess.run(["snakemake", "--use-conda", "--unlock"])
#         subprocess.run(["snakemake", "--use-conda"])
# =============================================================================
        
# =============================================================================
#             with open("Snakefile", "r+") as snake:
#                 line= snake.readline()
#                 if '"rules/common_dna.smk"' in line:
#                     self.textBrowser.setTextColor(self._colors['green']) 
#                     self.textBrowser.append("Analysis completed!! Close the iCOMIC window and do 'cat<space>results_dna/annotated/all.vcf' to view the annotated results \n" )
#                 else:
#                     self.textBrowser.setTextColor(self._colors['green'])
#                     self.textBrowser.append("Analysis completed!! Close the iCOMIC window and do 'cd<space>results' to move to the folder containing results \n")
# =============================================================================
# =============================================================================
#         if self.progressBar.value() == 100:
#             self._set_color(self._colors['green'].name(),pb =self.progressBar)
#             self.DAGButton.setEnabled(True)
#             self.DAGLabel.setEnabled(True)
#         else:
#             pass
# =============================================================================
        
#        self.textBrowser.insertPlainText("Analysis completed!! Please view results in results_dna/ \n\n")
        
    
        
    
        
        
    
# =============================================================================
#     def unlock_action(self):
#         subprocess.run(["snakemake", "--use-conda", "--unlock"])
# =============================================================================

#    def dag_action(self):
#        subprocess.run(["snakemake", "--dag", "annotated/all.vcf.gz", "|", "dot", "-Tsvg", ">", "dag.svg"])
#        self.textBrowser.insertPlainText("Please find your DAG in your working Directory... \n\n")
# =============================================================================
#     def show_dag(self):
#         svg_filename = "dag.svg"
#         self.diag = SVGDialog(svg_filename)
#         self.diag.show()
#
# =============================================================================
# =============================================================================
# class EditorLog(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
# =============================================================================

# =============================================================================
#     def initUI(self):
#         self.editor = QtWidgets.QPlainTextEdit(self)
#         cmd = 'snakemake -uuse-conda'
#         output = subprocess.check_output(cmd, shell = True)
#         print (output)
# =============================================================================



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
        
# =============================================================================
# class WarningMessage(QtWidgets.QMessageBox):
#     def __init__(self):
#         super().__init__()
#         self.title = 'Notification'
#         self.left = 10
#         self.top = 10
#         self.width = 320
#         self.height = 200
# #        self.setStandardButtons("Click on 'Run' below to start your analysis", QtWidgets.QMessageBox.Ok)
#         self.initUI()
#         
#     def initUI(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
#         self.setIcon(QtWidgets.QMessageBox.Information)
# #        self.information(self, 'Notification', "Click on 'Run' below to start your analysis", QtWidgets.QMessageBox.Ok)
# #        QtWidgets.QMessageBox.information(self, 'Notification', "Click on 'Run' below to start your analysis")
#         
# =============================================================================
        

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
            self.radio_true = QtWidgets.QCheckBox(label_name)
            if str(add_str_param.iloc[p, 4]) == "TRUE":
                self.radio_true.setChecked(True)
            else:
                self.radio_true.setChecked(False)
            self.label_list_str.append(self.radio_true)
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
#        self.check_list = []
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
#        self.show()
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
#        msgBox.move(50, 50) 
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
        #        f = open('results_dna/called/TCRBOA-1.vcf', 'r')
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
# =============================================================================
#         with zipfile.ZipFile('results_dna/filtered/all.vcf.gz', 'r') as zip_ref:
#             zip_ref.extractall('results_dna/filtered')
# =============================================================================
#        f = open('results_dna/filtered/all.vcf.gz', 'r')
        with gzip.open(path, 'rb') as f:
            data = f.read()
            self.textEdit.setText(data.decode("utf-8"))

# =============================================================================
#         f = open(txt_path, 'r')
# 
#         with f:
#             data = f.read()
#             self.textEdit.setText(data)
# =============================================================================

# =============================================================================
#     def showDialog(self, file, path):
# 
#         fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Snakefile', '/data/Priyanka/other_pipelines/iCOMIC')
# 
#         if fname[0]:
#             f = open(fname[0], 'r')
# 
#             with f:
#                 data = f.read()
#                 self.textEdit.setText(data)
# =============================================================================
        
                 
        
# =============================================================================
#         self.Webviewer = QWebView()
#         self.main_layout.addLayout(self.Webviewer)
#         self.page = QtWebKitWidgets.QWebPage(self.Webviewer)
#         self.Webviewer.setPage(self.page)
#         self.html_path = ('results_dna_qc/qc/fastqc/B-1.html')
#         self.Webviewer.load(QtCore.QUrl(self.html_path))
# =============================================================================

# =============================================================================
# class port:
#     def __init__(self,view):
#         self.view = view
# 
#     def write(self,*args):
#         self.view.append(*args)
# 
#     def flush(self):
#         pass
# 
# =============================================================================
# =============================================================================
# class SVGDialog(QtWidgets.QDialog):
#     """Dialog to show a SVG image"""
#     def __init__(self, filename):
#         super().__init__()
#         self.main_layout = QtWidgets.QVBoxLayout(self)
#         self.setWindowTitle("DAG")
#
#         if os.path.exists(filename):
#             widget = QSvgWidget(filename)
#             self.main_layout.addWidget(widget)
# =============================================================================



if __name__ == "__main__":
#    p1 = Process(target=func1)
#    p1.start()
#    p2 = Process(target=func2)
#    p2.start()
    
    app = QtWidgets.QApplication(sys.argv)
#    app.setStyle("breeze")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

