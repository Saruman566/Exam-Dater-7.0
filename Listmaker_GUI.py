# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Listmaker_GUI.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QToolButton, QVBoxLayout,
    QWidget)
import pictures

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(647, 830)
        MainWindow.setMinimumSize(QSize(640, 830))
        MainWindow.setMaximumSize(QSize(647, 830))
        MainWindow.setSizeIncrement(QSize(640, 830))
        self.actionNotenListe = QAction(MainWindow)
        self.actionNotenListe.setObjectName(u"actionNotenListe")
        self.actionListmaker = QAction(MainWindow)
        self.actionListmaker.setObjectName(u"actionListmaker")
        self.container = QWidget(MainWindow)
        self.container.setObjectName(u"container")
        self.gridLayout = QGridLayout(self.container)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(self.container)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.main_frame.setFrameShape(QFrame.Panel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.main_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 0, 5, 0)
        self.menu_container = QFrame(self.main_frame)
        self.menu_container.setObjectName(u"menu_container")
        self.menu_container.setMinimumSize(QSize(635, 300))
        self.menu_container.setMaximumSize(QSize(635, 300))
        self.menu_container.setSizeIncrement(QSize(635, 300))
        self.menu_container.setFrameShape(QFrame.Panel)
        self.menu_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.menu_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 9)
        self.menu_frame = QFrame(self.menu_container)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Sunken)
        self.gridLayout_3 = QGridLayout(self.menu_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Show_window2 = QFrame(self.menu_frame)
        self.Show_window2.setObjectName(u"Show_window2")
        self.Show_window2.setFrameShape(QFrame.Box)
        self.Show_window2.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_4 = QVBoxLayout(self.Show_window2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.themen_label = QLabel(self.Show_window2)
        self.themen_label.setObjectName(u"themen_label")
        self.themen_label.setMinimumSize(QSize(0, 0))
        self.themen_label.setMaximumSize(QSize(16777215, 16777215))
        self.themen_label.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Lucida Handwriting"])
        font.setPointSize(22)
        self.themen_label.setFont(font)
        self.themen_label.setFrameShape(QFrame.NoFrame)
        self.themen_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.themen_label)


        self.gridLayout_3.addWidget(self.Show_window2, 1, 0, 1, 1)

        self.del_button = QToolButton(self.menu_frame)
        self.del_button.setObjectName(u"del_button")
        self.del_button.setMinimumSize(QSize(50, 50))
        self.del_button.setMaximumSize(QSize(50, 50))
        self.del_button.setSizeIncrement(QSize(50, 50))
        self.del_button.setFont(font)
        self.del_button.setStyleSheet(u"image: url(:/delete/images/trashcan.png);")
        self.del_button.setPopupMode(QToolButton.InstantPopup)
        self.del_button.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.del_button.setArrowType(Qt.DownArrow)

        self.gridLayout_3.addWidget(self.del_button, 2, 4, 1, 1)

        self.teacher_del_button = QPushButton(self.menu_frame)
        self.teacher_del_button.setObjectName(u"teacher_del_button")
        self.teacher_del_button.setMinimumSize(QSize(50, 50))
        self.teacher_del_button.setMaximumSize(QSize(50, 50))
        self.teacher_del_button.setSizeIncrement(QSize(50, 50))
        self.teacher_del_button.setStyleSheet(u"image: url(:/back/images/back.png);")

        self.gridLayout_3.addWidget(self.teacher_del_button, 0, 4, 1, 1)

        self.Show_window1 = QFrame(self.menu_frame)
        self.Show_window1.setObjectName(u"Show_window1")
        self.Show_window1.setMinimumSize(QSize(371, 50))
        self.Show_window1.setMaximumSize(QSize(371, 50))
        self.Show_window1.setSizeIncrement(QSize(371, 50))
        self.Show_window1.setStyleSheet(u"")
        self.Show_window1.setFrameShape(QFrame.Box)
        self.Show_window1.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_3 = QVBoxLayout(self.Show_window1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lehrer_label = QLabel(self.Show_window1)
        self.lehrer_label.setObjectName(u"lehrer_label")
        self.lehrer_label.setMinimumSize(QSize(0, 0))
        self.lehrer_label.setMaximumSize(QSize(16777215, 16777215))
        self.lehrer_label.setSizeIncrement(QSize(0, 0))
        self.lehrer_label.setFont(font)
        self.lehrer_label.setFrameShape(QFrame.NoFrame)
        self.lehrer_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lehrer_label)


        self.gridLayout_3.addWidget(self.Show_window1, 0, 0, 1, 1)

        self.Show_window3 = QFrame(self.menu_frame)
        self.Show_window3.setObjectName(u"Show_window3")
        self.Show_window3.setFont(font)
        self.Show_window3.setFrameShape(QFrame.Box)
        self.Show_window3.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout = QHBoxLayout(self.Show_window3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.dateEdit = QDateEdit(self.Show_window3)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(0, 50))
        self.dateEdit.setMaximumSize(QSize(16777215, 50))
        self.dateEdit.setSizeIncrement(QSize(0, 50))
        font1 = QFont()
        font1.setFamilies([u"Lucida Handwriting"])
        font1.setPointSize(22)
        font1.setBold(False)
        font1.setItalic(False)
        self.dateEdit.setFont(font1)
        self.dateEdit.setStyleSheet(u"font: 22pt \"Lucida Handwriting\";")
        self.dateEdit.setAlignment(Qt.AlignCenter)
        self.dateEdit.setReadOnly(False)
        self.dateEdit.setDateTime(QDateTime(QDate(2023, 1, 5), QTime(1, 0, 0)))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setTimeSpec(Qt.LocalTime)

        self.horizontalLayout.addWidget(self.dateEdit)


        self.gridLayout_3.addWidget(self.Show_window3, 2, 0, 1, 1)

        self.themes_del_button = QPushButton(self.menu_frame)
        self.themes_del_button.setObjectName(u"themes_del_button")
        self.themes_del_button.setMinimumSize(QSize(50, 50))
        self.themes_del_button.setMaximumSize(QSize(50, 50))
        self.themes_del_button.setSizeIncrement(QSize(50, 50))
        self.themes_del_button.setStyleSheet(u"image: url(:/back/images/back.png);")

        self.gridLayout_3.addWidget(self.themes_del_button, 1, 4, 1, 1)

        self.btn_themen = QToolButton(self.menu_frame)
        self.btn_themen.setObjectName(u"btn_themen")
        self.btn_themen.setMinimumSize(QSize(120, 50))
        self.btn_themen.setMaximumSize(QSize(120, 50))
        self.btn_themen.setSizeIncrement(QSize(120, 50))
        self.btn_themen.setBaseSize(QSize(120, 50))
        font2 = QFont()
        font2.setFamilies([u"Lucida Handwriting"])
        font2.setPointSize(18)
        font2.setBold(False)
        self.btn_themen.setFont(font2)
        self.btn_themen.setPopupMode(QToolButton.InstantPopup)
        self.btn_themen.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.btn_themen.setArrowType(Qt.DownArrow)

        self.gridLayout_3.addWidget(self.btn_themen, 1, 3, 1, 1)

        self.btn_teacher = QToolButton(self.menu_frame)
        self.btn_teacher.setObjectName(u"btn_teacher")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_teacher.sizePolicy().hasHeightForWidth())
        self.btn_teacher.setSizePolicy(sizePolicy)
        self.btn_teacher.setMinimumSize(QSize(120, 50))
        self.btn_teacher.setMaximumSize(QSize(120, 50))
        self.btn_teacher.setSizeIncrement(QSize(120, 50))
        self.btn_teacher.setBaseSize(QSize(120, 50))
        font3 = QFont()
        font3.setFamilies([u"Lucida Handwriting"])
        font3.setPointSize(18)
        font3.setBold(False)
        font3.setItalic(False)
        self.btn_teacher.setFont(font3)
        self.btn_teacher.setFocusPolicy(Qt.TabFocus)
        self.btn_teacher.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btn_teacher.setAcceptDrops(False)
        self.btn_teacher.setLayoutDirection(Qt.LeftToRight)
        self.btn_teacher.setStyleSheet(u"")
        self.btn_teacher.setIconSize(QSize(0, 0))
        self.btn_teacher.setCheckable(False)
        self.btn_teacher.setPopupMode(QToolButton.InstantPopup)
        self.btn_teacher.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.btn_teacher.setAutoRaise(False)
        self.btn_teacher.setArrowType(Qt.DownArrow)

        self.gridLayout_3.addWidget(self.btn_teacher, 0, 3, 1, 1)

        self.save_button = QPushButton(self.menu_frame)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setMinimumSize(QSize(50, 50))
        self.save_button.setMaximumSize(QSize(50, 50))
        self.save_button.setSizeIncrement(QSize(50, 50))
        self.save_button.setStyleSheet(u"image: url(:/save/images/save.png);")

        self.gridLayout_3.addWidget(self.save_button, 2, 3, 1, 1)


        self.verticalLayout.addWidget(self.menu_frame)


        self.gridLayout_2.addWidget(self.menu_container, 0, 0, 1, 1)

        self.show_frame = QFrame(self.main_frame)
        self.show_frame.setObjectName(u"show_frame")
        self.show_frame.setMinimumSize(QSize(633, 480))
        self.show_frame.setMaximumSize(QSize(633, 480))
        self.show_frame.setSizeIncrement(QSize(633, 480))
        self.show_frame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.show_frame.setFrameShape(QFrame.Box)
        self.show_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.show_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.date_table = QTableWidget(self.show_frame)
        if (self.date_table.columnCount() < 4):
            self.date_table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.date_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.date_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.date_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.date_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.date_table.rowCount() < 8):
            self.date_table.setRowCount(8)
        self.date_table.setObjectName(u"date_table")
        self.date_table.setMinimumSize(QSize(633, 480))
        self.date_table.setMaximumSize(QSize(633, 480))
        self.date_table.setSizeIncrement(QSize(633, 480))
        self.date_table.setLayoutDirection(Qt.LeftToRight)
        self.date_table.setAutoFillBackground(False)
        self.date_table.setStyleSheet(u"font: 14pt \"Lucida Handwriting\";\n"
"background-color: rgb(85, 255, 255);")
        self.date_table.setFrameShape(QFrame.NoFrame)
        self.date_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.date_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.date_table.setShowGrid(False)
        self.date_table.setGridStyle(Qt.CustomDashLine)
        self.date_table.setSortingEnabled(False)
        self.date_table.setWordWrap(True)
        self.date_table.setCornerButtonEnabled(True)
        self.date_table.setRowCount(8)
        self.date_table.setColumnCount(4)
        self.date_table.horizontalHeader().setVisible(True)
        self.date_table.horizontalHeader().setCascadingSectionResizes(True)
        self.date_table.horizontalHeader().setMinimumSectionSize(0)
        self.date_table.horizontalHeader().setDefaultSectionSize(90)
        self.date_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.date_table.horizontalHeader().setStretchLastSection(True)
        self.date_table.verticalHeader().setVisible(False)
        self.date_table.verticalHeader().setCascadingSectionResizes(False)
        self.date_table.verticalHeader().setMinimumSectionSize(25)
        self.date_table.verticalHeader().setDefaultSectionSize(55)
        self.date_table.verticalHeader().setProperty("showSortIndicator", False)
        self.date_table.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.date_table)


        self.gridLayout_2.addWidget(self.show_frame, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.main_frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.container)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 647, 22))
        self.Menu = QMenu(self.menuBar)
        self.Menu.setObjectName(u"Menu")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.Menu.menuAction())
        self.Menu.addAction(self.actionNotenListe)
        self.Menu.addSeparator()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNotenListe.setText(QCoreApplication.translate("MainWindow", u"Notes-list", None))
#if QT_CONFIG(tooltip)
        self.actionNotenListe.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700; text-decoration: underline;\">Noten-Liste</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.actionListmaker.setText(QCoreApplication.translate("MainWindow", u"Listmaker", None))
        self.themen_label.setText("")
        self.del_button.setText("")
        self.teacher_del_button.setText("")
        self.lehrer_label.setText("")
        self.themes_del_button.setText("")
        self.btn_themen.setText(QCoreApplication.translate("MainWindow", u"Themes", None))
        self.btn_teacher.setText(QCoreApplication.translate("MainWindow", u"Teacher", None))
        self.save_button.setText("")
        ___qtablewidgetitem = self.date_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nr", None));
        ___qtablewidgetitem1 = self.date_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"   Date   ", None));
        ___qtablewidgetitem2 = self.date_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"      Teacher     ", None));
        ___qtablewidgetitem3 = self.date_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Theme", None));
        self.Menu.setTitle(QCoreApplication.translate("MainWindow", u"Data", None))
    # retranslateUi

