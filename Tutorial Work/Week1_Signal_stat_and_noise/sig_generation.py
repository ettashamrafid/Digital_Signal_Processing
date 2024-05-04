from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(0,1.0,2001)
#print(len(t))

sig_5hz= np.sin(2*np.pi*5*t)
sig_250hz= np.sin(2*np.pi*250*t)
sig_5_250hz= sig_5hz +sig_250hz


f, plt_arr=plt.subplots(3, sharex=True)

plt_arr[0].plot(sig_5hz, color='magenta')
plt_arr[1].plot(sig_250hz, color='green')
plt_arr[2].plot(sig_5_250hz)

plt.show()