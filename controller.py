import os
import sys

from views import MainWindow
from analytical_model import AnalyticalModel

from PyQt6.QtWidgets import QApplication, QMessageBox, QFileDialog
from PyQt6.QtCore import QProcess


class Controller(MainWindow):

    def __init__(self):
        super().__init__()

        # Атрибуты управления процессами
        self.process = None
        self.process_2 = None
        self.last_message = None

        # Меню
        self.instruction.triggered.connect(self.open_instructions)
        self.dlg_btn.released.connect(self.close_instructions)
        self.about.triggered.connect(self.open_about)
        self.exit.triggered.connect(self.exit_program)

        # Диаметр
        self.diameter.textChanged.connect(self.diameter_changed)
        self.is_diameter = False

        # Чекбоксы
        self.check_separate_graph.clicked.connect(self.sep_graph_changed)
        self.check_inverse_graph.clicked.connect(self.inv_graph_changed)

        # Путь к файлу
        self.path_to_btn.clicked.connect(self.open_file)
        self.path_label.textChanged.connect(self.path_label_changed)
        self.is_path_to = False

        # Путь для сохранения данных
        self.path_out_btn.clicked.connect(self.save_output)
        self.save_label.textChanged.connect(self.save_label_changed)

        # Название готовых результатов расчета
        self.output_filename.textChanged.connect(self.output_changed)

        # Кнопка начала расчета
        self.start_btn.released.connect(self.start_calculation)
        self.is_start_process = False
        self.process_error = False

    def open_instructions(self):
        if self.process is None:
            self.process_start('> Вы открыли инструкции к программе.',
                               'Instructions have been opened')
            self.create_dialog_instructions()

    def close_instructions(self):
        if self.process is None:
            self.process_start('> Окно инструкций закрыто.',
                               'Instructions window closed')
            self.dlg_instructions.close()

    def open_about(self):
        if self.process is None:
            self.process_start('> Вы открыли описание программы.',
                               'The description of the program has been opened')

    def exit_program(self):
        if self.process is None:
            self.process_start('> Вы пытаетесь покинуть программу.',
                               'Exiting the program?')
            self.create_exit_message()

    def diameter_changed(self):
        if self.process is None:
            self.process_start('> Вы изменили диметр контакта.',
                               'Contact diameter has been changed')

    def sep_graph_changed(self):
        if self.process is None:
            if self.check_separate_graph.isChecked():
                self.process_start('> Все графики будут построены по отдельности.',
                                   'Plot separator changed')
            else:
                self.process_start('> Все графики будут построены на одной оси координат.',
                                   'Plot separator changed')

    def inv_graph_changed(self):
        if self.process is None:
            if self.check_inverse_graph.isChecked():
                self.process_start('> Будут построены кривые из отрицательной области ВАХ.',
                                   'Inversion check changed')
            else:
                self.process_start('> Кривые из отрицательной области ВАХ не будут построены.',
                                   'Inversion check changed')

    def open_file(self):
        if self.process is None:
            self.process_start('> Укажите корректный путь к CSV файлу.',
                               'Specifying the path to the CSV file')

            path_to_file = QFileDialog.getOpenFileName(filter='*.csv')[0]
            if path_to_file:
                self.path_label.setText(path_to_file)

    def path_label_changed(self):
        if self.process is None:
            self.process_start('> Путь к файлу изменен.',
                               'File path changed')

    def save_output(self):
        if self.process is None:
            self.process_start('> Укажите корректный путь для сохранения конечных данных.',
                               'Changing the destination path for saving data')

            path_to_dir = QFileDialog.getExistingDirectory()
            if path_to_dir:
                self.save_label.setText(path_to_dir)

    def save_label_changed(self):
        if self.process is None:
            self.process_start('> Путь для сохранения данных изменен.',
                               'Path for saving data has been changed')

    def output_changed(self):
        if self.process is None:
            self.process_start('> Название конечных файлов применено.',
                               'File names changed')

    def start_calculation(self):
        if self.process is None:
            self.is_start_process = True
            self.start_btn.setEnabled(False)

            if self.last_message != '> Процесс расчета запущен. Ожидайте...':
                self.last_message = '> Процесс расчета запущен. Ожидайте...'
                self.output_inf.appendPlainText('> Процесс расчета запущен. Ожидайте...')
            self.status_bar.showMessage('Starting the calculation process')
            self.process = QProcess()
            self.process.start('python3')
            self.process.finished.connect(self.process_finished)

    def process_start(self, text_1, text_2):
        if self.last_message != text_1:
            self.last_message = text_1
            self.output_inf.appendPlainText(text_1)
        self.status_bar.showMessage(text_2)
        self.process = QProcess()
        self.process.start('python3')
        self.process.finished.connect(self.process_finished)

    def process_finished(self):

        if self.is_start_process and self.process_2 is None:
            self.validation()
            self.process_2 = QProcess()
            self.process_2.start('python3')
            if not self.is_diameter or not self.is_path_to:
                self.last_message = '> Упс, что-то пошло не так. Расчет не удался.'
                self.output_inf.appendPlainText('> Упс, что-то пошло не так. Расчет не удался.')
                self.status_bar.showMessage('Calculation failed')
                self.process_2.finished.connect(self.process_2_finished)
            else:
                self.run_calculate()
                if self.process_error:
                    self.last_message = '> Ошибка загрузки файла. Расчет не удался.'
                    self.output_inf.appendPlainText('> Ошибка загрузки файла. Расчет не удался.')
                    self.status_bar.showMessage('Calculation failed')
                    self.process_2.finished.connect(self.process_2_finished)
                else:
                    self.last_message = '> Расчет завершен успешно.'
                    self.output_inf.appendPlainText('> Расчет завершен успешно.')
                    self.status_bar.showMessage('Calculation completed successfully')
                    self.process_2.finished.connect(self.process_2_finished)

            self.is_start_process = False
            self.process_error = False
            self.start_btn.setEnabled(True)
        self.process = None

    def process_2_finished(self):
        self.process_2 = None

    def create_exit_message(self):
        """Генерирует окно выхода из программы.
        """
        reply = QMessageBox(self.main_window)
        reply.setStyleSheet("color: rgb(200, 200, 200);\n"
                            "background-color: rgb(60, 63, 65);")
        reply.setWindowTitle("Выход")
        reply.setText("Завершить работу с приложением?")
        reply.setIcon(QMessageBox.Icon.Question)

        yes_btn = reply.addButton("Выйти", reply.ButtonRole.ActionRole)
        yes_btn.setStyleSheet("background-color: #F4C430;\n"
                              "color: black;")

        no_btn = reply.addButton("Остаться", reply.ButtonRole.NoRole)
        no_btn.setStyleSheet("background-color: #F4C430;\n"
                             "color: black;")

        reply.exec()

        if reply.clickedButton() == yes_btn:
            app.exit()

    def validation(self):
        if float(self.diameter.text()) > 0:
            self.is_diameter = True
        else:
            self.is_diameter = False
            self.output_inf.appendPlainText('> Не указан диматер контакта!')

        if '.csv' not in self.path_label.text() or not os.path.isfile(self.path_label.text()):
            self.is_path_to = False
            self.output_inf.appendPlainText('> Файл для расчета указан не верно или не указан!')
        else:
            self.is_path_to = True

    def run_calculate(self):
        if self.is_diameter and self.is_path_to:
            calc_obj = AnalyticalModel(
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
                self.process_error = True
                self.last_message = '> Файл не найден!'
                self.output_inf.appendPlainText('> Файл не найден!')
            except UnicodeError:
                self.process_error = True
                self.last_message = '> Файл пустой или выбран неверно!'
                self.output_inf.appendPlainText('> Файл пустой или выбран неверно!')
            else:
                self.visual_result(calc_obj)

    def visual_result(self, calc_obj):
        """Выводит результаты расчетов в Лог.
        """
        for i in range(len(calc_obj.b.keys())):
            text = '> {}) φ = {} эВ,' \
                   ' b = {} А,' \
                   ' n = {}.'.format(str(i+1),
                                     calc_obj.special_rounder(calc_obj.fi[i]),
                                     calc_obj.special_rounder(calc_obj.b[i]),
                                     calc_obj.special_rounder(calc_obj.n[i]))
            self.last_message = text
            self.output_inf.appendPlainText(text)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    widget = Controller()
    widget.main_window.show()
    sys.exit(app.exec())
