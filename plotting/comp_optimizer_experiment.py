import pandas as pd
import matplotlib.pyplot as plt
from pylab import rcParams
import numpy as np

width = 0.25
labels = ["1", "2", "3", "4"]
x = np.arange(len(labels))


plt.rcParams['xtick.labelsize']=9
plt.rcParams['ytick.labelsize']=9

fig, ax = plt.subplots(figsize=(8,5))
plt.figure(figsize=(8, 5))
ax.grid(axis="both", color="0.9", linestyle='-', linewidth=1)
ax.set_axisbelow(True)

initial_memories = [128, 256, 512, 1024]
recomended_memories = [160, 320, 624, 1232]

ax.set_ylabel('Memory (MB)', fontsize = 12.0)

p1 = ax.bar(x - width, initial_memories, width=width, capsize=2, ecolor='blue', edgecolor='black', label='Initial Memory', color = 'w', hatch = 'oo' )
p2 = ax.bar(x, recomended_memories, width=width, capsize=2, ecolor='blue', edgecolor='black', label='Recommended Memory', color = 'w', hatch = '////' )

ax.set_xlabel('Experiment', fontsize = 12.0)
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize = 10.0)
ax.legend(fontsize = 10.0)
#ax.title.set_size(20)


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize = 9.0)


autolabel(p1)
autolabel(p2)
fig.tight_layout()

plt.show()
fig.savefig("../../images/6_comp_optimizer_experiment.png", format='png', dpi=300, bbox_inches='tight')

