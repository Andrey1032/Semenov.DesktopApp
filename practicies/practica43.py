import numpy as np


def triangular_membership_function(self, a, b, c, x_start, x_end, step=0.1):
    """
    Построение треугольной функции принадлежности.

    :param a: Левая граница треугольника
    :param b: Вершина треугольника
    :param c: Правая граница треугольника
    :param x_start: Начало отрезка
    :param x_end: Конец отрезка
    :param step: Шаг сетки
    :return: Массивы x и y для построения графика
    """
    # Генератор сеточных точек
    x_values = np.arange(x_start, x_end + step, step)

    # Определение функций принадлежности
    def triangle_f(x):
        if a <= x <= b:
            return (x - a) / (b - a)
        elif b < x <= c:
            return (c - x) / (c - b)
        else:
            return 0.0

    # Рассчитываем y-значения
    y_values = [triangle_f(x) for x in x_values]

    plot_graph(self, x_values, y_values)


def plot_graph(self, x_values, y_values):
    # Очищаем предыдущий график
    self.fig43.clear()
    ax = self.fig43.add_subplot(111)

    # Строим график
    ax.plot(x_values, y_values, label='Треугольная функция принадлежности')

    # Оформление графика
    ax.set_xlabel('X')
    ax.set_ylabel('Принадлежность')
    ax.set_title('Треугольная функция принадлежности')
    ax.grid(True)
    ax.legend()

    # Обновляем рисунок на холсте
    self.canvas43.draw()
