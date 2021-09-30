import pandas as pd
import matplotlib.pyplot as plt

data_user = pd.read_csv("mem_change_user_side.csv")
data_aws = pd.read_csv("mem_change_aws_side.csv")

fig, axs = plt.subplots(2, sharex=True)
axs[0].plot(data_user['Request Duration'], "-x", color="#0065bd")
axs[0].set_ylabel('Duration (ms)')

axs[1].plot(data_aws['Allocated Memory'], "-^", color="red")
axs[1].set_xlabel('Time (in minutes)')
axs[1].set_ylabel('Allocated Memory (MB)')

axs[0].grid(axis="both", color="0.9", linestyle='-', linewidth=1)
axs[1].grid(axis="both", color="0.9", linestyle='-', linewidth=1)
plt.subplots_adjust(hspace=0.0)
plt.savefig("../images/5_user_side.pdf", format='pdf', dpi=300, bbox_inches='tight')
plt.show()

