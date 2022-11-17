# @Daniel Zenglein - "Fiae202207"
import sqlite3
import tkinter as tk


class DataBase:

    def __init__(self):

        self.db = sqlite3.connect("dates-list.db")
        self.cursor = self.db.cursor()

    def fetch_all(self):

        self.db = sqlite3.connect("dates-list.db")
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute("SELECT * FROM DateList")
        except sqlite3.OperationalError:
            self.create_database()
        return self.cursor.fetchall()

    def create_database(self):

        self.cursor.execute("CREATE TABLE IF NOT EXISTS DateList (id INTEGER PRIMARY KEY, author varchar(9) NOT NULL,"
                            " theme varchar(12) NOT NULL, date varchar(9) NOT NULL)")

    def make_database_entry(self, e_auditor, e_theme, e_date):

        try:
            self.cursor.execute("SELECT id FROM DateList")
        except sqlite3.OperationalError:
            self.create_database()

        act_id = len(self.cursor.fetchall())

        if act_id < 8:

            self.cursor.execute("SELECT * FROM DateList")
            this_id = len(self.fetch_all())
            this_id += 1

            this_id_list = []

            for n in self.fetch_all():
                this_id_list.append(int(n[0]))

            if 1 not in this_id_list:
                this_id = 1
            else:
                if 2 not in this_id_list:
                    this_id = 2
                else:
                    if 3 not in this_id_list:
                        this_id = 3
                    else:
                        if 4 not in this_id_list:
                            this_id = 4
                        else:
                            if 5 not in this_id_list:
                                this_id = 5
                            else:
                                if 6 not in this_id_list:
                                    this_id = 6
                                else:
                                    if 7 not in this_id_list:
                                        this_id = 7
                                    else:
                                        if 8 not in this_id_list:
                                            this_id = 8

            self.cursor.execute(f"INSERT INTO DateList VALUES('{this_id}', '{e_auditor[:8]}',"
                                f"'{e_theme[:15]}','{e_date[:8]}')")
            self.db.commit()
        else:
            pass

    def delete_database_entry(self, num):

        if num != []:
            self.cursor.execute("SELECT * FROM DateList")
            self.cursor.execute(f"DELETE from DateList where id={num}")
            self.db.commit()
        else:
            pass

# New Author-Table

    def create_author_table(self):

        self.cursor.execute("CREATE TABLE IF NOT EXISTS AuthorList (id INTEGER PRIMARY KEY AUTOINCREMENT, author varchar(9) NOT NULL)")

    def author_new_entry(self):

        try:
            self.cursor.execute("SELECT id FROM AuthorList")
        except sqlite3.OperationalError:

            try:
                self.create_author_table()
            except sqlite3.OperationalError:
                self.create_database()

        authors = ["Eber", "Stegmann", "Helmecke", "Lange", "Laufer", "Grüger", "Bieber", "Strelnikova", "Dachwald",
                   "Rosenbusch", "Großhauser", "Ringer", "Jevtic", "Korn"]

        self.cursor.execute("SELECT author FROM AuthorList")
        all_authors = self.cursor.fetchall()

        if len(all_authors) >= 14:
            pass
        else:
            for name in authors:

                self.cursor.execute(f"INSERT INTO AuthorList ('author') VALUES('{name}')")
                self.db.commit()

    def check_all_authors(self):

        try:
            self.cursor.execute("SELECT author FROM AuthorList")
        except sqlite3.OperationalError:
            self.create_author_table()
            self.author_new_entry()

        all_authors = self.cursor.fetchall()

        return all_authors
