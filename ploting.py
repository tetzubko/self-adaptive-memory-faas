import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pylab import rcParams

values = [[298.6, 896, 4.355454250000001e-06], [252.0, 1024, 4.20084e-06], [253.8, 1027, 4.2432410566406256e-06], [233.8, 1155, 4.396045048828125e-06], [333.8, 850, 4.61892490234375e-06], [261.2, 978, 4.158604992187501e-06], [296.40000000000003, 999, 4.8203584101562515e-06], [241.6, 1127, 4.4325790468750004e-06], [268.6, 1175, 5.137827490234375e-06], [211.2, 1303, 4.4799583125e-06], [213.40000000000003, 1373, 4.769804681640626e-06], [179.0, 1501, 4.373905205078125e-06], [201.60000000000002, 1541, 5.057417531250001e-06], [178.8, 1669, 4.85802219140625e-06]]
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
line2 = ax2.plot(df["memory"], df["cost"], "-.r", label='Cost')
ax2.legend(['Cost'], loc='upper right')
ax2.set(ylim=(0.0, 0.00002))
ax2.ticklabel_format(style='plain')

plt.xticks(df["memory"])
plt.grid(axis="both", color="0.9", linestyle='-', linewidth=1)

plt.plot(850, 4.61892490234375e-06, 'g*')

ax1.set_ylabel('Request Durations (ms)', color='blue')
ax2.set_ylabel('Request Cost ($)', color='red')
ax1.set_xlabel('Memory (MB)')
plt.show()
# fig.savefig("../pictures/4_gradient_descent_cost_2.png", format='png', dpi=300, bbox_inches='tight')