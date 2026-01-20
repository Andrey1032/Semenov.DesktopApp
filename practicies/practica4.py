import numpy as np
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem

def calculate_average(matrix):
    print(matrix)
    # Конвертируем список в ndarray
    matrix = np.array(matrix, dtype=np.float64)
    
    # Геометрическое среднее строк (строго фиксированно, согласно исходнику)
    geometric_means = np.power(np.prod(matrix, axis=1), 1/6)
    
    # Сумма геометрических средних
    total_sum = np.sum(geometric_means)
    
    # Вес критериев (субнормированные веса)
    weights_subnormal = geometric_means / total_sum
    
    # Номинированные веса (вес в процентах)
    weights_normalized = weights_subnormal / np.max(weights_subnormal)
    
    # Транзиция матрицы и подсчёт суммарных значений
    sums_transpose = np.sum(matrix.T, axis=1)
    
    # Значение лямбда (мера согласования)
    lambda_val = np.dot(sums_transpose, weights_subnormal)
    
    # Величина несогласованности
    inconsistency_measure = lambda_val - matrix.shape[0]
    
    return weights_subnormal, weights_normalized, lambda_val, inconsistency_measure


def plot_graph(self, weights_subnormal, weights_normalized):
    # Очистить предыдущий график
    self.fig41.clear()
    ax = self.fig41.add_subplot(111)

    # Индексы точек (критерии)
    indices = np.arange(len(weights_subnormal))

    # Линия для субнормированных весов
    ax.plot(indices, weights_subnormal, marker='o', label='Субнормированный вес')

    # Линия для нормализованных весов
    ax.plot(indices, weights_normalized, marker='o', label='Нормализованный вес')

    # Оформление графика
    ax.set_xlabel('Критерий')
    ax.set_ylabel('Вес')
    ax.set_title('Вес критериев')
    ax.set_xticks(indices)
    ax.set_xticklabels(['1', '2', '3', '4', '5'])  # Метки осей X
    ax.legend()

    # Рисуем график на холсте
    self.canvas41.draw()


def on_calculate_average(self, input_data):
    # Вычисляем средние значения
    weights_subnormal, weights_normalized, lambda_val, inconsistency_measure = calculate_average(input_data)
    
    # Показать сообщение с результатами
    msg_box = QMessageBox()
    msg_box.setText(f'''
        Субнормированный вес:\n{weights_subnormal.round(3)}\n\n
        Нормализованный вес:\n{weights_normalized.round(3)}\n\n
        Лямбда: {lambda_val:.3f}\n\n
        Мера несогласованности: {inconsistency_measure:.3f}
    ''')
    msg_box.exec()
    
    # Строим график
    plot_graph(self, weights_subnormal, weights_normalized)


def reset_p4(self):
    # Установим размер таблицы
    num_rows = 5
    num_cols = 5

    # Заданные начальные значения матрицы
    initial_matrix = [
        [1, 5/7, 3/7, 2/7, 1/7],
        [7/5, 1, 3/5, 2/5, 1/5],
        [7/3, 5/3, 1, 2/3, 1/3],
        [7/2, 5/2, 3/2, 1, 1/2],
        [7, 5, 3, 2, 1]
    ]

    # Заносим начальные значения в таблицу
    for row in range(num_rows):
        for col in range(num_cols):
            item = QTableWidgetItem(str(initial_matrix[row][col]))
            self.ui.table_p41.setItem(row, col, item)

    # Дополнительно можем сбросить любые ранее созданные графики или отчёты
    self.fig41.clear()
    self.canvas41.draw()