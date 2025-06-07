import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
u = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 1, 2, 9, 6])
v = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86, 90])
plt.scatter(u, v, colour = 'hotpink')
u = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 1, 1, 4, 7, 14, 12])
v = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91, 80, 85, 108])
plt.scatter(u, v, colour = '#88c999')
plt.title("Observation of 13 cars and 15 cars differently and their respective speeds", loc = "center")
plt.show()
plt.savefig(sys.stdout.buffer)
sys.stdout.flush