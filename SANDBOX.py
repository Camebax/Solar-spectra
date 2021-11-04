import numpy as np
import pickle
import matplotlib.pyplot as plt
from Functions import get_string_data

rows_num = 48  # Количество строк из .csv, которые надо обработать
spec_val_num = 3648  # Количество заданных точек спектра из .csv, которое нужно прочитать
x_lim_low = 420
x_lim_high = 760
y_lim_low = 0
y_lim_high = 17000
avg_baseline = 471
l_w = 0.3  # Толщина линий на графиках


with open('python_spectra/Pickles/Senscurve sun1 (baseline considered)', 'rb') as f:
    plot_data = pickle.load(f)
plt.plot(plot_data[0], plot_data[1], linewidth=0.4, label='Новая АФ')
np.savetxt('x__sens_1', plot_data[0])
np.savetxt('y__sens_1', plot_data[1])
plt.title('Сравнение приборных функций для sun1')
with open('python_spectra/Pickles/WRONG Senscurve sun1', 'rb') as f:
    plot_data = pickle.load(f)
plt.plot(plot_data[0], plot_data[1], linewidth=0.4, label='Исходная АФ')
np.savetxt('x_initial_sens_1', plot_data[0])
np.savetxt('y_initial_sens_1', plot_data[1])
plt.legend()
plt.show()
