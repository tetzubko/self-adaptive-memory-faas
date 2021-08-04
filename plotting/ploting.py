import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pylab import rcParams

values = [[1190.8, 128, 2.4813295e-06], [1078, 256, 4.492565e-06], [1021, 384, 6.3825262500000004e-06], [1021, 512, 8.510035e-06], [987, 640, 1.028330625e-05], [971, 768, 1.21399275e-05], [1021, 896, 1.4892561250000003e-05], [959, 1024, 1.5986530000000002e-05]]
df = pd.DataFrame(np.array(values), columns=['duration', 'memory', 'cost'])
df.sort_values(by=['memory'], inplace=True)
print(df)

fig = plt.figure()

rcParams['figure.figsize'] = 6, 4
rcParams['axes.labelsize'] = 14
rcParams['axes.titlesize'] = 20
rcParams["font.size"] = 12

ax1 = fig.add_subplot(1, 1, 1)
ax2 = ax1.twinx()
line1 = ax1.plot(df["memory"], df["duration"], "--b", label='Duration')
ax1.legend(['Duration'], loc='upper left')
# ax1.plot(1536, 172, 'g*')
line2 = ax2.plot(df["memory"], df["cost"], "-.r", label='Cost')
ax2.legend(['Cost'], loc='upper right')
ax2.set(ylim=(0.0, 0.00004))
ax2.ticklabel_format(style='plain')
# plt.plot(1812,6.194598046875001e-07, 'g*')

plt.xticks(df["memory"])
plt.grid(axis="both", color="0.9", linestyle='-', linewidth=1)

ax1.set_ylabel('Request Durations (ms)', color='blue')
ax2.set_ylabel('Request Cost ($)', color='red')
ax1.set_xlabel('Memory (MB)')
plt.show()
fig.savefig("../../pictures/3_network_intensive.png", format='png', dpi=300, bbox_inches='tight')