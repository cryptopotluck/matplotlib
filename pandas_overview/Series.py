import numpy as np
import pandas as pd

label = ['a', 'b', 'c']
mylist = [10,20,30]
arr = np.array([10,20,30])
d = {'a':10,'b':20,'c':100}
go= pd.Series(mylist)

print(go)
print()

ser1 = pd.Series([1,2,3,4],index=['USA', 'China','UK','Iran'])
print(ser1)
