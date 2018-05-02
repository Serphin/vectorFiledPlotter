import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.gridspec as gridspec

rpart = np.genfromtxt('data/rpart.txt', delimiter=',')
zpart = np.genfromtxt('data/zpart.txt', delimiter=',')

ratio = 1
z = np.linspace(0,5,100)
r = np.linspace(-1,1,999)
R, Z = np.mgrid[0:5:100j, -1:1:999j]
#U = -1 - X**2 + Y
#V = 1 + X - Y**2
#speed = np.sqrt(U*U + V*V)

#fig = plt.figure(figsize=(7, 9))
#gs = gridspec.GridSpec(nrows=3, ncols=2, height_ratios=[1, 1, 2])
# Varying density along a streamline
#ax0 = fig.add_subplot(gs[0, 0])
plt.streamplot(Z, R, rpart, zpart, density=[1, 1])
#fig.set_title('Varying Density')

#fig.tight_layout()
plt.show()
