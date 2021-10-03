import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 4, 3, 4, 1, 2, 2, 4, 5, 4, 5,4,6,5,6,7,5,7,4,6,5,6])

plt.xticks(np.arange(0, 30, 1.0))
plt.plot(ypoints, linestyle = 'dotted', color="#0065bd")
plt.show()