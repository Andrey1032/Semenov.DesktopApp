# Semenov.DesktopApp
Комплекс прикладных программ для решения практических задач по дисциплине (PySide6)

# exe build
pyinstaller --onefile --noconsole --hidden-import="sklearn.cluster" main.py

#
pyside6-uic main-ui.ui -o main_ui.py