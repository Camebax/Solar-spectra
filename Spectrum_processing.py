from Functions import create_plot
from Functions import get_string_data
import matplotlib.pyplot as plt

filepath_base = 'sun_spectra/bases/base1/AVST_mesurement_1.csv'
rows_num = 48  # Количество строк из .csv, которые надо обработать
spec_val_num = 3648  # Количество заданных точек спектра из .csv, которое нужно прочитать
x_lim_low = 420
x_lim_high = 760
y_lim_low = 0
y_lim_high = 17000


"""Построение графика спектральной функции"""
filepath_sens = 'sun_spectra/sun1/Senscurve.csv'
filepath_wl = 'sun_spectra/sun1/Wavelenghts.csv'
x_data_sens = get_string_data(filepath_wl, spec_val_num)
y_data_sens = get_string_data(filepath_sens, spec_val_num)
plt.plot(x_data_sens, y_data_sens)
plt.xlim(x_lim_low, x_lim_high)
plt.title('Senscurve')
plt.savefig('python_spectra/processed_spectra/Senscurve', dpi=400)
# plt.show()


"""===================================Запись НЕОБРАБОТАННЫХ спектров в папку initial_spectra==================================="""
"""SUN1"""
filepath_pzs = 'sun_spectra/sun1/AVST_mesurement_1.csv'
filepath_wl = 'sun_spectra/sun1/Wavelenghts.csv'
create_plot(filepath_pzs,
            filepath_wl,
            rows_num,
            spec_val_num,
            result_dir_name='initial_spectra',
            average=False,
            title='sun1 from csv file',
            filename='sun1 from csv'
            )

"""SUN2"""
filepath_pzs = 'sun_spectra/sun2/AVST_mesurement_1.csv'
filepath_wl = 'sun_spectra/sun2/Wavelenghts.csv'
create_plot(filepath_pzs,
            filepath_wl,
            rows_num,
            spec_val_num,
            result_dir_name='initial_spectra',
            average=False,
            title='sun2 from csv file',
            filename='sun2 from csv'
            )

"""SUN3"""
filepath_pzs = 'sun_spectra/sun3/AVST_mesurement_1.csv'
filepath_wl = 'sun_spectra/sun3/Wavelenghts.csv'
create_plot(filepath_pzs,
            filepath_wl,
            rows_num,
            spec_val_num,
            result_dir_name='initial_spectra',
            average=False,
            title='sun3 from csv file',
            filename='sun3 from csv'
            )

"""SUN4"""
filepath_pzs = 'sun_spectra/sun4/AVST_mesurement_1.csv'
filepath_wl = 'sun_spectra/sun4/Wavelenghts.csv'
create_plot(filepath_pzs,
            filepath_wl,
            rows_num,
            spec_val_num,
            result_dir_name='initial_spectra',
            average=False,
            title='sun4 from csv file',
            filename='sun4 from csv'
            )




"""===================================Запись ОБРАБОТАННЫХ спектров в папку processed_spectra==================================="""

"""SUN1"""
filepath_pzs = 'sun_spectra/sun1/AVST_mesurement_1.csv'
filepath_wl = 'sun_spectra/sun1/Wavelenghts.csv'
plot_info = create_plot(filepath_pzs,
                        filepath_wl,
                        rows_num,
                        spec_val_num,
                        result_dir_name='processed_spectra',
                        average=True,
                        title='Initial averaged sun spectrum 1',
                        filename='Initial averaged sun spectrum 1'
                        )  # Усредненный спектр, который видит прибор
x_data = plot_info[0]
y_data = plot_info[1]
for i in range(0, len(y_data)):
    y_data[i] = y_data[i]/y_data_sens[i]
plt.clf()
plt.xlim(x_lim_low, x_lim_high)
plt.ylim(y_lim_low, y_lim_high)
plt.plot(x_data, y_data)
plt.title('Real sun 1 spectrum')
plt.savefig('python_spectra/processed_spectra/{}'.format('Real sun 1 spectrum'), dpi=400)
plt.show()  # Усредненный реальный спектр



"""SUN2"""
filepath_pzs = 'sun_spectra/sun2/AVST_mesurement_1.csv'
filepath_wl = 'sun_spectra/sun2/Wavelenghts.csv'
plot_info = create_plot(filepath_pzs,
                        filepath_wl,
                        rows_num,
                        spec_val_num,
                        result_dir_name='processed_spectra',
                        average=True,
                        title='Initial averaged sun spectrum 2',
                        filename='Initial averaged sun spectrum 2'
                        )  # Усредненный спектр, который видит прибор
x_data = plot_info[0]
y_data = plot_info[1]
for i in range(0, len(y_data)):
    y_data[i] = y_data[i]/y_data_sens[i]
plt.clf()
plt.xlim(x_lim_low, x_lim_high)
plt.ylim(y_lim_low, y_lim_high)
plt.plot(x_data, y_data)
plt.title('Real sun 2 spectrum')
plt.savefig('python_spectra/processed_spectra/{}'.format('Real sun 2 spectrum'), dpi=400)
plt.show()  # Усредненный реальный спектр


"""SUN3"""
filepath_pzs = 'sun_spectra/sun3/AVST_mesurement_1.csv'
filepath_wl = 'sun_spectra/sun3/Wavelenghts.csv'
plot_info = create_plot(filepath_pzs,
                        filepath_wl,
                        rows_num,
                        spec_val_num,
                        result_dir_name='processed_spectra',
                        average=True,
                        title='Real sun 3 spectrum',
                        filename='Real sun 3 spectrum'
                        )
x_data = plot_info[0]
y_data = plot_info[1]
for i in range(0, len(y_data)):
    y_data[i] = y_data[i]*y_data_sens[i]
plt.clf()
plt.xlim(x_lim_low, x_lim_high)
plt.ylim(y_lim_low, y_lim_high)
plt.plot(x_data, y_data)
plt.title('Initial averaged sun spectrum 3')
plt.savefig('python_spectra/processed_spectra/{}'.format('Initial averaged sun spectrum 3'), dpi=400)
plt.show()


"""SUN4"""
filepath_pzs = 'sun_spectra/sun4/AVST_mesurement_1.csv'
filepath_wl = 'sun_spectra/sun4/Wavelenghts.csv'
plot_info = create_plot(filepath_pzs,
                        filepath_wl,
                        rows_num,
                        spec_val_num,
                        result_dir_name='processed_spectra',
                        average=True,
                        title='Real sun 4 spectrum',
                        filename='Real sun 4 spectrum'
                        )
x_data = plot_info[0]
y_data = plot_info[1]
for i in range(0, len(y_data)):
    y_data[i] = y_data[i]*y_data_sens[i]
plt.clf()
plt.xlim(x_lim_low, x_lim_high)
plt.ylim(y_lim_low, y_lim_high)
plt.plot(x_data, y_data)
plt.title('Initial averaged sun spectrum 4')
plt.savefig('python_spectra/processed_spectra/{}'.format('Initial averaged sun spectrum 4'), dpi=400)
plt.show()
