from utils import extract_matrix_from_table
from PySide6.QtWidgets import QTableWidgetItem

import numpy as np


def update_table_dimensions(self, value, type):
    match type:
        case "m":
            # Устанавливаем одинаковое количество строк и столбцов равное значению спинбокса
            self.ui.p3_tableInput_1.setColumnCount(value)
            self.ui.p3_tableInput_2.setRowCount(value)
            column_headers_2 = row_headers_1 = [
                f"Характеристика {i+1}" for i in range(value)]
            self.ui.p3_tableInput_1.setHorizontalHeaderLabels(column_headers_2)
            self.ui.p3_tableInput_2.setVerticalHeaderLabels(row_headers_1)
        case 'n':
            # Устанавливаем одинаковое количество строк и столбцов равное значению спинбокса
            self.ui.p3_tableInput_1.setRowCount(value)
            self.ui.p3_tableInput_2.setColumnCount(value)
            self.ui.p3_tableResult.setRowCount(value)
            self.ui.p3_tableResult.setColumnCount(value)

            column_headers_2 = [f"Фамилия {i+1}" for i in range(value)]
            column_headers_1 = [f"Специальность {i+1}" for i in range(value)]
            self.ui.p3_tableInput_1.setVerticalHeaderLabels(column_headers_1)
            self.ui.p3_tableInput_2.setHorizontalHeaderLabels(column_headers_2)
            self.ui.p3_tableResult.setVerticalHeaderLabels(column_headers_1)
            self.ui.p3_tableResult.setHorizontalHeaderLabels(column_headers_2)
        case _:
            return


def composite_max_min(self):
    # Извлекаем данные из таблиц p3_tableInput_1 и p3_tableInput_2
    matrix_A = extract_matrix_from_table(self.ui.p3_tableInput_1)
    matrix_B = extract_matrix_from_table(self.ui.p3_tableInput_2)

    # Преобразуем обычные списки в массивы NumPy
    matrix_A = np.array(matrix_A)
    matrix_B = np.array(matrix_B)

    # Размеры матриц
    M, N = matrix_A.shape
    _, L = matrix_B.shape

    # Инициализируем результирующую матрицу
    result_matrix = np.zeros((M, L))

    # Применяем композиционное правило Max-Min
    for i in range(M):
        for j in range(L):
            temp_list = [min(matrix_A[i, k], matrix_B[k, j]) for k in range(N)]
            result_matrix[i, j] = max(temp_list)

    # Заполняем таблицу p3_tableResult результатами
    for i in range(M):
        for j in range(L):
            item = QTableWidgetItem(str(result_matrix[i, j]))
            self.ui.p3_tableResult.setItem(i, j, item)
