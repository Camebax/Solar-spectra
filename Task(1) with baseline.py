from Functions import create_plot
from Functions import get_string_data
import matplotlib.pyplot as plt
import pickle
"""============ВОЗВРАЩАЕТ СПЕКТРЫ, КОТОРЫЕ ВИДИТ ПРИБОР С УЧЕТОМ BASE (В ПАПКУ Raw spectra with baseline)========="""
rows_num = 48  # Количество строк из .csv, которые надо обработать
spec_val_num = 3648  # Количество заданных точек спектра из .csv, которое нужно прочитать
x_lim_low = 420
x_lim_high = 760
y_lim_low = 0
y_lim_high = 17000
avg_baseline = 471
l_w = 0.3  # Толщина линий на графиках
"""Построение графика спектральной функции ИЗ ЗАДАННОГО РАНЕЕ ФАЙЛА (неправильной)"""
filepath_sens = 'sun_spectra/sun1/Senscurve.csv'
filepath_wl = 'sun_spectra/sun1/Wavelenghts.csv'
x_data_sens = get_string_data(filepath_wl, spec_val_num)
y_data_sens = get_string_data(filepath_sens, spec_val_num)
plt.plot(x_data_sens, y_data_sens, linewidth=l_w)
plt.xlim(x_lim_low, x_lim_high)
plt.title('Senscurve (WRONG)')
plt.savefig('python_spectra/Trash/Senscurve_WRONG', dpi=500)
# plt.show()


"""=============================Запись Raw spectra С БЕЙЗЛАЙНОМ============================="""
"""SUN1"""
filepath_pzs = 'sun_spectra/sun1/AVST_mesurement_1.csv'
filepath_wl = 'sun_spectra/sun1/Wavelenghts.csv'
plot_info = create_plot(filepath_pzs,
                        filepath_wl,
                        rows_num,
                        spec_val_num,
                        result_dir_name='Trash',
                        average=True,
                        title='WRONG Initial averaged sun spectrum 1',
                        filename='WRONG Initial averaged sun spectrum 1'
                        )  # Усредненный ОШИБОЧНЫЙ спектр, который видит прибор
x_data = plot_info[0]
y_data = plot_info[1]
for i in range(0, len(y_data)):
    y_data[i] = y_data[i]/y_data_sens[i] - avg_baseline
plt.clf()
plt.xlim(x_lim_low, x_lim_high)
plt.ylim(y_lim_low, y_lim_high)
plt.plot(x_data, y_data, linewidth=l_w)
plt.title('Initial sun 1 spectrum (baseline considered)')
plt.savefig('python_spectra/Raw spectra with baseline/{}'.format('Initial sun 1 spectrum (baseline considered)'), dpi=500)
with open('python_spectra/Pickles/Initial sun 1 spectrum (baseline considered)', 'wb') as f:
    pickle.dump([x_data, y_data], f)
# Усредненный ПРАВИЛЬНЫЙ спектр, который видит прибор


"""SUN2"""
filepath_pzs = 'sun_spectra/sun2/AVST_mesurement_1.csv'
filepath_wl = 'sun_spectra/sun2/Wavelenghts.csv'
plot_info = create_plot(filepath_pzs,
                        filepath_wl,
                        rows_num,
                        spec_val_num,
                        result_dir_name='Trash',
                        average=True,
                        title='WRONG Initial averaged sun spectrum 2',
                        filename='WRONG Initial averaged sun spectrum 2'
                        )  # Усредненный ОШИБОЧНЫЙ спектр, который видит прибор
x_data = plot_info[0]
y_data = plot_info[1]
for i in range(0, len(y_data)):
    y_data[i] = y_data[i]/y_data_sens[i] - avg_baseline
plt.clf()
plt.xlim(x_lim_low, x_lim_high)
plt.ylim(y_lim_low, y_lim_high)
plt.plot(x_data, y_data, linewidth=l_w)
plt.title('Initial sun 2 spectrum (baseline considered)')
plt.savefig('python_spectra/Raw spectra with baseline/{}'.format('Initial sun 2 spectrum (baseline considered)'), dpi=500)
with open('python_spectra/Pickles/Initial sun 2 spectrum (baseline considered)', 'wb') as f:
    pickle.dump([x_data, y_data], f)
# Усредненный ПРАВИЛЬНЫЙ спектр, который видит прибор


"""SUN3"""
filepath_pzs = 'sun_spectra/sun3/AVST_mesurement_1.csv'
filepath_wl = 'sun_spectra/sun3/Wavelenghts.csv'
plot_info = create_plot(filepath_pzs,
                        filepath_wl,
                        rows_num,
                        spec_val_num,
                        result_dir_name='Trash',
                        average=True,
                        title='RIGHT initial sun 3 spectrum',
                        filename='RIGHT initial sun 3 spectrum'
                        )
x_data = plot_info[0]
y_data = plot_info[1]
for i in range(0, len(y_data)):
    y_data[i] = y_data[i]-avg_baseline
plt.clf()
plt.xlim(x_lim_low, x_lim_high)
plt.ylim(y_lim_low, y_lim_high)
plt.plot(x_data, y_data, linewidth=l_w)
plt.title('Initial sun 3 spectrum (baseline considered)')
plt.savefig('python_spectra/Raw spectra with baseline/{}'.format('Initial sun 3 spectrum (baseline considered)'), dpi=500)
with open('python_spectra/Pickles/Initial sun 3 spectrum (baseline considered)', 'wb') as f:
    pickle.dump([x_data, y_data], f)
# Усредненный ПРАВИЛЬНЫЙ спектр, который видит прибор


"""SUN4"""
filepath_pzs = 'sun_spectra/sun4/AVST_mesurement_1.csv'
filepath_wl = 'sun_spectra/sun4/Wavelenghts.csv'
plot_info = create_plot(filepath_pzs,
                        filepath_wl,
                        rows_num,
                        spec_val_num,
                        result_dir_name='Trash',
                        average=True,
                        title='RIGHT initial sun 4 spectrum',
                        filename='RIGHT initial sun 4 spectrum'
                        )
x_data = plot_info[0]
y_data = plot_info[1]
for i in range(0, len(y_data)):
    y_data[i] = y_data[i]-avg_baseline
plt.clf()
plt.xlim(x_lim_low, x_lim_high)
plt.ylim(y_lim_low, y_lim_high)
plt.plot(x_data, y_data, linewidth=l_w)
plt.title('Initial sun 4 spectrum (baseline considered)')
plt.savefig('python_spectra/Raw spectra with baseline/{}'.format('Initial sun 4 spectrum (baseline considered)'), dpi=500)
with open('python_spectra/Pickles/Initial sun 4 spectrum (baseline considered)', 'wb') as f:
    pickle.dump([x_data, y_data], f)
# Усредненный ПРАВИЛЬНЫЙ спектр, который видит прибор
