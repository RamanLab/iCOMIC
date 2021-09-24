import numpy as np
import pandas as pd
import os

test_dir = '/data/Priyanka/other_pipelines/iCOMIC_keerthika/test'

sample = []
unit = []
condition = []

for file in os.listdir(test_dir):
    if file.endswith(".counts"):
        sample.append(file)
    else:
        pass
    


for i in range(len(sample)):
   base = os.path.splitext(sample[i])[0]
   units = base.split('_')[1] + "_" + base.split('_')[2]
   unit.append(units)
   condition.append(base.split('_')[1])

    
units_data = pd.DataFrame({'sample': sample,
                           'unit': unit,
                           'condition': condition})
units_data.to_csv('emtable.tsv', sep = '\t', index=False)