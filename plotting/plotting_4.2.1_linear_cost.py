import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pylab import rcParams

values = [[5023.8, 128, 1.0468343250000001e-05], [2613, 256, 1.0468343250000001e-05], [1613, 384, 1.0468383250000001e-05], [1248, 512, 1.008326625e-05], [903, 640, 1.0402080000000002e-05], [781, 768, 9.40813125e-06], [682, 896, 9.764452500000001e-06], [635, 1024, 9.9478225e-06], [592, 1152, 1.0585450000000002e-05], [526, 1280, 1.1102220000000002e-05], [477, 1408, 1.0960525000000001e-05], [529, 1536, 1.0933436250000002e-05], [471, 1664, 1.3227645000000002e-05], [423, 1792, 1.2758801250000002e-05], [429, 1920, 1.2339967500000002e-05]]
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
line1 = ax1.plot(df["memory"], df["duration"], "--b", label='Duration', linewidth=2)
ax1.legend(['Duration'], loc='upper left')
# ax1.plot(1536, 172, 'g*')
line2 = ax2.plot(df["memory"], df["cost"], "-.r", label='Cost', linewidth=2)
ax2.legend(['Cost'], loc='upper right')
ax2.set(ylim=(0.0, 0.00002))
ax2.ticklabel_format(style='plain')

#annotations
plt.text(503,0.900000625e-05, 'A', fontsize=12)
plt.text(640,1.0498080000000002e-05, 'B', fontsize=12)
plt.text(760,8.50813125e-06, 'C', fontsize=12)
plt.text(1024,9.0478225e-06, 'D', fontsize=12)
plt.text(1280,1.1302220000000002e-05, 'E', fontsize=12)

#grid
plt.xticks(df["memory"])
plt.grid(axis="both", color="0.9", linestyle='-', linewidth=1)
# ax1.grid(axis="x", color="0.9", linestyle='-', linewidth=1)
# ax1.grid(axis="y", color="0.7", linestyle='--', linewidth=1)

ax1.set_ylabel('Request Durations (ms)', color='blue')
ax2.set_ylabel('Request Cost ($)', color='red')
ax1.set_xlabel('Memory (MB)')
plt.show()
fig.savefig("../../images/4_linear_cost.png", format='png', dpi=300, bbox_inches='tight')