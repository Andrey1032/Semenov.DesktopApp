# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main-ui.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QDoubleSpinBox,
    QFormLayout, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QSpinBox, QStackedWidget,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(916, 745)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet(u"/* \u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"* {\n"
"    font-family: Arial, Helvetica, sans-serif;\n"
"}\n"
"\n"
"/* \u041e\u043a\u0440\u0443\u0436\u0430\u044e\u0449\u0430\u044f \u0441\u0440\u0435\u0434\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0433\u043e \u043e\u043a\u043d\u0430 */\n"
"#main-window,\n"
"#practice2-window {\n"
"    background-color: #f8f8ff;\n"
"    padding: 20px;\n"
"}\n"
"\n"
"/* \u042f\u0440\u043b\u044b\u043a (label) */\n"
"QLabel {\n"
"    color: #333;\n"
"    font-size: 14px;\n"
"    margin-bottom: 10px;\n"
"}\n"
"\n"
"/* \u041f\u043e\u043b\u044f \u0432\u0432\u043e\u0434\u0430 (spin-box) */\n"
"QSpinBox,\n"
"QDoubleSpinBox  {\n"
"    width: 100px;\n"
"    height: 30px;\n"
"    border-radius: 5px;\n"
"    border: 1px solid #ccc;\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"/* \u041a\u043d\u043e\u043f\u043a\u0438 */\n"
"QPushButton {\n"
"    background-color: #4CAF50;\n"
"    color: wh"
                        "ite;\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    min-width: 100px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45A049;\n"
"}\n"
"\n"
"/* \u0422\u0430\u0431\u043b\u0438\u0446\u0430 (\u0434\u043b\u044f \u0437\u0430\u0434\u0430\u0447\u0438 \u043a\u043e\u043c\u043c\u0438\u0432\u043e\u044f\u0436\u0435\u0440\u0430) */\n"
"QTableWidget {\n"
"    border-collapse: collapse;\n"
"    selection-background-color: #4CAF50;\n"
"    alternate-background-color: #fafafa;\n"
"    gridline-color: #ddd;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #f8f8ff;\n"
"    border: none;\n"
"    padding-right: 10px;\n"
"    color: #333;\n"
"}\n"
"\n"
"/* \u042d\u043b\u0435\u043c\u0435\u043d\u0442 \u0432\u044b\u0432\u043e\u0434\u0430 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u0430 (\u0442\u0435\u043a\u0441\u0442\u043e\u0432\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c) */\n"
"QT"
                        "extEdit {\n"
"    background-color: #fff;\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    min-height: 100px;\n"
"}\n"
"\n"
"/* \u041a\u0430\u043d\u0432\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0430 (\u0434\u043b\u044f \u0437\u0430\u0434\u0430\u0447\u0438 \u043a\u043b\u0430\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u0438) */\n"
"#plot-canvas {\n"
"    max-height: 400px;\n"
"    max-width: 600px;\n"
"    background-color: white;\n"
"    border: 1px solid #ddd;\n"
"    box-shadow: 0 0 10px rgba(0,0,0,.1);\n"
"}")
        self.action9 = QAction(MainWindow)
        self.action9.setObjectName(u"action9")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action7_1 = QAction(MainWindow)
        self.action7_1.setObjectName(u"action7_1")
        self.action7_2 = QAction(MainWindow)
        self.action7_2.setObjectName(u"action7_2")
        self.action7_3 = QAction(MainWindow)
        self.action7_3.setObjectName(u"action7_3")
        self.action7_4 = QAction(MainWindow)
        self.action7_4.setObjectName(u"action7_4")
        self.action1 = QAction(MainWindow)
        self.action1.setObjectName(u"action1")
        self.action2 = QAction(MainWindow)
        self.action2.setObjectName(u"action2")
        self.action3 = QAction(MainWindow)
        self.action3.setObjectName(u"action3")
        self.action5 = QAction(MainWindow)
        self.action5.setObjectName(u"action5")
        self.action4_1 = QAction(MainWindow)
        self.action4_1.setObjectName(u"action4_1")
        self.action_1 = QAction(MainWindow)
        self.action_1.setObjectName(u"action_1")
        self.action_11 = QAction(MainWindow)
        self.action_11.setObjectName(u"action_11")
        self.action_12 = QAction(MainWindow)
        self.action_12.setObjectName(u"action_12")
        self.action_13 = QAction(MainWindow)
        self.action_13.setObjectName(u"action_13")
        self.action_14 = QAction(MainWindow)
        self.action_14.setObjectName(u"action_14")
        self.action_15 = QAction(MainWindow)
        self.action_15.setObjectName(u"action_15")
        self.action8 = QAction(MainWindow)
        self.action8.setObjectName(u"action8")
        self.action_17 = QAction(MainWindow)
        self.action_17.setObjectName(u"action_17")
        self.action10 = QAction(MainWindow)
        self.action10.setObjectName(u"action10")
        self.action4_2 = QAction(MainWindow)
        self.action4_2.setObjectName(u"action4_2")
        self.action4_3 = QAction(MainWindow)
        self.action4_3.setObjectName(u"action4_3")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.stackedPages = QStackedWidget(self.centralwidget)
        self.stackedPages.setObjectName(u"stackedPages")
        self.stackedPages.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.stackedPages.sizePolicy().hasHeightForWidth())
        self.stackedPages.setSizePolicy(sizePolicy1)
        self.stackedPages.setStyleSheet(u"")
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.gridLayout = QGridLayout(self.page1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget = QTableWidget(self.page1)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy2)
        self.tableWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tableWidget.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)
        self.tableWidget.setFrameShape(QFrame.Shape.Box)
        self.tableWidget.setFrameShadow(QFrame.Shadow.Plain)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setProperty(u"showDropIndicator", True)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(3)

        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 1)

        self.spinBox = QSpinBox(self.page1)
        self.spinBox.setObjectName(u"spinBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy3)
        self.spinBox.setMouseTracking(True)
        self.spinBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spinBox.setMinimum(3)
        self.spinBox.setMaximum(10)

        self.gridLayout.addWidget(self.spinBox, 2, 0, 1, 1)

        self.label = QLabel(self.page1)
        self.label.setObjectName(u"label")
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.page1)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)

        self.label_16 = QLabel(self.page1)
        self.label_16.setObjectName(u"label_16")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy5)
        self.label_16.setStyleSheet(u"    color: black;              /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font-weight: bold;         /* \u0416\u0438\u0440\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"    font-size: 14pt;           /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    padding: 4px 8px;          /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043e\u043a\u0440\u0443\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 */")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_16, 0, 0, 1, 1)

        self.stackedPages.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        sizePolicy1.setHeightForWidth(self.page2.sizePolicy().hasHeightForWidth())
        self.page2.setSizePolicy(sizePolicy1)
        self.page2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.page2.setAutoFillBackground(False)
        self.verticalLayout_3 = QVBoxLayout(self.page2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_15 = QLabel(self.page2)
        self.label_15.setObjectName(u"label_15")
        sizePolicy5.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy5)
        self.label_15.setStyleSheet(u"    color: black;              /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font-weight: bold;         /* \u0416\u0438\u0440\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"    font-size: 14pt;           /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    padding: 4px 8px;          /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043e\u043a\u0440\u0443\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 */")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_15)

        self.groupBox = QGroupBox(self.page2)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy6)
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy6.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy6)

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.num_points_spin = QSpinBox(self.groupBox)
        self.num_points_spin.setObjectName(u"num_points_spin")
        self.num_points_spin.setMinimum(10)
        self.num_points_spin.setMaximum(1000)

        self.gridLayout_3.addWidget(self.num_points_spin, 1, 0, 1, 1)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        sizePolicy6.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy6)

        self.gridLayout_3.addWidget(self.label_13, 2, 0, 1, 1)

        self.num_clusters_spin = QSpinBox(self.groupBox)
        self.num_clusters_spin.setObjectName(u"num_clusters_spin")
        self.num_clusters_spin.setMinimum(2)
        self.num_clusters_spin.setMaximum(10)

        self.gridLayout_3.addWidget(self.num_clusters_spin, 3, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.page2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy4.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy4)
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.run_button = QPushButton(self.groupBox_2)
        self.run_button.setObjectName(u"run_button")
        sizePolicy6.setHeightForWidth(self.run_button.sizePolicy().hasHeightForWidth())
        self.run_button.setSizePolicy(sizePolicy6)

        self.horizontalLayout.addWidget(self.run_button)

        self.step_button = QPushButton(self.groupBox_2)
        self.step_button.setObjectName(u"step_button")
        sizePolicy6.setHeightForWidth(self.step_button.sizePolicy().hasHeightForWidth())
        self.step_button.setSizePolicy(sizePolicy6)

        self.horizontalLayout.addWidget(self.step_button)

        self.reset_button = QPushButton(self.groupBox_2)
        self.reset_button.setObjectName(u"reset_button")
        sizePolicy6.setHeightForWidth(self.reset_button.sizePolicy().hasHeightForWidth())
        self.reset_button.setSizePolicy(sizePolicy6)

        self.horizontalLayout.addWidget(self.reset_button)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.stackedPages.addWidget(self.page2)
        self.page3 = QWidget()
        self.page3.setObjectName(u"page3")
        self.gridLayout_12 = QGridLayout(self.page3)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.p3_tableResult = QTableWidget(self.page3)
        self.p3_tableResult.setObjectName(u"p3_tableResult")
        self.p3_tableResult.setEnabled(True)
        self.p3_tableResult.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.p3_tableResult.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.p3_tableResult.setSupportedDragActions(Qt.DropAction.IgnoreAction)

        self.gridLayout_12.addWidget(self.p3_tableResult, 5, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.page3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy5.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy5)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_4.setStyleSheet(u"    color: black;              /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font-weight: bold;         /* \u0416\u0438\u0440\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"    font-size: 14pt;           /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    padding: 4px 8px;          /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043e\u043a\u0440\u0443\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 */")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4.setOpenExternalLinks(False)
        self.label_4.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_4.addWidget(self.label_4)

        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy5.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy5)

        self.verticalLayout_4.addWidget(self.label_2)

        self.p3_count_m = QSpinBox(self.groupBox_3)
        self.p3_count_m.setObjectName(u"p3_count_m")
        self.p3_count_m.setMinimum(2)

        self.verticalLayout_4.addWidget(self.p3_count_m)

        self.label_14 = QLabel(self.groupBox_3)
        self.label_14.setObjectName(u"label_14")
        sizePolicy5.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy5)

        self.verticalLayout_4.addWidget(self.label_14)

        self.p3_count_n = QSpinBox(self.groupBox_3)
        self.p3_count_n.setObjectName(u"p3_count_n")
        self.p3_count_n.setMinimum(2)

        self.verticalLayout_4.addWidget(self.p3_count_n)


        self.gridLayout_12.addWidget(self.groupBox_3, 1, 0, 1, 1)

        self.widget = QWidget(self.page3)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.p3_tableInput_1 = QTableWidget(self.widget)
        self.p3_tableInput_1.setObjectName(u"p3_tableInput_1")
        self.p3_tableInput_1.horizontalHeader().setCascadingSectionResizes(False)
        self.p3_tableInput_1.horizontalHeader().setMinimumSectionSize(115)
        self.p3_tableInput_1.horizontalHeader().setDefaultSectionSize(125)
        self.p3_tableInput_1.verticalHeader().setCascadingSectionResizes(False)

        self.horizontalLayout_2.addWidget(self.p3_tableInput_1)

        self.p3_tableInput_2 = QTableWidget(self.widget)
        self.p3_tableInput_2.setObjectName(u"p3_tableInput_2")
        self.p3_tableInput_2.horizontalHeader().setMinimumSectionSize(115)
        self.p3_tableInput_2.horizontalHeader().setDefaultSectionSize(125)

        self.horizontalLayout_2.addWidget(self.p3_tableInput_2)


        self.gridLayout_12.addWidget(self.widget, 2, 0, 1, 1)

        self.p3_run_button = QPushButton(self.page3)
        self.p3_run_button.setObjectName(u"p3_run_button")

        self.gridLayout_12.addWidget(self.p3_run_button, 4, 0, 1, 1)

        self.stackedPages.addWidget(self.page3)
        self.page4_1 = QWidget()
        self.page4_1.setObjectName(u"page4_1")
        sizePolicy1.setHeightForWidth(self.page4_1.sizePolicy().hasHeightForWidth())
        self.page4_1.setSizePolicy(sizePolicy1)
        self.verticalLayout_5 = QVBoxLayout(self.page4_1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.title_p4 = QLabel(self.page4_1)
        self.title_p4.setObjectName(u"title_p4")
        sizePolicy5.setHeightForWidth(self.title_p4.sizePolicy().hasHeightForWidth())
        self.title_p4.setSizePolicy(sizePolicy5)
        self.title_p4.setStyleSheet(u"    color: black;              /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font-weight: bold;         /* \u0416\u0438\u0440\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"    font-size: 14pt;           /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    padding: 4px 8px;          /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043e\u043a\u0440\u0443\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 */")
        self.title_p4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.title_p4)

        self.group_box_p4 = QGroupBox(self.page4_1)
        self.group_box_p4.setObjectName(u"group_box_p4")
        sizePolicy6.setHeightForWidth(self.group_box_p4.sizePolicy().hasHeightForWidth())
        self.group_box_p4.setSizePolicy(sizePolicy6)
        self.group_box_p4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.group_box_p4.setFlat(False)
        self.verticalLayout = QVBoxLayout(self.group_box_p4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.table_p41 = QTableWidget(self.group_box_p4)
        if (self.table_p41.columnCount() < 6):
            self.table_p41.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_p41.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_p41.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_p41.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_p41.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_p41.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_p41.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.table_p41.rowCount() < 6):
            self.table_p41.setRowCount(6)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_p41.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_p41.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_p41.setVerticalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_p41.setVerticalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_p41.setVerticalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_p41.setVerticalHeaderItem(5, __qtablewidgetitem11)
        self.table_p41.setObjectName(u"table_p41")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.table_p41.sizePolicy().hasHeightForWidth())
        self.table_p41.setSizePolicy(sizePolicy7)
        self.table_p41.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.table_p41.setRowCount(6)
        self.table_p41.setColumnCount(6)

        self.verticalLayout.addWidget(self.table_p41)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.run_p4 = QPushButton(self.group_box_p4)
        self.run_p4.setObjectName(u"run_p4")

        self.horizontalLayout_3.addWidget(self.run_p4)

        self.reset_p4 = QPushButton(self.group_box_p4)
        self.reset_p4.setObjectName(u"reset_p4")

        self.horizontalLayout_3.addWidget(self.reset_p4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_5.addWidget(self.group_box_p4)

        self.stackedPages.addWidget(self.page4_1)
        self.page4_2 = QWidget()
        self.page4_2.setObjectName(u"page4_2")
        sizePolicy1.setHeightForWidth(self.page4_2.sizePolicy().hasHeightForWidth())
        self.page4_2.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.page4_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_18 = QLabel(self.page4_2)
        self.label_18.setObjectName(u"label_18")
        sizePolicy5.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy5)
        self.label_18.setStyleSheet(u"    color: black;              /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font-weight: bold;         /* \u0416\u0438\u0440\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"    font-size: 14pt;           /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    padding: 4px 8px;          /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043e\u043a\u0440\u0443\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 */")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_18)

        self.groupBox_4_2 = QGroupBox(self.page4_2)
        self.groupBox_4_2.setObjectName(u"groupBox_4_2")
        sizePolicy6.setHeightForWidth(self.groupBox_4_2.sizePolicy().hasHeightForWidth())
        self.groupBox_4_2.setSizePolicy(sizePolicy6)
        self.formLayout_3 = QFormLayout(self.groupBox_4_2)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_12 = QLabel(self.groupBox_4_2)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_12)

        self.count_exprets_p4_2 = QSpinBox(self.groupBox_4_2)
        self.count_exprets_p4_2.setObjectName(u"count_exprets_p4_2")
        self.count_exprets_p4_2.setMinimum(1)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.count_exprets_p4_2)

        self.label_20 = QLabel(self.groupBox_4_2)
        self.label_20.setObjectName(u"label_20")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_20)

        self.count_terms_p4_2 = QSpinBox(self.groupBox_4_2)
        self.count_terms_p4_2.setObjectName(u"count_terms_p4_2")
        self.count_terms_p4_2.setMinimum(1)

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.count_terms_p4_2)

        self.label_17 = QLabel(self.groupBox_4_2)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_17)

        self.count_params_p4_2 = QSpinBox(self.groupBox_4_2)
        self.count_params_p4_2.setObjectName(u"count_params_p4_2")
        self.count_params_p4_2.setMinimum(2)

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.FieldRole, self.count_params_p4_2)

        self.run_p4_2 = QPushButton(self.groupBox_4_2)
        self.run_p4_2.setObjectName(u"run_p4_2")

        self.formLayout_3.setWidget(3, QFormLayout.ItemRole.SpanningRole, self.run_p4_2)


        self.verticalLayout_2.addWidget(self.groupBox_4_2)

        self.stackedPages.addWidget(self.page4_2)
        self.page4_3 = QWidget()
        self.page4_3.setObjectName(u"page4_3")
        self.gridLayout_15 = QGridLayout(self.page4_3)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.group_box_p4_3 = QGroupBox(self.page4_3)
        self.group_box_p4_3.setObjectName(u"group_box_p4_3")
        sizePolicy6.setHeightForWidth(self.group_box_p4_3.sizePolicy().hasHeightForWidth())
        self.group_box_p4_3.setSizePolicy(sizePolicy6)
        self.formLayout_2 = QFormLayout(self.group_box_p4_3)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_24 = QLabel(self.group_box_p4_3)
        self.label_24.setObjectName(u"label_24")
        sizePolicy2.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy2)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_24)

        self.label_25 = QLabel(self.group_box_p4_3)
        self.label_25.setObjectName(u"label_25")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_25)

        self.label_26 = QLabel(self.group_box_p4_3)
        self.label_26.setObjectName(u"label_26")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_26)

        self.input_a_p4_3 = QSpinBox(self.group_box_p4_3)
        self.input_a_p4_3.setObjectName(u"input_a_p4_3")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.input_a_p4_3)

        self.input_b_p4_3 = QSpinBox(self.group_box_p4_3)
        self.input_b_p4_3.setObjectName(u"input_b_p4_3")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.input_b_p4_3)

        self.input_c_p4_3 = QSpinBox(self.group_box_p4_3)
        self.input_c_p4_3.setObjectName(u"input_c_p4_3")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.input_c_p4_3)

        self.groupBox_6 = QGroupBox(self.group_box_p4_3)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy8)
        self.gridLayout_16 = QGridLayout(self.groupBox_6)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_27 = QLabel(self.groupBox_6)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_16.addWidget(self.label_27, 1, 0, 1, 1)

        self.label_28 = QLabel(self.groupBox_6)
        self.label_28.setObjectName(u"label_28")
        sizePolicy3.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy3)
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_16.addWidget(self.label_28, 1, 2, 1, 1)

        self.input_x_start_p4_3 = QSpinBox(self.groupBox_6)
        self.input_x_start_p4_3.setObjectName(u"input_x_start_p4_3")
        sizePolicy6.setHeightForWidth(self.input_x_start_p4_3.sizePolicy().hasHeightForWidth())
        self.input_x_start_p4_3.setSizePolicy(sizePolicy6)

        self.gridLayout_16.addWidget(self.input_x_start_p4_3, 1, 1, 1, 1)

        self.input_x_end_p4_3 = QSpinBox(self.groupBox_6)
        self.input_x_end_p4_3.setObjectName(u"input_x_end_p4_3")
        sizePolicy6.setHeightForWidth(self.input_x_end_p4_3.sizePolicy().hasHeightForWidth())
        self.input_x_end_p4_3.setSizePolicy(sizePolicy6)

        self.gridLayout_16.addWidget(self.input_x_end_p4_3, 1, 3, 1, 1)


        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.SpanningRole, self.groupBox_6)

        self.run_p4_3 = QPushButton(self.group_box_p4_3)
        self.run_p4_3.setObjectName(u"run_p4_3")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.SpanningRole, self.run_p4_3)


        self.gridLayout_15.addWidget(self.group_box_p4_3, 1, 0, 1, 1)

        self.label_19 = QLabel(self.page4_3)
        self.label_19.setObjectName(u"label_19")
        sizePolicy5.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy5)
        self.label_19.setStyleSheet(u"    color: black;              /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font-weight: bold;         /* \u0416\u0438\u0440\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"    font-size: 14pt;           /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    padding: 4px 8px;          /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043e\u043a\u0440\u0443\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 */")
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_15.addWidget(self.label_19, 0, 0, 1, 1)

        self.stackedPages.addWidget(self.page4_3)
        self.page5 = QWidget()
        self.page5.setObjectName(u"page5")
        self.gridLayout_4 = QGridLayout(self.page5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox_5 = QGroupBox(self.page5)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy6.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy6)
        self.gridLayout_14 = QGridLayout(self.groupBox_5)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.learning_rate = QDoubleSpinBox(self.groupBox_5)
        self.learning_rate.setObjectName(u"learning_rate")
        sizePolicy3.setHeightForWidth(self.learning_rate.sizePolicy().hasHeightForWidth())
        self.learning_rate.setSizePolicy(sizePolicy3)
        self.learning_rate.setDecimals(3)
        self.learning_rate.setMaximum(100.000000000000000)
        self.learning_rate.setSingleStep(0.010000000000000)

        self.gridLayout_14.addWidget(self.learning_rate, 3, 1, 1, 1)

        self.training_epochs = QSpinBox(self.groupBox_5)
        self.training_epochs.setObjectName(u"training_epochs")
        self.training_epochs.setMaximum(1000000000)
        self.training_epochs.setSingleStep(5)
        self.training_epochs.setValue(20)

        self.gridLayout_14.addWidget(self.training_epochs, 2, 1, 1, 1)

        self.label_21 = QLabel(self.groupBox_5)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_14.addWidget(self.label_21, 2, 0, 1, 1)

        self.label_22 = QLabel(self.groupBox_5)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_14.addWidget(self.label_22, 3, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox_5)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_14.addWidget(self.label_5, 0, 0, 1, 1)

        self.tolerance_error = QDoubleSpinBox(self.groupBox_5)
        self.tolerance_error.setObjectName(u"tolerance_error")
        self.tolerance_error.setMaximum(100.000000000000000)
        self.tolerance_error.setSingleStep(0.010000000000000)

        self.gridLayout_14.addWidget(self.tolerance_error, 4, 1, 1, 1)

        self.label_23 = QLabel(self.groupBox_5)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_14.addWidget(self.label_23, 4, 0, 1, 1)

        self.train_table = QTableWidget(self.groupBox_5)
        if (self.train_table.columnCount() < 4):
            self.train_table.setColumnCount(4)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.train_table.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.train_table.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.train_table.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.train_table.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        if (self.train_table.rowCount() < 5):
            self.train_table.setRowCount(5)
        self.train_table.setObjectName(u"train_table")
        sizePolicy4.setHeightForWidth(self.train_table.sizePolicy().hasHeightForWidth())
        self.train_table.setSizePolicy(sizePolicy4)
        self.train_table.setRowCount(5)

        self.gridLayout_14.addWidget(self.train_table, 1, 0, 1, 2)


        self.gridLayout_4.addWidget(self.groupBox_5, 0, 0, 1, 2)

        self.groupBox_4 = QGroupBox(self.page5)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_23 = QGridLayout(self.groupBox_4)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.run_training = QPushButton(self.groupBox_4)
        self.run_training.setObjectName(u"run_training")
        sizePolicy6.setHeightForWidth(self.run_training.sizePolicy().hasHeightForWidth())
        self.run_training.setSizePolicy(sizePolicy6)

        self.gridLayout_23.addWidget(self.run_training, 0, 0, 1, 1)

        self.progressBar_training = QProgressBar(self.groupBox_4)
        self.progressBar_training.setObjectName(u"progressBar_training")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.progressBar_training.sizePolicy().hasHeightForWidth())
        self.progressBar_training.setSizePolicy(sizePolicy9)
        self.progressBar_training.setValue(0)

        self.gridLayout_23.addWidget(self.progressBar_training, 0, 1, 1, 1)

        self.input = QTableWidget(self.groupBox_4)
        if (self.input.columnCount() < 3):
            self.input.setColumnCount(3)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.input.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.input.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.input.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        if (self.input.rowCount() < 1):
            self.input.setRowCount(1)
        self.input.setObjectName(u"input")
        sizePolicy1.setHeightForWidth(self.input.sizePolicy().hasHeightForWidth())
        self.input.setSizePolicy(sizePolicy1)
        self.input.setEditTriggers(QAbstractItemView.EditTrigger.AllEditTriggers)

        self.gridLayout_23.addWidget(self.input, 1, 0, 1, 2)

        self.run_test_model = QPushButton(self.groupBox_4)
        self.run_test_model.setObjectName(u"run_test_model")
        sizePolicy6.setHeightForWidth(self.run_test_model.sizePolicy().hasHeightForWidth())
        self.run_test_model.setSizePolicy(sizePolicy6)

        self.gridLayout_23.addWidget(self.run_test_model, 2, 0, 1, 1)

        self.progressBar_test_model = QProgressBar(self.groupBox_4)
        self.progressBar_test_model.setObjectName(u"progressBar_test_model")
        sizePolicy9.setHeightForWidth(self.progressBar_test_model.sizePolicy().hasHeightForWidth())
        self.progressBar_test_model.setSizePolicy(sizePolicy9)
        self.progressBar_test_model.setValue(0)

        self.gridLayout_23.addWidget(self.progressBar_test_model, 2, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_4, 1, 0, 1, 2)

        self.stackedPages.addWidget(self.page5)
        self.page7_1 = QWidget()
        self.page7_1.setObjectName(u"page7_1")
        self.gridLayout_7 = QGridLayout(self.page7_1)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_6 = QLabel(self.page7_1)
        self.label_6.setObjectName(u"label_6")
        sizePolicy6.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy6)
        self.label_6.setStyleSheet(u"    color: black;              /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font-weight: bold;         /* \u0416\u0438\u0440\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"    font-size: 14pt;           /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    padding: 4px 8px;          /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043e\u043a\u0440\u0443\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 */")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.label_6, 0, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QFormLayout.RowWrapPolicy.DontWrapRows)
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.formLayout.setHorizontalSpacing(30)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setContentsMargins(-1, -1, -1, 0)
        self.label_29 = QLabel(self.page7_1)
        self.label_29.setObjectName(u"label_29")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_29)

        self.count_experts_p7_1 = QSpinBox(self.page7_1)
        self.count_experts_p7_1.setObjectName(u"count_experts_p7_1")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.count_experts_p7_1)

        self.label_30 = QLabel(self.page7_1)
        self.label_30.setObjectName(u"label_30")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_30)

        self.accuracy_p7_1 = QDoubleSpinBox(self.page7_1)
        self.accuracy_p7_1.setObjectName(u"accuracy_p7_1")
        self.accuracy_p7_1.setDecimals(10)
        self.accuracy_p7_1.setMaximum(1.000000000000000)
        self.accuracy_p7_1.setSingleStep(0.000001000000000)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.accuracy_p7_1)

        self.run_p7_1 = QPushButton(self.page7_1)
        self.run_p7_1.setObjectName(u"run_p7_1")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.SpanningRole, self.run_p7_1)

        self.input_table_p7_1 = QTableWidget(self.page7_1)
        self.input_table_p7_1.setObjectName(u"input_table_p7_1")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.SpanningRole, self.input_table_p7_1)

        self.label_31 = QLabel(self.page7_1)
        self.label_31.setObjectName(u"label_31")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_31)

        self.output_p7_1 = QTextEdit(self.page7_1)
        self.output_p7_1.setObjectName(u"output_p7_1")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.output_p7_1)


        self.gridLayout_7.addLayout(self.formLayout, 1, 0, 1, 1)

        self.stackedPages.addWidget(self.page7_1)
        self.page7_2 = QWidget()
        self.page7_2.setObjectName(u"page7_2")
        self.gridLayout_8 = QGridLayout(self.page7_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_32 = QLabel(self.page7_2)
        self.label_32.setObjectName(u"label_32")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_32)

        self.label_33 = QLabel(self.page7_2)
        self.label_33.setObjectName(u"label_33")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_33)

        self.label_34 = QLabel(self.page7_2)
        self.label_34.setObjectName(u"label_34")

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_34)

        self.count_experts_p7_2 = QSpinBox(self.page7_2)
        self.count_experts_p7_2.setObjectName(u"count_experts_p7_2")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.FieldRole, self.count_experts_p7_2)

        self.count_event_p7_2 = QSpinBox(self.page7_2)
        self.count_event_p7_2.setObjectName(u"count_event_p7_2")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.FieldRole, self.count_event_p7_2)

        self.accuracy_p7_2 = QDoubleSpinBox(self.page7_2)
        self.accuracy_p7_2.setObjectName(u"accuracy_p7_2")
        self.accuracy_p7_2.setDecimals(10)
        self.accuracy_p7_2.setMaximum(1.000000000000000)
        self.accuracy_p7_2.setSingleStep(0.000001000000000)

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.FieldRole, self.accuracy_p7_2)

        self.input_table_p7_2 = QTableWidget(self.page7_2)
        self.input_table_p7_2.setObjectName(u"input_table_p7_2")
        sizePolicy1.setHeightForWidth(self.input_table_p7_2.sizePolicy().hasHeightForWidth())
        self.input_table_p7_2.setSizePolicy(sizePolicy1)

        self.formLayout_4.setWidget(3, QFormLayout.ItemRole.SpanningRole, self.input_table_p7_2)


        self.gridLayout_8.addLayout(self.formLayout_4, 2, 0, 1, 1)

        self.run_p7_2 = QPushButton(self.page7_2)
        self.run_p7_2.setObjectName(u"run_p7_2")

        self.gridLayout_8.addWidget(self.run_p7_2, 3, 0, 1, 1)

        self.label_7 = QLabel(self.page7_2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy6.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy6)
        self.label_7.setStyleSheet(u"    color: black;              /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font-weight: bold;         /* \u0416\u0438\u0440\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"    font-size: 14pt;           /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    padding: 4px 8px;          /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043e\u043a\u0440\u0443\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 */")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.label_7, 1, 0, 1, 1)

        self.output_p7_2 = QTextEdit(self.page7_2)
        self.output_p7_2.setObjectName(u"output_p7_2")
        sizePolicy1.setHeightForWidth(self.output_p7_2.sizePolicy().hasHeightForWidth())
        self.output_p7_2.setSizePolicy(sizePolicy1)

        self.gridLayout_8.addWidget(self.output_p7_2, 4, 0, 1, 1)

        self.stackedPages.addWidget(self.page7_2)
        self.page7_3 = QWidget()
        self.page7_3.setObjectName(u"page7_3")
        self.gridLayout_9 = QGridLayout(self.page7_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_8 = QLabel(self.page7_3)
        self.label_8.setObjectName(u"label_8")
        sizePolicy6.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy6)
        self.label_8.setStyleSheet(u"    color: black;              /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font-weight: bold;         /* \u0416\u0438\u0440\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"    font-size: 14pt;           /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    padding: 4px 8px;          /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043e\u043a\u0440\u0443\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 */")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_9.addWidget(self.label_8, 0, 0, 1, 1)

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_35 = QLabel(self.page7_3)
        self.label_35.setObjectName(u"label_35")

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_35)

        self.label_36 = QLabel(self.page7_3)
        self.label_36.setObjectName(u"label_36")

        self.formLayout_5.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_36)

        self.count_experts_p7_3 = QSpinBox(self.page7_3)
        self.count_experts_p7_3.setObjectName(u"count_experts_p7_3")

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.FieldRole, self.count_experts_p7_3)

        self.count_factors_p7_3 = QSpinBox(self.page7_3)
        self.count_factors_p7_3.setObjectName(u"count_factors_p7_3")

        self.formLayout_5.setWidget(1, QFormLayout.ItemRole.FieldRole, self.count_factors_p7_3)

        self.accuracy_p7_3 = QDoubleSpinBox(self.page7_3)
        self.accuracy_p7_3.setObjectName(u"accuracy_p7_3")
        self.accuracy_p7_3.setDecimals(8)
        self.accuracy_p7_3.setMinimum(0.001000000000000)
        self.accuracy_p7_3.setMaximum(1.000000000000000)
        self.accuracy_p7_3.setSingleStep(0.001000000000000)

        self.formLayout_5.setWidget(2, QFormLayout.ItemRole.FieldRole, self.accuracy_p7_3)

        self.label_37 = QLabel(self.page7_3)
        self.label_37.setObjectName(u"label_37")

        self.formLayout_5.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_37)

        self.output_p7_3 = QTextEdit(self.page7_3)
        self.output_p7_3.setObjectName(u"output_p7_3")

        self.formLayout_5.setWidget(4, QFormLayout.ItemRole.SpanningRole, self.output_p7_3)

        self.run_p7_3 = QPushButton(self.page7_3)
        self.run_p7_3.setObjectName(u"run_p7_3")

        self.formLayout_5.setWidget(3, QFormLayout.ItemRole.SpanningRole, self.run_p7_3)


        self.gridLayout_9.addLayout(self.formLayout_5, 1, 0, 1, 1)

        self.stackedPages.addWidget(self.page7_3)
        self.page7_4 = QWidget()
        self.page7_4.setObjectName(u"page7_4")
        self.gridLayout_10 = QGridLayout(self.page7_4)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_9 = QLabel(self.page7_4)
        self.label_9.setObjectName(u"label_9")
        sizePolicy5.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy5)
        self.label_9.setStyleSheet(u"    color: black;              /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font-weight: bold;         /* \u0416\u0438\u0440\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"    font-size: 14pt;           /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    padding: 4px 8px;          /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043e\u043a\u0440\u0443\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 */")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_10.addWidget(self.label_9, 0, 0, 1, 1)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_38 = QLabel(self.page7_4)
        self.label_38.setObjectName(u"label_38")

        self.formLayout_6.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_38)

        self.count_experts_p7_4 = QSpinBox(self.page7_4)
        self.count_experts_p7_4.setObjectName(u"count_experts_p7_4")
        self.count_experts_p7_4.setMinimum(1)

        self.formLayout_6.setWidget(0, QFormLayout.ItemRole.FieldRole, self.count_experts_p7_4)

        self.label_39 = QLabel(self.page7_4)
        self.label_39.setObjectName(u"label_39")

        self.formLayout_6.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_39)

        self.label_40 = QLabel(self.page7_4)
        self.label_40.setObjectName(u"label_40")

        self.formLayout_6.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_40)

        self.count_factors_p7_4 = QSpinBox(self.page7_4)
        self.count_factors_p7_4.setObjectName(u"count_factors_p7_4")
        self.count_factors_p7_4.setMinimum(1)

        self.formLayout_6.setWidget(1, QFormLayout.ItemRole.FieldRole, self.count_factors_p7_4)

        self.accuracy_p7_4 = QDoubleSpinBox(self.page7_4)
        self.accuracy_p7_4.setObjectName(u"accuracy_p7_4")
        self.accuracy_p7_4.setDecimals(9)
        self.accuracy_p7_4.setMinimum(0.000100000000000)
        self.accuracy_p7_4.setMaximum(1.000000000000000)

        self.formLayout_6.setWidget(2, QFormLayout.ItemRole.FieldRole, self.accuracy_p7_4)

        self.run_p7_4 = QPushButton(self.page7_4)
        self.run_p7_4.setObjectName(u"run_p7_4")

        self.formLayout_6.setWidget(4, QFormLayout.ItemRole.SpanningRole, self.run_p7_4)

        self.input_table_p7_4 = QTableWidget(self.page7_4)
        self.input_table_p7_4.setObjectName(u"input_table_p7_4")

        self.formLayout_6.setWidget(3, QFormLayout.ItemRole.SpanningRole, self.input_table_p7_4)

        self.output_p7_4 = QTextEdit(self.page7_4)
        self.output_p7_4.setObjectName(u"output_p7_4")

        self.formLayout_6.setWidget(5, QFormLayout.ItemRole.SpanningRole, self.output_p7_4)


        self.gridLayout_10.addLayout(self.formLayout_6, 1, 0, 1, 1)

        self.stackedPages.addWidget(self.page7_4)
        self.page8 = QWidget()
        self.page8.setObjectName(u"page8")
        self.gridLayout_11 = QGridLayout(self.page8)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_10 = QLabel(self.page8)
        self.label_10.setObjectName(u"label_10")
        sizePolicy6.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy6)
        self.label_10.setStyleSheet(u"    color: black;              /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font-weight: bold;         /* \u0416\u0438\u0440\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"    font-size: 14pt;           /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    padding: 4px 8px;          /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043e\u043a\u0440\u0443\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 */")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.label_10, 1, 0, 1, 1)

        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.label_41 = QLabel(self.page8)
        self.label_41.setObjectName(u"label_41")

        self.formLayout_7.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_41)

        self.input1_p8 = QSpinBox(self.page8)
        self.input1_p8.setObjectName(u"input1_p8")
        self.input1_p8.setMinimum(1)
        self.input1_p8.setMaximum(10)

        self.formLayout_7.setWidget(0, QFormLayout.ItemRole.FieldRole, self.input1_p8)

        self.input_table1_p8 = QTableWidget(self.page8)
        self.input_table1_p8.setObjectName(u"input_table1_p8")
        sizePolicy.setHeightForWidth(self.input_table1_p8.sizePolicy().hasHeightForWidth())
        self.input_table1_p8.setSizePolicy(sizePolicy)
        self.input_table1_p8.setMinimumSize(QSize(0, 0))
        self.input_table1_p8.setMaximumSize(QSize(16777215, 400))

        self.formLayout_7.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.input_table1_p8)

        self.reset_p8 = QPushButton(self.page8)
        self.reset_p8.setObjectName(u"reset_p8")

        self.formLayout_7.setWidget(2, QFormLayout.ItemRole.LabelRole, self.reset_p8)

        self.run_step1_p8 = QPushButton(self.page8)
        self.run_step1_p8.setObjectName(u"run_step1_p8")

        self.formLayout_7.setWidget(2, QFormLayout.ItemRole.FieldRole, self.run_step1_p8)

        self.output1_p8 = QTextEdit(self.page8)
        self.output1_p8.setObjectName(u"output1_p8")
        sizePolicy.setHeightForWidth(self.output1_p8.sizePolicy().hasHeightForWidth())
        self.output1_p8.setSizePolicy(sizePolicy)
        self.output1_p8.setMinimumSize(QSize(0, 0))
        self.output1_p8.setMaximumSize(QSize(16777215, 450))

        self.formLayout_7.setWidget(3, QFormLayout.ItemRole.SpanningRole, self.output1_p8)

        self.step2_p8 = QPushButton(self.page8)
        self.step2_p8.setObjectName(u"step2_p8")
        self.step2_p8.setStyleSheet(u"background: orange;")

        self.formLayout_7.setWidget(4, QFormLayout.ItemRole.SpanningRole, self.step2_p8)


        self.gridLayout_11.addLayout(self.formLayout_7, 2, 0, 1, 1)

        self.stackedPages.addWidget(self.page8)
        self.page8_2 = QWidget()
        self.page8_2.setObjectName(u"page8_2")
        self.gridLayout_24 = QGridLayout(self.page8_2)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.step1_p8 = QPushButton(self.page8_2)
        self.step1_p8.setObjectName(u"step1_p8")
        self.step1_p8.setStyleSheet(u"background: orange;")

        self.gridLayout_24.addWidget(self.step1_p8, 0, 0, 1, 1)

        self.label_42 = QLabel(self.page8_2)
        self.label_42.setObjectName(u"label_42")
        sizePolicy6.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy6)
        self.label_42.setStyleSheet(u"    color: black;              /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font-weight: bold;         /* \u0416\u0438\u0440\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"    font-size: 14pt;           /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    padding: 4px 8px;          /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043e\u043a\u0440\u0443\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 */")
        self.label_42.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_24.addWidget(self.label_42, 1, 0, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.formLayout_8 = QFormLayout()
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.label_43 = QLabel(self.page8_2)
        self.label_43.setObjectName(u"label_43")

        self.formLayout_8.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_43)

        self.input2_p8 = QSpinBox(self.page8_2)
        self.input2_p8.setObjectName(u"input2_p8")
        self.input2_p8.setMinimum(1)
        self.input2_p8.setMaximum(100)

        self.formLayout_8.setWidget(0, QFormLayout.ItemRole.FieldRole, self.input2_p8)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.run_step2_p8 = QPushButton(self.page8_2)
        self.run_step2_p8.setObjectName(u"run_step2_p8")

        self.horizontalLayout_4.addWidget(self.run_step2_p8)

        self.run_step3_p8 = QPushButton(self.page8_2)
        self.run_step3_p8.setObjectName(u"run_step3_p8")

        self.horizontalLayout_4.addWidget(self.run_step3_p8)


        self.formLayout_8.setLayout(1, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_4)

        self.reset2_p8 = QPushButton(self.page8_2)
        self.reset2_p8.setObjectName(u"reset2_p8")

        self.formLayout_8.setWidget(1, QFormLayout.ItemRole.LabelRole, self.reset2_p8)


        self.verticalLayout_6.addLayout(self.formLayout_8)


        self.gridLayout_24.addLayout(self.verticalLayout_6, 4, 0, 1, 1)

        self.stackedPages.addWidget(self.page8_2)
        self.page9 = QWidget()
        self.page9.setObjectName(u"page9")
        self.gridLayout_17 = QGridLayout(self.page9)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.tabWidget = QTabWidget(self.page9)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Triangular)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideMiddle)
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        sizePolicy1.setHeightForWidth(self.tab1.sizePolicy().hasHeightForWidth())
        self.tab1.setSizePolicy(sizePolicy1)
        self.gridLayout_5 = QGridLayout(self.tab1)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.doc1 = QWebEngineView(self.tab1)
        self.doc1.setObjectName(u"doc1")
        self.doc1.setUrl(QUrl(u"about:blank"))

        self.gridLayout_5.addWidget(self.doc1, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.gridLayout_13 = QGridLayout(self.tab2)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.doc2 = QWebEngineView(self.tab2)
        self.doc2.setObjectName(u"doc2")
        self.doc2.setUrl(QUrl(u"about:blank"))

        self.gridLayout_13.addWidget(self.doc2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QWidget()
        self.tab3.setObjectName(u"tab3")
        self.gridLayout_18 = QGridLayout(self.tab3)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.doc3 = QWebEngineView(self.tab3)
        self.doc3.setObjectName(u"doc3")
        self.doc3.setUrl(QUrl(u"about:blank"))

        self.gridLayout_18.addWidget(self.doc3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab3, "")
        self.tab4 = QWidget()
        self.tab4.setObjectName(u"tab4")
        self.gridLayout_19 = QGridLayout(self.tab4)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.doc4 = QWebEngineView(self.tab4)
        self.doc4.setObjectName(u"doc4")
        self.doc4.setUrl(QUrl(u"about:blank"))

        self.gridLayout_19.addWidget(self.doc4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab4, "")
        self.tab5 = QWidget()
        self.tab5.setObjectName(u"tab5")
        self.gridLayout_20 = QGridLayout(self.tab5)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.doc5 = QWebEngineView(self.tab5)
        self.doc5.setObjectName(u"doc5")
        self.doc5.setUrl(QUrl(u"about:blank"))

        self.gridLayout_20.addWidget(self.doc5, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab5, "")
        self.tab7 = QWidget()
        self.tab7.setObjectName(u"tab7")
        self.gridLayout_21 = QGridLayout(self.tab7)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.doc7 = QWebEngineView(self.tab7)
        self.doc7.setObjectName(u"doc7")
        self.doc7.setUrl(QUrl(u"about:blank"))

        self.gridLayout_21.addWidget(self.doc7, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab7, "")
        self.tab8 = QWidget()
        self.tab8.setObjectName(u"tab8")
        self.tab8.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.gridLayout_22 = QGridLayout(self.tab8)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.doc8 = QWebEngineView(self.tab8)
        self.doc8.setObjectName(u"doc8")
        self.doc8.setUrl(QUrl(u"about:blank"))

        self.gridLayout_22.addWidget(self.doc8, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab8, "")

        self.gridLayout_17.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.stackedPages.addWidget(self.page9)
        self.page10 = QWidget()
        self.page10.setObjectName(u"page10")
        self.gridLayout_2 = QGridLayout(self.page10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_11 = QLabel(self.page10)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"    color: black;              /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font-weight: bold;         /* \u0416\u0438\u0440\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"    font-size: 14pt;           /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    padding: 4px 8px;          /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043e\u043a\u0440\u0443\u0433 \u0442\u0435\u043a\u0441\u0442\u0430 */")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_11.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1)

        self.stackedPages.addWidget(self.page10)

        self.gridLayout_6.addWidget(self.stackedPages, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 916, 20))
        self.menu_1 = QMenu(self.menubar)
        self.menu_1.setObjectName(u"menu_1")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        self.menu_5 = QMenu(self.menubar)
        self.menu_5.setObjectName(u"menu_5")
        self.menu_7 = QMenu(self.menubar)
        self.menu_7.setObjectName(u"menu_7")
        self.menu_8 = QMenu(self.menubar)
        self.menu_8.setObjectName(u"menu_8")
        self.menu_9 = QMenu(self.menubar)
        self.menu_9.setObjectName(u"menu_9")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu_1.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu_7.menuAction())
        self.menubar.addAction(self.menu_8.menuAction())
        self.menubar.addAction(self.menu_9.menuAction())
        self.menu_1.addAction(self.action1)
        self.menu_2.addAction(self.action2)
        self.menu_3.addAction(self.action3)
        self.menu_4.addAction(self.action4_1)
        self.menu_4.addAction(self.action4_2)
        self.menu_4.addAction(self.action4_3)
        self.menu_5.addAction(self.action5)
        self.menu_7.addAction(self.action7_1)
        self.menu_7.addAction(self.action7_2)
        self.menu_7.addAction(self.action7_3)
        self.menu_7.addAction(self.action7_4)
        self.menu_8.addAction(self.action8)
        self.menu_9.addAction(self.action9)
        self.menu_9.addAction(self.action10)

        self.retranslateUi(MainWindow)

        self.stackedPages.setCurrentIndex(12)
        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action9.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043e\u0440\u0438\u044f", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043e\u0440\u0438\u044f", None))
        self.action7_1.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u044c 1 \u041a\u043e\u043c\u043f\u0435\u0442\u0435\u043d\u0442\u043d\u043e\u0441\u0442\u044c \u044d\u043a\u0441\u043f\u0435\u0440\u0442\u043e\u0432", None))
        self.action7_2.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u044c 2 \u0413\u0440\u0443\u043f\u043f\u043e\u0432\u0430\u044f \u044d\u043a\u0441\u043f\u0435\u0440\u0442\u043d\u0430\u044f \u043e\u0446\u0435\u043d\u043a\u0430", None))
        self.action7_3.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u044c 3 \u041c\u0435\u0442\u043e\u0434 \u043f\u0430\u0440\u043d\u044b\u0445 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0439", None))
        self.action7_4.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u044c 4 \u041c\u0435\u0442\u043e\u0434 \u043e\u0431\u043e\u0431\u0449\u0435\u043d\u043d\u044b\u0445 \u0440\u0430\u043d\u0436\u0438\u0440\u043e\u0432\u043e\u043a", None))
        self.action1.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0430 \u041a\u043e\u043c\u043c\u0438\u0432\u043e\u044f\u0436\u0435\u0440\u0430", None))
        self.action2.setText(QCoreApplication.translate("MainWindow", u"K-means \u043a\u043b\u0430\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.action3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u043f\u043e\u0437\u0438\u0446\u0438\u043e\u043d\u043d\u043e\u0435 \u043f\u0440\u0430\u0432\u0438\u043b\u043e Max-min", None))
        self.action5.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0439\u0440\u043e\u043d\u043d\u0430\u044f \u0441\u0435\u0442\u044c", None))
        self.action4_1.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u043f\u0430\u0440\u043d\u044b\u0445 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0439", None))
        self.action_1.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043e\u0440\u0438\u044f", None))
        self.action_11.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043e\u0440\u0438\u044f", None))
        self.action_12.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043e\u0440\u0438\u044f", None))
        self.action_13.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043e\u0440\u0438\u044f", None))
        self.action_14.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043e\u0440\u0438\u044f", None))
        self.action_15.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043e\u0440\u0438\u044f", None))
        self.action8.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043d\u044f\u0442\u0438\u0435 \u0440\u0435\u0448\u0435\u043d\u0438\u0439 \u043c\u0435\u0442\u043e\u0434\u043e\u043c \u0430\u043d\u0430\u043b\u0438\u0437\u0430 \u0438\u0435\u0440\u0430\u0440\u0445\u0438\u0439", None))
        self.action_17.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043e\u0440\u0438\u044f", None))
        self.action10.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.action4_2.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u0435\u0440\u0442\u043d\u0430\u044f \u043e\u0446\u0435\u043d\u043a\u0430", None))
        self.action4_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435 \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u043e\u0439 \u0444\u0443\u043d\u043a\u0446\u0438\u0438 \u043f\u0440\u0438\u043d\u0430\u0434\u043b\u0435\u0436\u043d\u043e\u0441\u0442\u0438", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440\u043d\u043e\u0441\u0442\u044c \u043c\u0430\u0442\u0440\u0438\u0446\u044b", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0448\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443 \u043a\u043e\u043c\u043c\u0438\u0432\u043e\u044f\u0436\u0435\u0440\u0430", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0430 \u041a\u043e\u043c\u043c\u0438\u0432\u043e\u044f\u0436\u0435\u0440\u0430", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"K-means \u043a\u043b\u0430\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.groupBox.setTitle("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0442\u043e\u0447\u0435\u043a:", None))
