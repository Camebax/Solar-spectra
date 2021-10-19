from Functions import create_plot
from Functions import get_string_data
from Functions import get_etalon
import pickle
import matplotlib.pyplot as plt

x_lim_low = 420
x_lim_high = 760
y_lim_low = 0
y_lim_high = 17000
avg_baseline = 471
l_w = 0.3  # Толщина линий на графиках
"""==================ВОЗВРАЩАЕТ ПРИБОРНЫЕ ФУНКЦИИ ДЛЯ КАЖДОГО ИЗ СЛУЧАЕВ==============="""

"""SUN1"""
with open('python_spectra/Pickles/RIGHT initial sun 1 spectrum', 'rb') as f:
    plot_info = pickle.load(f)
x_data1 = plot_info[0]
y_data1 = plot_info[1]

with open('python_spectra/Pickles/RIGHT initial sun 2 spectrum', 'rb') as f:
    plot_info = pickle.load(f)
x_data2 = plot_info[0]
y_data2 = plot_info[1]

with open('python_spectra/Pickles/RIGHT initial sun 3 spectrum', 'rb') as f:
    plot_info = pickle.load(f)
x_data3 = plot_info[0]
y_data3 = plot_info[1]

with open('python_spectra/Pickles/RIGHT initial sun 4 spectrum', 'rb') as f:
    plot_info = pickle.load(f)
x_data4 = plot_info[0]
y_data4 = plot_info[1]

plt.clf()
plt.xlim(x_lim_low, x_lim_high)
plt.ylim(y_lim_low, y_lim_high)
plt.plot(x_data1, y_data1, label='Приборный спектр 1', linewidth=l_w)
plt.plot(x_data2, y_data2, label='Приборный спектр 2', linewidth=l_w)
plt.plot(x_data3, y_data3, label='Приборный спектр 3', linewidth=l_w)
plt.plot(x_data4, y_data4, label='Приборный спектр 4', linewidth=l_w)
plt.title('Приборные спектры солнца')
plt.legend()
plt.show()
