import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

values = [[189.8, 2528, 468.56875], [182.4, 2656, 473.1], [151.4, 2323, 343.4591796875], [180.4, 2451, 431.797265625], [152.6, 2140, 318.91015625], [160.2, 2268, 354.81796875], [151.20000000000002, 1944, 287.04375000000005], [167.0, 2072, 337.9140625], [163.8, 1763, 282.0111328125], [174.60000000000002, 1891, 322.43027343750003], [194.8, 1549, 294.673046875], [172.6, 1677, 282.6662109375], [181.0, 1757, 310.5634765625], [174.60000000000002, 1885, 321.40722656250006], [167.0, 1603, 261.4267578125], [168.4, 1731, 284.668359375]]
df = pd.DataFrame(np.array(values), columns=['duration', 'memory', 'cost'])
df.sort_values(by=['memory'], inplace=True)
print(df)

plt.plot(df["memory"], df["duration"], label='Duration')
plt.plot(df["memory"], df["cost"], label='Cost')
plt.xticks(df["memory"])
plt.legend()
plt.show()
