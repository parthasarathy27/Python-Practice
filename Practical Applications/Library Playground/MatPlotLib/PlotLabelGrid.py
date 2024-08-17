# label and grid function

import numpy as np
import matplotlib.pyplot as plt

xpoint = np.array([80, 85, 90, 100, 105, 110, 115, 120, 125])
ypoint= np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family' : 'serif', 'color' : 'blue', 'size' : 15}
font2 = {'family' : 'serif', 'color' : 'darkred', 'size' : 15}

plt.title("Players Data", fontdict= font1)
plt.xlabel("Average Pulse", fontdict= font2)
plt.ylabel("Calorie Burnage", fontdict= font2)

plt.plot(xpoint)
plt.plot(ypoint)

plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.show()
