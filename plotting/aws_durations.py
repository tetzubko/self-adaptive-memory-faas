import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("durations_aws_comp_optimizer.csv")
data.plot()
plt.legend(bbox_to_anchor=(1, 1), loc='upper left', title='Allocated Memory')

plt.xlabel('Hours of Experiment')
plt.ylabel('Duration (ms)')

plt.savefig("../../images/6_durations_with_different_memories.png", format='png', dpi=300, bbox_inches='tight')
plt.show()