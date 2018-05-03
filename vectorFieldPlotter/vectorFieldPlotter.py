import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
#from matplotlib import rc

print ('Libs have been loaded')

rpart = np.genfromtxt('data/rpart.txt', delimiter = ',')
zpart = np.genfromtxt('data/zpart.txt', delimiter = ',')
potent = np.genfromtxt('data/potent.txt', delimiter = ',')
potent = potent/potent.max()
ampl = np.sqrt(rpart*rpart + zpart*zpart)
print('Data has been loaded and processed')

R, Z = np.mgrid[0:5:100j, -1:1:999j]

lw = 3*ampl / ampl.max()

fig, ax = plt.subplots()
ax.axis([-1.1,1.1, 0.0,3.0])

levels = MaxNLocator(nbins = 40).tick_values(potent.min(), potent.max())
cmap = plt.get_cmap('plasma')


strm = plt.streamplot(Z, R, rpart, zpart, density = [1, 0.5], color = 'w', linewidth = 0.7)

print('Stream plot has been created')

cnt = plt.contourf(Z, R, potent, antialiased = 1, levels=levels, cmap = cmap)

print('Contour plot has been created')
for i in cnt.collections:
    i.set_edgecolor("face")


plt.colorbar()
plt.rcParams["font.family"] = "Times New Roman"
ax.set_title('Contour plot of potential and streamlines')

ax.set_xlabel(r'r/R')
ax.set_ylabel(r'z/$\lambda$')
fig.savefig('figures/CP_and_SL.pdf', dpi = 100)
#plt.show()