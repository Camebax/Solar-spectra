from Functions import create_plot
import matplotlib.pyplot as plt
import pickle

filepath_base = 'sun_spectra/bases/base1/AVST_mesurement_1.csv'
rows_num = 48  # Количество строк из .csv, которые надо обработать
spec_val_num = 3648  # Количество заданных точек спектра из .csv, которое нужно прочитать'


"""Запись НЕОБРАБОТАННЫХ спектров в папку initial_spectra"""
# filepath_pzs = 'sun_spectra/sun1/AVST_mesurement_1.csv'
# filepath_wl = 'sun_spectra/sun1/Wavelenghts.csv'
# create_plot(filepath_pzs, filepath_wl, rows_num, spec_val_num, 'initial_spectra')
#
# filepath_pzs = 'sun_spectra/sun2/AVST_mesurement_1.csv'
# filepath_wl = 'sun_spectra/sun2/Wavelenghts.csv'
# create_plot(filepath_pzs, filepath_wl, rows_num, spec_val_num, 'initial_spectra')
#
# filepath_pzs = 'sun_spectra/sun3/AVST_mesurement_1.csv'
# filepath_wl = 'sun_spectra/sun3/Wavelenghts.csv'
# create_plot(filepath_pzs, filepath_wl, rows_num, spec_val_num, 'initial_spectra')
#
# filepath_pzs = 'sun_spectra/sun4/AVST_mesurement_1.csv'
# filepath_wl = 'sun_spectra/sun4/Wavelenghts.csv'
# create_plot(filepath_pzs, filepath_wl, rows_num, spec_val_num, 'initial_spectra')


"""Запись ОБРАБОТАННЫХ спектров в папку initial_spectra"""
filepath_pzs = 'sun_spectra/sun1/AVST_mesurement_1.csv'
filepath_wl = 'sun_spectra/sun1/Wavelenghts.csv'
# create_plot(filepath_pzs, filepath_wl, rows_num, spec_val_num, 'processed_spectra', average=False)
plot_info = create_plot(filepath_pzs, filepath_wl, rows_num, spec_val_num, 'processed_spectra', average=True)

filepath_pzs = 'sun_spectra/sun2/AVST_mesurement_1.csv'
filepath_wl = 'sun_spectra/sun2/Wavelenghts.csv'
# create_plot(filepath_pzs, filepath_wl, rows_num, spec_val_num, 'processed_spectra', average=False)
plot_info = create_plot(filepath_pzs, filepath_wl, rows_num, spec_val_num, 'processed_spectra', average=True)

filepath_pzs = 'sun_spectra/sun3/AVST_mesurement_1.csv'
filepath_wl = 'sun_spectra/sun3/Wavelenghts.csv'
# create_plot(filepath_pzs, filepath_wl, rows_num, spec_val_num, 'processed_spectra', average=False)
create_plot(filepath_pzs, filepath_wl, rows_num, spec_val_num, 'processed_spectra', average=True)

filepath_pzs = 'sun_spectra/sun4/AVST_mesurement_1.csv'
filepath_wl = 'sun_spectra/sun4/Wavelenghts.csv'
# create_plot(filepath_pzs, filepath_wl, rows_num, spec_val_num, 'processed_spectra', average=False)
create_plot(filepath_pzs, filepath_wl, rows_num, spec_val_num, 'processed_spectra', average=True)
