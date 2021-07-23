import pandas as pd
import matplotlib.pyplot as plt
from pylab import rcParams
import numpy as np

rcParams['figure.figsize'] = 10, 8
rcParams['axes.labelsize'] = 14
rcParams['axes.titlesize'] = 14
rcParams["font.size"] = 12

data_iterations=[["CPU-Intensive",23,14],
      ["I/O-Intensive",48,17],
      ["Memory-Intensive",20,17],
      ["Network-Intensive",15,17]
     ]

# data_allocated_memory = [["CPU-Intensive",460,606,1024],
#       ["I/O-Intensive",832,2600,690],
#       ["Memory-Intensive",1024,1812,1028],
#       ["Network-Intensive",128,130,275]
#      ]

df=pd.DataFrame(data_iterations,columns=["Function Type", "Optimization Values","Duration Change"])
df.plot(x="Function Type", y=["Optimization Values", "Duration Change"], kind="bar")
plt.xticks(rotation=0)
plt.yticks(np.arange(0, 60, 5))
plt.legend(loc='best')

plt.savefig("../pictures/balanced/4_iterations_per_algorithm_balanced.png", format='png', dpi=300, bbox_inches='tight')

plt.show()

