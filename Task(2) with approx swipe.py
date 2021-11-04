from Functions import create_plot
from Functions import get_string_data
from Functions import get_etalon
import pickle
import matplotlib.pyplot as plt

x_lim_low = 420
x_lim_high = 760
y_lim_low = 0
y_lim_high = 4
l_w = 0.3  # Толщина линий на графиках
"""==================ВОЗВРАЩАЕТ ПРИБОРНЫЕ ФУНКЦИИ ДЛЯ КАЖДОГО ИЗ СЛУЧАЕВ==============="""
x_data = []
filepath_wl = 'sun_spectra/Wavelength_swipe.txt'
with open(filepath_wl, 'r') as f:
    for line in f:
        x_data.append(float(line.replace(',', '.')))

"""SUN1"""
with open('python_spectra/Pickles/Initial sun 1 spectrum (baseline considered)', 'rb') as f:
    plot_info = pickle.load(f)
y_data = plot_info[1]
y_data_etalon = []
for i in range(0, len(x_data)):
    y_data_etalon.append(get_etalon(x_data[i]))
y_max = max(y_data)
y_et_max = max(y_data_etalon)
for i in range(0, len(x_data)):
    y_data[i] = y_data[i] / y_max
    y_data_etalon[i] = y_data_etalon[i] / y_et_max
    y_data[i] = y_data_etalon[i] / y_data[i]

# with open('python_spectra/Pickles/Fraunhofer', 'rb') as f:  # Загружаем Линии Фраунгофера
#     F_lines = pickle.load(f)
plt.clf()
plt.xlim(x_lim_low, x_lim_high)
plt.ylim(y_lim_low, y_lim_high)
# plt.plot(x_data, y_data_etalon, linewidth=l_w)
plt.plot(x_data, y_data, linewidth=l_w)
# for i in range(0, len(F_lines)):
    # plt.vlines(F_lines, -10, 10, linewidth=0.05)
plt.title('Приборная функция sun1')
# plt.savefig('python_spectra/Senscurves_swipe/{}'.format('Senscurve sun1'), dpi=2000)
plt.show()
with open('python_spectra/Pickles/Senscurve sun1 (baseline considered)', 'wb') as f:
    pickle.dump([x_data, y_data], f)