#if QT_CONFIG(tooltip)
        self.num_points_spin.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u043b\u0430\u0441\u0442\u0435\u0440\u043e\u0432:", None))
        self.groupBox_2.setTitle("")
        self.run_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c", None))
        self.step_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u0439 \u0448\u0430\u0433", None))
        self.reset_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.groupBox_3.setTitle("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u043f\u043e\u0437\u0438\u0446\u0438\u043e\u043d\u043d\u043e\u0435 \u043f\u0440\u0430\u0432\u0438\u043b\u043e Max-min", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u043b-\u0432\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a (m):", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u043b-\u0432\u043e \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u0435\u0439 (n):", None))
        self.p3_run_button.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.title_p4.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u043f\u0430\u0440\u043d\u044b\u0445 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0439", None))
        self.group_box_p4.setTitle("")
        ___qtablewidgetitem = self.table_p41.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"170", None));
        ___qtablewidgetitem1 = self.table_p41.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"175", None));
        ___qtablewidgetitem2 = self.table_p41.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"180", None));
        ___qtablewidgetitem3 = self.table_p41.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"185", None));
        ___qtablewidgetitem4 = self.table_p41.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"190", None));
        ___qtablewidgetitem5 = self.table_p41.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"195", None));
        ___qtablewidgetitem6 = self.table_p41.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"170", None));
        ___qtablewidgetitem7 = self.table_p41.verticalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"175", None));
        ___qtablewidgetitem8 = self.table_p41.verticalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"180", None));
        ___qtablewidgetitem9 = self.table_p41.verticalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"185", None));
        ___qtablewidgetitem10 = self.table_p41.verticalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"190", None));
        ___qtablewidgetitem11 = self.table_p41.verticalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"195", None));
        self.run_p4.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c", None))
        self.reset_p4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u043a \u043d\u0430\u0447\u0430\u043b\u044c\u043d\u044b\u043c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f\u043c", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u0435\u0440\u0442\u043d\u0430\u044f \u043e\u0446\u0435\u043d\u043a\u0430", None))
        self.groupBox_4_2.setTitle("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e \u044d\u043a\u0441\u043f\u0435\u0440\u0442\u043e\u0432", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e \u0442\u0435\u0440\u043c\u043e\u0432", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432", None))
        self.run_p4_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.group_box_p4_3.setTitle("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 a:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 b:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 c:", None))
        self.groupBox_6.setTitle("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043e\u0442\u0440\u0435\u0437\u043e\u043a \u043f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u044f: \u043e\u0442", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u0434\u043e", None))
        self.run_p4_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c ", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435 \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u043e\u0439 \u0444\u0443\u043d\u043a\u0446\u0438\u0438 \u043f\u0440\u0438\u043d\u0430\u0434\u043b\u0435\u0436\u043d\u043e\u0441\u0442\u0438", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u041d\u0421", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e \u044d\u043f\u043e\u0445 \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f (training epochs)", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f (learning rate)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0443\u0447\u0430\u044e\u0449\u0430\u044f \u0432\u044b\u0431\u043e\u0440\u043a\u0430", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043f\u0443\u0441\u0442\u0438\u043c\u0430\u044f \u043e\u0448\u0438\u0431\u043a\u0430 (tolerance error)", None))
        ___qtablewidgetitem12 = self.train_table.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"x1", None));
        ___qtablewidgetitem13 = self.train_table.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"x2", None));
        ___qtablewidgetitem14 = self.train_table.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"x3", None));
        ___qtablewidgetitem15 = self.train_table.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"y", None));
        self.groupBox_4.setTitle("")
        self.run_training.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u0435 \u043c\u043e\u0434\u0435\u043b\u0438", None))
        ___qtablewidgetitem16 = self.input.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"x1", None));
        ___qtablewidgetitem17 = self.input.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"x2", None));
        ___qtablewidgetitem18 = self.input.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"x3", None));
        self.run_test_model.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043c\u043e\u0434\u0435\u043b\u0438", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u044c 1 \u041a\u043e\u043c\u043f\u0435\u0442\u0435\u043d\u0442\u043d\u043e\u0441\u0442\u044c \u044d\u043a\u0441\u043f\u0435\u0440\u0442\u043e\u0432", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0441\u043b\u043e \u044d\u043a\u0441\u043f\u0435\u0440\u0442\u043e\u0432", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0447\u043d\u043e\u0441\u0442\u044c", None))
        self.run_p7_1.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0441\u0442\u0438 \u043e\u0446\u0435\u043d\u043a\u0443", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0448\u0435\u043d\u0438\u0435:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0441\u043b\u043e \u044d\u043a\u0441\u043f\u0435\u0440\u0442\u043e\u0432:", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0441\u043b\u043e \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0439:", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0447\u043d\u043e\u0441\u0442\u044c:", None))
        self.run_p7_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0441\u0442\u0438 \u043e\u0446\u0435\u043d\u043a\u0443", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u044c 2 \u0413\u0440\u0443\u043f\u043f\u043e\u0432\u0430\u044f \u044d\u043a\u0441\u043f\u0435\u0440\u0442\u043d\u0430\u044f \u043e\u0446\u0435\u043d\u043a\u0430", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u044c 3 \u041c\u0435\u0442\u043e\u0434 \u043f\u0430\u0440\u043d\u044b\u0445 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0439", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0441\u043b\u043e \u044d\u043a\u0441\u043f\u0435\u0440\u0442\u043e\u0432:", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0441\u043b\u043e \u0444\u0430\u043a\u0442\u043e\u0440\u043e\u0432:", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0447\u043d\u043e\u0441\u0442\u044c:", None))
        self.run_p7_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0441\u0442\u0438 \u043e\u0446\u0435\u043d\u043a\u0443", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u044c 4 \u041c\u0435\u0442\u043e\u0434 \u043e\u0431\u043e\u0431\u0449\u0435\u043d\u043d\u044b\u0445 \u0440\u0430\u043d\u0436\u0438\u0440\u043e\u0432\u043e\u043a", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0441\u043b\u043e \u044d\u043a\u0441\u043f\u0435\u0440\u0442\u043e\u0432:", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0441\u043b\u043e \u0444\u0430\u043a\u0442\u043e\u0440\u043e\u0432:", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0447\u043d\u043e\u0441\u0442\u044c:", None))
        self.run_p7_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0441\u0442\u0438 \u043e\u0446\u0435\u043d\u043a\u0443", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043d\u044f\u0442\u0438\u0435 \u0440\u0435\u0448\u0435\u043d\u0438\u0439 \u043c\u0435\u0442\u043e\u0434\u043e\u043c \u0430\u043d\u0430\u043b\u0438\u0437\u0430 \u0438\u0435\u0440\u0430\u0440\u0445\u0438\u0439", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u043b-\u0432\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a:", None))
        self.reset_p8.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u043a \u0442\u0435\u0441\u0442\u043e\u0432\u044b\u043c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f\u043c", None))
        self.run_step1_p8.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0441\u0442\u0438 \u0430\u043d\u0430\u043b\u0438\u0437 2 \u0443\u0440\u043e\u0432\u043d\u044f", None))
        self.step2_p8.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0439\u0442\u0438 \u043a \u0430\u043d\u0430\u043b\u0438\u0437\u0443 3 \u0443\u0440\u043e\u0432\u043d\u044f", None))
        self.step1_p8.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u043a \u0430\u043d\u0430\u043b\u0438\u0437\u0443 2 \u0443\u0440\u043e\u0432\u043d\u044f", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043d\u044f\u0442\u0438\u0435 \u0440\u0435\u0448\u0435\u043d\u0438\u0439 \u043c\u0435\u0442\u043e\u0434\u043e\u043c \u0430\u043d\u0430\u043b\u0438\u0437\u0430 \u0438\u0435\u0440\u0430\u0440\u0445\u0438\u0439", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u043b-\u0432\u043e \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a:", None))
        self.run_step2_p8.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0441\u0442\u0438 \u0430\u043d\u0430\u043b\u0438\u0437 3 \u0443\u0440\u043e\u0432\u043d\u044f", None))
        self.run_step3_p8.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0433\u043b\u043e\u0431\u0430\u043b\u044c\u043d\u044b\u0439 \u043f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442", None))
        self.reset2_p8.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u043a \u0442\u0435\u0441\u0442\u043e\u0432\u044b\u043c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f\u043c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u043a\u0442\u0438\u043a\u0430 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u043a\u0442\u0438\u043a\u0430 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u043a\u0442\u0438\u043a\u0430 3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab4), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u043a\u0442\u0438\u043a\u0430 4", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab5), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u043a\u0442\u0438\u043a\u0430 5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab7), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u043a\u0442\u0438\u043a\u0430 7", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab8), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u043a\u0442\u0438\u043a\u0430 8", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435:\n"
