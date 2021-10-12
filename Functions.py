import csv
import matplotlib.pyplot as plt
import numpy as np


def get_table_data(filepath_pzs, rows_num=1, spec_val_num=3):
    """Возвращает массив rows, каждый элемент которого соответствует набору сигналов ПЗС матрицы при каждом измерении"""
    with open(filepath_pzs, newline='') as f:
        reader = csv.reader(f, delimiter='\t')
        row_index = 0
        rows = []
        for row in reader:
            columns = []
            for column in row[1:spec_val_num + 1]:
                columns.append(column)
            rows.append(columns)
            row_index += 1
            if row_index >= rows_num:
                break
    return rows


def get_string_data(filepath_wl, spec_val_num):
    """Возвращает массив columns, элементами которого являются длины волн, соотв. каждому пикселю ПЗС матрицы"""
    with open(filepath_wl, newline='') as f:
        reader = csv.reader(f, delimiter='\t')
        columns = []
        for column in reader:
            for wl in column:
                try:
                    columns.append(float(wl))
                except ValueError:
                    pass
        return columns[0:spec_val_num]


def create_plot(filepath_pzs,  # Путь к файлу с таблицей показаний ПЗС
                filepath_wl,  # Путь к файлу с массивом длин волн
                rows_num,  # Число строящихся кривых
                spec_val_num,  # Число длин волн, для кот. строятся графики
                result_dir_name='',  # Имя директории для записи построенных графиков
                average=True,  # Вкл/откл усреднение по всем кривым
                title='Untitled',  # Подпись на графике
                filename='Default',  # Имя файла
                x_lim_low=420,  # Масштабы осей
                x_lim_high=760,
                y_lim_low=0,
                y_lim_high=17000
                ):
    """Строит графики с заданными пар-ми и возвращает массив с массивами x_data и y_data для всех построенных кривых"""
    graphs = []
    rows_pzs = get_table_data(filepath_pzs, rows_num, spec_val_num)  # таблица из строк в данными от ПЗС
    x_data = get_string_data(filepath_wl, spec_val_num)  # строка с сдлинами волн
    plt.clf()  # Очищает предыдущие построенные графици
    if not average:
        for row in rows_pzs:
            y_data = []
            for column in row:
                y_data.append(int(column.split('.')[0]))
            graphs.append(y_data)
            plt.plot(x_data, y_data)
        plt.plot(x_data, y_data)
        plt.xlim(x_lim_low, x_lim_high)
        plt.ylim(y_lim_low, y_lim_high)
        plt.title(title)
        plt.savefig('python_spectra/{}/{}'.format(result_dir_name, filename), dpi=400)
        # plt.show()
        return x_data, graphs

    if average:
        y_data = np.zeros(spec_val_num)
        for row in rows_pzs:
            i = 0
            for column in row:
                y_data[i] += int(column.split('.')[0])
                i += 1
        for i in range(0, len(y_data)):
            y_data[i] = y_data[i] / rows_num
        plt.plot(x_data, y_data)
        plt.xlim(x_lim_low, x_lim_high)
        plt.ylim(y_lim_low, y_lim_high)
        plt.title(title)
        plt.savefig('python_spectra/{}/{}'.format(result_dir_name, filename), dpi=400)
        # plt.show()
        return x_data, y_data
