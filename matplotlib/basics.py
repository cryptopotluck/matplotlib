import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import numpy as np

x = np.linspace(0,5,11)
y = x ** 2

print(x)

print(y)


plt.plot(x,y)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Level of Awesome')
#plt.show()


#Two Graphs
plt.title('Relationship')
plt.subplot(1,2,1)
plt.plot(x,y,'r')
plt.xlabel('Crazy Level')
plt.ylabel('Hot Level')
plt.subplot(1,2,2)
plt.plot(y,x,'b')
plt.xlabel('Crazy Level')
plt.ylabel('Ugly Level')
#plt.show()


fig = plt.figure()
# left -> bottom -> Width -> height
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])

axes1.plot(x,y)
axes1.set_title('Larger Plot')
axes2.plot(y,x)
axes2.set_title('Smaller Plot')

plt.show()