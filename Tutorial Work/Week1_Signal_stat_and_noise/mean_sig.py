import numpy as np
import sig_1_15 as sig

#Using Numpy for mean
signal_mean=np.mean(sig.InputSignal_1kHz_15kHz)
print(signal_mean)

#Using no libraries

def sig_mean(sig, mean=0):
    for i in sig:
        mean+= float(i)
    mean= mean/ len(sig)
    return mean

print(sig_mean(sig.InputSignal_1kHz_15kHz))
