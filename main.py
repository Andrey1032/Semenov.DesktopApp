import sys
from PySide6.QtWidgets import QApplication, QMainWindow
import practicies.practica1 as practica1
import practicies.practica2 as practica2
import practicies.practica3 as practica3
import practicies.practica4 as practica4
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
        self.ui.action5.triggered.connect(
            # Нейронная сеть (Практика-5)
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
        self.ui.action9.triggered.connect(
            lambda _: self.open_practice(12))  # О программе
        self.ui.action10.triggered.connect(
            lambda _:  self.open_practice(13))  # Теория

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
        self.fig41 = Figure(figsize=(5, 4))
        self.canvas41 = FigureCanvas(self.fig41)
        self.ui.verticalLayout_5.addWidget(self.canvas41)

        self.ui.run_p4.clicked.connect(self.run_p4)
        self.ui.reset_p4.clicked.connect(self.reset_p4)
        # Практика 4.2

        # Практика 4.3

        # Теория
        THEORY_PATH = resource_path('theory')

        # Загрузка HTML-документов
        self.ui.doc1.load(f'file:///{THEORY_PATH}/1.html')
        self.ui.doc2.load(f'file:///{THEORY_PATH}/2.html')
        self.ui.doc3.load(f'file:///{THEORY_PATH}/3.html')
        self.ui.doc4.load(f'file:///{THEORY_PATH}/4.html')
        self.ui.doc5.load(f'file:///{THEORY_PATH}/5.html')
        self.ui.doc7.load(f'file:///{THEORY_PATH}/7.html')
        self.ui.doc8.load(f'file:///{THEORY_PATH}/8.html')

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

    # ----------4---------
    def reset_p4(self):
        practica4.reset_p4(self)

    def run_p4(self):
        if check_and_process_matrix(self, self.ui.table_p41):
            matrix_p4 = extract_matrix_from_table(self.ui.table_p41)
            practica4.on_calculate_average(self, matrix_p4)

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

        # Стандартная процедура закрытия окна
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Praсticies()
    window.show()
    sys.exit(app.exec())
