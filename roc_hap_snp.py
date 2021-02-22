import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data_snp = pd.read_csv("benchmark_data/bench_pfda_ga4gh1/qfy.roc.Locations.SNP.csv")
#data_indel = pd.read_csv("/home/anjana/Documents/icomic_local/happy2.roc.Locations.INDEL.csv")
plot1 = sns.lineplot(data=data_snp, x='QUERY.FP',y='QUERY.TP', color='darkorange', linewidth=2)
#plot2 = sns.lineplot(data=data_indel, x='QUERY.FP',y='QUERY.TP', color='darkblue', linewidth=2)
plt.savefig("benchmark_data/bench_pfda_ga4gh1/roc_snp_s.png")