"\u0412\u0435\u0431-\u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u00ab\u041a\u043e\u043c\u043f\u043b\u0435\u043a\u0441 \u043f\u0440\u0438\u043a\u043b\u0430\u0434\u043d\u044b\u0445 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c \u0434\u043b\u044f \u0440\u0435\u0448\u0435\u043d\u0438\u044f \u043f\u0440\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u0437\u0430\u0434\u0430\u0447 \u043f\u043e \u0434\u0438\u0441\u0446\u0438\u043f\u043b\u0438\u043d\u0435\u00bb \u043f\u0440\u0435\u0434\u043e\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u0442 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u0440\u0435\u0448\u0438\u0442\u044c \u043c\u043d\u043e\u0436\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u0437\u0430\u0434\u0430\u0447 \u043f\u043e \u0434\u0438\u0441\u0446\u0438\u043f\u043b\u0438\u043d\u0435, \u0430 \u0438\u043c\u0435\u043d\u043d\u043e:\n"
"\u041f\u0440\u0430"
                        "\u043a\u0442\u0438\u043a\u0430 1:\n"
" - \u0417\u0430\u0434\u0430\u0447\u0430 \u043a\u043e\u043c\u043c\u0438\u0432\u043e\u044f\u0436\u0435\u0440\u0430;\n"
"\u041f\u0440\u0430\u043a\u0442\u0438\u043a\u0430 2:\n"
" - K-means \u043a\u043b\u0430\u0441\u0442\u0435\u0440\u0438\u0437\u0430\u0446\u0438\u044f;\n"
"\u041f\u0440\u0430\u043a\u0442\u0438\u043a\u0430 3:\n"
" - \u041a\u043e\u043c\u043f\u043e\u0437\u0438\u0446\u0438\u043e\u043d\u043d\u043e\u0435 \u043f\u0440\u0430\u0432\u0438\u043b\u043e Max-min;\n"
"\u041f\u0440\u0430\u043a\u0442\u0438\u043a\u0430 4:\n"
" - \u041c\u0435\u0442\u043e\u0434 \u043f\u0430\u0440\u043d\u044b\u0445 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0439;\n"
" - \u042d\u043a\u0441\u043f\u0435\u0440\u0442\u043d\u0430\u044f \u043e\u0446\u0435\u043d\u043a\u0430;\n"
" - \u041f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435 \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u043e\u0439 \u0444\u0443\u043d\u043a\u0446\u0438\u0438 \u043f\u0440\u0438\u043d\u0430\u0434\u043b\u0435\u0436"
                        "\u043d\u043e\u0441\u0442\u0438;\n"
