import csv
import numpy
import matplotlib.pyplot as plt
import os
from math import log, exp, pi


class AnalitycalCalc:
    """Получает файл и обрабатывает его особым образом.
    """

    def __init__(self, path_to_file, diameter, separate_graph, inverse_graph, path_to_save, files_name):

        # Основные входные данные.
        self.path_to_file = path_to_file
        self.diameter = float(diameter)
        self.is_separate = separate_graph
        self.is_inverse = inverse_graph
        self.path_to_save = path_to_save
        self.filename = files_name

        # Изменяемые и считываемые данные.
        self.direct_current = None
        self.direct_voltage = None

        if self.is_inverse:
            self.reverse_current = None
            self.reverse_voltage = None

        # Усеченные значения для расчетов коэффициентов.
        self.trunc_current = {}
        self.trunc_voltage = {}

        # Расчетные значения коэффициентов.
        self.b = {}    # Ток насыщения
        self.fi = {}   # Высота барьера
        self.n = {}    # Коэффициент идеальности

        # Прочие настройки
        self.file_format = '.png'
        self.x_label = 'U, В'
        self.y_label = 'I, А'
        self.title = 'Зависимость Тока от Напряжения'

    def __read_file(self):
        """Чтение CSV документа и парсинг данных.
        """
        try:
            with open(self.path_to_file, 'r') as file:
                reader = csv.reader(file, delimiter=',')

                direct_current = []
                direct_voltage = []

                if self.is_inverse:
                    reverse_current = []
                    reverse_voltage = []

                for line in reader:
                    if 'DataValue' in line:
                        direct_current.append(line[1])
                        direct_voltage.append(line[2])

                        if self.is_inverse:
                            reverse_current.append(line[3])
                            reverse_voltage.append(line[4])

                if not direct_current or not direct_voltage:
                    raise UnicodeError

        except FileNotFoundError:
            raise FileNotFoundError('Файл не найден!')
        else:
            self.direct_current = self.__arr_separator(direct_current)
            self.direct_voltage = self.__arr_separator(direct_voltage)

            if self.is_inverse:
                self.reverse_current = self.__arr_separator(reverse_current)
                self.reverse_voltage = self.__arr_separator(reverse_voltage)

    def __filter_mass(self):
        """
        Отфильтровывает выпадающие значения по напряжению и в соответсвии с этим корректирует длину массива токов.
        Метод нужен только для прямых токов из-за особенности измерительного оборудования.
        """
        c = 0
        filtered_i = []
        filtered_v = []

        for m in self.direct_voltage:
            t_i = []
            t_v = []
            for index in range(0, len(m) - 1):
                if m[index] > 0:
                    t_v.append(m[index])
                    t_i.append(self.direct_current[c][index])
            c += 1
            filtered_i.append(t_i)
            filtered_v.append(t_v)

        self.direct_current = filtered_i
        self.direct_voltage = filtered_v

    def __coefficient_calc(self):
        for i in range(len(self.direct_current)):
            self.trunc_current[i], self.trunc_voltage[i] = self.__range_clipping(self.direct_current[i],
                                                                                 self.direct_voltage[i])
            self.b[i] = self.__search_b(self.trunc_voltage[i], self.trunc_current[i])
            self.fi[i] = self.__search_fi(self.b[i], self.diameter)
            self.n[i] = self.__search_b(self.trunc_current[i], self.trunc_voltage[i])

    def __range_clipping(self, x, y):
        """Отсекает в массивах данные, входящие определенный диапазон и возвращает эти данные.

        Данные отсекаются в диапазоне Токов [10е-5 : 10е-4].
        Проводится отсечение значений Токов (x) и по этим же индексам отсечение значений Напряжений (y).

            i - начальный индекс для отсечения.
            m - конечный индекс для отсечения.
        new_x - усеченный массив токов, привиденных к натуральному логарифму.
        new_y - усеченный массив напряжений.
        """
        i, m = self.__index_search(x)
        new_x = list(map(log, x[i: m + 1]))
        new_y = y[i: m + 1]

        return new_x, new_y

    def __generate_filename(self, incomplete_name, graph_direction):
        """Генеирирует конечное имя файлов и путь для их дальнейшего сохранения.
        """
        if self.filename == '  Введите название...':
            self.filename = 'ВАХ'

        if os.path.isdir(self.path_to_save):
            new_dir = os.path.join(self.path_to_save, graph_direction)
            if not os.path.isdir(new_dir):
                os.mkdir(new_dir)
            filename = self.filename + '_' + incomplete_name + self.file_format
            saving_path_name = os.path.join(new_dir, filename)
        else:
            new_dir = os.path.join(os.getcwd(), graph_direction)
            if not os.path.isdir(new_dir):
                os.mkdir(new_dir)
            filename = self.filename + '_' + incomplete_name + self.file_format
            saving_path_name = os.path.join(new_dir, filename)

        return saving_path_name

    def __plot_graphics(self):
        """Строит графики по данным из файла.
        """
        if self.is_inverse:
            self.__generate_graphics(self.direct_current, self.direct_voltage, 'direct')
            self.__generate_graphics(self.reverse_current, self.reverse_voltage, 'reverse')
        else:
            self.__generate_graphics(self.direct_current, self.direct_voltage, 'direct')

    def __generate_graphics(self, current, voltage, graph_direction):
        """Обрабатывает данные и строит графики в зависимости от передаваемых параметров в программе.
        """
        if self.is_separate:
            for i in range(len(current)):
                axs = self.__plot_settings()
                c = list(map(abs, current[i]))
                v = voltage[i][:len(current[i])]

                plt.plot(v, c, label=('\nφ= {} эВ'
                                      '\nb= {} А'
                                      '\nn= {}'.format(self.special_rounder(self.fi[i]),
                                                       self.special_rounder(self.b[i]),
                                                       self.special_rounder(self.n[i]))
                                      ))
                if graph_direction == 'direct':
                    plt.legend(loc=2, bbox_to_anchor=(1.05, 1), borderaxespad=0.)
                if max(v) < 0:
                    axs.set_xlim([min(v), 0])
                else:
                    axs.set_xlim([0, max(v)])

                incomplete_name = graph_direction + '_' + str(i)
                saving_path = self.__generate_filename(incomplete_name, graph_direction)
                plt.savefig(saving_path, bbox_inches='tight')
        else:
            axs = self.__plot_settings()
            for i in range(len(current)):
                c = list(map(abs, current[i]))
                v = voltage[i][:len(current[i])]

                plt.plot(v, c, label=('\nφ= {} эВ'
                                      '\nb= {} А'
                                      '\nn= {}'.format(self.special_rounder(self.fi[i]),
                                                       self.special_rounder(self.b[i]),
                                                       self.special_rounder(self.n[i]))
                                      ))
                if max(v) < 0:
                    axs.set_xlim([min(v), 0])
                else:
                    axs.set_xlim([0, max(v)])

            if graph_direction == 'direct':
                plt.legend(loc=2, bbox_to_anchor=(1.05, 1), borderaxespad=0.)
            saving_path = self.__generate_filename(graph_direction, graph_direction)

            plt.savefig(saving_path, bbox_inches='tight')

    def __plot_settings(self):
        """Создание экземпляра графика и его настроек.
        """
        fig = plt.figure()
        # axs = fig.add_axes([0.13, 0.1, 0.55, 0.75])
        axs = fig.add_subplot(1, 1, 1)

        # Настройки графика.
        axs.set_yscale('log')
        axs.minorticks_on()
        axs.grid(True)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(self.title)

        return axs

    @staticmethod
    def special_rounder(number):
        """Округляет длинные числа для читабельного вывода.
        """
        if 'e' in str(number):
            num = str(number).split('e')
            round_num = str(round(float(num[0]), 3))
            return round_num + 'E' + num[1]

        return str(round(number, 3))

    def print_coefficient(self):
        """Выводит коэффициенты в консоль.
        """
        if self.b:
            for i in range(len(self.direct_current)):
                print('Ток насыщения: ', self.b[i])
                print('Высота барьера: ', self.fi[i])
                print('Коэффициент идеальности: ', self.n[i])
        else:
            print('Коэффициенты не были рассчитаны.')

    def run_program(self):
        """Запуск обработки файла, расчета данных и построения графиков.
        """
        self.__read_file()
        self.__filter_mass()
        self.__coefficient_calc()
        # self.print_coefficient()
        self.__plot_graphics()

    @staticmethod
    def __arr_separator(array):
        """Разделяет массив на подмассивы, если в нем встречаются пробелы.
        Дополнительно пересохраняет данные из str формата в float.

        :param array - массив, в котором нужно выделить значения и разделить на подмассивы, если встречаются пробелы.
                 out - возвращаемый массив, если в array встречаются пробелы.
        time_massive - массив, используемый для генерации подмассивов, если встречаются пробелы;
                       в противном случае данный массив является возвращаемым значением функции.
        """
        out = []
        time_missive = []
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

    @staticmethod
    def __index_search(x):
        """Поиск индексов для отсечения данных.

        Данные отсекаются в диапазоне Токов [10е-5 : 10е-4].
        Осуществляется поиск крайних индексов, в которых значения массива Токов попадают в данный диапазон.

        :param x - массив значений Токов.
            i, m - возвращаемые значения начального и конечного индекса диапазона.
        """
        i = 0
        m = 0

        for v in range(len(x)):
            if x[v] >= 1e-5:
                i = v
                break
        for v in range(i, len(x)):
            if x[v] >= 1e-4:
                m = v
                break

        return i, m

    @staticmethod
    def __search_b(x, y):
        """
        Поиск Тока насыщения по методу наименьших квадратов (МНК).

        :param  x - массив Напряжений.
        :param  y - массив Токов.
        :return m - возвращаемое экспоненциальное значение от найденного коэффициента в амперах.
        """
        x = numpy.array(x)
        y = numpy.array(y)
        massive = numpy.vstack([x, numpy.ones(len(x))]).T
        k, m = numpy.linalg.lstsq(massive, y, rcond=None)[0]
        m = exp(m)
        return m

    @staticmethod
    def __search_fi(bi, d):
        """
        Поиск Высоты барьера.

        :param bi - коэффициент (ток насыщения в А) найденный по методу МНК в функции search_b.
        :param  d - диаметр контакта в мкм.
        :return f - Возвращаемый коэффициент Фи - высота барьера в электронвольтах.
        """
        # Объявление констант.
        __K = 1.38e-23  # Постоянная Больцмана.
        __A = 264       # Постоянная Ридчарсона.
        __T = 300       # Температура нагрева во время измерения.
        __Q = 1.6e-19   # Заряд

        f = ((__K * __T) / __Q) * log(((__A * (__T ** 2)) / (bi / (((d ** 2) * pi) / 4))))

        return f

    @staticmethod
    def __search_n(current, voltage):
        """Поиск коэффициента идеальности.

        :param current - усеченный массив токов.
        :param voltage - усеченный массив напряжений.
        :return n      - возвращаемый коэффициент идеальности (безразмерная величина).
        """
        # Объявление констант.
        __K = 1.38e-23  # Постоянная Больцмана.
        __T = 300       # Температура нагрева во время измерения.
        __Q = 1.6e-19   # Заряд

        n = ((voltage[-1] - voltage[0])/(log(current[-1]) - log(current[0]))) * (__Q / (__K * __T))

        return n
