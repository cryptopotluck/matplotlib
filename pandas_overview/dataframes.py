import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from numpy.random import randn

np.random.seed(101)

# pd.DataFrame -> Data -> Index -> col Name
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])

print(df)

print()

#call collum
print(df['X'])

print()

#call multiple colums
print(df[['W', 'X']])

print()

#add New Collum

df['new'] = df['W'] + df['Y']

print(df)

print()

print(df)

df.drop('new',axis=1)
print()

#letssee = plt.plot(df.loc['A'], df.loc['B'])
#plt.show(letssee)