" \u041f\u0440\u0430\u043a\u0442\u0438\u043a\u0430 5: \n"
" - \u041d\u0435\u0439\u0440\u043e\u043d\u043d\u0430\u044f \u0441\u0435\u0442\u044c (\u041f\u0435\u0440\u0446\u0435\u043f\u0442\u0440\u043e\u043d);\n"
"\u041f\u0440\u0430\u043a\u0442\u0438\u043a\u0430 7 (\u0420\u0430\u0441\u0447\u0435\u0442 \u0433\u0440\u0443\u043f\u043f\u043e\u0432\u044b\u0445 \u043e\u0446\u0435\u043d\u043e\u043a \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0439): \n"
" - \u041a\u043e\u043c\u043f\u0435\u0442\u0435\u043d\u0442\u043d\u043e\u0441\u0442\u044c \u044d\u043a\u0441\u043f\u0435\u0440\u0442\u043e\u0432; \n"
" - \u0413\u0440\u0443\u043f\u043f\u043e\u0432\u0430\u044f \u044d\u043a\u0441\u043f\u0435\u0440\u0442\u043d\u0430\u044f \u043e\u0446\u0435\u043d\u043a\u0430; \n"
" - \u041c\u0435\u0442\u043e\u0434 \u043f\u0430\u0440\u043d\u044b\u0445 \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0439; \n"
" - \u041c\u0435\u0442\u043e\u0434 \u043e\u0431\u043e\u0431\u0449\u0435\u043d\u043d"
                        "\u044b\u0445 \u0440\u0430\u043d\u0436\u0438\u0440\u043e\u0432\u043e\u043a;\n"
