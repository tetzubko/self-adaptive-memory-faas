import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pylab import rcParams

values = [[4680.8, 128, 0.0000090536], [2484, 256, 0.0000097536], [1821, 384, 0.0000103521], [1218, 512, 0.0000113835], [876, 640, 0.0000155520], [771, 768, 0.0000149268], [663, 896, 0.0000099394], [681, 1024, 0.0000096707], [627, 1152, 0.0000113523], [448, 1280, 0.0000117586], [444, 1408, 0.0000119352], [445, 1536, 0.0000129352], [458, 1664, 0.0000121272], [406, 1792, 0.0000124066], [424, 1920, 0.0000118440], [452, 2048, 0.0000132527]]
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
line1 = ax1.plot(df["memory"], df["duration"], "--", color="#0065bd", label='Duration')
ax1.legend(['Duration'], loc='upper left')
line2 = ax2.plot(df["memory"], df["cost"], "-.", color="#e37222", label='Cost')
ax2.legend(['Cost'], loc='upper right')
ax2.set(ylim=(0.0, 0.00006))

plt.plot(129, 0.0000090536, 'r*')
plt.text(129,0.0000060536, 'A', color="red")
plt.plot(1024, 0.0000096707, 'g*')
plt.text(1022,0.000011007, 'B', color="green")
ax1.plot(1280, 448, 'b*')
ax1.text(1280,500, 'C', color="blue")
# ax2.ticklabel_format(style='plain')
# plt.plot(1812,6.194598046875001e-07, 'g*')

plt.xticks(df["memory"])
plt.grid(axis="both", color="0.9", linestyle='-', linewidth=1)

ax1.set_ylabel('Duration (ms)', color='#0065bd')
ax2.set_ylabel('Cost ($)', color='#e37222')
ax1.set_xlabel('Memory (MB)')
plt.show()
# fig.savefig("../../images/3_optimiz_goals.png", format='png', dpi=300, bbox_inches='tight')
