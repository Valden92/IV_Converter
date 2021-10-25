from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QMessageBox
import sys

from analitycal_func import analytical_run


class Ui_MainWindow(QWidget):

    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(602, 700)
        MainWindow.setStyleSheet("background-color: rgb(40, 40, 40);")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_text_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_text_3.setGeometry(QtCore.QRect(40, 260, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_text_3.setFont(font)
        self.label_text_3.setStyleSheet("color: rgb(225, 225, 225);")
        self.label_text_3.setObjectName("label_text_3")

        self.label_text_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_text_4.setGeometry(QtCore.QRect(40, 20, 451, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_text_4.setFont(font)
        self.label_text_4.setStyleSheet("color: rgb(225, 225, 225);\n")
        self.label_text_4.setObjectName("label_text_4")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 230, 602, 3))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")

        self.label_text_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_text_5.setGeometry(QtCore.QRect(40, 360, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_text_5.setFont(font)
        self.label_text_5.setStyleSheet("color: rgb(225, 225, 225);")
        self.label_text_5.setObjectName("label_text_5")

        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 390, 411, 36))
        self.layoutWidget.setObjectName("layoutWidget")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetNoConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.ButtonSave = QtWidgets.QToolButton(self.layoutWidget)
        self.ButtonSave.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonSave.sizePolicy().hasHeightForWidth())
        self.ButtonSave.setSizePolicy(sizePolicy)
        self.ButtonSave.setMinimumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ButtonSave.setFont(font)
        self.ButtonSave.setStyleSheet("background-color: rgb(60, 63, 65);\n"
                                      "selection-background-color: rgb(60, 63, 65);\n"
                                      "color: rgb(225, 225, 225);")
        self.ButtonSave.setObjectName("ButtonSave")
        self.horizontalLayout_2.addWidget(self.ButtonSave)
        self.ButtonSave.clicked.connect(self.path_to_save)

        self.save_label = QtWidgets.QLineEdit(self.layoutWidget)
        self.save_label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.save_label.setFont(font)
        self.save_label.setStyleSheet("background-color: rgb(60, 63, 65);\n"
                                      "color: rgb(225, 225, 225);")
        self.save_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignJustify | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.save_label.setObjectName("save_label")
        self.horizontalLayout_2.addWidget(self.save_label)

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 500, 602, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")

        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(40, 540, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.startButton.setFont(font)
        self.startButton.setStyleSheet("background-color: rgb(73, 156, 84);")
        self.startButton.setObjectName("startButton")
        self.startButton.clicked.connect(self.start_analytical_part)

        self.logging = QtWidgets.QLabel(self.centralwidget)
        self.logging.setGeometry(QtCore.QRect(180, 530, 381, 111))
        self.logging.setStyleSheet("background-color: rgb(60, 63, 65);")
        self.logging.setText("")
        self.logging.setObjectName("logging")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 530, 331, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 530, 381, 20))
        self.label_2.setStyleSheet("color: rgb(225, 225, 225);\n"
                                   "background-color: rgb(51, 72, 83);")
        self.label_2.setObjectName("label_2")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 60, 271, 41))
        self.widget.setObjectName("widget")

        self.horizontalLayout_diameter = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_diameter.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_diameter.setObjectName("horizontalLayout_diameter")

        self.label_text = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_text.setFont(font)
        self.label_text.setStyleSheet("color: rgb(225, 225, 225);")
        self.label_text.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_text.setObjectName("label_text")
        self.horizontalLayout_diameter.addWidget(self.label_text)

        self.diameter = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.diameter.setFont(font)
        self.diameter.setStyleSheet("background-color: rgb(60, 63, 65);\n"
                                    "color: rgb(225, 225, 225);")
        self.diameter.setObjectName("diameter")
        self.horizontalLayout_diameter.addWidget(self.diameter)

        self.label_text_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_text_2.setFont(font)
        self.label_text_2.setStyleSheet("color: rgb(225, 225, 225);")
        self.label_text_2.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_text_2.setObjectName("label_text_2")
        self.horizontalLayout_diameter.addWidget(self.label_text_2)

        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(40, 290, 411, 36))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.ButtonPath = QtWidgets.QToolButton(self.widget1)
        self.ButtonPath.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonPath.sizePolicy().hasHeightForWidth())
        self.ButtonPath.setSizePolicy(sizePolicy)
        self.ButtonPath.setMinimumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ButtonPath.setFont(font)
        self.ButtonPath.setStyleSheet("background-color: rgb(60, 63, 65);\n"
                                      "selection-background-color: rgb(60, 63, 65);\n"
                                      "color: rgb(225, 225, 225);")
        self.ButtonPath.setObjectName("ButtonPath")
        self.horizontalLayout.addWidget(self.ButtonPath)
        self.ButtonPath.clicked.connect(self.path_to_open)

        self.path_label = QtWidgets.QLineEdit(self.widget1)
        self.path_label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.path_label.setFont(font)
        self.path_label.setStyleSheet("background-color: rgb(60, 63, 65);\n"
                                      "color: rgb(225, 225, 225);")
        self.path_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignJustify | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.path_label.setObjectName("path_label")
        self.horizontalLayout.addWidget(self.path_label)

        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(40, 130, 281, 81))
        self.widget2.setObjectName("widget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.check_separate_graph = QtWidgets.QCheckBox(self.widget2)
        self.check_separate_graph.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.check_separate_graph.setFont(font)
        self.check_separate_graph.setStyleSheet("color: rgb(225, 225, 225);")
        self.check_separate_graph.setObjectName("check_separate_graph")
        self.verticalLayout.addWidget(self.check_separate_graph)

        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.check_inverse_graph = QtWidgets.QCheckBox(self.widget2)
        self.check_inverse_graph.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.check_inverse_graph.setFont(font)
        self.check_inverse_graph.setStyleSheet("color: rgb(225, 225, 225);")
        self.check_inverse_graph.setObjectName("check_inverse_graph")
        self.verticalLayout.addWidget(self.check_inverse_graph)

        self.widget3 = QtWidgets.QWidget(self.centralwidget)
        self.widget3.setGeometry(QtCore.QRect(40, 450, 523, 32))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.label_text_6 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_text_6.setFont(font)
        self.label_text_6.setStyleSheet("color: rgb(225, 225, 225);")
        self.label_text_6.setObjectName("label_text_6")
        self.horizontalLayout_3.addWidget(self.label_text_6)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)

        self.output_filename = QtWidgets.QLineEdit(self.widget3)
        self.output_filename.setMinimumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.output_filename.setFont(font)
        self.output_filename.setStyleSheet("background-color: rgb(60, 63, 65);\n"
                                           "color: rgb(225, 225, 225);")
        self.output_filename.setInputMask("")
        self.output_filename.setObjectName("output_filename")
        self.horizontalLayout_3.addWidget(self.output_filename)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 602, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("background-color: rgb(60, 63, 65);\n"
                                   "color: rgb(230, 230, 230);\n"
                                   "selection-background-color: rgb(0, 170, 255);")
        self.menubar.setObjectName("menubar")

        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setGeometry(QtCore.QRect(339, 102, 183, 125))
        self.menu.setMouseTracking(True)
        self.menu.setStyleSheet("selection-background-color: rgb(0, 170, 255);")
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("background-color: rgb(60, 63, 65);")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.instraction = QtGui.QAction(MainWindow)
        self.instraction.setObjectName("instraction")
        self.about = QtGui.QAction(MainWindow)
        self.about.setObjectName("about")
        self.exit = QtGui.QAction(MainWindow)
        self.exit.setObjectName("exit")
        self.exit.triggered.connect(self.close_window)

        self.menu.addAction(self.instraction)
        self.menu.addAction(self.about)
        self.menu.addSeparator()
        self.menu.addAction(self.exit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IV Converter"))
        self.label_text_3.setText(_translate("MainWindow", "Открыть файл:"))
        self.label_text_4.setText(_translate("MainWindow", "Основные настройки расчета и построения графиков"))
        self.label_text_5.setText(_translate("MainWindow", "Указать папку для сохранения данных:"))
        self.ButtonSave.setText(_translate("MainWindow", "..."))
        self.save_label.setText(_translate("MainWindow", "  Путь сохранения данных"))
        self.startButton.setText(_translate("MainWindow", "START"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "  Результаты"))
        self.label_text.setText(_translate("MainWindow", "Диаметр контакта:"))
        self.diameter.setInputMask(_translate("MainWindow", "0.0000"))
        self.diameter.setText(_translate("MainWindow", "0.0000"))
        self.label_text_2.setText(_translate("MainWindow", "мкм"))
        self.ButtonPath.setText(_translate("MainWindow", "..."))
        self.path_label.setText(_translate("MainWindow", "  Файл..."))
        self.check_separate_graph.setText(_translate("MainWindow", "  Разбить на отдельные графики"))
        self.check_inverse_graph.setText(_translate("MainWindow", "  Строить обратные кривые"))
        self.label_text_6.setText(_translate("MainWindow", "Название готовых файлов:"))
        self.output_filename.setText(_translate("MainWindow", "  File Name..."))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.instraction.setText(_translate("MainWindow", "Инструкция"))
        self.about.setText(_translate("MainWindow", "О программе"))
        self.exit.setText(_translate("MainWindow", "Выход"))

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

    def close_window(self):
        """Закрывает приложение.
        """
        reply = QMessageBox(self)
        reply.setWindowTitle("Выход")
        reply.setText("Завершить работу с приложением?")
        reply.setIcon(QMessageBox.Icon.Question)

        yesButton = reply.addButton("Выйти", reply.ButtonRole.ActionRole)
        noButton = reply.addButton("Остаться", reply.ButtonRole.NoRole)

        reply.exec()

        if reply.clickedButton() == yesButton:
            app.exit()

    def start_analytical_part(self):
        """Начинает парсинг и расчет документа.
        """
        if float(self.diameter.text()) <= 0:
            print('Не указан диаметер контакта.')

        if '.csv' not in self.path_label.text():
            print('Файл не выбран или выбран не верно.')

        analytical_run(self.path_label.text(),
                       self.diameter.text(),
                       self.check_separate_graph.isChecked(),
                       self.check_inverse_graph.isChecked(),
                       self.save_label.text(),
                       self.output_filename.text()
                       )


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec())
