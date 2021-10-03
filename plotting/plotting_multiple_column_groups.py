import pandas as pd
import matplotlib.pyplot as plt
from pylab import rcParams
import numpy as np

rcParams['figure.figsize'] = 10, 8
rcParams['axes.labelsize'] = 14
rcParams['axes.titlesize'] = 14
rcParams["font.size"] = 12

data_iterations_2=[["CPU-Intensive",18,8],
      ["I/O-Intensive",11,4],
      ["Memory-Intensive",13,9],
      ["Network-Intensive",9,3]
     ]

# data_iterations_3 = [["CPU-Intensive",17,46,66],
#       ["I/O-Intensive",14,56,29],
#       ["Memory-Intensive",16,51,64],
#       ["Network-Intensive",12,55,27]
#      ]

# df=pd.DataFrame(data_iterations_3,columns=["Function Type", "Linear", "Binary", "Gradient Descent"])
# ax = df.plot(x="Function Type", y=["Linear", "Binary", "Gradient Descent"], kind="bar", color=["#0065bd", "#e37222", "#a2ad00"])
df=pd.DataFrame(data_iterations_2,columns=["Function Type", "Optimization Values","Duration Change"])
ax = df.plot(x="Function Type", y=["Optimization Values", "Duration Change"], kind="bar")
plt.xticks(rotation=0)
plt.yticks(np.arange(0, 25, 5))
plt.legend(loc='best')
plt.ylabel('Iterations')

rects = ax.patches
for rect in rects:
    height = rect.get_height()
    ax.text(
        rect.get_x() + rect.get_width() / 2, height + 0.4, height, ha="center", va="bottom"
    )

plt.savefig("../../images/4_iterations_per_algorithm_balanced.png", format='png', dpi=300, bbox_inches='tight')

plt.show()

