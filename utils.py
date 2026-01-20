from PySide6.QtWidgets import QMessageBox
from PySide6 import QtWidgets, QtGui
import sys, os

class IntOnlyDelegate(QtWidgets.QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = super(IntOnlyDelegate, self).createEditor(
            parent, option, index)
        if isinstance(editor, QtWidgets.QLineEdit):
            validator = QtGui.QIntValidator()
            editor.setValidator(validator)
        return editor

def check_and_process_matrix(self, table):
    """
    Проверяет заполненность матрицы и выводит предупреждение, если матрица неполная.
    Если матрица заполнена, выполняет нужную операцию (например, task1).
    """
    # Проверяем заполненность таблицы
    rows = table.rowCount()
    cols = table.columnCount()

    for r in range(rows):
        for c in range(cols):
            item = table.item(r, c)
            if (item is None or len(item.text().strip()) == 0):
                # Нашли пустую ячейку
                QMessageBox.warning(
                    self, "Внимание", "Необходимо заполнить все ячейки матрицы.")
                return
    return True


def extract_matrix_from_table(table):
    """
    Извлекает все числовые значения из таблицы и формирует матрицу.
    """
    rows = table.rowCount()
    cols = table.columnCount()

    # Создаем пустую матрицу подходящего размера
    matrix = [[0]*cols for _ in range(rows)]

    # Заполняем матрицу данными из таблицы
    for r in range(rows):
        for c in range(cols):
            item = table.item(r, c)
            if item is not None:
                try:
                    matrix[r][c] = int(item.text())
                except:
                    matrix[r][c] = float(int(item.text()[0]) / int(item.text()[2]))

    return matrix

def resource_path(relative_path):
    """
    Получает абсолютный путь к ресурсам, корректно работающий как в разработке,
    так и после упаковки PyInstaller.
    """
    try:
        # Режим разработки возвращает абсолютный путь
        base_path = os.path.abspath(".")
    except Exception:
        # В режиме PyInstaller берем временную директорию
        base_path = getattr(sys, "_MEIPASS", os.path.abspath("."))

    # Формируем путь, используя только прямые слэши
    path = os.path.join(base_path, relative_path).replace("\\", "/")
    return path
