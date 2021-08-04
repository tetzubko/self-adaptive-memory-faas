import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Minimum (128 MB)', 'MAFF (768 MB)', 'Maximum (2304 MB)')
y_pos = np.arange(len(objects))
performance = [4.33878425e-06,4.1633325e-06,6.301260000000001e-06]

plt.bar(y_pos, performance, align='center', alpha=0.5, color = 'orange')
plt.xticks(y_pos, objects)
plt.ylabel('Cost ($)')
plt.title('Execution Cost Depending on the Allocated Memory')

plt.show()