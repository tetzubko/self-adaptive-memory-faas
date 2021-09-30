import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pylab import rcParams

values = [[127.4, 128, 2.6546975000000005e-07], [49, 256, 2.042075e-07], [49, 384, 3.0631125000000003e-07], [21, 512, 1.75035e-07], [14, 640, 1.458625e-07], [17, 768, 2.125425e-07], [8, 896, 1.1669000000000001e-07], [9, 1024, 1.5003e-07], [10, 1152, 1.8753750000000003e-07], [9, 1280, 1.8753750000000003e-07], [14, 1408, 3.208975e-07], [9, 1536, 2.2504500000000001e-07], [12, 1664, 3.2506500000000006e-07], [84, 1792, 2.4504900000000002e-06], [20, 1920, 6.25125e-07], [28, 2048, 9.335200000000001e-07], [85, 2176, 3.0110187500000005e-06], [10, 2304, 3.7507500000000007e-07], [11, 2432, 4.3550375000000005e-07], [11, 2560, 4.5842500000000003e-07], [10, 2688, 4.3758750000000003e-07], [10, 2816, 4.5842500000000003e-07], [9, 2944, 4.3133625e-07], [16, 3072, 8.0016e-07], [10, 3200, 5.209375e-07], [12, 3328, 6.501300000000001e-07]]
df = pd.DataFrame(np.array(values), columns=['duration', 'memory', 'cost'])
df.sort_values(by=['memory'], inplace=True)
print(df)

fig = plt.figure()

rcParams['figure.figsize'] = 6, 4
rcParams['axes.labelsize'] = 12
rcParams['axes.titlesize'] = 20
rcParams["font.size"] = 10

ax1 = fig.add_subplot(1, 1, 1)
ax2 = ax1.twinx()
line1 = ax1.plot(df["memory"], df["duration"], "-x", color="#0065bd", label='Duration')
ax1.legend(['Duration'], loc='upper left')
# ax1.plot(1536, 172, 'g*')
line2 = ax2.plot(df["memory"], df["cost"], "-^", color="#e37222", label='Cost')
ax2.legend(['Cost'], loc='upper right')
ax2.set(ylim=(0.0, 0.000006))
# ax2.ticklabel_format(style='plain')
# plt.plot(1812,6.194598046875001e-07, 'g*')

plt.xticks(df["memory"])
#plt.grid(axis="both", color="0.9", linestyle='-', linewidth=1)

ax1.set_ylabel('Duration (ms)', color='#0065bd')
ax2.set_ylabel('Cost ($)', color='#e37222')
ax1.set_xlabel('Memory (MB)')
ax1.set_xticklabels(df["memory"], rotation=90, ha='center')

plt.show()
fig.savefig("../images/5_cpu_intensive.png", format='png', dpi=300, bbox_inches='tight')
