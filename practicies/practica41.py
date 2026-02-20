import numpy as np
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem


def calculate_average(start_matrix):
    # Геометрическое среднее строк матрицы
    w_matrix = np.prod(start_matrix, axis=1)**(1/len(start_matrix))
    # Сумма элементов w_matrix
    sum_w = np.sum(w_matrix)

    # Первоначальная нормализация
    w_matrix_sub_normal = w_matrix / sum_w

    # Суммы столбцов исходной матрицы
    a_matrix = np.sum(start_matrix.T, axis=1)

    # Итоговая нормализация
    w_matrix_normal = w_matrix_sub_normal / np.max(w_matrix_sub_normal)

    # Расчёт оценки согласованности
    lambda_value = np.max(np.linalg.eigvals(start_matrix).real)

    # Результаты
    result = [
        {"subnorm": round(value, 4), "norm": round(norm, 4)}
        for value, norm in zip(w_matrix_sub_normal, w_matrix_normal)
    ], lambda_value, lambda_value - len(start_matrix)

    return result


import numpy as np
import matplotlib.pyplot as plt

def plot_graph(self, weights_subnormal, weights_normalized):
    # Очищаем старый график
    self.fig41.clear()
    ax = self.fig41.add_subplot(111)

    # Индексы критериев
    num_criteria = len(weights_subnormal)
    indices = np.arange(num_criteria)

    # График субнормированного веса
    line1 = ax.plot(indices, weights_subnormal, marker='o', color="blue", label='Субнормированный вес')[0]

    # График нормализованного веса
    line2 = ax.plot(indices, weights_normalized, marker='s', color="green", label='Нормализованный вес')[0]

    # Добавляем подписи к точкам
    for idx, (x, y) in enumerate(zip(indices, weights_subnormal)):
        ax.annotate(f'{y:.4f}', xy=(x, y), xytext=(5, -10), textcoords='offset points', ha='center', va='top')

    for idx, (x, y) in enumerate(zip(indices, weights_normalized)):
        ax.annotate(f'{y:.4f}', xy=(x, y), xytext=(5, 10), textcoords='offset points', ha='center', va='bottom')

    # Оформление графика
    ax.set_xlabel('Номер критерия')
    ax.set_ylabel('Вес')
    ax.set_title('График весов критериев')
    ax.set_xticks(indices)
    ax.set_xticklabels([str(i*5+170) for i in range(num_criteria)])
    ax.grid(True)
    ax.legend(loc='best')

    # Обновляем рисунок на холсте
    self.canvas41.draw()


def on_calculate_average(self, input_data):
    start_matrix = np.array(input_data)
    result = calculate_average(start_matrix)
    # Извлекаем субнормальные веса
    weights_subnormal = np.array([item['subnorm'] for item in result[0]])
    # Извлекаем нормализованные веса
    weights_normalized = np.array([item['norm'] for item in result[0]])
    lambda_val = result[1]  # Лямбда-значение
    inconsistency_measure = result[2]  # Мерой несогласованности

    # Формируем красивую таблицу для Message Box
    header = "{:^10} {:^20} {:^20}".format(
        "Критерий", "Субнормирован.", "Нормализирован.")
    rows = "\n".join(
        "{:^15} {:^30.4f} {:^30.4f}".format(i*5+170, sn, nw)
        for i, (sn, nw) in enumerate(zip(weights_subnormal, weights_normalized))
    )

    # Составляем красивое сообщение
    text = (
        f"{header}\n{'-' * 50}\n{rows}\n\n"
        f"Лямбда: {lambda_val:.3f}\n"
        f"Мера несогласованности: {inconsistency_measure:.3f}"
    )

    # Сообщение с результатами
    msg_box = QMessageBox()
    msg_box.setText(text)
    msg_box.exec()

    # Отображаем график
    plot_graph(self, weights_subnormal, weights_normalized)


def reset_p4(self):
    # Установим размер таблицы
    num_rows = 6
    num_cols = 6

    # Заданные начальные значения матрицы
    initial_matrix = [
        ['1', '1/2', '1/4', '1/6', '1/8', '1/9'],
        ['2', '1', '1/3', '1/5', '1/7', '1/8'],
        ['4', '3', '1', '1/4', '1/4', '1/5'],
        ['6', '5', '4', '1', '1/3', '1/3'],
        ['8', '7', '4', '3', '1', '1'],
        ['9', '8', '5', '3', '1', '1']
    ]

    # Заносим начальные значения в таблицу
    for row in range(num_rows):
        for col in range(num_cols):
            item = QTableWidgetItem(str(initial_matrix[row][col]))
            self.ui.table_p41.setItem(row, col, item)

    # Дополнительно можем сбросить любые ранее созданные графики или отчёты
    self.fig41.clear()
    self.canvas41.draw()
