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

        # Менюбар
        self.menubar = QtWidgets.QMenuBar(self.MainWindow)
        self.menu = QtWidgets.QMenu(self.menubar)
        self.instraction = QtGui.QAction(self.MainWindow)
        self.about = QtGui.QAction(self.MainWindow)
        self.exit = QtGui.QAction(self.MainWindow)

        # Статусбар
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)


    def setupUi(self):
        """Основные настройки.
        """
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(602, 700)
        self.MainWindow.setFixedSize(602, 700)
        self.MainWindow.setStyleSheet("background-color: rgb(40, 40, 40);")
        self.MainWindow.setWindowIcon(QtGui.QIcon(os.path.join(os.getcwd(), 'image', 'IV_logo.png')))
        self.MainWindow.setWindowTitle("IV Converter")
        self.MainWindow.setCentralWidget(self.centralwidget)

        self.MainWindow.setMenuBar(self.createMenu())
        self.MainWindow.setStatusBar(self.createStatusbar())

        self.MainWindow.show()

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
        self.instraction.setText("Инструкция")
        self.instraction.setObjectName("instraction")

        # Кнопка "О программе"
        self.about.setText("О программе")
        self.about.setObjectName("about")

        # Кнопка "Выход"
        self.exit.setText("Выход")
        self.exit.setObjectName("exit")
        self.exit.triggered.connect(self.close_window)

        # Расположение кнопок в Меню
        self.menu.addAction(self.instraction)
        self.menu.addAction(self.about)
        self.menu.addSeparator()
        self.menu.addAction(self.exit)
        self.menubar.addAction(self.menu.menuAction())

        return self.menubar

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

    def close_window(self):
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
    ui.setupUi()
    sys.exit(app.exec())
