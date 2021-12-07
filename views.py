from PyQt6.QtCore import QRect, Qt, QSize
from PyQt6.QtGui import QIcon, QAction, QFont, QKeySequence
from PyQt6.QtWidgets import (QMainWindow, QWidget, QMenuBar, QMenu, QLineEdit, QVBoxLayout, QHBoxLayout,
                             QCheckBox, QToolButton, QPushButton, QPlainTextEdit, QStatusBar, QSpacerItem,
                             QSizePolicy, QLayout, QLabel, QFrame, QDialog, QTextBrowser)

import os


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Общие настройки и настройки основного окна
        self.main_window = QMainWindow()
        self.central_widget = QWidget(self.main_window)
        self.main_window.setCentralWidget(self.central_widget)
        self.setup_main(700, 600)

        # Создание надписей в рабочем окне
        self.label_inf = self.create_label(self.central_widget, 40, 15, 500, 40,
                                           "Настройки расчета и построения графиков",
                                           bold=True, pointsize=13, weight=75)
        self.label_open_file = self.create_label(self.central_widget, 40, 260, 121, 21,
                                                 "Открыть файл:",
                                                 pointsize=12)
        self.label_save_path = self.create_label(self.central_widget, 40, 360, 301, 21,
                                                 "Указать папку для сохранения данных:",
                                                 pointsize=12)
        self.label_output = self.create_label(self.central_widget, 180, 510, 383, 20,
                                              "  Сообщения программы:",
                                              background="background-color: rgb(51, 72, 83);")

        # Созание линий-разделителей областей
        self.line_1 = self.create_line(self.central_widget, 0, 230, 600, 3)
        self.line_2 = self.create_line(self.central_widget, 0, 500, 600, 3)

        # Настройка и создание менюбара
        self.menu_bar = QMenuBar(self.main_window)
        self.menu = QMenu(self.menu_bar)
        self.instruction = QAction(self.menu)
        self.about = QAction(self.menu)
        self.exit = QAction(self.menu)
        self.setup_menu()
        self.main_window.setMenuBar(self.menu_bar)

        # Вызов диалогового окна Инструкций к программе
        self.dlg_instructions = QDialog(self.main_window)
        self.dlg_btn = QPushButton(self.dlg_instructions)


        # Вызов диалогового окна Описания к программе

        # Настройка и создание окна ввода диаметра
        self.widget_diameter = QWidget(self.central_widget)
        self.h_layout_diameter = QHBoxLayout(self.widget_diameter)
        self.diameter = QLineEdit(self.widget_diameter)
        self.setup_diameter()
        self.is_diameter = False

        # Настройка и создание чекбоксов
        self.widget_checkbox = QWidget(self.central_widget)
        self.v_layout_checkbox = QVBoxLayout(self.widget_checkbox)
        self.check_separate_graph = QCheckBox(self.widget_checkbox)
        self.check_inverse_graph = QCheckBox(self.widget_checkbox)
        self.setup_checkbox()

        # Настройка и создание области пути к файлу
        self.widget_path_to = QWidget(self.central_widget)
        self.h_layout_path_to = QHBoxLayout(self.widget_path_to)
        self.path_to_btn = QToolButton(self.widget_path_to)
        self.path_label = QLineEdit(self.widget_path_to)
        self.setup_path_to()
        self.is_path_to = False

        # Настройка и создание области ввода пути для сохранения результатов
        self.widget_path_out = QWidget(self.central_widget)
        self.h_layout_path_out = QHBoxLayout(self.widget_path_out)
        self.path_out_btn = QToolButton(self.widget_path_out)
        self.save_label = QLineEdit(self.widget_path_out)
        self.setup_path_out()

        # Настройка и создание области ввода названия готовых результатов
        self.widget_filename = QWidget(self.central_widget)
        self.h_layout_filename = QHBoxLayout(self.widget_filename)
        self.output_filename = QLineEdit(self.widget_filename)
        self.setup_filename()

        # Настройка и создание кнопки старта
        self.start_btn = QPushButton(self.central_widget)
        self.setup_start_btn()

        # Настройки и создание окна вывода информации
        self.output_inf = QPlainTextEdit(self.central_widget)
        self.setup_output_inf()

        # Настройка и создание статусбара
        self.status_bar = QStatusBar(self.central_widget)
        self.setup_status_bar()
        self.main_window.setStatusBar(self.status_bar)

    def setup_main(self, height: int, length: int):
        """Настрйка главного рабочего окна.
        """
        self.main_window.setObjectName("Main Window")
        self.main_window.setFixedSize(length, height)
        self.main_window.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.main_window.setWindowIcon(QIcon(os.path.join(os.getcwd(), 'image', 'IV_logo.png')))
        self.main_window.setWindowTitle("VAC plotter")

    def setup_menu(self):
        """Настройка меню.
        """
        self.menu_bar.setGeometry(QRect(0, 0, 602, 23))
        font = QFont()
        font.setPointSize(10)
        self.menu_bar.setFont(font)
        self.menu_bar.setStyleSheet("background-color: rgb(60, 63, 65);\n"
                                    "color: rgb(230, 230, 230);\n"
                                    "selection-background-color: rgb(0, 170, 255);")
        self.menu_bar.setObjectName("Menu Bar")

        # Кнопка "Меню"
        self.menu.setTitle("Меню")
        self.menu.setGeometry(QRect(339, 102, 183, 125))
        self.menu.setMouseTracking(True)
        self.menu.setStyleSheet("selection-background-color: rgb(0, 170, 255);")
        self.menu.setObjectName("Menu")

        # Кнопка "Инструкция"
        self.instruction.setText("Инструкция")
        self.instruction.setObjectName("instruction")
        self.instruction.setShortcut(QKeySequence('Ctrl+N'))

        # Кнопка "О программе"
        self.about.setText("О программе")
        self.about.setObjectName("about")
        self.about.setShortcut(QKeySequence('Ctrl+A'))

        # Кнопка "Выход"
        self.exit.setText("Выход")
        self.exit.setObjectName("exit")
        self.exit.setShortcut(QKeySequence('Esc'))

        # Расположение кнопок в Меню
        self.menu.addAction(self.instruction)
        self.menu.addAction(self.about)
        self.menu.addSeparator()
        self.menu.addAction(self.exit)
        self.menu_bar.addAction(self.menu.menuAction())

    def create_dialog_instructions(self):
        """Генерирует диалоговое окно после нажатия на кнопку инструкций.
        """
        w = 570
        h = 600
        self.dlg_instructions.setWindowTitle('Инструкции к программе')
        self.dlg_instructions.setFixedSize(w, h)

        text_html = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\">\n"\
                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"\
                    "p, li { white-space: pre-wrap; }\n"\
                    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"\
                    "<p align=\"justify\" style=\"-qt-paragraph-type:empty; font-size:8pt;\"><br /></p>\n"\
                    "<p align=\"justify\" style=\"margin-left:10px; margin-right:10px;\"><span style=\" font-size:10pt;\">Для успешного использования программы заполните все необходимые данные в полях ввода и нажмите кнопку </span><span style=\" font-size:10pt; font-weight:600;\">“START”</span><span style=\" font-size:10pt;\">. Минимальные и необходимые данные для начала работы:</span></p>\n"\
                    "<p align=\"justify\" style=\"margin-left:10px; margin-right:10px;\"><span style=\" font-size:10pt;\">            - диаметр в микрометрах;</span></p>\n"\
                    "<p align=\"justify\" style=\"margin-left:10px; margin-right:10px;\"><span style=\" font-size:10pt;\">            - путь к CSV файлу с данными для расчета.</span></p>\n"\
                    "<p align=\"justify\" style=\"margin-left:10px; margin-right:10px;\"><span style=\" font-size:10pt;\">Программа умеет работать только с файлами формата CSV, которые заполнены особым образом с помощью программы измерения вольт-амперных характеристик. </span></p>\n"\
                    "<p align=\"justify\" style=\"margin-left:10px; margin-right:10px;\"><span style=\" font-size:10pt;\">При работе с программой стоит учитывать: </span></p>\n"\
                    "<p align=\"justify\" style=\"margin-left:10px; margin-right:10px;\"><span style=\" font-size:10pt;\">- Если в одном CSV файле окажутся измерения с контактов разных диаметров, программа не сможет этого распознать и расчеты будут произведены неверно.</span></p>\n"\
                    "<p align=\"justify\" style=\"margin-left:10px; margin-right:10px;\"><span style=\" font-size:10pt;\">- При отсутствии пути для сохранения готовых файлов, результаты будут сохранены в папку с данной программой и разбиты на категории &quot;direct&quot; и &quot;reverse&quot;.</span></p>\n"\
                    "<p align=\"justify\" style=\"margin-left:10px; margin-right:10px;\"><span style=\" font-size:10pt;\">- Все сообщения об ошибках и результаты удачных расчетов можно найти в окне &quot;Сообщения программы&quot;.</span></p>\n"\
                    "<p align=\"justify\" style=\"font-size:10pt;\"><br /></p>\n"\
                    "<p align=\"justify\" style=\"margin-left:10px; margin-right:10px;\"><span style=\" font-size:11pt; font-weight:600;\">Дополнительные настройки:</span></p>\n"\
                    "<p align=\"justify\" style=\"margin-left:10px; margin-right:10px;\"><span style=\" font-size:10pt;\">Чекбокс &quot;Разбить на отдельные графики&quot; позволяет строить каждую кривую на собственной оси координат. Результат будет сохранен в отдельный файл. В противном случае все кривые будут построены на одной оси координат и сохранены в один файл.</span></p>\n"\
                    "<p align=\"justify\" style=\"margin-left:10px; margin-right:10px;\"><span style=\" font-size:10pt;\">Чекбокс &quot;Строить обратные кривые&quot; позволяет построить вольт-амперные характеристики из отрицательной зоны оси координат. Данные будут сохранены на отдельных файлах в папке &quot;reverse&quot;.</span></p>\n"\
                    "<p align=\"justify\" style=\"font-size:10pt;\"><br /></p>\n"\
                    "<p align=\"justify\" style=\"margin-left:10px; margin-right:10px;\"><span style=\" font-size:12pt; font-weight:600;\">Горячие клавиши: </span></p>\n"\
                    "<p align=\"justify\" style=\"margin-left:10px; margin-right:10px;\"><span style=\" font-size:10pt;\">Ctrl + N – Открыть инструкцию к программе.</span></p>\n"\
                    "<p align=\"justify\" style=\"margin-left:10px; margin-right:10px;\"><span style=\" font-size:10pt;\">Ctrl + A – Открыть описание программы.</span></p>\n"\
                    "<p align=\"justify\" style=\"margin-left:10px; margin-right:10px;\"><span style=\" font-size:10pt;\">Ctrl + O – Указать путь к файлу.</span></p>\n"\
                    "<p align=\"justify\" style=\"margin-left:10px; margin-right:10px;\"><span style=\" font-size:10pt;\">Ctrl + D – Указать директорию для сохранения данных.</span></p>\n"\
                    "<p align=\"justify\" style=\"margin-left:10px; margin-right:10px;\"><span style=\" font-size:10pt;\">Ctrl + S – Запустить расчет.</span></p>\n"\
                    "<p align=\"justify\" style=\"margin-left:10px; margin-right:10px;\"><span style=\" font-size:10pt;\">     Esc – Закрыть программу или активное окно.</span></p>" \
                    "<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"\
                    "</body></html>"

        text_edit = QTextBrowser(self.dlg_instructions)
        text_edit.setFixedSize(w, 559)
        text_edit.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        text_edit.setHtml(text_html)
        text_edit.setStyleSheet("background-color: rgb(60, 63, 65);\n"
                                "color: rgb(200, 200, 200);\n")

        # Настройка кнопки закрытия окна
        self.dlg_btn.setGeometry(QRect(0, 560, 600, 40))
        self.dlg_btn.setText('ОК')
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.dlg_btn.setFont(font)
        self.dlg_btn.setStyleSheet("background-color: #F4C430;\n"
                                   "color: rgb(40, 40, 40);")

        self.dlg_instructions.exec()

    def setup_diameter(self):
        """Настройка окна ввода диаметра контакта.
        """
        self.widget_diameter.setGeometry(QRect(40, 60, 271, 41))
        self.widget_diameter.setObjectName("Diameter Widget")

        self.h_layout_diameter.setContentsMargins(0, 0, 0, 0)
        self.h_layout_diameter.setObjectName("Horizontal Layout Diameter")

        label_diameter_text_1 = self.create_label(self.widget_diameter, 0, 0, 0, 0,
                                                  "Диаметр контакта:", pointsize=12)
        label_diameter_text_1.setAlignment(Qt.AlignmentFlag.AlignLeading |
                                           Qt.AlignmentFlag.AlignLeft |
                                           Qt.AlignmentFlag.AlignVCenter)
        self.h_layout_diameter.addWidget(label_diameter_text_1)

        self.diameter.setInputMask("0.0000")
        self.diameter.setText("0.0000")
        self.diameter.setWhatsThis("Введите диаметр контакта, на котором проводилось измерение (в микрометрах). "
                                   "Обязательный параметр!")
        font = QFont()
        font.setPointSize(11)
        self.diameter.setFont(font)
        self.diameter.setStyleSheet("background-color: rgb(60, 63, 65);\n"
                                    "color: rgb(225, 225, 225);")
        self.diameter.setObjectName("Diameter")
        self.h_layout_diameter.addWidget(self.diameter)

        label_diameter_text_2 = self.create_label(self.widget_diameter, 0, 0, 0, 0,
                                                  "мкм", pointsize=12)
        label_diameter_text_2.setAlignment(Qt.AlignmentFlag.AlignLeading |
                                           Qt.AlignmentFlag.AlignLeft |
                                           Qt.AlignmentFlag.AlignVCenter)
        self.h_layout_diameter.addWidget(label_diameter_text_2)

    def setup_checkbox(self):
        """Настройка чекбоксов.
        """
        self.widget_checkbox.setGeometry(QRect(40, 130, 281, 81))
        self.widget_checkbox.setObjectName("Checkbox Widget")

        self.v_layout_checkbox.setContentsMargins(0, 0, 0, 0)
        self.v_layout_checkbox.setObjectName("Vertical Layout Checkbox")

        self.check_separate_graph.setText("  Разбить на отдельные графики")
        self.check_separate_graph.setMinimumSize(QSize(0, 20))
        font = QFont()
        font.setPointSize(12)
        self.check_separate_graph.setFont(font)
        self.check_separate_graph.setStyleSheet("color: rgb(225, 225, 225);")
        self.check_separate_graph.setObjectName("Check Separate")
        self.check_separate_graph.setWhatsThis('Поставте галочку, если желаете, чтобы графики не объединялись '
                                               'на одной оси координат. Граифики будут построены по отдельности, '
                                               'в соответсвии с предоставленными данными.')
        self.v_layout_checkbox.addWidget(self.check_separate_graph)

        # Разделитель между чекбоксами
        spacer_item = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.v_layout_checkbox.addItem(spacer_item)

        self.check_inverse_graph.setText("  Строить обратные кривые")
        self.check_inverse_graph.setMinimumSize(QSize(0, 20))
        font = QFont()
        font.setPointSize(12)
        self.check_inverse_graph.setFont(font)
        self.check_inverse_graph.setStyleSheet("color: rgb(225, 225, 225);")
        self.check_inverse_graph.setObjectName("Check Inverse")
        self.check_inverse_graph.setWhatsThis('Поставте галочку, если желаете, чтобы были обработаны данные для '
                                              'обратных смещений.')
        self.v_layout_checkbox.addWidget(self.check_inverse_graph)

    def setup_path_to(self):
        """Настройка окна ввода пути к обрабатываемому файлу.
        """
        self.widget_path_to.setGeometry(QRect(40, 290, 522, 36))
        self.widget_path_to.setObjectName("Widget Path to")
        self.widget_path_to.setWhatsThis('Выберите CSV файл с иземерениями, либо укажите путь к нему.')

        self.h_layout_path_to.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.h_layout_path_to.setContentsMargins(0, 0, 0, 0)
        self.h_layout_path_to.setSpacing(10)
        self.h_layout_path_to.setObjectName("Horizontal Layout Path to")

        self.path_to_btn.setEnabled(True)
        size_policy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.path_to_btn.sizePolicy().hasHeightForWidth())
        self.path_to_btn.setSizePolicy(size_policy)
        self.path_to_btn.setMinimumSize(QSize(30, 30))
        self.path_to_btn.setText('...')
        font = QFont()
        font.setPointSize(10)
        self.path_to_btn.setFont(font)
        self.path_to_btn.setStyleSheet("background-color: #F4C430;\n"
                                       "selection-background-color: rgb(60, 63, 65);\n"
                                       "color: rgb(0, 0, 0);")
        self.path_to_btn.setShortcut(QKeySequence('Ctrl+O'))
        self.h_layout_path_to.addWidget(self.path_to_btn)

        self.path_label.setMaximumSize(QSize(16777215, 30))
        self.path_label.setText('  Путь к CSV файлу')
        font = QFont()
        font.setPointSize(10)
        self.path_label.setFont(font)
        self.path_label.setStyleSheet("background-color: rgb(60, 63, 65);\n"
                                      "color: rgb(225, 225, 225);")
        self.path_label.setAlignment(Qt.AlignmentFlag.AlignJustify |
                                     Qt.AlignmentFlag.AlignVCenter)
        self.path_label.setObjectName("Path Label")
        self.h_layout_path_to.addWidget(self.path_label)

    def setup_path_out(self):
        """Настройка области ввода пути для сохранения результатов.
        """
        self.widget_path_out.setGeometry(QRect(40, 390, 522, 36))
        self.widget_path_out.setObjectName("Widget Path out")
        self.widget_path_out.setWhatsThis('Выберите папку или впишите путь для сохранения результатов расчета.'
                                          ' Если конечная папка не будет выбрана, то результаты сохранятся в'
                                          ' директории программы.')

        self.h_layout_path_out.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.h_layout_path_out.setContentsMargins(0, 0, 0, 0)
        self.h_layout_path_out.setSpacing(10)
        self.h_layout_path_out.setObjectName("Horizontal Layout Path out")

        self.path_out_btn.setEnabled(True)
        size_policy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.path_out_btn.sizePolicy().hasHeightForWidth())
        self.path_out_btn.setSizePolicy(size_policy)
        self.path_out_btn.setMinimumSize(QSize(30, 30))
        self.path_out_btn.setText('...')
        font = QFont()
        font.setPointSize(10)
        self.path_out_btn.setFont(font)
        self.path_out_btn.setStyleSheet("background-color: #F4C430;\n"
                                        "selection-background-color: rgb(60, 63, 65);\n"
                                        "color: rgb(0, 0, 0);")
        self.path_out_btn.setShortcut(QKeySequence('Ctrl+D'))
        self.h_layout_path_out.addWidget(self.path_out_btn)

        self.save_label.setMaximumSize(QSize(16777215, 30))
        self.save_label.setText('  Путь сохранения данных')
        font = QFont()
        font.setPointSize(10)
        self.save_label.setFont(font)
        self.save_label.setStyleSheet("background-color: rgb(60, 63, 65);\n"
                                      "color: rgb(225, 225, 225);")
        self.save_label.setAlignment(Qt.AlignmentFlag.AlignJustify |
                                     Qt.AlignmentFlag.AlignVCenter)
        self.save_label.setObjectName("save_label")
        self.h_layout_path_out.addWidget(self.save_label)

    def setup_filename(self):
        """Настройка области ввода названия готовых файлов.
        """
        self.widget_filename.setGeometry(QRect(40, 450, 523, 32))
        self.widget_filename.setObjectName("Filename Widget")
        self.widget_filename.setWhatsThis('Впишите конечное имя для файлов с результатами для дальнейшей'
                                          ' идентификации.')

        self.h_layout_filename.setContentsMargins(0, 0, 0, 0)
        self.h_layout_filename.setObjectName("Horizontal Layout Filename")

        label_text = self.create_label(self.widget_filename, 0, 0, 0, 0,
                                       "Название готовых файлов:", pointsize=12)
        self.h_layout_filename.addWidget(label_text)

        spacer_item = QSpacerItem(10, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        self.h_layout_filename.addItem(spacer_item)

        self.output_filename.setMinimumSize(QSize(300, 30))
        self.output_filename.setText("  Введите название...")
        font = QFont()
        font.setPointSize(10)
        self.output_filename.setFont(font)
        self.output_filename.setStyleSheet("background-color: rgb(60, 63, 65);\n"
                                           "color: rgb(225, 225, 225);")
        self.output_filename.setObjectName("output_filename")
        self.h_layout_filename.addWidget(self.output_filename)

    def setup_start_btn(self):
        """Настройка кнокпи начала расчета.
        """
        self.start_btn.setGeometry(QRect(40, 536, 100, 100))
        self.start_btn.setText('START')
        font = QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.start_btn.setFont(font)
        self.start_btn.setStyleSheet("background-color: rgb(73, 156, 84);\n"
                                     "color: rgb(40, 40, 40);")
        self.start_btn.setObjectName("Start Button")
        self.start_btn.setWhatsThis('Нажать для начала процесса обработки данных файла.')
        self.start_btn.setShortcut(QKeySequence('Ctrl+S'))

    def setup_output_inf(self):
        """Настройка окна вывода информации для пользователя.
        """
        self.output_inf.setGeometry(QRect(180, 530, 383, 110))
        self.output_inf.setStyleSheet("background-color: rgb(60, 63, 65);\n"
                                      "color: rgb(200, 200, 200);\n"
                                      "text-align: bottom;")
        self.output_inf.setWhatsThis('Здесь выводятся сообщения для пользователя о работе программы и результатах'
                                     ' расчетов.')
        self.output_inf.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        self.output_inf.verticalScrollBar().setValue(self.output_inf.maximumHeight())
        self.output_inf.setPlainText('> Программа запущена. Удачных расчетов!')

    def setup_status_bar(self):
        """Настройка статус бара.
        """
        self.status_bar.setStyleSheet("color: rgb(150, 150, 150);\n"
                                      "background-color: rgb(60, 63, 65);\n")
        self.status_bar.setObjectName("Status Bar")
        my_message = QLabel(self.central_widget)
        my_message.setText(chr(169) + ' Created by Danio (2021)  ')
        self.status_bar.addPermanentWidget(my_message)

    @staticmethod
    def create_label(some_widget, x, y, length, height, text, bold=False, pointsize=None, weight=None,
                     background=None):
        """Генерирует статичную надпись.
        """
        label_text = QLabel(some_widget)
        label_text.setGeometry(QRect(x, y, length, height))
        label_text.setText(text)
        font = QFont()
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

    @staticmethod
    def create_line(some_widget, x, y, length, height):
        """Строит линию-разделитель.
        """
        line = QFrame(some_widget)
        line.setGeometry(QRect(x, y, length, height))
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)

        return line


if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.main_window.show()
    sys.exit(app.exec())
