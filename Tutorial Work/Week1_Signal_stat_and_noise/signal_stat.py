import matplotlib.pyplot as plt
from matplotlib import style

x1=[1,2,3,4,5,6]
y1=[3,4,2,1,4,6]

x2=[1,2,3,4,5,6]
y2=[6,5,4,6,7,8]

style.use('dark_background')
plt.plot(x1,y1,label='One')
plt.plot(x2, y2, label='Two')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.legend()
plt.show()