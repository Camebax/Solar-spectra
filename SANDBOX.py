from Functions import get_string_data
from Functions import create_plot
import matplotlib.pyplot as plt

filepath_sens = 'sun_spectra/sun1/Senscurve.csv'
filepath_wl = 'sun_spectra/sun1/Wavelenghts.csv'
rows_num = 48
spec_val_num = 3648

filepath_pzs = 'sun_spectra/sun4/AVST_mesurement_1.csv'
filepath_wl = 'sun_spectra/sun4/Wavelenghts.csv'
create_plot(filepath_pzs,
            filepath_wl,
            rows_num,
            spec_val_num,
            result_dir_name='',
            average=False,
            title='sun4 from csv file',
            filename='sun4 from csv'
            )
