from Functions import create_plot
from Functions import get_string_data

filepath_base = 'sun_spectra/bases/base1/AVST_mesurement_1.csv'
filepath_wl = 'sun_spectra/bases/base1/Wavelenghts.csv'

rows_num = 1  # Количество строк из .csv, которые надо обработать
spec_val_num = 3648  # Количество заданных точек спектра из .csv, которое нужно прочитать
x_lim_low = 420
x_lim_high = 760
y_lim_low = 0
y_lim_high = 17000

create_plot(filepath_base,
            filepath_wl,
            rows_num,
            spec_val_num,
            result_dir_name='',
            average=False,
            title='Baselines 1 not averaged',
            filename='Baselines 1 not averaged',
            x_lim_low=420,
            x_lim_high=760,
            y_lim_low=0,
            y_lim_high=1000
            )
