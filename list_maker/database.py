# @Daniel Zenglein - "Fiae202207"
import sqlite3


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

        self.cursor.execute("CREATE TABLE IF NOT EXISTS DateList (id INTEGER PRIMARY KEY AUTOINCREMENT,"
                            "author varchar NOT NULL, theme varchar NOT NULL, date varchar NOT NULL)")

    def create_author_table(self):

        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS AuthorList (id INTEGER PRIMARY KEY AUTOINCREMENT, author varchar NOT NULL)")

    def create_theme_table(self):

        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS ThemeList (id INTEGER PRIMARY KEY AUTOINCREMENT, theme varchar NOT NULL)")

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

    def delete_database_entry(self, num):

        x = num + 1
        counter = 0
        for n in (self.fetch_all()):
            counter += 1
            if counter == x:

                self.cursor.execute("SELECT * FROM DateList")
                self.cursor.execute(f"DELETE from DateList where rowid={n[0]}")
                self.db.commit()

# New Author-Table

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

                self.cursor.execute(f"INSERT INTO AuthorList ('author') VALUES ('{name}')")
                self.db.commit()

    def check_all_authors(self):

        try:
            self.cursor.execute("SELECT author FROM AuthorList")
        except sqlite3.OperationalError:

            self.create_author_table()
            self.author_new_entry()

        all_authors = [name[0] for name in self.cursor.fetchall()]

        return all_authors

    def theme_new_entry(self):

        try:
            self.cursor.execute("SELECT id FROM ThemeList")
        except sqlite3.OperationalError:

            try:
                self.create_theme_table()
            except sqlite3.OperationalError:
                self.create_database()

        themes = ["WISO", "IT-Systems", "IT-Security", "Programming", "NetworkTechnology",  "Databases",
                  "Cyberphysical-systems", "Networks and Services", "Data Analysis", "English"]

        self.cursor.execute("SELECT theme FROM ThemeList")
        all_themes = self.cursor.fetchall()

        if len(all_themes) >= 10:
            pass
        else:
            for them in themes:

                self.cursor.execute(f"INSERT INTO ThemeList ('theme') VALUES ('{them}')")
                self.db.commit()

    def check_all_themes(self):

        try:
            self.cursor.execute("SELECT theme FROM ThemeList")
        except sqlite3.OperationalError:
            self.create_theme_table()
            self.theme_new_entry()

        all_themes = [theme[0] for theme in self.cursor.fetchall()]

        return all_themes
