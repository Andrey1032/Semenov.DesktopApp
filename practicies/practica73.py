import numpy as np
from PySide6.QtWidgets import QTableWidget, QLabel
from utils import extract_matrix_from_table, check_and_process_matrix


def update_tables(self, count_tables):
    size_table = self.ui.count_factors_p7_3.value()

    for i in range(count_tables):
        table_widget = QTableWidget(size_table, size_table
                                    )
        table_widget.setMinimumSize(400, 150)  # Ширина 400px, Высота 150px
        label = QLabel(f"Эксперт № {i + 1}")
        self.group_box_table_input_layout_p7_3.addWidget(label)
        self.group_box_table_input_layout_p7_3.addWidget(table_widget)


def update_size_tables(self, size_table):
    headers = [
        f"Фактор {i+1}" for i in range(size_table)]
    for index in range(self.group_box_table_input_layout_p7_3.count()):
        widget = self.group_box_table_input_layout_p7_3.itemAt(index).widget()
        if isinstance(widget, QTableWidget):
            widget.setRowCount(size_table)
            widget.setColumnCount(size_table)
            widget.setVerticalHeaderLabels(headers)
            widget.setHorizontalHeaderLabels(headers)


def run(self, E):
    matrices = []  # Матрицы, извлечённые из таблиц
    for index in range(self.group_box_table_input_layout_p7_3.count()):
        widget = self.group_box_table_input_layout_p7_3.itemAt(index).widget()
        if isinstance(widget, QTableWidget):
            if not check_and_process_matrix(self, widget):
                return False
            extracted_matrix = extract_matrix_from_table(widget)
            matrices.append(np.array(extracted_matrix))

    # Получаем размер матрицы (предполагаем, что матрица квадратных размеров)
    m = len(matrices[0])
    n = len(matrices)

    # Создание пустой матрицы размером m x m
    matrix = np.zeros((m, m))

    # Заполняем итоговую матрицу суммой всех входящих матриц
    for mat in matrices:
        matrix += mat

    # Нормализуем матрицу путём деления на количество матриц
    matrix /= n

    # Округлим значения матрицы до трех десятичных знаков
    matrix = np.round(matrix, decimals=3)

    # Определяем начальное значение вектора k
    k = np.ones(m)

    # Формат строки для вывода
    resultat = f"k[0]= {[float(x) for x in k]}\n"

    # Основная вычислительная часть
    for t in range(1, 100):
        # Рассчитываем знаменатель
        denominator = np.sum(matrix @ k)
        lambda_ = round(1 / denominator, 3)

        # Вычисляем новый вектор kt
        kt = lambda_ * (matrix @ k)
        kt = np.round(kt, decimals=3)

        # Проверка условий выхода
        if np.allclose(k, kt, atol=E):
            k = kt.copy()
            resultat += f"k[{t}]= {[float(x) for x in k]}\n"
            break
        else:
            k = kt.copy()
            resultat += f"k[{t}]= {[float(x) for x in k]}\n"

    self.ui.output_p7_3.append(resultat)
