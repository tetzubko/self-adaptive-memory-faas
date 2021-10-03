import matplotlib.pyplot as plt
import numpy as np

N = 3
correct = (16, 0, 12)
wrong = (4, 20, 8)
ind = np.arange(N)   # the x locations for the groups
width = 0.4     # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()

p1 = ax.bar(ind, correct, width, label='Correct', color="#60B217", align="center")
p2 = ax.bar(ind, wrong, width, bottom=correct, label='Wrong', color="#F04827", align="center")

ax.axhline(0, color='grey', linewidth=0.8)
ax.set_ylabel('Iterations')
ax.set_title('Accuracy of Algorithms')
ax.set_xticks(ind)
ax.set_xticklabels(('Linear', 'Binary', 'Gradient Descent'))
ax.legend(bbox_to_anchor=(1, 1), loc='upper left')

# Label with label_type 'center' instead of the default 'edge'
# ax.bar_label(p1, label_type='center')
ax.bar_label(p2, label_type='center')

plt.text(0, 8, '16', ha="center")
plt.text(2, 6, '12', ha="center")

plt.show()
fig.savefig("../../images/5_accuracy_duration.png", format='png', dpi=300, bbox_inches='tight')