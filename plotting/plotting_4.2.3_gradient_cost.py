import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
x = np.linspace(0.0, 2.0)
y = np.cos(2 * np.pi * x) * np.exp(-x)

plt.plot(x, y, "-.", color='#0065bd')
plt.axhline(0, color='#999999')

plt.annotate('Local Min', xy=(1.5, -0.24), xytext=(1.5, -0.5), color='#0065bd',
            arrowprops=dict(facecolor='#0065bd', width=0.01, headwidth=8))

plt.annotate('Global Min', xy=(0.55, -0.6), xytext=(0.8, -0.6), color='#0065bd',
            arrowprops=dict(facecolor='#0065bd', width=0.01, headwidth=8))

plt.annotate('Local Max', xy=(0.98, 0.4), xytext=(0.98, 0.8), color='#e37222',
            arrowprops=dict(facecolor='#e37222', width=0.01, headwidth=8))

plt.annotate('Global Max', xy=(0.02, 1), xytext=(0.2, 0.9), color='#e37222',
            arrowprops=dict(facecolor='#e37222', width=0.01, headwidth=8))

plt.show()
fig.savefig("../../images/4_gradient_descent_local_min.png", format='png', dpi=300, bbox_inches='tight')