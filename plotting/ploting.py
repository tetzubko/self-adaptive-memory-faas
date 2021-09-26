import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pylab import rcParams

values = [[11713.2, 128, 2.4407380500000003e-05], [5780, 256, 2.4088150000000004e-05], [4007, 384, 2.5048758750000002e-05], [2997, 512, 2.4979995e-05], [2306, 640, 2.4025637500000002e-05], [1927, 768, 2.40923175e-05], [1732, 896, 2.5263385000000002e-05], [1439, 1024, 2.3988130000000004e-05], [1140, 1152, 2.1379275000000002e-05], [1075, 1280, 2.24003125e-05], [1119, 1408, 2.5648878750000005e-05], [895, 1536, 2.2379475000000003e-05], [895, 1664, 2.4244431250000005e-05], [836, 1792, 2.4388210000000002e-05], [891, 1920, 2.784931875e-05], [815, 2048, 2.71721e-05], [818, 2176, 2.89766275e-05], [855, 2304, 3.2068912500000005e-05]]
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
ax2.set(ylim=(0.0, 0.00006))
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