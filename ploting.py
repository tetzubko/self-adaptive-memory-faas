import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pylab import rcParams

values = [[2039.0, 128, 4.24876625e-06], [1004, 256, 4.18417e-06], [683, 384, 4.269603750000001e-06], [654, 512, 5.45109e-06], [404, 640, 4.209175000000001e-06], [357, 768, 4.463392500000001e-06], [429, 896, 6.25750125e-06], [251, 1024, 4.18417e-06], [222, 1152, 4.1633325e-06], [210, 1280, 4.375875000000001e-06], [258, 1408, 5.9136825e-06], [178, 1536, 4.450890000000001e-06], [168, 1664, 4.55091e-06], [164, 1792, 4.78429e-06], [160, 1920, 5.001e-06], [169, 2048, 5.634460000000001e-06], [157, 2176, 5.56152875e-06], [171, 2304, 6.413782500000001e-06], [178, 2432, 7.0472425000000005e-06], [156, 2560, 6.501300000000001e-06], [153, 2688, 6.6950887500000006e-06], [155, 2816, 7.105587500000001e-06], [167, 2944, 8.00368375e-06], [156, 3072, 7.80156e-06], [150, 3200, 7.8140625e-06], [154, 3328, 8.343335000000001e-06], [153, 3456, 8.607971250000001e-06], [168, 3584, 9.801960000000001e-06]]
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
ax2.set(ylim=(0.0, 0.00002))
ax2.ticklabel_format(style='plain')
# plt.plot(1812,6.194598046875001e-07, 'g*')

plt.xticks(df["memory"])
plt.grid(axis="both", color="0.9", linestyle='-', linewidth=1)

ax1.set_ylabel('Request Durations (ms)', color='blue')
ax2.set_ylabel('Request Cost ($)', color='red')
ax1.set_xlabel('Memory (MB)')
plt.show()
# fig.savefig("../pictures/3_network_intensive.png", format='png', dpi=300, bbox_inches='tight')