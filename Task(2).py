from Functions import create_plot
from Functions import get_string_data
from Functions import get_etalon
import pickle
import matplotlib.pyplot as plt

x_lim_low = 420
x_lim_high = 760
y_lim_low = 0
y_lim_high = 1.5
"""==================ВОЗВРАЩАЕТ ПРИБОРНЫЕ ФУНКЦИИ ДЛЯ КАЖДОГО ИЗ СЛУЧАЕВ==============="""

"""SUN1"""
with open('python_spectra/Pickles/RIGHT initial sun 1 spectrum.pickle', 'rb') as f:
    plot_info = pickle.load(f)
x_data = plot_info[0]
y_data = plot_info[1]
y_data_etalon = []
swipe = 1.5  # Сдвиг по длинам волн оси OX
for i in range(0, len(x_data)):
    x_data[i] = x_data[i] + swipe  # Сдвиг по длинам волн оси OX
    y_data_etalon.append(get_etalon(x_data[i]))
y_max = max(y_data)
y_et_max = max(y_data_etalon)
for i in range(0, len(x_data)):
    y_data[i] = y_data[i]/y_max
    y_data_etalon[i] = y_data_etalon[i]/y_et_max
    y_data[i] = y_data[i] / y_data_etalon[i]

plt.clf()
plt.xlim(x_lim_low, x_lim_high)
plt.ylim(y_lim_low, y_lim_high)
# plt.plot(x_data, y_data_etalon)
plt.plot(x_data, y_data)
plt.title('Приборная функция sun1')
plt.savefig('python_spectra/Senscurves/{}'.format('Senscurve sun1'), dpi=400)
plt.show()
with open('python_spectra/Pickles/Senscurve sun1', 'wb') as f:
    pickle.dump([x_data, y_data], f)


"""SUN2"""
with open('python_spectra/Pickles/RIGHT initial sun 2 spectrum.pickle', 'rb') as f:
    plot_info = pickle.load(f)
x_data = plot_info[0]
y_data = plot_info[1]
y_data_etalon = []
swipe = 1.5  # Сдвиг по длинам волн оси OX
for i in range(0, len(x_data)):
    x_data[i] = x_data[i] + swipe  # Сдвиг по длинам волн оси OX
    y_data_etalon.append(get_etalon(x_data[i]))
y_max = max(y_data)
y_et_max = max(y_data_etalon)
for i in range(0, len(x_data)):
    y_data[i] = y_data[i]/y_max
    y_data_etalon[i] = y_data_etalon[i]/y_et_max
    y_data[i] = y_data[i] / y_data_etalon[i]

plt.clf()
plt.xlim(x_lim_low, x_lim_high)
plt.ylim(y_lim_low, y_lim_high)

# plt.plot(x_data, y_data_etalon)
plt.plot(x_data, y_data)
plt.title('Приборная функция sun2')
plt.savefig('python_spectra/Senscurves/{}'.format('Senscurve sun2'), dpi=400)
plt.show()
with open('python_spectra/Pickles/Senscurve sun2', 'wb') as f:
    pickle.dump([x_data, y_data], f)


"""SUN3"""
with open('python_spectra/Pickles/RIGHT initial sun 3 spectrum.pickle', 'rb') as f:
    plot_info = pickle.load(f)
x_data = plot_info[0]
y_data = plot_info[1]
y_data_etalon = []
swipe = 1.55  # Сдвиг по длинам волн оси OX
for i in range(0, len(x_data)):
    x_data[i] = x_data[i] + swipe  # Сдвиг по длинам волн оси OX
    y_data_etalon.append(get_etalon(x_data[i]))
y_max = max(y_data)
y_et_max = max(y_data_etalon)
for i in range(0, len(x_data)):
    y_data[i] = y_data[i]/y_max
    y_data_etalon[i] = y_data_etalon[i]/y_et_max
    y_data[i] = y_data[i] / y_data_etalon[i]

plt.clf()
plt.xlim(x_lim_low, x_lim_high)
plt.ylim(y_lim_low, y_lim_high)

# plt.plot(x_data, y_data_etalon)
plt.plot(x_data, y_data)
plt.title('Приборная функция sun3')
plt.savefig('python_spectra/Senscurves/{}'.format('Senscurve sun3'), dpi=400)
plt.show()
with open('python_spectra/Pickles/Senscurve sun3', 'wb') as f:
    pickle.dump([x_data, y_data], f)


"""SUN4"""
with open('python_spectra/Pickles/RIGHT initial sun 4 spectrum.pickle', 'rb') as f:
    plot_info = pickle.load(f)
x_data = plot_info[0]
y_data = plot_info[1]
y_data_etalon = []
swipe = 1.56  # Сдвиг по длинам волн оси OX
for i in range(0, len(x_data)):
    x_data[i] = x_data[i] + swipe  # Сдвиг по длинам волн оси OX
    y_data_etalon.append(get_etalon(x_data[i]))
y_max = max(y_data)
y_et_max = max(y_data_etalon)
for i in range(0, len(x_data)):
    y_data[i] = y_data[i]/y_max
    y_data_etalon[i] = y_data_etalon[i]/y_et_max
    y_data[i] = y_data[i] / y_data_etalon[i]

plt.clf()
plt.xlim(x_lim_low, x_lim_high)
plt.ylim(y_lim_low, y_lim_high)

# plt.plot(x_data, y_data_etalon)
plt.plot(x_data, y_data)
plt.title('Приборная функция sun4')
plt.savefig('python_spectra/Senscurves/{}'.format('Senscurve sun4'), dpi=400)
plt.show()
with open('python_spectra/Pickles/Senscurve sun4', 'wb') as f:
    pickle.dump([x_data, y_data], f)


"""==========Все функции на одном графике=========="""
with open('python_spectra/Pickles/Senscurve sun1', 'rb') as f:
    plot_info = pickle.load(f)
x_data = plot_info[0]
y_data = plot_info[1]

plt.plot(x_data, y_data)
with open('python_spectra/Pickles/Senscurve sun2', 'rb') as f:
    plot_info = pickle.load(f)
x_data = plot_info[0]
y_data = plot_info[1]
plt.plot(x_data, y_data)

with open('python_spectra/Pickles/Senscurve sun3', 'rb') as f:
    plot_info = pickle.load(f)
x_data = plot_info[0]
y_data = plot_info[1]
plt.plot(x_data, y_data)

with open('python_spectra/Pickles/Senscurve sun4', 'rb') as f:
    plot_info = pickle.load(f)
x_data = plot_info[0]
y_data = plot_info[1]
plt.plot(x_data, y_data)

plt.title('Все приборные функции')
plt.xlim(x_lim_low, x_lim_high)
plt.ylim(y_lim_low, y_lim_high)
plt.savefig('python_spectra/Senscurves/{}'.format('All_senscurves'), dpi=400)
plt.show()
