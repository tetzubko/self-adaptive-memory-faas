import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pylab import rcParams
import matplotlib.lines as mlines

red_X = mlines.Line2D([], [], color='red', marker='X', label='Result')

values = [[1458.4, 1024, 2.4311528000000003e-05], [1690.8000000000002, 896, 2.4662431500000006e-05], [1187.6, 1196, 2.3122618390625e-05], [1270.2, 1068, 2.2084064367187504e-05], [1370.0, 1023, 2.281559736328125e-05], [1661.2, 895, 2.420363533203125e-05], [1115.0, 1199, 2.1763547802734376e-05], [1406.1999999999998, 1071, 2.451727552148437e-05], [954.4000000000001, 1452, 2.2559667281250002e-05], [1153.4, 1324, 2.4860140304687504e-05], [901.8, 1657, 2.4325870060546876e-05], [962.2, 1529, 2.395016342382813e-05], [1048.2, 1438, 2.4537973019531252e-05], [1031.6, 1310, 2.19997766796875e-05], [1067.4, 1285, 2.232883010742188e-05], [1303.4, 1157, 2.454972992773438e-05], [977.0, 1433, 2.2791683076171878e-05], [1083.8, 1305, 2.3024770048828127e-05], [1224.4, 1220, 2.4317492734375e-05], [1391.1999999999998, 1092, 2.4731351531250002e-05], [1038.6, 1364, 2.30620724296875e-05], [1220.8000000000002, 1236, 2.456397431250001e-05], [903.0, 1507, 2.2153209052734375e-05], [1109.8, 1379, 2.4914067103515624e-05], [980.4, 1706, 2.72281398515625e-05], [959.0, 1578, 2.4635492519531253e-05]]
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

plt.plot(10, 2.4325870060546876e-05, 'rX', markersize=10)
plt.legend(handles=[red_X])

plt.show()
fig.savefig("../../images/5_duration_gradient_descent_cpu_cost.png", format='png', dpi=300, bbox_inches='tight')
