import numpy as np


def run(values, accuracy):
    n = len(values)       # Количество альтернатив
    m = len(values[0])    # Количество критериев

    # Этап 1: формирование матрицы парных сравнений
    valuesMatrix = np.zeros((n, m, m))
    for i in range(n):
        for x in range(m):
            for y in range(m):
                if x == y:
                    valuesMatrix[i, x, y] = 0.5
                elif values[x][i] < values[y][i]:
                    valuesMatrix[i, x, y] = 1
                else:
                    valuesMatrix[i, x, y] = 0

    # Этап 2: получение усреднённой матрицы A
    matrix = np.mean(valuesMatrix, axis=0)
    matrix = np.round(matrix, decimals=3)

    # Этап 3: расчёт собственных чисел и коэффициентов k
    k = np.ones(m)
    resultat = f"{'='*50}\n" \
        f"Начальное значение k[0]: {[float(val) for val in k]}\n"

    for t in range(1, 100):
        # Расчет собственного числа lambda
        denominator = np.sum(matrix @ k)
        lambda_ = round(1 / denominator, 3)

        # Новое приближение вектора k
        kt = lambda_ * (matrix @ k)
        kt = np.round(kt, decimals=3)

        # Добавляем красивое представление хода вычислений
        resultat += f"{'='*50}\n" \
            f"Итерация №{t}:\n" \
            f"Lambda({t}) = {lambda_:.3f}\n" \

        # Проверка условия остановки
        if np.allclose(k, kt, atol=accuracy):
            resultat += f"Финальный результат:\nk[{t}] = {[float(val) for val in kt]}\n"
            break
        else:
            k = kt.copy()
            resultat += f"Промежуточный результат:\nk[{t}] = {[float(val) for val in k]}\n"

    return resultat.strip()
