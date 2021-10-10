from Functions import get_string_data
import matplotlib.pyplot as plt

filepath_sens = 'sun_spectra/sun1/Senscurve.csv'
filepath_wl = 'sun_spectra/sun1/Wavelenghts.csv'
spec_val_num = 3648

plt.plot(get_string_data(filepath_wl, spec_val_num), get_string_data(filepath_sens, spec_val_num))
plt.show()
