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

linear = [17, 14, 16, 12]
binary = [46, 56, 51, 55]
gd = [66, 29, 64, 27]
ax.set_ylabel('Number of iterations', fontsize = 12.0)

# linear = [144529, 6235, 7880, 41062]
# binary = [205493, 16758, 17701, 145622]
# gd = [249552, 43681, 38649, 64170]
# ax.set_ylabel('Execution Duration (ms)', fontsize = 12.0)


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
fig.savefig("../../images/4_iterations_per_algorithm_duration.pdf", format='pdf', dpi=300, bbox_inches='tight')



