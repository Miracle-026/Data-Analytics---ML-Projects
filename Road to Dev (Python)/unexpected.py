import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
s = np.array([0, 2, 3, 4, 5, 6, 7, 8, 9, 10])
t = np.array([0, 4, 9, 16, 25, 36, 49, 64, 81, 100])
plt.xlabel("Whole Numbers")
plt.ylabel("Perfect Squares")
plt.subplot(1, 2, 1)
plt.plot(s, t, 'd--k')
plt.grid(color = 'cyan', ls = '-', lw = 1.0)
u = np.array([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
v = np.array([121, 144, 169, 196, 225, 256, 289, 324, 361, 400])
plt.title("Graph of Whole Numbers against Perfect Squares", loc = "left")
plt.xlabel("Whole Numbers")
plt.ylabel("Perfect Squares")
plt.subplot(1, 2, 2)
plt.plot(s, t, 'd--k')
plt.grid(color = 'cyan', ls = '-', lw = 1.0)
plt.show()
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()