" \u041f\u0440\u0430\u043a\u0442\u0438\u043a\u0430 8:\n"
" - \u041f\u0440\u0438\u043d\u044f\u0442\u0438\u0435 \u0440\u0435\u0448\u0435\u043d\u0438\u0439 \u043c\u0435\u0442\u043e\u0434\u043e\u043c \u0430\u043d\u0430\u043b\u0438\u0437\u0430 \u0438\u0435\u0440\u0430\u0440\u0445\u0438\u0439.\n"
"\n"
"\u0410\u0432\u0442\u043e\u0440\u044b:\n"
"\u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c \u043f\u0440\u043e\u0435\u043a\u0442\u0430:\n"
"\u0434\u043e\u0446\u0435\u043d\u0442 \u043a\u0430\u0444\u0435\u0434\u0440\u044b \u041f\u041e\u0412\u0422\u0410\u0421 \u0421\u0435\u043c\u0435\u043d\u043e\u0432 \u0410.\u041c.\n"
"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0441\u0442\u044b:\n"
"\u0441\u0442\u0443\u0434\u0435\u043d\u0442\u044b \u043a\u0430\u0444\u0435\u0434\u0440\u044b \u041f\u041e\u0412\u0422\u0410\u0421 \u0433\u0440\u0443\u043f\u043f\u044b 25\u041f\u0438\u043d\u0436(\u043c)\u0420\u0418\u0422\u0441 \u041c"
                        "\u0430\u0440\u0442\u044b\u043d\u043e\u0432 \u0410.\u0412. \u0438 \u0427\u0435\u0431\u043e\u0442\u0430\u0435\u0432\u0430 \u0415.\u0412.\n"
"\u0413\u043e\u0434 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0438: 2026", None))
        self.menu_1.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u043a\u0442\u0438\u043a\u0430 1", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u043a\u0442\u0438\u043a\u0430 2", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u043a\u0442\u0438\u043a\u0430 3", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u043a\u0442\u0438\u043a\u0430 4", None))
        self.menu_5.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u043a\u0442\u0438\u043a\u0430 5", None))
        self.menu_7.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u043a\u0442\u0438\u043a\u0430 7", None))
        self.menu_8.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u043a\u0442\u0438\u043a\u0430 8", None))
        self.menu_9.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
    # retranslateUi

