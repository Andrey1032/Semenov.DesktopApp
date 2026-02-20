import numpy as np
import logging
from PySide6.QtWidgets import QMessageBox


# Настройка базовой конфигурации логгера
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

# Инициализация весов и смещений
weights_1 = np.random.randn(3, 2)
bias_1 = np.random.randn(1, 2)
weights_2 = np.random.randn(2, 1)
bias_2 = np.random.randn(1, 1)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def forward_pass(inputs):
    global weights_1, weights_2
    hidden_layer_input = np.dot(inputs, weights_1) + bias_1
    hidden_layer_output = sigmoid(hidden_layer_input)

    output_layer_input = np.dot(hidden_layer_output, weights_2) + bias_2
    prediction = sigmoid(output_layer_input)

    return prediction, hidden_layer_output


def backward_pass(prediction, target, hidden_layer_output, input, learning_rate):
    global weights_1, weights_2, bias_1, bias_2

    # Ошибку считаем по среднему квадратичному отклонению
    error = ((prediction.item() - target)**2)
    logging.debug("\nError: %.4f", (error))

    # Производная от сигмоиды
    gradient2 = prediction * (1 - prediction)
    del2 = (prediction[0] - target) * gradient2

    logging.debug("\nGradient Output Layer: %s", str(gradient2))
    logging.debug("Delta Output Layer: %s", str(del2))

    # Пропускаем ошибку назад через скрытый слой
    gradient1 = hidden_layer_output * (1 - hidden_layer_output)
    del1 = del2 @ weights_2.T * gradient1

    logging.debug("\nGradient Hidden Layer: %s", str(gradient1))
    logging.debug("Delta Hidden Layer: %s", str(del1))

    # Обновляем веса и свободного коэф.
    weights_1 -= learning_rate * (input @ del1)
    weights_2 -= learning_rate * hidden_layer_output.T @ del2
    bias_1 -= learning_rate * np.sum(del1, axis=0)
    bias_2 -= learning_rate * np.sum(del2, axis=0)

    logging.debug("\nWeights Updated: \n%s\n%s",
                  str(weights_1), str(weights_2))


def train(self, inputs, targets, options):
    global weights_1, weights_2, bias_1, bias_2

    # Генерация весов (при каждом запуске обучения новые веса)
    weights_1 = np.random.randn(3, 2)
    bias_1 = np.random.randn(1, 2)
    weights_2 = np.random.randn(2, 1)
    bias_2 = np.random.randn(1, 1)

    self.ui.progressBar_training.setValue(0)
    inputs = np.array(inputs)
    targets = np.array(targets).reshape(-1, 1)
    mse = 0
    for epoch in range(options['training_epochs']):
        # Обнуление ошибки для каждой эпохи
        total_error = 0
        for i in range(len(inputs)):
            # Прямой проход
            prediction, hidden_layer_output = forward_pass(inputs[i:i+1])

            # Накапливаем общую ошибку
            total_error += (prediction.item() - targets[i:i+1].item()) ** 2

            # Обратное распространение ошибки
            backward_pass(
                prediction, targets[i][0], hidden_layer_output, inputs[i:i+1].T, options['learning_rate'])

        # Средняя ошибка для текущей эпохи
        mse = float(total_error / len(inputs))

        # Прогресс-бар отображается пропорционально номеру эпохи
        progress_value = int((epoch + 1) / options['training_epochs'] * 100)
        self.ui.progressBar_training.setValue(progress_value)

        if epoch % 500 == 0 or epoch == options['training_epochs'] - 1:
            logging.info('Epoch %d - Average Error: %.4f', epoch, mse)

        # Критерий останова обучения
        if mse < options['tolerance_error']**2:
            logging.info('Epoch %d - Average Error: %.4f', epoch, mse)
            self.ui.progressBar_training.setValue(100)
            break

    QMessageBox.information(self, "Результат обучения",
                            f'Нейронная сеть обучена, MSE (среднеквадратичная ошибка) в процессе обучения: {mse:.4f}')

# if __name__ == "__main__":
#     inputs = np.array([[0.1, 0.2, 0.3],
#                        [0.8, 0.1, 0.1],
#                        [0.4, 0.5, 0.1],
#                        [0.2, 0.2, 0.6],
#                        [0.7, 0.1, 0.2],
#                        [0.3, 0.3, 0.4]])  # shape(4,3)
#     targets = np.array([0.6, 1.0, 1.0, 1.0, 1.0, 1.0]
#                        ).reshape(-1, 1)  # [[0],[1],[1],[0]]
#     learning_rate = 1  # Скорость обучения
#     training_epochs = 10000  # Количество эпох обучения
#     tolerance_error = 0.02
#     train(inputs[:5])
#     output, _ = forward_pass(inputs[-2:-1])
#     print(f"Output: {output[0][0]:.4f}")
