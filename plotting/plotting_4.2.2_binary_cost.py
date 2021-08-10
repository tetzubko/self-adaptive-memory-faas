import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

#plot 1:
x = np.array([1000, 2000, 3000, 4000])
y = np.array([3.0000000e-06, 3.0000000e-06, 6.0000000e-06, 7.0000000e-06])

ax1 = plt.subplot(2, 2, 1)
ax1.axvline(x=2500, color="#999999")
ax1.set_ylabel('Cost ($)')
# ax1.set_xlabel('Memory (MB)')
ax1.text(1000,6.8000000e-06, '1', weight='bold')
ax1.plot(2000, 3.0000000e-06, 'b*', label='Min cost')
ax1.axvspan(1000, 2500, alpha=0.5, color="0.9", hatch = '/')
ax1.legend(bbox_to_anchor=(0.04,1.2), loc="upper left")
plt.plot(x,y, color="#0065bd")


#plot 2:
x = np.array([1000, 2000, 3000, 4000])
y = np.array([3.5000000e-06, 2.0000000e-06, 3.0000000e-06, 5.0000000e-06])

ax2 = plt.subplot(2, 2, 2)
ax2.axvline(x=2500, color="#999999")
ax2.set_ylabel('Cost ($)')
# ax2.set_xlabel('Memory (MB)')
ax2.text(1000, 4.8500000e-06, '2', weight='bold')
ax2.plot(2000, 2.0000000e-06, 'b*')
ax2.axvspan(2500, 4000, alpha=0.5, color="0.9", hatch = '/')
plt.plot(x,y,color="#a2ad00")

#plot 3:
x = np.array([1000, 2000, 3000, 4000])
y = np.array([3.0000000e-06, 4.0000000e-06, 4.0000000e-06, 2.0000000e-06])

ax3 = plt.subplot(2, 2, 3)
ax3.axvline(x=2500, color="#999999")
ax3.set_ylabel('Cost ($)')
ax3.set_xlabel('Memory (MB)')
ax3.text(1000, 3.9000000e-06, '3', weight='bold')
ax3.plot(4000, 2.0000000e-06, 'b*')
ax3.axvspan(1000, 2500, alpha=0.5, color="0.9", hatch = '/')
plt.plot(x,y,color="#e37222")

#plot 4:
x = np.array([1000, 2000, 3000, 4000])
y = np.array([4.0000000e-06, 4.0000000e-06, 4.0000000e-06, 3.0000000e-06])

ax4 = plt.subplot(2, 2, 4)
ax4.axvline(x=2500, color="#999999")
ax4.set_ylabel('Cost ($)')
ax4.set_xlabel('Memory (MB)')
ax4.text(1000, 3.9500000e-06, '4', weight='bold')
ax4.plot(4000, 3.0000000e-06, 'b*')
ax4.axvspan(1000, 2500, alpha=0.5, color="0.9", hatch = '/')
plt.plot(x,y,color="#64a0c8")
plt.show()
fig.savefig("../../images/4_binary_cost.png", format='png', dpi=300, bbox_inches='tight')