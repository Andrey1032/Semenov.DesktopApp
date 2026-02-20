
def run(values_copy, accuracy):
    # Исходные переменные
    resultat = ""
    y = sum(sum(row) for row in values_copy)

    k = [1] * len(values_copy)
    k_temp = [0.0] * len(values_copy)

    # Главный цикл алгоритма
    for i in range(100):

        for j in range(len(values_copy)):
            k_temp[j] = round(
                sum(value * k[index]
                    for index, value in enumerate(values_copy[j])) / y, 4
            )

        # Добавляем промежуточный результат в итоговую строку
        resultat += f'k[{i}]={k_temp}\n'

        # Проверяем условие остановки цикла:
        # Если разница между элементами старых и новых значений меньше заданной точности Е
        if all(abs(k[ind] - val) <= accuracy for ind, val in enumerate(k_temp)):
            k = list(k_temp)  # Обновляем основной массив K
            break
        else:
            # Иначе обновляем основной массив K и заново вычисляем новое значение Y
            k = list(k_temp)
            y = round(
                sum(sum(cur_val2 * k[cur_ind] for cur_ind, cur_val2 in enumerate(cur_val))
                    for cur_val in values_copy), 4
            )

    return resultat
