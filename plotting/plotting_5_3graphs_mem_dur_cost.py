import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pylab import rcParams
import matplotlib.lines as mlines

red_X = mlines.Line2D([], [], color='red', marker='X', label='Result')

values = [[11908.400000000001, 128, 2.4814128500000005e-05], [5570, 256, 2.3212975e-05], [3923, 384, 2.4523653750000002e-05], [2976, 512, 2.480496e-05], [2221, 640, 2.3140043750000003e-05], [1767, 768, 2.2091917500000002e-05], [1674, 896, 2.44173825e-05], [1343, 1024, 2.238781e-05], [1282, 1152, 2.4042307500000002e-05], [1147, 1280, 2.39006125e-05], [995, 1408, 2.280664375e-05], [897, 1536, 2.2429485e-05]]
df = pd.DataFrame(np.array(values), columns=['duration', 'memory', 'cost'])
# df.sort_values(by=['memory'], inplace=True)
print(df)

fig = plt.figure()

rcParams['figure.figsize'] = 6, 4
rcParams['axes.labelsize'] = 12
rcParams['axes.titlesize'] = 20
rcParams["font.size"] = 10

# plt.plot( df["memory"], "-x", color="#0065bd", label='Memory', linewidth=3.0)
# plt.ylabel('Memory(MB)', color='#0065bd')
# plt.plot( df["duration"], "-x", color="#e37222", label='Duration', linewidth=3.0)
# plt.ylabel('Duration(ms)', color='#e37222')
plt.plot( df["cost"], "-x", color="#a2ad00", label='Cost', linewidth=3.0)
plt.ylabel('Cost($)', color='#a2ad00')


plt.xlabel('Iterations')
plt.xticks(np.arange(0, len(values)+1, 1.0), rotation=90, ha='center')

plt.plot(5, 2.2091917500000002e-05, 'rX', markersize=10)
plt.legend(handles=[red_X])

plt.show()
fig.savefig("../../images/5_balanced_duration_change_cpu_cost.png", format='png', dpi=300, bbox_inches='tight')
