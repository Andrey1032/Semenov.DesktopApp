import numpy as np
from PySide6.QtWidgets import QTableWidget, QLabel, QTableWidgetItem, QMessageBox
from utils import extract_matrix_from_table, check_and_process_matrix


def reset_table1(self):
    initial_matrix = [
        ["1", "5", "3", "7", "6", "6", "1/3", "1/4",],
        ["1/5", "1", "1/3", "5", "3", "3", "1/5", "1/7"],
        ["1/3", "3", "1", "6", "3", "4", "6", "1/5"],
        ["1/7", "1/5", "1/6", "1", "1/3", "1/4", "1/7", "1/8"],
        ["1/6", "1/3", "1/3", "3", "1", "1/2", "1/5", "1/6"],
        ["1/6", "1/3", "1/4", "4", "2", "1", "1/5", "1/6"],
        ["3", "5", "1/6", "7", "5", "5", "1", "1/2"],
        ["4", "7", "5", "8", "6", "6", "2", "1"]
    ]

    num_rows = len(initial_matrix)
    num_cols = len(initial_matrix[0])
    self.ui.input_table1_p8.setColumnCount(num_cols)
    self.ui.input_table1_p8.setRowCount(num_rows)
    for row in range(num_rows):
        for col in range(num_cols):
            item = QTableWidgetItem(str(initial_matrix[row][col]))
            self.ui.input_table1_p8.setItem(row, col, item)
    headersRows = [
        f"x {i+1}" for i in range(num_rows)]
    headersCols = [
        f"x {i+1}" for i in range(num_cols)]
    self.ui.input_table1_p8.setHorizontalHeaderLabels(headersCols)
    self.ui.input_table1_p8.setVerticalHeaderLabels(headersRows)
    self.ui.input1_p8.setValue(num_rows)
    self.clear_layout(self.group_box_table_input_layout_p8_2)
    self.ui.input2_p8.setValue(3)
    update_tables_step2(self, 3)


def reset_table2(self):
    matrices = [
        [
            ["1", "6", "8"],
            ["1/6", "1", "4"],
            ["1/8", "1/4", "1"],
        ],
        [
            ["1", "7", "1/5"],
            ["1/7", "1", "1/8"],
            ["5", "8", "1"],
        ],
        [
            ["1", "8", "6"],
            ["1/8", "1", "1/4"],
            ["1/6", "4", "1"],
        ],
        [
            ["1", "1", "1"],
            ["1", "1", "1"],
            ["1", "1", "1"],
        ],
        [
            ["1", "5", "4"],
            ["1/5", "1", "1/3"],
            ["1/4", "3", "1"],
        ],
        [
            ["1", "8", "6"],
            ["1/8", "1", "1/5"],
            ["1/6", "5", "1"],
        ],
        [
            ["1", "1/2", "1/2"],
            ["2", "1", "1"],
            ["2", "1", "1"],
        ],
        [
            ["1", "1/7", "1/5"],
            ["7", "1", "3"],
            ["5", "1/3", "1"],
        ],
    ]
    self.clear_layout(self.group_box_table_input_layout_p8_2)
    for i, matrix in enumerate(matrices):
        table_widget = QTableWidget(len(matrix), len(matrix[0]))
        table_widget.setMinimumSize(400, 200)

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                cell_item = QTableWidgetItem(str(matrix[row][col]))
                table_widget.setItem(row, col, cell_item)

        label = QLabel(f"Характеристика № {i + 1}")
        self.group_box_table_input_layout_p8_2.addWidget(label)
        self.group_box_table_input_layout_p8_2.addWidget(table_widget)


def alg81(self, values):
    # Размер матрицы
    n = len(values)

    # Преобразование массива в NumPy-матрицу
    matrix = np.array(values)

    # Геометрическое среднее строк матрицы
    w_matrix = np.prod(matrix, axis=1)**(1/n)

    # Сумма элементов
    sum_w = np.sum(w_matrix)

    # Нормализованный вектор приоритетов
    w_matrix_sub_normal = [(val/sum_w).round(4) for val in w_matrix]

    # Транспозиция матрицы
    matrix_trans = np.transpose(matrix)

    # Суммируем столбцы
    col_sums = np.sum(matrix_trans, axis=1)

    # Максимальное собственное значение λ_max
    lambda_max = round(np.dot(col_sums, w_matrix_sub_normal), 3)

    # Индекс согласованности (IS)
    is_value = round((lambda_max-n)/(n-1), 3)

    # Среднее значение случайной согласованности (примерно заданное)
    # Можно задать произвольные средние значения случайной согласованности для разных размеров матриц
    sred_sogl = {
        1: 0,       # Матрица 1x1
        2: 0,       # Матрица 2x2
        3: 0.58,    # Матрица 3x3
        4: 0.9,     # Матрица 4x4
        5: 1.12,    # Матрица 5x5
        6: 1.24,    # Матрица 6x6
        7: 1.32,    # Матрица 7x7
        8: 1.41,    # Матрица 8x8
        9: 1.45,    # Матрица 9x9
        10: 1.49    # Матрица 10x10
    }

    os_value = round(is_value/sred_sogl.get(n-1, 1), 3)

    # Формируем строку вывода
    output = f"Вектор приоритетов:\n"
    for idx, val in enumerate(w_matrix_sub_normal):
        output += f"{idx+1}. {val:.4f}\n"

    output += f"\nλmax: {lambda_max:.3f}\nИС: {is_value:.3f}\nОС: {os_value:.3f}"
    self.ui.output1_p8.clear()
    self.ui.output1_p8.append(output)

    return w_matrix_sub_normal


