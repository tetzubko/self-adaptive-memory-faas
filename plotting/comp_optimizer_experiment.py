import pandas as pd
import matplotlib.pyplot as plt
from pylab import rcParams
import numpy as np

rcParams['figure.figsize'] = 10, 8
rcParams['axes.labelsize'] = 14
rcParams['axes.titlesize'] = 14
rcParams["font.size"] = 12

memories=[["1",128,160],
      ["2",256,320],
      ["3",512,624],
      ["4",1024,1232]
     ]

df=pd.DataFrame(memories,columns=["Experiment", "Initial Memory, MB","Recommended Memory, MB"])
ax = df.plot(x="Experiment", y=["Initial Memory, MB","Recommended Memory, MB"], kind="bar")
plt.xticks(rotation=0)
plt.legend(loc='best')

rects = ax.patches
for rect in rects:
    height = rect.get_height()
    ax.text(
        rect.get_x() + rect.get_width() / 2, height + 1, height, ha="center", va="bottom"
    )

plt.savefig("../../images/6_comp_optimizer_experiment.png", format='png', dpi=300, bbox_inches='tight')

plt.show()

