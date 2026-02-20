import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QGroupBox, QScrollArea, QMessageBox
from practicies import practica1, practica2, practica3, practica41, practica42, practica43, practica5, practica71, practica72, practica73, practica74, practica8
from main_ui import Ui_MainWindow
from utils import check_and_process_matrix, extract_matrix_from_table, IntOnlyDelegate, resource_path
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import os


class Praсticies(QMainWindow):
    def __init__(self):
        super(Praсticies, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Связываем сигнал изменения спинбокса с обработчиком

        self.ui.spinBox.valueChanged.connect(self.update_table_dimensions_p1)
        self.ui.p3_count_m.valueChanged.connect(
            self.update_table_dimensions_p3_m)
        self.ui.p3_count_n.valueChanged.connect(
            self.update_table_dimensions_p3_n)

        # Использовать делегат для нужного столбца таблицы

        self.ui.tableWidget.setItemDelegate(IntOnlyDelegate())
        self.ui.p3_tableInput_1.setItemDelegate(IntOnlyDelegate())
        self.ui.p3_tableInput_2.setItemDelegate(IntOnlyDelegate())

        # Соединяем действия меню с обработчиком open_practice
        # Задача коммивояжера (Практика-1)

        self.ui.action1.triggered.connect(
            lambda _: self.open_practice(0))

        # K-means кластеризация (Практика-2)

        self.ui.action2.triggered.connect(
            lambda _: self.open_practice(1))

        # Композиционное правило Max-min (Практика-3)

        self.ui.action3.triggered.connect(
            lambda _: self.open_practice(2))

        # Функция принадлежности (Практика-4-1)

        self.ui.action4_1.triggered.connect(
            lambda _: self.open_practice(3))

        # Функция принадлежности (Практика-4-2)

        self.ui.action4_2.triggered.connect(
            lambda _: self.open_practice(4))

        # Функция принадлежности (Практика-4-3)

        self.ui.action4_3.triggered.connect(
            lambda _: self.open_practice(5))

        # Нейронная сеть (Практика-5)

        self.ui.action5.triggered.connect(
            lambda _: self.open_practice(6))

        # Расчет групповых оценок мероприятий (Практика-7) Часть 1

        self.ui.action7_1.triggered.connect(
            lambda _: self.open_practice(7))

        # Расчет групповых оценок мероприятий (Практика-7) Часть 2

        self.ui.action7_2.triggered.connect(
            lambda _: self.open_practice(8))

        # Расчет групповых оценок мероприятий (Практика-7) Часть 3

        self.ui.action7_3.triggered.connect(
            lambda _: self.open_practice(9))

        # Расчет групповых оценок мероприятий (Практика-7) Часть 4

        self.ui.action7_4.triggered.connect(
            lambda _: self.open_practice(10))

        # Принятие решений методом анализа иерархий (Практика-8)

        self.ui.action8.triggered.connect(
            lambda _: self.open_practice(11))
        self.ui.step2_p8.clicked.connect(lambda _:  self.open_practice(12))
        self.ui.step1_p8.clicked.connect(lambda _:  self.open_practice(11))

        # О программе
        self.ui.action9.triggered.connect(

            lambda _: self.open_practice(13))
        # Теория
        self.ui.action10.triggered.connect(
            lambda _:  self.open_practice(14))

        # Практика 1

        self.ui.pushButton.clicked.connect(self.practice1)
        self.update_table_dimensions_p1(self.ui.spinBox.value())

        # Практика 2

        self.fig = Figure(figsize=(5, 4))
        self.canvas = FigureCanvas(self.fig)
        self.ui.verticalLayout_3.addWidget(self.canvas)

        # Инициализация переменных

        self.num_points_spin = self.ui.num_points_spin
        self.num_clusters_spin = self.ui.num_clusters_spin
        self.points = None
        self.clusters = None
        self.kmeans = None
        self.current_step = 0

        # Подключение сигналов

        self.ui.run_button.clicked.connect(self.run_algorithm)
        self.ui.step_button.clicked.connect(self.step_algorithm)
        self.ui.reset_button.clicked.connect(self.reset)

        # инициализация таблиц

        self.update_table_dimensions_p3_m(self.ui.p3_count_m.value())
        self.update_table_dimensions_p3_n(self.ui.p3_count_n.value())

        # Практика 3

        self.ui.p3_run_button.clicked.connect(self.practica3)

        # Практика 4.1

        self.averages = []
        self.fig41 = Figure(figsize=(5, 5))
        self.canvas41 = FigureCanvas(self.fig41)
        self.ui.verticalLayout_5.addWidget(self.canvas41)

        self.ui.run_p4.clicked.connect(self.run_p4_1)
        self.ui.reset_p4.clicked.connect(self.reset_p4_1)

        # Практика 4.2
        self.main_layout_p4_1 = self.ui.page4_2.layout()

        self.group_box_table_input_p4_2 = QGroupBox("")
        self.group_box_table_input_layout_p4_2 = QVBoxLayout(
            self.group_box_table_input_p4_2)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.group_box_table_input_p4_2)

        self.main_layout_p4_1.addWidget(scroll_area)  # type: ignore

        self.fig42 = Figure(figsize=(5, 5))
        self.canvas42 = FigureCanvas(self.fig42)
        self.main_layout_p4_1.addWidget(self.canvas42)  # type: ignore

        practica42.update_tables(self, self.ui.count_exprets_p4_2.value())

        self.ui.count_exprets_p4_2.valueChanged.connect(self.update_tables)
        self.ui.count_params_p4_2.valueChanged.connect(
            self.update_column_tables)
        self.ui.count_terms_p4_2.valueChanged.connect(self.update_row_tables)
        self.ui.run_p4_2.clicked.connect(self.run_p4_2)
        # Практика 4.3
        self.fig43 = Figure(figsize=(5, 4))
        self.canvas43 = FigureCanvas(self.fig43)
        layout_p4_3 = self.ui.page4_3.layout()
        layout_p4_3.addWidget(self.canvas43)  # type: ignore
        self.ui.run_p4_3.clicked.connect(self.run_p4_3)
        # Практика 5

        self.p5 = {}
        self.p5['training_epochs'] = 0
        self.p5['learning_rate'] = 0
        self.p5['tolerance_error'] = 0
        self.ui.training_epochs.valueChanged.connect(self.changeTrainingEpochs)
        self.ui.learning_rate.valueChanged.connect(self.changeLearningRate)
        self.ui.tolerance_error.valueChanged.connect(self.changeToleranceError)

        self.ui.run_training.clicked.connect(self.run_train_p5)
        self.ui.run_test_model.clicked.connect(self.run_test_p5)

        # Практика 7.1

        self.ui.count_experts_p7_1.valueChanged.connect(
            self.changeCountExperts_p7_1)
        self.ui.run_p7_1.clicked.connect(self.run_p7_1)

        # Практика 7.2
        self.ui.count_experts_p7_2.valueChanged.connect(
            self.changeCountExperts_p7_2)
        self.ui.count_event_p7_2.valueChanged.connect(
            self.changeCountEvents_p7_2)
        self.ui.run_p7_2.clicked.connect(self.run_p7_2)

        # Практика 7.3

        self.main_layout_p7_3 = self.ui.page7_3.layout()

        self.group_box_table_input_p7_3 = QGroupBox("")
        self.group_box_table_input_layout_p7_3 = QVBoxLayout(
            self.group_box_table_input_p7_3)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.group_box_table_input_p7_3)

        self.main_layout_p7_3.addWidget(scroll_area)  # type: ignore

        practica73.update_tables(self, self.ui.count_experts_p7_3.value())

        self.ui.count_experts_p7_3.valueChanged.connect(
            self.update_tables_p7_3)
        self.ui.count_factors_p7_3.valueChanged.connect(
            self.update_size_tables_p7_3)
        self.ui.run_p7_3.clicked.connect(self.run_p7_3)

        # Практика 7.4
        self.ui.count_experts_p7_4.valueChanged.connect(
            self.changeCountExperts_p7_4)
        self.ui.count_factors_p7_4.valueChanged.connect(
            self.changeCountFactors_p7_4)
        self.ui.run_p7_4.clicked.connect(self.run_p7_4)

        # Практика 8-1

        self.ui.reset_p8.clicked.connect(self.reset_p8)
        self.ui.run_step1_p8.clicked.connect(self.run_step1_p8)
        self.ui.input1_p8.valueChanged.connect(
            self.update_table_input1_p8)

        # Практика 8-2
        self.main_layout_p8_2 = self.ui.page8_2.layout()

        self.group_box_table_input_p8_2 = QGroupBox("")
        self.group_box_table_input_layout_p8_2 = QVBoxLayout(
            self.group_box_table_input_p8_2)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.group_box_table_input_p8_2)

        self.main_layout_p8_2.addWidget(scroll_area)  # type: ignore

        self.ui.run_step2_p8.clicked.connect(self.run_step2_p8)
        self.ui.reset2_p8.clicked.connect(self.reset2_p8)
        self.ui.input2_p8.valueChanged.connect(
            self.update_table_input2_p8)
        self.ui.run_step3_p8.clicked.connect(self.run_step3_p8)

        # Теория

        THEORY_PATH = resource_path('theory')

        # Загрузка HTML-документов
        self.ui.doc1.load(f'file:///{THEORY_PATH}/1.htm')
        self.ui.doc2.load(f'file:///{THEORY_PATH}/2.htm')
        self.ui.doc3.load(f'file:///{THEORY_PATH}/3.htm')
        self.ui.doc4.load(f'file:///{THEORY_PATH}/4.htm')
        self.ui.doc5.load(f'file:///{THEORY_PATH}/5.htm')
        self.ui.doc7.load(f'file:///{THEORY_PATH}/7.htm')
        self.ui.doc8.load(f'file:///{THEORY_PATH}/8.htm')

    def open_practice(self, index):
        self.ui.stackedPages.setCurrentIndex(index)

    # Работа с таблицами (изменение и т.д.)

    def update_table_dimensions_p1(self, value):
        self.ui.tableWidget.setRowCount(value)
        self.ui.tableWidget.setColumnCount(value)

    def update_table_dimensions_p3_m(self, value):
        practica3.update_table_dimensions(self, value, "m")

    def update_table_dimensions_p3_n(self, value):
        practica3.update_table_dimensions(self, value, "n")

    # ---------1----------

    def practice1(self):
        if check_and_process_matrix(self, self.ui.tableWidget):
            distance_matrix = extract_matrix_from_table(self.ui.tableWidget)
            practica1.solve_tsp(self, distance_matrix)

    # ----------2---------
    def run_algorithm(self):
        practica2.run_algorithm(self)

    def step_algorithm(self):
        practica2.step_algorithm(self)

    def reset(self):
        practica2.reset(self)

    # ----------3---------

    def practica3(self):
        if check_and_process_matrix(self, self.ui.p3_tableInput_1) and check_and_process_matrix(self, self.ui.p3_tableInput_2):
            practica3.composite_max_min(self)

    # ----------4-1---------
    def reset_p4_1(self):
        practica41.reset_p4(self)

    def run_p4_1(self):
        if check_and_process_matrix(self, self.ui.table_p41):
            matrix_p4 = extract_matrix_from_table(self.ui.table_p41)
            practica41.on_calculate_average(self, matrix_p4)

    # ----------4-2---------
    def run_p4_2(self):
        practica42.run_expert_mark(self)

    def update_tables(self, count_tables):
        self.clear_layout(self.group_box_table_input_layout_p4_2)
        practica42.update_tables(self, count_tables)

    def update_column_tables(self, count_colums):
        practica42.update_column_tables(self, count_colums)

    def update_row_tables(self, count_rows):
        practica42.update_row_tables(self, count_rows)
    # ----------4-3---------

    def run_p4_3(self):
        a = self.ui.input_a_p4_3.value()
        b = self.ui.input_b_p4_3.value()
        c = self.ui.input_c_p4_3.value()
        x_start = self.ui.input_x_start_p4_3.value()
        x_end = self.ui.input_x_end_p4_3.value()
        practica43.triangular_membership_function(
            self, a, b, c, x_start, x_end)
    # ------------5-------------

    def changeTrainingEpochs(self, value):
        self.p5['training_epochs'] = value

    def changeLearningRate(self, value):
        self.p5['learning_rate'] = value

    def changeToleranceError(self, value):
        self.p5['tolerance_error'] = value

    def run_train_p5(self):
        if check_and_process_matrix(self, self.ui.train_table):
            data = extract_matrix_from_table(self.ui.train_table)
            inputs = [x[:-1] for x in data]
            targets = [x[-1] for x in data]
            practica5.train(self, inputs, targets, self.p5)

    def run_test_p5(self):
        if check_and_process_matrix(self, self.ui.input):
            input = extract_matrix_from_table(self.ui.input)
            prediction, _ = practica5.forward_pass(input)
            QMessageBox.information(
                self, "Вывод нейронной сети:", f'{prediction.item():.4f}')

    # ------------7.1-------------

    def run_p7_1(self):
        self.ui.output_p7_1.clear()
        if check_and_process_matrix(self, self.ui.input_table_p7_1):
            values = extract_matrix_from_table(self.ui.input_table_p7_1)
            accuracy = self.ui.accuracy_p7_1.value()
            resultat = practica71.run(values, accuracy)
            self.ui.output_p7_1.append(resultat)

    def changeCountExperts_p7_1(self, value):
        self.ui.input_table_p7_1.setRowCount(value)
        self.ui.input_table_p7_1.setColumnCount(value)
        headers = [
            f"Эксперт {i+1}" for i in range(value)]
        self.ui.input_table_p7_1.setHorizontalHeaderLabels(headers)
        self.ui.input_table_p7_1.setVerticalHeaderLabels(headers)
    # ------------7.2-------------

    def run_p7_2(self):
        self.ui.output_p7_2.clear()
        if check_and_process_matrix(self, self.ui.input_table_p7_2):
            values = extract_matrix_from_table(self.ui.input_table_p7_2)
            accuracy = self.ui.accuracy_p7_2.value()
            resultat = practica72.run(values, accuracy)
            self.ui.output_p7_2.append(resultat)

    def changeCountExperts_p7_2(self, value):
        self.ui.input_table_p7_2.setColumnCount(value)
        headers = [
            f"Эксперт {i+1}" for i in range(value)]
        self.ui.input_table_p7_2.setHorizontalHeaderLabels(headers)

    def changeCountEvents_p7_2(self, value):
        self.ui.input_table_p7_2.setRowCount(value)
        headers = [
            f"Мероприятие {i+1}" for i in range(value)]
        self.ui.input_table_p7_2.setVerticalHeaderLabels(headers)
    # ------------7.3-------------

    def update_tables_p7_3(self, count_tables):
        self.clear_layout(self.group_box_table_input_layout_p7_3)
        practica73.update_tables(self, count_tables)

    def update_size_tables_p7_3(self, size_tables):
        practica73.update_size_tables(self, size_tables)

    def run_p7_3(self):
        self.ui.output_p7_3.clear()
        accuracy = self.ui.accuracy_p7_3.value()
        practica73.run(self, accuracy)

    # ------------7.4-------------
    def changeCountExperts_p7_4(self, value):
        self.ui.input_table_p7_4.setColumnCount(value)
        headers = [
            f"Эксперт {i+1}" for i in range(value)]
        self.ui.input_table_p7_4.setHorizontalHeaderLabels(headers)

    def changeCountFactors_p7_4(self, value):
        self.ui.input_table_p7_4.setRowCount(value)
        headers = [
            f"Фактор {i+1}" for i in range(value)]
        self.ui.input_table_p7_4.setVerticalHeaderLabels(headers)

    def run_p7_4(self):
        self.ui.output_p7_4.clear()
        if check_and_process_matrix(self, self.ui.input_table_p7_4):
            values = extract_matrix_from_table(self.ui.input_table_p7_4)
            accuracy = self.ui.accuracy_p7_4.value()
            resultat = practica74.run(values, accuracy)
            self.ui.output_p7_4.append(resultat)

    # -------------8-1---------------

    def reset_p8(self):
        practica8.reset_table1(self)

    def run_step1_p8(self):
        if check_and_process_matrix(self, self.ui.input_table1_p8):
            matrix1_p8 = extract_matrix_from_table(self.ui.input_table1_p8)
            practica8.alg81(self, matrix1_p8)

    def update_table_input1_p8(self, value):
        self.ui.input_table1_p8.setColumnCount(value)
        self.ui.input_table1_p8.setRowCount(value)
        headers = [
            f"x {i+1}" for i in range(value)]
        self.ui.input_table1_p8.setHorizontalHeaderLabels(headers)
        self.ui.input_table1_p8.setVerticalHeaderLabels(headers)

    # -------------8-2---------------

    def run_step2_p8(self):
        _, final_output = practica8.alg82(self)
        if len(final_output) != 0:
            msg_box = QMessageBox()
            msg_box.setText("Результаты расчетов")
            msg_box.setInformativeText(str(final_output))
            msg_box.exec()

    def reset2_p8(self):
        practica8.reset_table2(self)

    def update_table_input2_p8(self, value):
        self.clear_layout(self.group_box_table_input_layout_p8_2)
        practica8.update_tables_step2(self, value)

    def run_step3_p8(self):
        practica8.alg83(self)
    # -------------Theory-------------

    def closeEvent(self, event):
        """
        Специальный обработчик события закрытия окна.
        Сюда добавляем всю необходимую логику для полной остановки приложения.
        """

        # Удаление объектов QWebEngineView
        if hasattr(self, 'ui'):
            if hasattr(self.ui, 'doc1'):
                self.ui.doc1.deleteLater()
            if hasattr(self.ui, 'doc2'):
                self.ui.doc2.deleteLater()
            if hasattr(self.ui, 'doc3'):
                self.ui.doc3.deleteLater()
            if hasattr(self.ui, 'doc4'):
                self.ui.doc4.deleteLater()
            if hasattr(self.ui, 'doc5'):
                self.ui.doc5.deleteLater()
            if hasattr(self.ui, 'doc7'):
                self.ui.doc7.deleteLater()
            if hasattr(self.ui, 'doc8'):
                self.ui.doc8.deleteLater()
            # Остальные web view виджеты аналогично

        # Завершаем любое другое активное действие
        # Если используется KMeans алгоритм или другой тяжелый процесс
        if hasattr(self, 'kmeans'):
            del self.kmeans

        # Очистка графика перед закрытием
        self.fig.clear()
        self.fig41.clear()

        self.clear_layout(self.ui.centralwidget.layout())
        # Стандартная процедура закрытия окна
        event.accept()

    def clear_layout(self, layout):
        """
        Полностью очищает указанный макет от всех виджетов и освобождает память.
        :param layout: экземпляр QLayout (QVBoxLayout, QHBoxLayout, QGridLayout и т.п.)
        """
        if layout is not None:
            while layout.count():  # Пока в макете есть элементы...
                child = layout.takeAt(0)  # Извлекаем первый элемент

                if child.widget():  # Если извлечённый элемент является виджетом
                    widget = child.widget()
                    # Отвязываем виджет от текущего родителя
                    widget.setParent(None)
                    widget.deleteLater()   # Планируем удаление виджета

                elif child.layout():  # Если извлечённый элемент сам является вложенным макетом
                    # Рекурсивно чистим вложенный макет
                    self.clear_layout(child.layout())
                    # Убираем пустой вложенный макет
                    layout.removeItem(child)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Praсticies()
    window.show()
    sys.exit(app.exec())
