x=[0,1,4,-3]
h=[1,0,-1,-1]

import numpy as np

print('valid')
s=np.convolve(x,h, mode='valid')
print(s)

print('Same')
s=np.convolve(x,h, mode='same')
print(s)

print('full')
s=np.convolve(x,h, mode='full')
print(s)