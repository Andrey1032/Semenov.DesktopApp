import numpy as np

def run(values, accuracy, n_val=None):
    values_np = np.array(values)

    if n_val is None:
        n = values_np.shape[1]
    else:
        n = n_val

    k = np.full(n, round(1/n, 3))

    x = np.round(np.dot(values_np, k), 3)

    # Подготовка красивого вывода
    resultat = "\n" + "="*50 + "\n"
    resultat += f"Результат шага №1\n"
    resultat += f"Исходные значения k[1]: {[float(val) for val in x]}\n"

    for t in range(2, n + 2):
        sum_rows = np.sum(values_np, axis=1)
        lambda_val = np.round(np.sum(np.round(sum_rows * x, 3)), 3)

        dot_product_tx = np.dot(values_np.T, x)

        temp_kt_base = np.round(dot_product_tx * (1 / lambda_val), 4)

        kt = np.zeros(n)

        if n > 0:
            kt[:-1] = temp_kt_base[:-1]

        kt[-1] = np.round(1 - np.sum(kt[:-1]), 4)

        xt = np.round(np.dot(values_np, kt), 4)

        # Дополняем вывод
        resultat += "\n" + "="*50 + "\n"
        resultat += f"Шаг #{t}\n"
        resultat += f"Значение λ(t): {lambda_val:.3f}\n"
        resultat += f"Новый вектор k[t]: {[float(val) for val in kt]}\n"
        resultat += f"Новое приближение x[t]: {[float(val) for val in xt]}\n"

        if np.all(np.abs(xt - x) < accuracy):
            x = np.array(xt)
            resultat += f"Финальный результат k[{t}]=[{[float(val) for val in x]}]\n"
            break
        else:
            x = np.array(xt)
            resultat += f"Промежуточный результат k[{t}]=[{[float(val) for val in x]}]\n"

    return resultat.strip()