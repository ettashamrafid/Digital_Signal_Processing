import sig_1_15 as sig
import matplotlib.pyplot as plt
import math
from matplotlib import style

def calc_dft(signal):
    sig_imaginary= [None]*int(len(signal)/2)
    sig_real= [None]*int(len(signal)/2)
    sig_mag= [None]*int(len(signal)/2)

    for i in range(int(len(signal)/2)):
        sig_imaginary[i]=0
        sig_real[i]=0
    
    for i in range(int(len(signal)/2)):
        for j in range(int(len(signal))):
            sig_real[i]= sig_real[i]+ signal[j]*math.cos(2*math.pi*i*j/len(signal))
            sig_imaginary[i]= sig_imaginary[i]- signal[j]*math.sin(2*math.pi*i*j/len(signal))

    for i in range(int(len(signal)/2)):
        sig_mag[i]=math.sqrt(math.pow(sig_real[i],2)+math.pow(sig_imaginary[i],2))

    style.use('ggplot')
    f, plt_arr= plt.subplots(4, sharex=True)
    f.suptitle('Discrete Fourier Transform')

    plt_arr[0].plot(signal, color='red')
    plt_arr[1].plot(sig_real, color='green')
    plt_arr[2].plot(sig_imaginary, color='blue')
    plt_arr[3].plot(sig_mag, color='magenta')

    plt.show()


calc_dft(sig.InputSignal_1kHz_15kHz)