import csv
import datetime

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from Listmaker_GUI import Ui_MainWindow
from notes_list import NotsList
from database import DataBase
import datetime as dt


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Exam Dates")
        self.exicon = QIcon()
        self.exicon.addFile("images/Examdater1.ico")
        self.setWindowIcon(self.exicon)
        self.window = ()
        self.ui = ()
        self.note_window = ()

        # Data_table_headers
        self.date_table.resizeColumnsToContents()

        # Messagebox
        self.teacherBox = ()
        self.themeBox = ()
        self.saveBox = ()

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
        self.note_li = ()
        self.actionNotenListe.triggered.connect(self.note_list)

        # Lists
        self.authors = []
        self.themes = []

        # Datetime
        self.actually_date = dt.date.today()
        self.dateEdit.setDate(self.actually_date)
        self.today = self.actually_date.today().strftime("%d.%m.%Y")

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

    def check_date(self, row_counter):

        item = self.date_table.item(row_counter, 1).text()
        date_today = dt.datetime.strptime(self.today, "%d.%m.%Y")
        exam_date = dt.datetime.strptime(item, "%d.%m.%Y")
        delta = exam_date - date_today

        if delta.days < 0:
            for n in DataBase().fetch_all():
                if exam_date.strftime('%d.%m.%Y') in n[3]:
                    DataBase().delete_database_entry(int(n[0]))

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

            a = QTableWidgetItem(str(n[3]))
            b = QTableWidgetItem(str(n[1]))
            c = QTableWidgetItem(str(n[2]))
            d = QTableWidgetItem(str(row_label_counter))

            self.date_table.setItem(row_counter, column_counter, d)
            d.setTextAlignment(Qt.AlignCenter)
            d.setFlags(d.flags() & ~ Qt.ItemIsEditable)
            column_counter += 1

            self.date_table.setItem(row_counter, column_counter, a)
            a.setTextAlignment(Qt.AlignCenter)
            a.setFlags(a.flags() & ~ Qt.ItemIsEditable)
            column_counter += 1

            self.date_table.setItem(row_counter, column_counter, b)
            b.setTextAlignment(Qt.AlignCenter)
            b.setFlags(b.flags() & ~ Qt.ItemIsEditable)
            column_counter += 1

            self.date_table.setItem(row_counter, column_counter, c)
            c.setTextAlignment(Qt.AlignCenter)
            c.setFlags(c.flags() & ~ Qt.ItemIsEditable)

            self.font_color(column_counter, row_counter)
            self.check_date(row_counter)

            row_counter += 1
            row_label_counter += 1

    def font_color(self, column_counter, row_counter):

        item = self.date_table.item(row_counter, 1).text()
        date_today = dt.datetime.strptime(self.today, "%d.%m.%Y")
        exam_date = dt.datetime.strptime(item, "%d.%m.%Y")
        delta = exam_date - date_today

        if 3 < delta.days <= 5:
            for n in range(column_counter + 1):
                self.date_table.item(row_counter, n).setBackground(QBrush("#ff8633"))
        elif delta.days <= 3:
            for n in range(column_counter + 1):
                self.date_table.item(row_counter, n).setBackground(QBrush("#ff3333"))

    def saving(self):

        self.teacherBox = QMessageBox()
        self.themeBox = QMessageBox()
        self.saveBox = QMessageBox()

        if self.lehrer_label.text() == "":
            self.teacherBox = QMessageBox.warning(self, "Keine/n Pruefer/in gewaehlt!",
                                                "Sorry,sie koennen nicht speichern wenn sie keine/n Pruefer/in"
                                                " ausgewaehlt haben\nBitte fuellen sie alle Felder aus.",
                                                QMessageBox.StandardButton(QMessageBox.StandardButton.Ok),
                                                QMessageBox.StandardButton(QMessageBox.StandardButton.Ok))

        elif self.themen_label.text() == "":
            self.themeBox = QMessageBox.warning(self, "Kein Thema gewaehlt!",
                                                "Sorry, sie koennen nicht speichern wenn sie kein Thema ausgewaehlt"
                                                " haben.\nBitte fuellen sie alle Felder aus.",
                                                QMessageBox.StandardButton(QMessageBox.StandardButton.Ok),
                                                QMessageBox.StandardButton(QMessageBox.StandardButton.Ok))
        else:
            a = QTableWidgetItem(self.dateEdit.text())
            a.setTextAlignment(Qt.AlignCenter)
            a.setFlags(a.flags() & ~ Qt.ItemIsEditable)

            b = QTableWidgetItem(self.lehrer_label.text())
            b.setTextAlignment(Qt.AlignCenter)
            b.setFlags(b.flags() & ~ Qt.ItemIsEditable)

            c = QTableWidgetItem(self.themen_label.text())
            c.setTextAlignment(Qt.AlignCenter)
            c.setFlags(c.flags() & ~ Qt.ItemIsEditable)

            date_today = dt.datetime.strptime(self.today, "%d.%m.%Y")
            exam_date = dt.datetime.strptime(a.text(), "%d.%m.%Y")

            if exam_date > date_today or exam_date == date_today:
                DataBase().make_database_entry(e_auditor=self.lehrer_label.text(), e_theme=self.themen_label.text(),
                                               e_date=self.dateEdit.text())
                self.make_list()
                self.del_menu()
                self.del_all_entry()
            else:
                self.themeBox = QMessageBox.warning(self, "Falsches Datum!",
                                                    "Sorry, dies ist keine Zeitmaschine.\n"
                                                    "Bitte geben sie das heutige oder ein zukuenftiges Datum ein",
                                                    QMessageBox.StandardButton(QMessageBox.StandardButton.Ok),
                                                    QMessageBox.StandardButton(QMessageBox.StandardButton.Ok))

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

    def note_list(self):

        self.note_window = NotsList().topLevelWidget()
        self.note_window.show()

    def closeEvent(self, event):

        for n in QApplication.topLevelWidgets():
            n.close()


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()

    app.exec()

