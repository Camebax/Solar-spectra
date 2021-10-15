from Functions import get_string_data
from Functions import get_etalon
import matplotlib.pyplot as plt
import pickle

filepath_sens = 'sun_spectra/sun1/Senscurve.csv'
filepath_wl = 'sun_spectra/sun1/Wavelenghts.csv'

rows_num = 48
spec_val_num = 3648

filepath_pzs = 'sun_spectra/sun4/AVST_mesurement_1.csv'
filepath_wl = 'sun_spectra/sun4/Wavelenghts.csv'

x_data = []
y_data = []
for wl in range(900, 930):
    x_data.append(wl/3)
    y_data.append(get_etalon(wl/3))

plt.plot(x_data, y_data)
plt.show()
