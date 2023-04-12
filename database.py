# @Daniel Zenglein - "FIAE-202207"
import sqlite3


class DataBase:

    def __init__(self):

        self.all = ()

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

    def fetch_all_nots(self):

        self.db = sqlite3.connect("dates-list.db")
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute("SELECT * FROM NotsList")
        except sqlite3.OperationalError:
            self.create_nots_list()
        return self.cursor.fetchall()

    def create_database(self):

        self.cursor.execute("CREATE TABLE IF NOT EXISTS DateList (id INTEGER PRIMARY KEY AUTOINCREMENT,"
                            "author varchar NOT NULL, theme varchar NOT NULL, date varchar NOT NULL)")

    def create_nots_list(self):

        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS NotsList (id INTEGER PRIMARY KEY AUTOINCREMENT, nots varchar)")

        self.cursor.execute("SELECT * FROM NotsList")

    def make_database_entry(self, e_auditor, e_theme, e_date):

        try:
            self.cursor.execute("SELECT id FROM DateList")
        except sqlite3.OperationalError:
            self.create_database()

        act_id = len(self.cursor.fetchall())

        if act_id < 8:

            self.cursor.execute("SELECT * FROM DateList")
            self.cursor.execute(f"INSERT INTO DateList (author, theme, date) VALUES('{e_auditor}',"
                                f"'{e_theme}','{e_date}')")
            self.db.commit()
        else:
            pass

    def entry_nots(self, nots):

        try:
            self.cursor.execute("SELECT id FROM NotsList")
        except sqlite3.OperationalError:
            self.create_nots_list()

        self.cursor.execute("SELECT * FROM NotsList")
        self.cursor.execute(f"INSERT INTO NotsList (nots) VALUES('{nots}',")
        self.db.commit()

    def delete_database_entry(self, num):

        for n in (self.fetch_all()):

            if n[0] == num:

                self.cursor.execute("SELECT * FROM DateList")
                self.cursor.execute(f"DELETE from DateList where rowid={n[0]}")
                self.db.commit()