def alg82(self):
    values_list = []
    results = []
    final_output = ""    # Переменная для сбора всего вывода
    for index in range(self.group_box_table_input_layout_p8_2.count()):
        widget = self.group_box_table_input_layout_p8_2.itemAt(index).widget()
        if isinstance(widget, QTableWidget):
            if check_and_process_matrix(self, widget):
                new_matrix = extract_matrix_from_table(widget)
                values_list.append(np.array(new_matrix))
            else:
                return results, final_output

    for index, values in enumerate(values_list):
        n = len(values)
        matrix = np.array(values)

        # Рассчитываем вектор приоритетов и согласованность
        try:
            w_matrix = np.prod(matrix, axis=1)**(1/n)
            sum_w = np.sum(w_matrix)
            w_matrix_sub_normal = [np.round(val/sum_w, 4) for val in w_matrix]

            matrix_trans = np.transpose(matrix)
            col_sums = np.sum(matrix_trans, axis=1)
            lambda_max = round(np.dot(col_sums, w_matrix_sub_normal), 3)

            is_value = round((lambda_max-n)/(n-1), 3)

            sred_sogl = {
                1: 0,         # Матрица 1x1
                2: 0,         # Матрица 2x2
                3: 0.58,      # Матрица 3x3
                4: 0.9,       # Матрица 4x4
                5: 1.12,      # Матрица 5x5
                6: 1.24,      # Матрица 6x6
                7: 1.32,      # Матрица 7x7
                8: 1.41,      # Матрица 8x8
                9: 1.45,      # Матрица 9x9
                10: 1.49      # Матрица 10x10
            }

            os_value = round(is_value/sred_sogl.get(n, 1), 3)

            # Сохраняем результаты
            results.append({
                'vector': w_matrix_sub_normal,
                'lambda_max': lambda_max,
                'is': is_value,
                'os': os_value
            })

            # Подготавливаем сообщение для вывода
            output = (
                f"-----------Для характеристики {index+1}-----------\n"
                f"Вектор приоритетов: {[f'{val:.4f}' for val in w_matrix_sub_normal]}\n"
                f"λmax: {lambda_max:.3f},\n"
                f"Индекс согласованности (ИС): {is_value:.3f},\n"
                f"Отношение согласованности (ОС): {os_value:.3f}\n\n"
            )
            final_output += output
        except Exception as e:
            # Логируем исключение, если возникла проблема
            print(f"Произошла ошибка: {e}")
            break

    return results, final_output


def alg83(self):
    # Шаг 1: получаем главную матрицу и её вектор приоритетов
    main_matrix = extract_matrix_from_table(self.ui.input_table1_p8)
    if not check_and_process_matrix(self, self.ui.input_table1_p8):
        return False
    main_local_priorities = alg81(self, main_matrix)

    # Шаг 2: извлекаем частные матрицы и их векторы приоритетов
    private_results, _ = alg82(self)

    # Шаг 3: рассчитываем глобальные приоритеты
    global_priorities = calculate_global_priorities(main_local_priorities, private_results)

    # Финальный вывод
    formatted_report = format_final_report(global_priorities)
    show_message(self, formatted_report)



def calculate_global_priorities(main_local_priorities, private_results):
    """
    Выполняет расчет глобальных приоритетов путем комбинации главного вектора приоритетов
    и частных векторов приоритетов.
    """
    # Глобальные приоритеты
    global_priorities = []

    # Число альтернатив
    num_alternatives = len(private_results[0]['vector'])

    # По каждой альтернативе считаем суммарный приоритет
    for alt_idx in range(num_alternatives):
        total_priority = 0
        for priors, weight in zip(private_results, main_local_priorities):
            vector = priors['vector']
            total_priority += vector[alt_idx] * weight
        
        global_priorities.append(total_priority)

    return global_priorities


def format_final_report(global_priorities):
    """
    Возвращает отчёт с информацией о глобальных приоритетах и лучшей альтернативе.
    """
    sorted_indices = np.argsort(-np.array(global_priorities))  # Сортируем индексы по убыванию
    best_alternative = sorted_indices[0] + 1  # Первая альтернатива становится лучшей

    # Составляем отчет
    report = f"Глобальные приоритеты:\n"
    for idx, priority in enumerate(global_priorities):
        report += f"{idx+1}: {priority:.3f}\n"

    report += f"\nЛучшая альтернатива: #{best_alternative}"
    return report


def show_message(self, text):
    msg_box = QMessageBox()
    msg_box.setText(text)
    msg_box.exec()


def update_tables_step2(self, size_table):
    count_tables = self.ui.input1_p8.value()

    for i in range(count_tables):
        table_widget = QTableWidget(size_table, size_table
                                    )
        table_widget.setMinimumSize(400, 200)  # Ширина 400px, Высота 150px
        label = QLabel(f"характеристика № {i + 1}")
        self.group_box_table_input_layout_p8_2.addWidget(label)
        self.group_box_table_input_layout_p8_2.addWidget(table_widget)
