import csv
import numpy
import matplotlib.pyplot as plt
from math import log, exp, pi


def arr_separator(array: list) -> list:
    """Разделяет массив на подмассивы, если в нем встречаются пробелы.
    Дополнительно пересохраняет данные из str формата в float.

    :param array - массив, в котором нужно выделить значения и разделить на подмассивы, если встречаются пробелы.
             out - возвращаемый массив, если в array встречаются пробелы.
    time_massive - массив, используемый для генерации подмассивов, если встречаются пробелы;
                   в противном случае данный массив является возвращаемым значением функции.
    """
    out: list = []
    time_missive: list = []
    for value in range(len(array)):
        if array[value].isspace():
            if time_missive:
                out.append(time_missive)
                time_missive = []
        else:
            time_missive.append(float(array[value]))

    # Если встречались пробелы, то массив out будет содержать подмассивы, иначе будет пустым.
    if not out:
        return time_missive
    else:
        return out


def filter_mass(error_massive: list, massive: list) -> (list, list):
    """Отфильтровывает выпадающие значения по напряжению и в соответсвии с этим корректирует длину массива токов.
    """
    c: int = 0
    filtered_i: list = []
    filtered_v: list = []

    for m in error_massive:
        t_i: list = []
        t_v: list = []
        for index in range(0, len(m) - 1):
            if m[index] > 0:
                t_v.append(m[index])
                t_i.append(massive[c][index])
        c += 1
        filtered_i.append(t_i)
        filtered_v.append(t_v)

    return filtered_i, filtered_v


def index_search(x: list) -> (int, int):
    """Поиск индексов для отсечения данных.

    Данные отсекаются в диапазоне Токов [10е-5 : 10е-4].
    Осуществляется поиск крайних индексов, в которых значения массива Токов попадают в данный диапазон.

    :param x - массив значений Токов.
        i, m - возвращаемые значения начального и конечного индекса диапазона.
    """
    i: int = 0
    m: int = 0

    for v in range(len(x)):
        if x[v] >= 1e-5:
            i = v
            break
    for v in range(i, len(x)):
        if x[v] >= 1e-4:
            m = v
            break

    return i, m


def range_clipping(x: list, y: list) -> (list, list):
    """Отсекает в массивах данные, входящие определенный диапазон и возвращает эти данные.

    Данные отсекаются в диапазоне Токов [10е-5 : 10е-4].
    Проводится отсечение значений Токов (x) и по этим же индексам отсечение значений Напряжений (y).

        i - начальный индекс для отсечения.
        m - конечный индекс для отсечения.
    new_x - усеченный массив токов, привиденных к натуральному логарифму.
    new_y - усеченный массив напряжений.
    """
    i, m = index_search(x)
    new_x: list = list(map(log, x[i: m+1]))
    new_y: list = y[i: m+1]

    return new_x, new_y


def search_b(x: list, y: list) -> float:
    """
    Поиск коэффициента b по методу наименьших квадратов (МНК).

    :param  x - массив Напряжений.
    :param  y - массив Токов.
    :return m - возвращаемое экспоненциальное значение от найденного коэффициента.
    """
    x = numpy.array(x)
    y = numpy.array(y)
    massive = numpy.vstack([x, numpy.ones(len(x))]).T
    k, m = numpy.linalg.lstsq(massive, y, rcond=None)[0]
    m = exp(m)
    return m


def search_fi(bi: float, d: float) -> float:
    """
    Поиск коэффициента Фи.

    :param bi - коэффициент найденный по методу МНК в функции search_b.
    :param  d - диаметр контакта.
    :return f - Возвращаемый коэффициент Фи.
    """
    # Объявление констант.
    __K: float = 1.38e-23  # Постоянная Больцмана.
    __A: int = 264         # Постоянная Ридчарсона.
    __T: int = 300         # Температура нагрева во время измерения.
    __Q: float = 1.6e-19   # Заряд

    f: float = ((__K * __T) / __Q) * log(((__A * (__T ** 2)) / (bi / (((d ** 2) * pi) / 4))))

    return f


def show_plot(m_y, m_x, n_y=None, n_x=None):
    """Строит графики для всех переданных данных.
    """
    data = [[m_y, m_x], [n_y, n_x]]

    if n_y is None:
        fig = plt.figure()
        axs = fig.add_subplot(1, 1, 1)

        # Настройки графика.
        axs.set_yscale('log')
        axs.minorticks_on()
        axs.grid(True)
        visual(data[0][0], data[0][1], axs)
    else:
        for i in range(2):
            fig = plt.figure()
            axs = fig.add_subplot(1, 1, 1)

            # Настройки графика.
            axs.set_yscale('log')
            axs.minorticks_on()
            axs.grid(True)
            visual(data[i][0], data[i][1], axs)


def visual(i_out: list, v_out: list, axis) -> None:
    """Построение графика.
    """
    axs = axis

    for x in range(len(i_out)):
        current: list = list(map(abs, i_out[x]))
        voltage: list = v_out[x][:len(i_out[x])]

        plt.plot(voltage, current)
        if max(voltage) < 0:
            axs.set_xlim([min(voltage), 0])
        else:
            axs.set_xlim([0, max(voltage)])

    plt.show()


def analytical_run(path_to_file, diam, separate_graph, inverse_graph, path_to_save, files_name):
    """Основное тело парсинга файла и аналитического расчета.

    :param   path_to_file - путь по которому находится обрабатываемый файл.
    :param           diam - диаметр контакта, на котором проводятся измерения (в микрометрах).
    :param separate_graph - булево значение "нужно ли строить графики по отдельности, если их много".
    :param  inverse_graph - булево значение "нужно ли обрабатывать значения обратных токов и напряжений и строит по
                            ним графики".
    :param   path_to_save - путь для сохранения готовых файлов.
    :param     files_name - общее название готовых файлов, позволяющее идентифицировать их.

           direct_current - прямые токи в (...).
           direct_voltage - прямые напряжения в (...).
          reverse_current - обратные токи в (...).
          reverse_voltage - обратыне напряжения в (...).
    """
    try:
        with open(path_to_file, 'r') as file:
            reader = csv.reader(file, delimiter=',')

            direct_current: list = []
            direct_voltage: list = []

            if inverse_graph:
                reverse_current: list = []
                reverse_voltage: list = []

            for line in reader:
                if 'DataValue' in line:
                    direct_current.append(line[1])
                    direct_voltage.append(line[2])

                    if inverse_graph:
                        reverse_current.append(line[3])
                        reverse_voltage.append(line[4])
    except FileNotFoundError:
        raise FileNotFoundError('Файл не найден!')
    else:
        # Прямые токи и напряжения
        direct_current = arr_separator(direct_current)
        direct_voltage = arr_separator(direct_voltage)
        direct_current, direct_voltage = filter_mass(direct_voltage, direct_current)

        d: float = float(diam)

        for i in range(len(direct_current)):
            trunc_current, trunc_voltage = range_clipping(direct_current[i], direct_voltage[i])
            b = search_b(trunc_voltage, trunc_current)
            fi = search_fi(b, d)
            print(fi)

        if inverse_graph:
            reverse_current = arr_separator(reverse_current)
            reverse_voltage = arr_separator(reverse_voltage)

            show_plot(direct_current, direct_voltage, reverse_current, reverse_voltage)
        else:
            show_plot(direct_current, direct_voltage)
