import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


sns.set_style('darkgrid', {'legend.frameon':True})

data = pd.read_csv("/home/florian/Downloads/ErsteWelle_reproduction.csv")[["Trial", "Robot Confidence", "Ball Confidence"]]

dfm = data.melt('Trial', var_name='Metric', value_name='Confidence')

g = sns.barplot(data=dfm, x="Trial", y="Confidence", hue="Metric", ci="sd")
g.set_xticklabels(g.get_xticklabels(), rotation=45, ha="right")

plt.tight_layout()

plt.savefig("test.png", dpi=600, format="png")

plt.show()
