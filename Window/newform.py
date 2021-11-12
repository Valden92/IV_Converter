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

        # Настройки окна ввода диаметра
        self.widget_diameter = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayout_diameter = QtWidgets.QHBoxLayout(self.widget_diameter)
        self.label_diameter_text_1 = QtWidgets.QLabel(self.widget_diameter)
        self.diameter = QtWidgets.QLineEdit(self.widget_diameter)
        self.label_diameter_text_2 = QtWidgets.QLabel(self.widget_diameter)

        # Настройки чекбоксов
        self.widget_checkbox = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_checkbox)
        self.check_separate_graph = QtWidgets.QCheckBox(self.widget_checkbox)
        self.check_inverse_graph = QtWidgets.QCheckBox(self.widget_checkbox)

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
        self.createLabel_text(40, 20, 451, 21,
                              "Основные настройки расчета и построения графиков",
                              bold=True, pointsize=12, weight=75)
        self.widget_diameter = self.createDiameter_widget()
        self.widget_checkbox = self.createCheckbox_widgets()
        self.createLine(0, 230, self.length_window, 3)
        self.createLabel_text(40, 260, 121, 21,
                              "Открыть файл:",
                              pointsize=12)
        self.createLine(0, 500, self.length_window, 3)

        self.MainWindow.setCentralWidget(self.createCentral_widget())

        self.MainWindow.setStatusBar(self.createStatusbar())

    def createCentral_widget(self):
        self.centralwidget.setObjectName("centralwidget")
        return self.centralwidget

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
        self.instruction.setObjectName("instraction")

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

    def createLabel_text(self, x, y, length, height, text, bold=False, pointsize=None, weight=None):
        """Надпись, указывающая на основные настройки расчета.
        """
        label_text = QtWidgets.QLabel(self.centralwidget)
        label_text.setGeometry(QtCore.QRect(x, y, length, height))
        label_text.setText(text)
        font = QtGui.QFont()
        if pointsize:
            font.setPointSize(pointsize)
        font.setBold(bold)
        if weight:
            font.setWeight(weight)
        label_text.setFont(font)
        label_text.setStyleSheet("color: rgb(225, 225, 225);")

        return label_text

    def createDiameter_widget(self):
        """Создает окно ввода диаметра контакта.
        """
        self.widget_diameter.setGeometry(QtCore.QRect(40, 60, 271, 41))
        self.widget_diameter.setObjectName("widget")

        self.horizontalLayout_diameter.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_diameter.setObjectName("horizontalLayout_diameter")

        self.label_diameter_text_1.setText("Диаметр контакта:")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_diameter_text_1.setFont(font)
        self.label_diameter_text_1.setStyleSheet("color: rgb(225, 225, 225);")
        self.label_diameter_text_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading |
                                                QtCore.Qt.AlignmentFlag.AlignLeft |
                                                QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_diameter_text_1.setObjectName("label_diameter_text_1")
        self.horizontalLayout_diameter.addWidget(self.label_diameter_text_1)

        self.diameter.setInputMask("0.0000")
        self.diameter.setText("0.0000")
        font = QtGui.QFont()
        font.setPointSize(11)
        self.diameter.setFont(font)
        self.diameter.setStyleSheet("background-color: rgb(60, 63, 65);\n"
                                    "color: rgb(225, 225, 225);")
        self.diameter.setObjectName("diameter")
        self.horizontalLayout_diameter.addWidget(self.diameter)

        self.label_diameter_text_2.setText("мкм")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_diameter_text_2.setFont(font)
        self.label_diameter_text_2.setStyleSheet("color: rgb(225, 225, 225);")
        self.label_diameter_text_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading |
                                                QtCore.Qt.AlignmentFlag.AlignLeft |
                                                QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_diameter_text_2.setObjectName("label_diameter_text_2")
        self.horizontalLayout_diameter.addWidget(self.label_diameter_text_2)

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

        return self.check_inverse_graph

    def createLine(self, x, y, length, height):
        """Строит линию-разделитель в окне по передаваемым параметрам.
        """
        line = QtWidgets.QFrame(self.centralwidget)
        line.setGeometry(QtCore.QRect(x, y, length, height))
        line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        return line

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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show_window()
    sys.exit(app.exec())
