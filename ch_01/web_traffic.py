import scipy as sp
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

data = sp.genfromtxt('web_traffic.tsv', delimiter='\t')

x = data[:, 0]
y = data[:, 1]

x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]


print(plt.get_backend())

plt.scatter(x, y)
plt.grid()
plt.show()
