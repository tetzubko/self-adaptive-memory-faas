import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

values = [[323.8, 128, 6.747182500000001e-07], [142, 256, 5.91785e-07], [141, 384, 8.8142625e-07], [61, 512, 5.08435e-07], [53, 640, 5.5219375e-07], [50, 768, 6.25125e-07], [75, 896, 1.0939687500000002e-06], [25, 1024, 4.1675e-07], [21, 1152, 3.9382875000000005e-07], [31, 1280, 6.459625000000001e-07], [43, 1408, 9.8561375e-07], [54, 1536, 1.3502700000000002e-06], [25, 1664, 6.772187500000001e-07], [26, 1792, 7.58485e-07], [21, 1920, 6.5638125e-07], [37, 2048, 1.2335800000000002e-06], [25, 2176, 8.855937500000001e-07], [23, 2304, 8.626725e-07], [25, 2432, 9.8978125e-07], [24, 2560, 1.0002000000000002e-06], [40, 2688, 1.7503500000000001e-06], [24, 2816, 1.10022e-06], [23, 2944, 1.10230375e-06], [25, 3072, 1.25025e-06]]
df = pd.DataFrame(np.array(values), columns=['duration', 'memory', 'cost'])
df.sort_values(by=['memory'], inplace=True)
print(df)

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax2 = ax1.twinx()
line1 = ax1.plot(df["memory"], df["duration"], "-b", label='Duration')
ax1.legend(['Duration'], loc='upper left')
line2 = ax2.plot(df["memory"], df["cost"], "-r", label='Cost')
ax2.legend(['Cost'], loc='upper right')
ax2.set(ylim=(0.0, 0.00006))
ax2.ticklabel_format(style='plain')

plt.xticks(df["memory"])

ax1.set_ylabel('Request Durations (ms)', color='blue')
ax2.set_ylabel('Request Cost ($)', color='red')
ax1.set_xlabel('Memory (MB)')
plt.show()