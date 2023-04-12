# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nots2.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(450, 450)
        Form.setMinimumSize(QSize(450, 450))
        Form.setMaximumSize(QSize(450, 450))
        Form.setSizeIncrement(QSize(450, 450))
        Form.setBaseSize(QSize(450, 450))
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.show_frame = QFrame(Form)
        self.show_frame.setObjectName(u"show_frame")
        self.show_frame.setMinimumSize(QSize(450, 450))
        self.show_frame.setMaximumSize(QSize(450, 450))
        self.show_frame.setSizeIncrement(QSize(450, 450))
        self.show_frame.setBaseSize(QSize(450, 450))
        self.show_frame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.show_frame.setFrameShape(QFrame.NoFrame)
        self.show_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.show_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_container = QFrame(self.show_frame)
        self.menu_container.setObjectName(u"menu_container")
        self.menu_container.setMinimumSize(QSize(450, 450))
        self.menu_container.setMaximumSize(QSize(450, 450))
        self.menu_container.setSizeIncrement(QSize(450, 450))
        self.menu_container.setBaseSize(QSize(450, 450))
        self.menu_container.setFrameShape(QFrame.Panel)
        self.menu_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.menu_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_frame = QFrame(self.menu_container)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMinimumSize(QSize(435, 410))
        self.menu_frame.setMaximumSize(QSize(435, 410))
        self.menu_frame.setSizeIncrement(QSize(435, 410))
        self.menu_frame.setBaseSize(QSize(435, 410))
        self.menu_frame.setFrameShape(QFrame.NoFrame)
        self.menu_frame.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_3 = QVBoxLayout(self.menu_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.date_table = QTableWidget(self.menu_frame)
        if (self.date_table.columnCount() < 5):
            self.date_table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.date_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.date_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.date_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.date_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.date_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.date_table.setObjectName(u"date_table")
        self.date_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.date_table.setRowCount(0)
        self.date_table.setColumnCount(5)
        self.date_table.horizontalHeader().setMinimumSectionSize(50)
        self.date_table.horizontalHeader().setDefaultSectionSize(140)

        self.verticalLayout_3.addWidget(self.date_table)

        self.frame = QFrame(self.menu_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 5, 20, 5)
        self.btn_durchschnitt_berechnen = QPushButton(self.frame)
        self.btn_durchschnitt_berechnen.setObjectName(u"btn_durchschnitt_berechnen")
        self.btn_durchschnitt_berechnen.setMinimumSize(QSize(180, 0))
        self.btn_durchschnitt_berechnen.setMaximumSize(QSize(180, 16777215))
        self.btn_durchschnitt_berechnen.setSizeIncrement(QSize(180, 0))
        self.btn_durchschnitt_berechnen.setBaseSize(QSize(180, 0))

        self.horizontalLayout_2.addWidget(self.btn_durchschnitt_berechnen)

        self.lbl_durchschnitt_label = QLabel(self.frame)
        self.lbl_durchschnitt_label.setObjectName(u"lbl_durchschnitt_label")
        self.lbl_durchschnitt_label.setMinimumSize(QSize(30, 0))
        self.lbl_durchschnitt_label.setMaximumSize(QSize(30, 16777215))
        self.lbl_durchschnitt_label.setSizeIncrement(QSize(30, 0))
        self.lbl_durchschnitt_label.setBaseSize(QSize(30, 0))
        self.lbl_durchschnitt_label.setFrameShape(QFrame.Box)
        self.lbl_durchschnitt_label.setAlignment(Qt.AlignCenter)
        self.lbl_durchschnitt_label.setMargin(0)

        self.horizontalLayout_2.addWidget(self.lbl_durchschnitt_label)

        self.safe_csv = QPushButton(self.frame)
        self.safe_csv.setObjectName(u"safe_csv")

        self.horizontalLayout_2.addWidget(self.safe_csv)


        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout.addWidget(self.menu_frame)


        self.horizontalLayout.addWidget(self.menu_container)


        self.verticalLayout_2.addWidget(self.show_frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.date_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"               Themes               ", None));
        ___qtablewidgetitem1 = self.date_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"     Notes      ", None));
        ___qtablewidgetitem2 = self.date_table.horizontalHeaderItem(3)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"      Notes       ", None));
        self.btn_durchschnitt_berechnen.setText(QCoreApplication.translate("Form", u"Calculate grade point average", None))
        self.lbl_durchschnitt_label.setText("")
        self.safe_csv.setText(QCoreApplication.translate("Form", u"Save Notes as .xlx Data", None))
    # retranslateUi

