#import webbrowser
#url = 'results_dna_qc/qc/fastqc/B-2.html'
#webbrowser.open(url, new=1)  # open in new tab

import webbrowser
import os

for file in os.listdir("results_dna_qc/qc/fastqc"):
    if file.endswith(".html"):
        filename = os.path.join("results_dna_qc/qc/fastqc", file)
        webbrowser.open(filename, new=2) 

