import matplotlib.pyplot as plt
from matplotlib import style
import sig_1_15 as sig 

style.use('ggplot')
f, pltr_arr= plt.subplots(2, sharex=True)
f.suptitle('Multiplot')

pltr_arr[0].plot(sig.InputSignal_1kHz_15kHz, color='magenta')
pltr_arr[0].set_title('Subplot-1')
pltr_arr[1].plot(sig.InputSignal_1kHz_15kHz)
pltr_arr[1].set_title('Subplot-2')
plt.show()

