import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pylab import rcParams

rcParams['figure.figsize'] = 6, 4
rcParams['axes.labelsize'] = 14
rcParams['axes.titlesize'] = 20
rcParams["font.size"] = 12

values1 = [[21.200000000000003, 128, 4.417550000000001e-08], [3, 256, 1.25025e-08], [3, 384, 1.875375e-08], [2, 512, 1.667e-08], [3, 640, 3.1256250000000006e-08], [3, 768, 3.75075e-08], [3, 896, 4.375875e-08], [3, 1024, 5.001e-08], [3, 1152, 5.6261250000000004e-08], [3, 1280, 6.251250000000001e-08], [3, 1408, 6.876375e-08], [3, 1536, 7.5015e-08]]
df1 = pd.DataFrame(np.array(values1), columns=['duration', 'memory', 'cost'])

values2 = [[268.4, 128, 5.592785e-07], [196, 256, 8.1683e-07], [85, 384, 5.3135625e-07], [46, 512, 4.959325e-07], [44, 640, 7.188937500000001e-07], [39, 768, 7.876575000000001e-07], [34, 896, 4.959325e-07], [25, 1024, 4.1675e-07], [23, 1152, 4.3133625e-07], [20, 1280, 4.1675e-07], [28, 1408, 6.41795e-07], [21, 1536, 5.25105e-07]]
df2 = pd.DataFrame(np.array(values2), columns=['duration', 'memory', 'cost'])

values3 = [[8001.6, 128, 1.6673334e-05], [4087, 256, 1.70325725e-05], [2631, 384, 1.644703875e-05], [2024, 512, 1.6870040000000002e-05], [1592, 640, 1.658665e-05], [1341, 768, 1.67658525e-05], [1141, 896, 1.664291125e-05], [991, 1024, 1.6519970000000002e-05], [940, 1152, 1.7628525000000004e-05], [801, 1280, 1.66908375e-05], [738, 1408, 1.69158825e-05], [678, 1536, 1.6953390000000002e-05]]
df3 = pd.DataFrame(np.array(values3), columns=['duration', 'memory', 'cost'])

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.plot(df1["memory"], df1["duration"], "--b", label='Base 3')
ax1.plot(df2["memory"], df2["duration"], "-.r", label='Base 6')
ax2.plot(df3["memory"], df3["duration"], "-g", label='Base 9')

ax1.legend(['CPU-Bound, base 3', 'CPU-Bound, base 6'], loc='upper right')
ax2.legend(['CPU-Bound, base 9'], loc='upper left')

ax1.set_xlabel('Memory, MB')
ax1.set_ylabel('Duration, s')
ax2.set_ylabel('Duration, s', color='g')

plt.show()
fig.savefig("../../pictures/durations_changing_inputs.png", format='png', dpi=300, bbox_inches='tight')