import csv
import xlsxwriter
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from nots2 import Ui_Form
from database import *


class NotsList(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Note list")
        self.exicon = QIcon()
        self.exicon.addFile("images/Examdater1.ico")
        self.setWindowIcon(self.exicon)

        # Data_table_headers
        self.date_table.resizeColumnsToContents()

        # Button
        self.btn_durchschnitt_berechnen.clicked.connect(self.avg_calculator)
        self.safe_csv.clicked.connect(self.make_note_csv)

        # Lists
        self.authors = []
        self.themes_note = []

        with open("lists/themeFields.csv") as file:
            x = csv.reader(file)
            for themeFields in x:
                self.themes_note.append(str(themeFields[0]))

        DataBase().create_nots_list()

        self.make_nots_list()

    def make_nots_list(self):

        row_counter = 0

        for themes in self.themes_note:
            row_posit = self.date_table.rowCount()
            self.date_table.insertRow(row_posit)

            a = QTableWidgetItem(str(themes))
            b = QTableWidgetItem(str(""))
            c = QTableWidgetItem(str("x2"))
            d = QTableWidgetItem(str(""))
            e = QTableWidgetItem(str("x2"))

            self.date_table.setItem(row_counter, 0, a)
            a.setTextAlignment(Qt.AlignCenter)
            a.setFlags(a.flags() & ~ Qt.ItemIsEditable)

            self.date_table.setItem(row_counter, 1, b)
            b.setTextAlignment(Qt.AlignCenter)

            c.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
            c.setCheckState(Qt.CheckState.Unchecked)

            self.date_table.setItem(row_counter, 2, c)

            self.date_table.setItem(row_counter, 3, d)
            d.setTextAlignment(Qt.AlignCenter)

            e.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
            e.setCheckState(Qt.CheckState.Unchecked)

            self.date_table.setItem(row_counter, 4, e)

            row_counter += 1

    def avg_calculator(self):

        row_counter = 0
        div_counter = 0
        list_of_items = []
        new_list = []

        # first column

        for n in range(len(self.themes_note)):

            new_item = self.date_table.item(row_counter, 1).text()
            checkbox = self.date_table.item(row_counter, 2).checkState()
            new_item_1 = self.date_table.item(row_counter, 3).text()
            checkbox_1 = self.date_table.item(row_counter, 4).checkState()

            row_counter += 1
            if new_item == "" or new_item_1 == "":
                pass
            if len(new_item) == 1 or len(new_item_1) == 1:
                new_item += "0"
                new_item_1 += "0"
            if checkbox == Qt.CheckState.Checked:
                new_item += "!"
            if checkbox_1 == Qt.CheckState.Checked:
                new_item_1 += "!"

            list_of_items.append(new_item.replace(",", ""))
            list_of_items.append(new_item_1.replace(",", ""))

            for t in list_of_items:
                if t == "":
                    list_of_items.remove(t)

        new_list_of_items = [nots if "." not in nots else nots.replace(".", "") for nots in list_of_items]

        if "" in new_list_of_items:
            new_list_of_items.remove("")

        for nobs in new_list_of_items:
            if "!" not in nobs:
                nobs = int(nobs)
                new_list.append(nobs)
            else:
                try:
                    nobs = int(nobs.replace("!", ""))
                except ValueError:
                    pass
                else:
                    new_list.append(nobs * 2)
                    div_counter += 1

        div_counter += len(new_list)

        try:
            result = (((sum(new_list)) / 10) / div_counter)
        except ZeroDivisionError:
            pass
        else:
            last_result = round(result, 2)
            self.lbl_durchschnitt_label.setText(str(last_result))

    def make_note_csv(self):

        row_counter = 0
        xl_counter = 2
        avg = self.lbl_durchschnitt_label.text()

        workbook = xlsxwriter.Workbook("lists/Themes_and_Notes.xlsx")
        worksheet = workbook.add_worksheet()
        cell_format = workbook.add_format()
        cell_format.set_bold()
        cell_format.set_align('center')
        cell_format = workbook.add_format({'bold': True, 'align': 'center'})

        for n in range(11):

            item = self.date_table.item(row_counter, 0).text()
            item2 = self.date_table.item(row_counter, 1).text()
            item3 = self.date_table.item(row_counter, 3).text()
            worksheet.write(f"A1", "Themes", cell_format)
            worksheet.write(f"B1", "Notes", cell_format)
            worksheet.write(f"C1", "Notes", cell_format)
            xl_counter += 1
            worksheet.write(f"A{xl_counter}", f"{item}", cell_format)
            worksheet.write(f"B{xl_counter}", f"{item2}", cell_format)
            worksheet.write(f"C{xl_counter}", f"{item3}", cell_format)
            row_counter += 1
            xl_counter += 1

        xl_counter += 1
        worksheet.write(f"A{xl_counter}", f"Grade point average:", cell_format)
        worksheet.write(f"B{xl_counter}", f"{avg}", cell_format)
        workbook.close()
