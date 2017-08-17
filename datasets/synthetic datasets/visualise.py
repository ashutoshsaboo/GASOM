import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('two_spirals.txt',names=[str(i) for i in range(3)], sep='\t')
data =  np.array( [ df[str(i)] for i in range(2) ]).T
x = data[:,0]
y = data[:,1]
plt.scatter(x,y)
plt.show()
