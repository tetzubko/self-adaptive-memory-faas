import pandas as pd
import matplotlib.pyplot as plt
from pylab import rcParams
import numpy as np

width = 0.3
labels = ["CPU-Intensive", "I/O-Intensive", "Memory-Intensive", "Network-Intensive"]
x = np.arange(len(labels))


plt.rcParams['xtick.labelsize']=9
plt.rcParams['ytick.labelsize']=9

fig, ax = plt.subplots(figsize=(8,5))
plt.figure(figsize=(8, 5))
ax.grid(axis="both", color="0.9", linestyle='-', linewidth=1)
ax.set_axisbelow(True)

opt_vals = [18, 11, 13, 9]
due_change = [8, 4, 9, 3]



p1 = ax.bar(x - width, opt_vals, width=width, capsize=2, ecolor='blue', edgecolor='black', label='Optimization Values', color = 'w', hatch = 'xxx' )
p2 = ax.bar(x, due_change, width=width, capsize=2, ecolor='blue', edgecolor='black', label='Duration Change', color = 'w', hatch = '---' )
#p3 = ax.bar(x + width, gd, width=width, capsize=2, ecolor='blue', edgecolor='black', label='Gradient Descent', color = 'w', hatch = '++' )


ax.set_ylabel('Number of iterations', fontsize = 12.0)
ax.set_xticks(x-0.15)
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

#plt.show()
fig.savefig("../images/4_iterations_per_algorithm_balanced.pdf", format='pdf', dpi=300, bbox_inches='tight')



