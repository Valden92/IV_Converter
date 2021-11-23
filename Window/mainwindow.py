from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget
import sys
import os
from analitycal_class import AnalitycalCalc


class Ui_MainWindow(QWidget):

    def __init__(self):
        """Инициализация атрибутов.
        """
        super().__init__()
        self.MainWindow = QtWidgets.QMainWindow()
        self.centralwidget = QWidget(self.MainWindow)

        # Высота и ширина основного окна
        self.height_window = 700
        self.length_window = 602

        # Менюбар
        self.menubar = QtWidgets.QMenuBar(self.MainWindow)
        self.menu = QtWidgets.QMenu(self.menubar)
        self.instruction = QtGui.QAction(self.MainWindow)
        self.about = QtGui.QAction(self.MainWindow)
        self.exit = QtGui.QAction(self.MainWindow)

        # Ввод диаметра
        self.widget_diameter = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayout_diameter = QtWidgets.QHBoxLayout(self.widget_diameter)
        self.diameter = QtWidgets.QLineEdit(self.widget_diameter)
        self.is_diameter = False

        # Чекбоксы
        self.widget_checkbox = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_checkbox)
        self.check_separate_graph = QtWidgets.QCheckBox(self.widget_checkbox)
        self.check_inverse_graph = QtWidgets.QCheckBox(self.widget_checkbox)

        # Путь к файлу
        self.widget_path_to = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayout_path_to = QtWidgets.QHBoxLayout(self.widget_path_to)
        self.path_label = QtWidgets.QLineEdit(self.widget_path_to)
        self.is_path_to = False

        # Путь сохранения
        self.widget_path_out = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayout_path_out = QtWidgets.QHBoxLayout(self.widget_path_out)
        self.save_label = QtWidgets.QLineEdit(self.widget_path_out)

        # Названия готовых файлов
        self.widget_filename = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayout_filename = QtWidgets.QHBoxLayout(self.widget_filename)
        self.output_filename = QtWidgets.QLineEdit(self.widget_filename)

        # Кнопка начала процесса обработки
        self.startButton = QtWidgets.QPushButton(self.centralwidget)

        # Логгинизация процессов
        self.logging = QtWidgets.QScrollArea(self.centralwidget)
        self.logging_text = '> Программа запущена. Удачных расчетов!'

        # Статусбар
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)

    def setupUi(self):
        """Основные настройки.
        """
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.setFixedSize(self.length_window, self.height_window)
        self.MainWindow.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.MainWindow.setWindowIcon(QtGui.QIcon(os.path.join(os.getcwd(), 'image', 'IV_logo.png')))
        self.MainWindow.setWindowTitle("IV Converter")
        self.MainWindow.setMenuBar(self.createMenu())

        self.createLabel_text(self.centralwidget, 40, 20, 451, 21,
                              "Основные настройки расчета и построения графиков",
                              bold=True, pointsize=12, weight=75)
        self.widget_diameter = self.createDiameter_widget()
        self.widget_checkbox = self.createCheckbox_widgets()

        self.createLine(0, 230, self.length_window, 3)

        self.createLabel_text(self.centralwidget, 40, 260, 121, 21,
                              "Открыть файл:",
                              pointsize=12)
        self.widget_path_to = self.createPath_to_file_widget()
        self.createLabel_text(self.centralwidget, 40, 360, 301, 21,
                              "Указать папку для сохранения данных:",
                              pointsize=12)
        self.widget_path_out = self.createPath_to_save_widget()
        self.widget_filename = self.createFilename_widget()

        self.createLine(0, 500, self.length_window, 3)

        self.startButton = self.createStart_button()
        self.logging = self.createLog_area()
        self.createLabel_text(self.centralwidget, 180, 510, 383, 20,
                              "  Сообщения программы:",
                              background="background-color: rgb(51, 72, 83);")

        self.MainWindow.setCentralWidget(self.centralwidget)

        self.MainWindow.setStatusBar(self.createStatusbar())

    def createMenu(self):
        """Настройки Меню.
        """
        self.menubar.setGeometry(QtCore.QRect(0, 0, 602, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("background-color: rgb(60, 63, 65);\n"
                                   "color: rgb(230, 230, 230);\n"
                                   "selection-background-color: rgb(0, 170, 255);")
        self.menubar.setObjectName("menubar")

        # Кнопка "Меню"
        self.menu.setTitle("Меню")
        self.menu.setGeometry(QtCore.QRect(339, 102, 183, 125))
        self.menu.setMouseTracking(True)
        self.menu.setStyleSheet("selection-background-color: rgb(0, 170, 255);")
        self.menu.setObjectName("menu")

        # Кнопка "Инструкция"
        self.instruction.setText("Инструкция")
        self.instruction.setObjectName("instruction")

        # Кнопка "О программе"
        self.about.setText("О программе")
        self.about.setObjectName("about")

        # Кнопка "Выход"
        self.exit.setText("Выход")
        self.exit.setObjectName("exit")
        self.exit.triggered.connect(self.close_program)

        # Расположение кнопок в Меню
        self.menu.addAction(self.instruction)
        self.menu.addAction(self.about)
        self.menu.addSeparator()
        self.menu.addAction(self.exit)
        self.menubar.addAction(self.menu.menuAction())

        return self.menubar

    def createDiameter_widget(self):
        """Создает окно ввода диаметра контакта.
        """
        self.widget_diameter.setGeometry(QtCore.QRect(40, 60, 271, 41))
        self.widget_diameter.setObjectName("widget_diameter")

        self.horizontalLayout_diameter.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_diameter.setObjectName("horizontalLayout_diameter")

        label_diameter_text_1 = self.createLabel_text(self.widget_diameter, 0, 0, 0, 0,
                                                      "Диаметр контакта:",
                                                      pointsize=12)
        label_diameter_text_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading |
                                           QtCore.Qt.AlignmentFlag.AlignLeft |
                                           QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.horizontalLayout_diameter.addWidget(label_diameter_text_1)

        self.diameter.setInputMask("0.0000")
        self.diameter.setText("0.0000")
        self.diameter.setWhatsThis("Введите диаметр контакта, на котором проводилось измерение (в микрометрах). "
                                   "Обязательный параметр!")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.diameter.setFont(font)
        self.diameter.setStyleSheet("background-color: rgb(60, 63, 65);\n"
                                    "color: rgb(225, 225, 225);")
        self.diameter.setObjectName("diameter")

        self.horizontalLayout_diameter.addWidget(self.diameter)

        label_diameter_text_2 = self.createLabel_text(self.widget_diameter, 0, 0, 0, 0,
                                                      "мкм",
                                                      pointsize=12)
        label_diameter_text_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading |
                                           QtCore.Qt.AlignmentFlag.AlignLeft |
                                           QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.horizontalLayout_diameter.addWidget(label_diameter_text_2)

        return self.widget_diameter

    def createCheckbox_widgets(self):
        """Создает окна чекбоксов с настройками для графика.
        """
        self.widget_checkbox.setGeometry(QtCore.QRect(40, 130, 281, 81))
        self.widget_checkbox.setObjectName("widget_checkbox")

        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.verticalLayout.addWidget(self.create_checkbox_is_separate())

        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.verticalLayout.addWidget(self.create_checkbox_is_inverse())

        return self.widget_checkbox

    def create_checkbox_is_separate(self):
        """Настройки проверки разделения графиков при построении.
        """
        self.check_separate_graph.setText("  Разбить на отдельные графики")
        self.check_separate_graph.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.check_separate_graph.setFont(font)
        self.check_separate_graph.setStyleSheet("color: rgb(225, 225, 225);")
        self.check_separate_graph.setObjectName("check_separate_graph")
        self.check_separate_graph.setWhatsThis('Поставте галочку, если желаете, чтобы графики не объединялись '
                                               'на одной оси координат. Граифики будут построены по отдельности, '
                                               'в соответсвии с предоставленными данными.')

        return self.check_separate_graph

    def create_checkbox_is_inverse(self):
        """Настройки проверки построения части графика с обратными кривыми.
        """
        self.check_inverse_graph.setText("  Строить обратные кривые")
        self.check_inverse_graph.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.check_inverse_graph.setFont(font)
        self.check_inverse_graph.setStyleSheet("color: rgb(225, 225, 225);")
        self.check_inverse_graph.setObjectName("check_inverse_graph")
        self.check_inverse_graph.setWhatsThis('Поставте галочку, если желаете, чтобы были обработаны данные для '
                                              'обратных смещений.')

        return self.check_inverse_graph

    def createPath_to_file_widget(self):
        """Создает окно для указания пути к файлу.
        """
        self.widget_path_to.setGeometry(QtCore.QRect(40, 290, 411, 36))
        self.widget_path_to.setObjectName("widget_path_to")
        self.widget_path_to.setWhatsThis('Выберите CSV файл с иземерениями, либо укажите путь к нему.')

        self.horizontalLayout_path_to.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetNoConstraint)
        self.horizontalLayout_path_to.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_path_to.setSpacing(10)
        self.horizontalLayout_path_to.setObjectName("horizontalLayout_path_to")

        ButtonPath = QtWidgets.QToolButton(self.widget_path_to)
        ButtonPath.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ButtonPath.sizePolicy().hasHeightForWidth())
        ButtonPath.setSizePolicy(sizePolicy)
        ButtonPath.setMinimumSize(QtCore.QSize(30, 30))
        ButtonPath.setText('...')
        font = QtGui.QFont()
        font.setPointSize(10)
        ButtonPath.setFont(font)
        ButtonPath.setStyleSheet("background-color: #F4C430;\n"
                                 "selection-background-color: rgb(60, 63, 65);\n"
                                 "color: rgb(0, 0, 0);")
        self.horizontalLayout_path_to.addWidget(ButtonPath)
        ButtonPath.clicked.connect(self.path_to_open)

        self.path_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.path_label.setText('  Файл...')
        font = QtGui.QFont()
        font.setPointSize(11)
        self.path_label.setFont(font)
        self.path_label.setStyleSheet("background-color: rgb(60, 63, 65);\n"
                                      "color: rgb(225, 225, 225);")
        self.path_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignJustify |
                                     QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.path_label.setObjectName("path_label")
        self.horizontalLayout_path_to.addWidget(self.path_label)

        return self.widget_path_to

    def createPath_to_save_widget(self):
        """Строит окно для указания пути сохранения готовых результатов.
        """
        self.widget_path_out.setGeometry(QtCore.QRect(40, 390, 411, 36))
        self.widget_path_out.setObjectName("widget_path_out")
        self.widget_path_out.setWhatsThis('Выберите папку или впишите путь для сохранения результатов расчета.'
                                          ' Если конечная папка не будет выбрана, то результаты сохранятся в'
                                          ' директории программы.')

        self.horizontalLayout_path_out.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetNoConstraint)
        self.horizontalLayout_path_out.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_path_out.setSpacing(10)
        self.horizontalLayout_path_out.setObjectName("horizontalLayout_path_out")

        ButtonSave = QtWidgets.QToolButton(self.widget_path_out)
        ButtonSave.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ButtonSave.sizePolicy().hasHeightForWidth())
        ButtonSave.setSizePolicy(sizePolicy)
        ButtonSave.setMinimumSize(QtCore.QSize(30, 30))
        ButtonSave.setText('...')
        font = QtGui.QFont()
        font.setPointSize(10)
        ButtonSave.setFont(font)
        ButtonSave.setStyleSheet("background-color: #F4C430;\n"
                                 "selection-background-color: rgb(60, 63, 65);\n"
                                 "color: rgb(0, 0, 0);")
        self.horizontalLayout_path_out.addWidget(ButtonSave)
        ButtonSave.clicked.connect(self.path_to_save)

        self.save_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.save_label.setText('  Путь сохранения данных')
        font = QtGui.QFont()
        font.setPointSize(11)
        self.save_label.setFont(font)
        self.save_label.setStyleSheet("background-color: rgb(60, 63, 65);\n"
                                      "color: rgb(225, 225, 225);")
        self.save_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignJustify |
                                     QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.save_label.setObjectName("save_label")
        self.horizontalLayout_path_out.addWidget(self.save_label)

        return self.widget_path_out

    def createFilename_widget(self):
        """Создает окно ввода имен готовых файлов.
        """
        self.widget_filename.setGeometry(QtCore.QRect(40, 450, 523, 32))
        self.widget_filename.setObjectName("widget_filename")
        self.widget_filename.setWhatsThis('Впишите конечное имя для файлов с результатами для дальнейшей'
                                          ' идентификации.')

        self.horizontalLayout_filename.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_filename.setObjectName("horizontalLayout_filename")

        label_text = self.createLabel_text(self.widget_filename, 0, 0, 0, 0,
                                           "Название готовых файлов:",
                                           pointsize=12)
        self.horizontalLayout_filename.addWidget(label_text)

        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_filename.addItem(spacerItem)

        self.output_filename.setMinimumSize(QtCore.QSize(300, 30))
        self.output_filename.setText("  Введите название...")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.output_filename.setFont(font)
        self.output_filename.setStyleSheet("background-color: rgb(60, 63, 65);\n"
                                           "color: rgb(225, 225, 225);")
        self.output_filename.setObjectName("output_filename")
        self.horizontalLayout_filename.addWidget(self.output_filename)

        return self.widget_filename

    def createStart_button(self):
        """Создает кнопку для начала обработки файла.
        """
        self.startButton.setGeometry(QtCore.QRect(40, 540, 101, 91))
        self.startButton.setText('START')
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.startButton.setFont(font)
        self.startButton.setStyleSheet("background-color: rgb(73, 156, 84);\n"
                                       "color: rgb(40, 40, 40);")
        self.startButton.setObjectName("startButton")
        self.startButton.setWhatsThis('Нажать для начала процесса обработки данных файла.')

        self.startButton.clicked.connect(self.start_analytical_part)

        return self.startButton

    def createLog_area(self):
        """Создает окно с логами.
        """
        self.logging.setGeometry(QtCore.QRect(180, 530, 383, 111))
        self.logging.setStyleSheet("background-color: rgb(60, 63, 65);\n"
                                   "color: rgb(200, 200, 200);")
        self.logging.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft |
                                  QtCore.Qt.AlignmentFlag.AlignBottom)
        self.logging.setWhatsThis('Здесь выводятся сообщения для пользователя о работе программы и результатах'
                                  ' расчетов.')

        log_text_widget = QtWidgets.QLabel(self.logging_text, parent=self.logging)
        log_text_widget.setMargin(5)
        log_text_widget.setWordWrap(False)
        log_text_widget.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        log_text_widget.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)

        self.logging.setWidget(log_text_widget)

        return self.logging

    def createStatusbar(self):
        """Настройки статусбара.
        """
        self.statusbar.setStyleSheet("color: rgb(150, 150, 150);\n"
                                     "background-color: rgb(60, 63, 65);")
        # self.statusbar.setStyleSheet("QStatusBar{border: None;"
        #                              "color: rgb(150, 150, 150);"
        #                              "background-color: rgb(60, 63, 65);}")
        self.statusbar.setObjectName("statusbar")

        my_message = QtWidgets.QLabel(self.MainWindow)
        my_message.setText(chr(169) + ' Created by Zaytsev D A (2021)  ')
        self.statusbar.addPermanentWidget(my_message)

        return self.statusbar

    # Методы построения различных общих элементов.

    @staticmethod
    def createLabel_text(some_widget, x, y, length, height, text, bold=False, pointsize=None, weight=None,
                         background=None):
        """Генерирует статичную надпись.
        """
        label_text = QtWidgets.QLabel(some_widget)
        label_text.setGeometry(QtCore.QRect(x, y, length, height))
        label_text.setText(text)
        font = QtGui.QFont()
        if pointsize:
            font.setPointSize(pointsize)
        font.setBold(bold)
        if weight:
            font.setWeight(weight)
        label_text.setFont(font)
        if background:
            label_text.setStyleSheet("color: rgb(225, 225, 225);\n" + background)
        else:
            label_text.setStyleSheet("color: rgb(225, 225, 225);\n")

        return label_text

    def createLine(self, x, y, length, height):
        """Строит линию-разделитель.
        """
        line = QtWidgets.QFrame(self.centralwidget)
        line.setGeometry(QtCore.QRect(x, y, length, height))
        line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        return line


    # Прочие методы, инициализирующие внутреннюю работу программы.

    def show_window(self):
        """Запускает программное окно.
        """
        self.setupUi()
        self.MainWindow.show()

    def close_program(self):
        """Закрывает приложение.
        """
        reply = QtWidgets.QMessageBox(self.MainWindow)
        reply.setStyleSheet("color: rgb(200, 200, 200);\n"
                            "background-color: rgb(60, 63, 65);")
        reply.setWindowTitle("Выход")
        reply.setText("Завершить работу с приложением?")
        reply.setIcon(QtWidgets.QMessageBox.Icon.Question)

        yesButton = reply.addButton("Выйти", reply.ButtonRole.ActionRole)
        yesButton.setStyleSheet("background-color: #F4C430;\n"
                                "color: black;")

        noButton = reply.addButton("Остаться", reply.ButtonRole.NoRole)
        noButton.setStyleSheet("background-color: #F4C430;\n"
                               "color: black;")

        reply.exec()

        if reply.clickedButton() == yesButton:
            app.exit()

    def path_to_open(self):
        """Считывает путь к указанному файлу для его открытия.
        """
        path_to_file = QtWidgets.QFileDialog.getOpenFileName(filter='*.csv')[0]

        if path_to_file:
            self.path_label.setText(path_to_file)

    def path_to_save(self):
        """Считывает путь к указанной директории для сохранения конечных результатов.
        """
        path_to_dir = QtWidgets.QFileDialog.getExistingDirectory()

        if path_to_dir:
            self.save_label.setText(path_to_dir)

    def data_validation(self):
        """Проверка ввода необходимых данных.
        """
        if float(self.diameter.text()) > 0:
            self.is_diameter = True

        if '.csv' in self.path_label.text():
            self.is_path_to = True

        if not self.is_diameter:
            text = self.logging_text
            self.logging_text = text + '\n' + '> Не указан диаметр контакта.'

        if not self.is_path_to:
            text = self.logging_text
            self.logging_text = text + '\n' + '> Файл не выбран или выбран не верно.'

        self.logging = self.createLog_area()

    def visual_result(self, calc_obj):
        """Выводит результаты расчетов в Лог.
        """
        for i in range(len(calc_obj.b.keys())):
            self.logging_text = self.logging_text + '\n' +\
                                '> {}) Высота барьера: {} эВ,\n' \
                                '      Ток насыщения: {} А'.format(str(i+1),
                                                                   calc_obj.special_rounder(calc_obj.fi[i]),
                                                                   calc_obj.special_rounder(calc_obj.b[i]))
        self.logging_text = self.logging_text + '\n' + '> Конвертирование завершено удачно.\n> Графики построены.\n'
        self.logging = self.createLog_area()

    def start_analytical_part(self):
        """Начинает парсинг и расчет документа.
        """
        self.data_validation()

        if self.is_diameter and self.is_path_to:
            calc_obj = AnalitycalCalc(
                self.path_label.text(),
                self.diameter.text(),
                self.check_separate_graph.isChecked(),
                self.check_inverse_graph.isChecked(),
                self.save_label.text(),
                self.output_filename.text()
            )
            try:
                calc_obj.run_program()
            except FileNotFoundError:
                text = self.logging_text
                self.logging_text = text + '\n' + '> Файл не найден!'
                self.logging = self.createLog_area()
            except UnicodeError:
                text = self.logging_text
                self.logging_text = text + '\n' + '> Файл пустой или выбран неверно!'
                self.logging = self.createLog_area()
            else:
                self.visual_result(calc_obj)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show_window()
    sys.exit(app.exec())
