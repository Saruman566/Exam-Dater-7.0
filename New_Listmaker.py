import csv
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from Listmaker_GUI import Ui_MainWindow
from database import DataBase
import datetime as dt


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Datemaker")
        self.notelist = ()

        # Data_table_headers
        self.date_table.resizeColumnsToContents()

        # Messagebox
        self.teacherBox = ()
        self.themeBox = ()

        # Popup Menus
        self.teacher_menu = QMenu(self)
        self.themes_menu = QMenu(self)
        self.delete_menu = QMenu(self)

        # Buttons
        self.btn_teacher.setMenu(self.teacher_menu)
        self.btn_themen.setMenu(self.themes_menu)
        self.teacher_del_button.clicked.connect(self.lehrer_label.clear)
        self.themes_del_button.clicked.connect(self.themen_label.clear)
        self.del_button.setMenu(self.delete_menu)
        self.save_button.clicked.connect(self.saving)

        # Lists
        self.authors = []
        self.themes = []

        # Datetime
        self.actually_date = dt.date.today()
        self.dateEdit.setDate(self.actually_date)

        # CSV Files
        with open("lists/teacher.csv") as file:
            x = csv.reader(file)
            for teacher in x:
                self.authors.append(str(teacher[0]))

        with open("lists/themeFields.csv") as file:
            x = csv.reader(file)
            for themeFields in x:
                self.themes.append(str(themeFields[0]))

        [self.teacher_menu.addAction(name, self.get_name) for name in self.authors]
        [self.themes_menu.addAction(theme, self.get_theme) for theme in self.themes]

        self.del_menu()
        self.make_list()

    def get_name(self):
        x = self.sender().text()
        self.lehrer_label.setText(x)

    def get_theme(self):
        x = self.sender().text()
        self.themen_label.setText(x)

    def make_list(self):

        row_counter = 0
        row_label_counter = 1

        row_posit = self.date_table.rowCount()
        self.date_table.insertRow(row_posit)

        for n in DataBase().fetch_all():

            column_counter = 0

            a = QTableWidgetItem(n[3])
            b = QTableWidgetItem(n[1])
            c = QTableWidgetItem(n[2])
            d = QTableWidgetItem(str(row_label_counter))

            self.date_table.setItem(row_counter, column_counter, d)
            d.setTextAlignment(Qt.AlignCenter)
            d.setFlags(d.flags() & ~ Qt.ItemIsEditable)
            column_counter += 1

            self.date_table.setItem(row_counter, column_counter, a)
            a.setTextAlignment(Qt.AlignCenter)
            a.setFlags(a.flags() & ~ Qt.ItemIsEditable)
            self.font_color(a)
            column_counter += 1

            self.date_table.setItem(row_counter, column_counter, b)
            b.setTextAlignment(Qt.AlignCenter)
            b.setFlags(a.flags() & ~ Qt.ItemIsEditable)
            column_counter += 1

            self.date_table.setItem(row_counter, column_counter, c)
            c.setTextAlignment(Qt.AlignCenter)
            c.setFlags(a.flags() & ~ Qt.ItemIsEditable)

            row_counter += 1
            row_label_counter += 1

    def font_color(self, a):

        today = self.actually_date.today().strftime("%d")
        print(today)
        for n in DataBase().fetch_all():
            days = n[3][:2]
            if int(today) + 5 == int(days):
                print(n[3])
                print("5 days left")
                a.setForeground(QBrush("#FF0000"))

    def saving(self):

        self.teacherBox = QMessageBox()
        self.themeBox = QMessageBox()

        if self.lehrer_label.text() == "":
            self.teacherBox = QMessageBox.warning(self, "No Auditor",
                                                  "Sorry, can`t save without an Auditor\nPlease fill all three Entry`s",
                                                  QMessageBox.StandardButton(QMessageBox.StandardButton.Ok),
                                                  QMessageBox.StandardButton(QMessageBox.StandardButton.Ok))

        elif self.themen_label.text() == "":
            self.themeBox = QMessageBox.warning(self, "No Theme!",
                                                "Sorry, can`t save without a Theme.\nPlease fill all three Entry`s",
                                                QMessageBox.StandardButton(QMessageBox.StandardButton.Ok),
                                                QMessageBox.StandardButton(QMessageBox.StandardButton.Ok))
        else:
            a = QTableWidgetItem(self.dateEdit.text())
            a.setTextAlignment(Qt.AlignCenter)
            a.setFlags(a.flags() & ~ Qt.ItemIsEditable)

            b = QTableWidgetItem(self.lehrer_label.text())
            b.setTextAlignment(Qt.AlignCenter)
            b.setFlags(a.flags() & ~ Qt.ItemIsEditable)

            c = QTableWidgetItem(self.themen_label.text())
            c.setTextAlignment(Qt.AlignCenter)
            c.setFlags(a.flags() & ~ Qt.ItemIsEditable)

            DataBase().make_database_entry(e_auditor=self.lehrer_label.text(), e_theme=self.themen_label.text(),
                                           e_date=self.dateEdit.text())

            self.make_list()
            self.del_menu()
            self.del_all_entry()

    def del_all_entry(self):
        self.lehrer_label.clear()
        self.themen_label.clear()

    def del_menu(self):

        self.delete_menu.clear()

        counter = 1

        for num in DataBase().fetch_all():

            x = str(counter)
            self.delete_menu.addAction(x, self.get_id)
            counter += 1

    def get_id(self):
        x = self.sender().text()
        self.del_database(x)

    def del_database(self, x):

        x = int(x)
        x -= 1
        db_list = [num for num in DataBase().fetch_all()]
        del_id = int(db_list[x][0])
        DataBase().delete_database_entry(del_id)
        self.date_table.removeRow(x)
        self.del_menu()


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
