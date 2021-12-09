import sys
from controller import Controller
from PyQt6.QtWidgets import QApplication


app = QApplication(sys.argv)
widget = Controller()
widget.main_window.show()
sys.exit(app.exec())