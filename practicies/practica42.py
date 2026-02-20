import numpy as np
from PySide6.QtWidgets import QTableWidget, QLabel
from utils import extract_matrix_from_table, check_and_process_matrix
from matplotlib.figure import Figure


def update_tables(self, count_tables):
    count_columns, count_rows = self.ui.count_params_p4_2.value(), self.ui.count_terms_p4_2.value(
    ),

    for i in range(count_tables):
        table_widget = QTableWidget(count_rows, count_columns
                                    )
        table_widget.setMinimumSize(400, 150)  # Ширина 400px, Высота 150px
        label = QLabel(f"Эксперт № {i + 1}")
        self.group_box_table_input_layout_p4_2.addWidget(label)
        self.group_box_table_input_layout_p4_2.addWidget(table_widget)


def update_column_tables(self, count_columns):
    # Проход по всем виджетам в group_box_table_input_layout_p4_2 и обновление количества столбцов
    for index in range(self.group_box_table_input_layout_p4_2.count()):
        widget = self.group_box_table_input_layout_p4_2.itemAt(index).widget()
        if isinstance(widget, QTableWidget):
            widget.setColumnCount(count_columns)


def update_row_tables(self, count_rows):
    # Проход по всем виджетам в group_box_table_input_layout_p4_2 и обновление количества строк
    for index in range(self.group_box_table_input_layout_p4_2.count()):
        widget = self.group_box_table_input_layout_p4_2.itemAt(index).widget()
        if isinstance(widget, QTableWidget):
            widget.setRowCount(count_rows)


def run_expert_mark(self):
    matrices = []
    for index in range(self.group_box_table_input_layout_p4_2.count()):
        tableWidget = self.group_box_table_input_layout_p4_2.itemAt(
            index).widget()
        if isinstance(tableWidget, QTableWidget):
            if check_and_process_matrix(self, tableWidget):
                new_matrix = extract_matrix_from_table(tableWidget)
                matrices.append(np.array(new_matrix))
            else:
                return False
    if not matrices:
        raise ValueError("No valid matrices found")
    # Вычисление среднего массива
    avg_matrix = np.mean(matrices, axis=0)
    plot_graph(self, avg_matrix)


def plot_graph(self, avg_matrix):
    # Очищаем предыдущий график
    self.fig42.clear()
    ax = self.fig42.add_subplot(111)

    # Количество строк в матрице
    num_rows = avg_matrix.shape[0]
    indices = np.arange(avg_matrix.shape[1])  # Кол-во колонок (индексы по x)

    # Проходим по каждой строке и строим линию
    for i in range(num_rows):
        values = avg_matrix[i, :]  # Значения строки
        ax.plot(indices, values, marker='o', label=f'Терм {i}')
        # Добавляем аннотации к каждой точке
        for idx, value in zip(indices, values):
            ax.annotate(f"{value:.2f}", xy=(idx, value),
                        xytext=(5, -10), textcoords='offset points',
                        ha='center', va='top')

    # Оформление графика
    ax.set_xlabel('Параметр')
    ax.set_ylabel('экспертная оценка')
    ax.set_title('График экспертной оценки')
    ax.grid(True)
    ax.legend(loc='best')  # Легенда для идентификации линий

    # Обновляем рисунок на холсте
    self.canvas42.draw()
