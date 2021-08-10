import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fig = plt.figure()
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

memories=[128, 256, 384, 512, 640, 768, 896, 1024, 1152]
y=[1/128, 1/256, 1/384, 1/512, 1/640, 1/768, 1/896, 1/1024, 1/1152]
durations=[1/120, 1/200, 1/300, 1/300, 1/600, 1/700, 1/800, 1/900, 1/1000]


plt.plot(memories, durations, "-.", color='#98c6ea', label='Duration')
plt.plot(memories, y, color='#0065bd', label='Hyperbola')

# line 1
x2, y2 = [128, 1152], [1/128, 1/1152]
plt.plot(x2, y2, "--", color='#999999')
# line 2
x2, y2 = [385, 550], [0.00254, 0.00489]
plt.plot(x2, y2, "--", color='#999999')

# axes names
plt.xlabel('Memory (MB)')
plt.ylabel('Duration (ms)')

plt.legend(loc="upper right")
plt.plot(385,0.00255,'o')
plt.text(350,0.002, 'Vertex')
plt.grid(axis="both", color="0.9", linestyle='-', linewidth=1)


plt.show()
fig.savefig("../../images/4_balanced_on_duration.png", format='png', dpi=300, bbox_inches='tight')