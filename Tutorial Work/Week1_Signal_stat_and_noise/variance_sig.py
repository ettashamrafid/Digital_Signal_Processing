import numpy as np
import sig_1_15
import mean_sig

#Using Library
variance= np.var(sig_1_15.InputSignal_1kHz_15kHz)
print(variance)

#Using No Library
def variance(sig, sum_d=0):
    mean=mean_sig.sig_mean(sig)
    for i in sig:
        sum_d+= (float(i)-mean)**2
    sum_d= sum_d/ (len(sig)-1)
    return sum_d

print(variance(sig_1_15.InputSignal_1kHz_15kHz))