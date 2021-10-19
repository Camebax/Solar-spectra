from Functions import create_plot
import matplotlib.pyplot as plt
import numpy as np
import pickle

filepath_base = 'sun_spectra/bases/base1/AVST_mesurement_1.csv'
filepath_wl = 'sun_spectra/bases/base1/Wavelenghts.csv'
rows_num = 48  # Количество строк из .csv, которые надо обработать
spec_val_num = 3648  # Количество заданных точек спектра из .csv, которое нужно прочитать
l_w = 0.3  # Толщина линий на графиках

"""===============Возвращает бейзлайны 1-5 из папки base и выводит их графики==============="""
"""BASE1"""
plot_info1 = create_plot(filepath_base,
                         filepath_wl,
                         rows_num,
                         spec_val_num,
                         result_dir_name='Bases',
                         average=True,
                         title='baseline 1 averaged',
                         filename='baseline 1 averaged',
                         y_lim_low=0,
                         y_lim_high=800
                         )
x_data1 = plot_info1[0]
y_data1 = plot_info1[1]
with open('python_spectra/Pickles/baseline 1 averaged', 'wb') as f:
    pickle.dump([x_data1, y_data1], f)
base1_val = np.mean(y_data1)


"""BASE2"""
filepath_base = 'sun_spectra/bases/base2/AVST_mesurement_1.csv'
filepath_wl = 'sun_spectra/bases/base2/Wavelenghts.csv'
plot_info2 = create_plot(filepath_base,
                         filepath_wl,
                         rows_num,
                         spec_val_num,
                         result_dir_name='Bases',
                         average=True,
                         title='baseline 2 averaged',
                         filename='baseline 2 averaged',
                         y_lim_low=0,
                         y_lim_high=800
                         )
x_data2 = plot_info2[0]
y_data2 = plot_info2[1]
with open('python_spectra/Pickles/baseline 2 averaged', 'wb') as f:
    pickle.dump([x_data2, y_data2], f)
base2_val = np.mean(y_data2)


"""BASE3"""
filepath_base = 'sun_spectra/bases/base3/AVST_mesurement_1.csv'
filepath_wl = 'sun_spectra/bases/base3/Wavelenghts.csv'
plot_info3 = create_plot(filepath_base,
                         filepath_wl,
                         rows_num,
                         spec_val_num,
                         result_dir_name='Bases',
                         average=True,
                         title='baseline 3 averaged',
                         filename='baseline 3 averaged',
                         y_lim_low=0,
                         y_lim_high=800
                         )
x_data3 = plot_info3[0]
y_data3 = plot_info3[1]
with open('python_spectra/Pickles/baseline 3 averaged', 'wb') as f:
    pickle.dump([x_data3, y_data3], f)
base3_val = np.mean(y_data3)


"""BASE4"""
filepath_base = 'sun_spectra/bases/base4/AVST_mesurement_1.csv'
filepath_wl = 'sun_spectra/bases/base4/Wavelenghts.csv'
plot_info4 = create_plot(filepath_base,
                         filepath_wl,
                         rows_num,
                         spec_val_num,
                         result_dir_name='Bases',
                         average=True,
                         title='baseline 4 averaged',
                         filename='baseline 4 averaged',
                         y_lim_low=0,
                         y_lim_high=800
                         )
x_data4 = plot_info4[0]
y_data4 = plot_info4[1]
with open('python_spectra/Pickles/baseline 4 averaged', 'wb') as f:
    pickle.dump([x_data4, y_data4], f)
base4_val = np.mean(y_data4)


"""BASE5"""
filepath_base = 'sun_spectra/bases/base5/AVST_mesurement_1.csv'
filepath_wl = 'sun_spectra/bases/base5/Wavelenghts.csv'
plot_info5 = create_plot(filepath_base,
                         filepath_wl,
                         rows_num,
                         spec_val_num,
                         result_dir_name='Bases',
                         average=True,
                         title='baseline 5 averaged',
                         filename='baseline 5 averaged',
                         y_lim_low=0,
                         y_lim_high=800
                         )
x_data5 = plot_info5[0]
y_data5 = plot_info5[1]
with open('python_spectra/Pickles/baseline 5 averaged', 'wb') as f:
    pickle.dump([x_data5, y_data5], f)
base5_val = np.mean(y_data5)


plt.plot(x_data1, y_data1, label='base 1', linewidth=l_w)
plt.plot(x_data2, y_data2, label='base 2', linewidth=l_w)
plt.plot(x_data3, y_data3, label='base 3', linewidth=l_w)
plt.plot(x_data4, y_data4, label='base 4', linewidth=l_w)
plt.plot(x_data5, y_data5, label='base 5', linewidth=l_w)
plt.title('All bases')
plt.legend()
plt.ylim(400, 500)
plt.savefig('python_spectra/Bases/All bases', dpi=500)
plt.show()

print('Эмпирическое наиболее вероятное среднее значение бейзлайна: ', round(base3_val))
