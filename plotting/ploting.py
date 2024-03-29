import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pylab import rcParams

values = [[10677.8, 128, 2.224986575e-05], [5371, 256, 2.2383642500000003e-05], [3527, 384, 2.2048158750000002e-05], [2607, 512, 2.1729345000000002e-05], [2259, 640, 2.3535956250000005e-05], [1788, 768, 2.2354470000000002e-05], [1509, 896, 2.201065125e-05], [1469, 1024, 2.4488230000000003e-05], [1289, 1152, 2.4173583750000002e-05], [1156, 1280, 2.4088150000000004e-05], [1070, 1408, 2.45257375e-05], [986, 1536, 2.4654930000000002e-05], [929, 1664, 2.5165448750000003e-05], [891, 1792, 2.5992697500000003e-05], [869, 1920, 2.7161681250000005e-05]]
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
ax2.set(ylim=(0.0, 0.00004))
# ax2.ticklabel_format(style='plain')
# plt.plot(1812,6.194598046875001e-07, 'g*')

plt.xticks(df["memory"])
#plt.grid(axis="both", color="0.9", linestyle='-', linewidth=1)

ax1.set_ylabel('Duration (ms)', color='#0065bd')
ax2.set_ylabel('Cost ($)', color='#e37222')
ax1.set_xlabel('Memory (MB)')
ax1.set_xticklabels(df["memory"], rotation=90, ha='center')

plt.show()
# fig.savefig("../images/5_cpu_intensive.png", format='png', dpi=300, bbox_inches='tight')
