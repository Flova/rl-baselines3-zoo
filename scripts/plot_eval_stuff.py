import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


sns.set_theme(style="darkgrid")

plt.gcf().subplots_adjust(bottom=0.30)

channel =   ["Robot Conf",      "Ball Conf"]
average =   [0.358617174915292, 0.403477753707715]
sd =        [0.279794203820386, 0.445602823413386]
conc =      ["velocity_history",        "velocity_history"]

channel +=  ["Robot Conf",      "Ball Conf"]
average +=  [0.418033383325001, 0.535289951674721]
sd +=       [0.283385570327668, 0.447000356294705]
conc +=     ["velocity_demo",        "velocity_demo"]

channel +=  ["Robot Conf",      "Ball Conf"]
average +=  [0.347603732711215, 0.425208298616897]
sd +=       [0.278568283154208, 0.458753657516472]
conc +=     ["velocity_base",        "velocity_base"]

channel +=  ["Robot Conf",      "Ball Conf"]
average +=  [0.420483252791201, 0.615718213631062]
sd +=       [0.285841348757463, 0.458612491485986]
conc +=     ["position_history",   "position_history"]

channel +=  ["Robot Conf",      "Ball Conf"]
average +=  [0.423617174915292, 0.535236627228795]
sd +=       [0.286657712874037, 0.437375409257827]
conc +=     ["position_demo",   "position_demo"]

channel +=  ["Robot Conf",         "Ball Conf"]
average +=  [0.447875354107649,    0.635989001833028]
sd +=       [0.447875354107649,    0.423879597952317]
conc +=     ["position_demo_ball", "position_demo_ball"]

channel +=  ["Robot Conf",      "Ball Conf"]
average +=  [0.389670054990835, 0.476028161973004]
sd +=       [0.298856520864028, 0.473408556037963]
conc +=     ["position_base",   "position_base"]

channel +=  ["Robot Conf",      "Ball Conf"]
average +=  [0.526578070321613, 0.554438426928845]
sd +=       [0.260823445543461, 0.452704261696712]
conc +=     ["pattern_base",    "pattern_base"]

channel +=  ["Robot Conf",      "Ball Conf"]
average +=  [0.406240071099261, 0.471380603232795]
sd +=       [0.260519333125335, 0.474351891529418]
conc +=     ["abs_base",        "abs_base"]


df = pd.DataFrame({"Metric": channel,
                  "Confidence": average,
                  "sd" : np.array(sd),
                  "Trial": conc})

g = sns.barplot(x="Trial", y="Confidence", hue="Metric", data=df, ci=None)
g.set_xticklabels(g.get_xticklabels(), rotation=45)


num = len(df["Trial"]) // 2
conc2 = np.array([[i,i] for i in range(num)]).flatten()
width = .25
add = [-0.8*width, 0.8*width] * num
x = np.array(conc2)+np.array(add)

plt.errorbar(x = x, y = df['Confidence'],
            yerr=df['sd'], fmt='none', c= 'black', capsize = 2)

plt.savefig("test.png", dpi=600, format="png")

plt.show()
