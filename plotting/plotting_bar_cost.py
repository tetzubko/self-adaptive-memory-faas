import pandas as pd
import matplotlib.pyplot as plt
from pylab import rcParams
import numpy as np

width = 0.25
labels = ["CPU-Intensive", "I/O-Intensive", "Memory-Intensive", "Network-Intensive"]
x = np.arange(len(labels))


plt.rcParams['xtick.labelsize']=9
plt.rcParams['ytick.labelsize']=9

fig, ax = plt.subplots(figsize=(8,5))
plt.figure(figsize=(8, 5))
ax.grid(axis="both", color="0.9", linestyle='-', linewidth=1)
ax.set_axisbelow(True)

# linear = [15, 16, 17, 9]
# binary = [64, 31, 53, 53]
# gd = [38, 19, 22, 13]
# ax.set_ylabel('Number of iterations', fontsize = 12.0)

linear = [196906, 9464, 12182, 43589]
binary = [447145, 18938, 21589, 168829]
gd = [156390, 5570, 5473, 41048]
ax.set_ylabel('Execution Duration (ms)', fontsize = 12.0)

p1 = ax.bar(x - width, linear, width=width, capsize=2, ecolor='blue', edgecolor='black', label='Linear', color = 'w', hatch = 'oo' )
p2 = ax.bar(x, binary, width=width, capsize=2, ecolor='blue', edgecolor='black', label='Binary', color = 'w', hatch = '////' )
p3 = ax.bar(x + width, gd, width=width, capsize=2, ecolor='blue', edgecolor='black', label='Gradient Descent', color = 'w', hatch = '++' )


ax.set_xlabel('Function Type', fontsize = 12.0)
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
autolabel(p3)
fig.tight_layout()

plt.show()
fig.savefig("../../images/5_duration_per_algorithm_cost.pdf", format='pdf', dpi=300, bbox_inches='tight')



