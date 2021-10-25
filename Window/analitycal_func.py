import csv
import numpy
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
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
    """Отфильтровывает выпадающие значения по напряжению.
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
    Поиск коэффициента b по методу наименьших квадратов.

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

    :param bi - коэффициент найденный по методу МНК в функции search_b
    :param  d - диаметр контакта
    :return f - Возвращаемый коэффициент Фи.
    """
    # Объявление констант.
    __K: float = 1.38e-23  # Постоянная Больцмана.
    __A: int = 264         # Постоянная Ридчарсона.
    __T: int = 300         # Температура нагрева во время измерения.
    __Q: float = 1.6e-19   # Заряд

    f: float = ((__K * __T) / __Q) * log(((__A * (__T ** 2)) / (bi / (((d ** 2) * pi) / 4))))

    return f


def analytical_run(path_to_file, diam, separate_graph, inverse_graph, path_to_save, files_name):
    """Основное тело парсинга файла и аналитического расчета.
    """
    try:
        with open(path_to_file, 'r') as file:
            reader = csv.reader(file, delimiter=',')

            i_out_f: list = []
            v_out_f: list = []

            if inverse_graph:
                i_out_r: list = []
                v_out_r: list = []

            for line in reader:
                if 'DataValue' in line:
                    i_out_f.append(line[1])
                    v_out_f.append(line[2])
                    if inverse_graph:
                        i_out_r.append(line[3])
                        v_out_r.append(line[4])
    except FileNotFoundError:
        print('Файл не найден.')
    else:
        # Прямые токи и напряжения
        i_out_f = arr_separator(i_out_f)
        v_out_f = arr_separator(v_out_f)

        i_out_f, v_out_f = filter_mass(v_out_f, i_out_f)

        d: float = float(diam)

        if len(i_out_f) > 0:
            for q in range(len(i_out_f)):
                i_f, v_f = range_clipping(i_out_f[q], v_out_f[q])
                b = search_b(v_f, i_f)
                fi = search_fi(b, d)
                print(fi)
        else:
            print("Значения не найдены.")

        # Обратные токи и напряжения
        # i_out_r = arr_separator(i_out_r)
        # v_out_r = arr_separator(v_out_r)



    # print(path_to_file)
    # print(diam)
    # print(separate_graph)
    # print(inverse_graph)
    # print(path_to_save)
    # print(files_name)