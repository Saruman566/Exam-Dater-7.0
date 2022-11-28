# @Daniel Zenglein - "FIAE-202207"
import csv
import tkcalendar
import tkinter as tk
from tkinter import messagebox
from database import DataBase
import datetime

CANVAS_LIST_A = []
CANVAS_LIST_B = []
CANVAS_LIST_C = []
HIGH_COUNTER = 209
BUTTON_LIST = []


class ListMaker:
    
    def __init__(self):

        # Main-Window

        window_x = 500
        window_y = 200

        self.window = tk.Tk()
        self.window.title("Exam-Dater")
        self.window.geometry(f"700x700+{window_x}+{window_y}")
        self.window.iconbitmap(r'Examdater1.ico')
        self.window.resizable(False, False)

        self.calendar_window = tk.Canvas()

        # Images

        self.icon = tk.PhotoImage(file="trashcan.png")
        self.icon2 = tk.PhotoImage(file="save.png")
        self.icon3 = tk.PhotoImage(file="back.png")

        # Labels and Entry's

        self.background = tk.Canvas(width=700, height=700,  background="#FAEBD7")
        self.background.grid(row=0, column=0, sticky="n,w")

        self.main_label = tk.Label(text="EXAM - DATER", font="Georgia 30 bold", fg="#8B8378", bg="#FAEBD7")
        self.main_label.grid(row=0, column=0, pady=0, padx=208, sticky="n,w")

        self.first_label = tk.Label(text="Auditor", background="#FAEBD7", font="Georgia 20")
        self.first_label.grid(row=0, column=0, pady=55, padx=20, sticky="n,w")

        self.e_auditor = tk.StringVar()

        self.ent_auditor = tk.Entry(width=22, background="#FAEBD7", font="Georgia 20", fg="#CD853F", state="disabled",
                                    textvariable=self.e_auditor, justify="center")
        self.ent_auditor.grid(row=0, column=0, pady=55, padx=136, sticky="n,w")

        self.second_label = tk.Label(text="Theme", background="#FAEBD7", font="Georgia 20")
        self.second_label.grid(row=0, column=0, pady=100, padx=25, sticky="n,w")

        self.e_theme = tk.StringVar()

        self.ent_theme = tk.Entry(width=22, background="#FAEBD7", font="Georgia 20", fg="#CD853F", state="disabled",
                                  textvariable=self.e_theme, justify="center")
        self.ent_theme.grid(row=0, column=0, pady=100, padx=136, sticky="n,w")

        self.date_label = tk.Label(text="Date", background="#FAEBD7", font="Georgia 20")
        self.date_label.grid(row=0, column=0, pady=145, padx=40, sticky="n,w")

        self.e_date = tk.StringVar()

        self.ent_date = tk.Entry(width=20, background="#FAEBD7", font="Helvetica 18", fg="#CD853F", state="disabled",
                                 textvariable=self.e_date, justify="center")
        self.ent_date.grid(row=0, column=0, pady=145, padx=136, ipadx=1, ipady=2, sticky="n,w")

        self.e_delete = tk.StringVar()

        # Canvas
        global CANVAS_LIST_A
        global CANVAS_LIST_B
        global CANVAS_LIST_C

        for n in range(8):
            a = self.list_canvas_n = tk.Label()
            b = self.list_canvas_na = tk.Label()
            c = self.list_canvas_nb = tk.Label()
            CANVAS_LIST_A.append(a)
            CANVAS_LIST_B.append(b)
            CANVAS_LIST_C.append(c)
            n += 1

        # Buttons

        self.drop_down_bu = tk.Button(width=10, height=2, text="Auditors", font="Georgia 8 bold", fg="#A52A2A",
                                      command=self.drop_down)
        self.drop_down_bu.grid(row=0, column=0, pady=52, padx=548, sticky="n,w")

        self.remove_button_1 = tk.Button(image=self.icon3, width=34, height=34, font="Georgia 8 bold", fg="#A52A2A",
                                         command=self.clear_var_1)
        self.remove_button_1.grid(row=0, column=0, pady=52, padx=648, sticky="n,w")

        self.drop_down_1 = tk.Button(width=10, height=2, text="Themes", font="Georgia 8 bold", fg="#A52A2A",
                                     command=self.drop_down_themes)
        self.drop_down_1.grid(row=0, column=0, pady=98, padx=548, sticky="n,w")

        self.remove_button_2 = tk.Button(image=self.icon3, width=34, height=34, font="Georgia 8 bold", fg="#A52A2A",
                                         command=self.clear_var_2)
        self.remove_button_2.grid(row=0, column=0, pady=98, padx=648, sticky="n,w")

        self.drop_down_2 = tk.Button(width=10, height=2, text="Date", font="Georgia 8 bold", fg="#A52A2A",
                                     command=self.calendar)
        self.drop_down_2.grid(row=0, column=0, pady=144, padx=548, sticky="n,w")

        self.remove_button_3 = tk.Button(image=self.icon3, width=34, height=34, font="Georgia 8 bold", fg="#A52A2A",
                                         command=self.clear_var_3)
        self.remove_button_3.grid(row=0, column=0, pady=144, padx=648, sticky="n,w")

        self.save_button = tk.Button(image=self.icon2, width=34, height=34, font="Georgia 8 bold", fg="#A52A2A",
                                     command=self.save_date)
        self.save_button.grid(row=0, column=0, pady=144, padx=420, sticky="n,w")

        self.delete_button = tk.Button(image=self.icon, width=34, height=34,
                                       font="Georgia 8 bold", fg="#FF3030", command= self.get_id)
        self.delete_button.grid(row=0, column=0, pady=144, padx=473, sticky="n,w")

        self.calendar_button = ()

        self.dropdown_frame = ()
        self.dropdown_themes_frame = ()
        self.dropdown_drop_window = ()
        self.dropdown_themes_window = ()

        for n in range(1, 15):
            a = self.menu_button_n = ()
            BUTTON_LIST.append(a)

        self.canvas()

        self.calendar_frame = ()
        self.cal = tkcalendar.Calendar()
        self.calendar_window = ()

        self.delete_window = ()
        self.dropdown_delete = ()

    def canvas(self):

        global HIGH_COUNTER

        HIGH_COUNTER = 209
        for n in CANVAS_LIST_A:
            n.config(width=15, height=2, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold", borderwidth=2,
                     relief="groove", anchor="center", text="")
            n.grid(row=0, column=0, pady=HIGH_COUNTER, padx=17, sticky="n,w")
            HIGH_COUNTER += 60

        HIGH_COUNTER = 209
        for t in CANVAS_LIST_B:
            t.config(width=24, height=2, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold", borderwidth=2,
                     relief="groove", anchor="center", text="")
            t.grid(row=0, column=0, pady=HIGH_COUNTER, padx=224, sticky="n,w")
            HIGH_COUNTER += 60

        HIGH_COUNTER = 209
        for c in CANVAS_LIST_C:
            c.config(width=10, height=2, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold", borderwidth=2,
                     relief="groove", anchor="center", text="")
            c.grid(row=0, column=0, pady=HIGH_COUNTER, padx=548, sticky="n,w")
            HIGH_COUNTER += 60

        self.make_new_list()

    def save_date(self):

        if self.e_auditor.get() == "":
            tk.messagebox.showwarning(
                "No Auditor", "Sorry, can`t save without an Auditor\nPlease fill all three Entry`s")
            pass
        if self.e_theme.get() == "":
            tk.messagebox.showwarning("No Theme", "Sorry, can`t save without a Theme.\nPlease fill all three Entry`s")
            pass
        if self.e_date.get() == "":
            tk.messagebox.showwarning("No Date", "Sorry, can`t save without a Date.\nPlease fill all three Entry`s")
            pass
        if self.e_auditor.get() != "" and self.e_theme.get() != "" and self.e_date.get() != "":
            DataBase().make_database_entry(e_auditor=self.ent_auditor.get(), e_theme=self.ent_theme.get(),
                                           e_date=self.ent_date.get())
            self.make_new_list()

    def make_new_list(self):

        new_list = []
        counter = 0
        list_counter = 0
        counter_list = []
        list_number = 0

        for n in range(len(DataBase().fetch_all())):

            new_string = DataBase().fetch_all()[counter]

            new_list.append(new_string)
            counter_list.append(new_list[counter][0])

            CANVAS_LIST_A[list_counter].config(text=f"{list_number + 1} {new_list[counter][1]}")

            CANVAS_LIST_B[list_counter].config(text=f"{new_list[counter][2]}")

            CANVAS_LIST_C[list_counter].config(text=f"{new_list[counter][3]}")

            list_counter += 1
            counter += 1
            list_number += 1

            self.clear_var()
            self.window.update()

        return list_number

    def clear_var_1(self):

        self.ent_auditor.config(state="normal")
        self.ent_auditor.delete(0, "end")
        self.ent_auditor.config(state="disabled")

    def clear_var_2(self):

        self.ent_theme.config(state="normal")
        self.ent_theme.delete(0, "end")
        self.ent_theme.config(state="disabled")

    def clear_var_3(self):

        self.ent_date.config(state="normal")
        self.ent_date.delete(0, "end")
        self.ent_date.config(state="disabled")

    def clear_var(self):

        self.clear_var_1()
        self.clear_var_2()
        self.clear_var_3()

    def drop_down(self):

        global BUTTON_LIST
        authors = []

        x = self.window.winfo_children()
        if x[-1] == self.dropdown_themes_window or x[-1] == self.calendar_window or x[-1] == self.delete_window:
            x[-1].destroy()

        if x[-1] == self.dropdown_drop_window:
            pass
        else:
            x = self.window.winfo_x()
            y = self.window.winfo_y()

            self.dropdown_drop_window = tk.Toplevel(self.window)
            self.dropdown_drop_window.overrideredirect(True)
            self.dropdown_drop_window.geometry("+%d+%d" % (x + 346, y + 84))
            self.dropdown_drop_window.resizable(False, False)

            self.dropdown_frame = tk.Canvas(self.dropdown_drop_window)
            self.dropdown_frame.grid(row=0, column=0, sticky="n,w")

            with open("teacher.csv") as file:
                x = csv.reader(file)
                for teacher in x:
                    authors.append(str(teacher[0]))

            button_counter = 0

            for name in authors:

                BUTTON_LIST[button_counter] = tk.Button(self.dropdown_frame, width=20, height=1, bg="#A52A2A",
                                                        fg="#F4A460", font="Courier 12 bold",
                                                        activebackground="#A52A2A", activeforeground="#F4A460",
                                                        text=name, command=lambda t=name: self.menu_buttons(t))
                BUTTON_LIST[button_counter].grid(column=0, row=button_counter, sticky="n,w")
                button_counter += 1

    def menu_buttons(self, t):

        self.ent_auditor.config(state="normal")
        self.ent_auditor.delete(0, "end")
        self.ent_auditor.insert(0, t)
        self.ent_auditor.config(state="disabled")
        self.del_drop_menu()

    def drop_down_themes(self):

        global BUTTON_LIST

        x = self.window.winfo_children()
        if x[-1] == self.dropdown_drop_window or x[-1] == self.calendar_window or x[-1] == self.delete_window:
            x[-1].destroy()

        if x[-1] == self.dropdown_themes_window:
            pass
        else:
            x = self.window.winfo_x()
            y = self.window.winfo_y()

            self.dropdown_themes_window = tk.Toplevel(self.window)
            self.dropdown_themes_window.overrideredirect(True)
            self.dropdown_themes_window.geometry("+%d+%d" % (x + 316, y + 130))
            self.dropdown_themes_window.resizable(False, False)

            self.dropdown_themes_frame = tk.Canvas(self.dropdown_themes_window, width=200)
            self.dropdown_themes_frame.grid(row=0, column=0, sticky="n,w")

            themes = []

            with open("themeFields.csv") as file:
                x = csv.reader(file)
                for themeFields in x:
                    themes.append(str(themeFields[0]))

            button_counter = 0

            for theme in themes:

                BUTTON_LIST[button_counter] = tk.Button(self.dropdown_themes_frame, width=23, height=1, bg="#A52A2A",
                                                        fg="#F4A460", font="Courier 12 bold",
                                                        activebackground="#A52A2A", activeforeground="#F4A460",
                                                        text=theme, command=lambda t=theme: self.theme_menu_buttons(t))
                BUTTON_LIST[button_counter].grid(column=0, row=button_counter)
                button_counter += 1

    def theme_menu_buttons(self, t):

        self.ent_theme.config(state="normal")
        self.ent_theme.delete(0, "end")
        self.ent_theme.insert(0, t)
        self.ent_theme.config(state="disabled")
        self.del_drop_menu()

    def calendar(self):

        x = self.window.winfo_children()
        if x[-1] == self.dropdown_drop_window or x[-1] == self.dropdown_themes_window or x[-1] == self.delete_window:
            x[-1].destroy()

        if x[-1] == self.calendar_window:
            pass
        else:
            x = self.window.winfo_x()
            y = self.window.winfo_y()

            self.calendar_window = tk.Toplevel()
            self.calendar_window.overrideredirect(True)
            self.calendar_window.geometry("+%d+%d" % (x + 305, y + 176))
            self.calendar_window.resizable(False, False)

            self.cal = tkcalendar.Calendar(self.calendar_window, selectmode='day')
            self.cal.grid(row=0, column=0, sticky="n,w")

            self.calendar_button = tk.Button(self.calendar_window, width=14, height=1, text="Get Date",
                                             font="Georgia 19 bold", fg="#A52A2A", command=self.calendar_buttons)
            self.calendar_button.grid(row=1, column=0, padx=2, sticky="")
            self.window.update()

    def calendar_buttons(self):

        c = self.cal.selection_get()
        new_c = datetime.datetime.strftime(c, '%d.%m.%y')
        self.ent_date.config(state="normal")
        self.ent_date.delete(0, "end")
        self.ent_date.insert(0, new_c)
        self.ent_date.config(state="disabled")
        self.del_drop_menu()

    def del_drop_menu(self):

        x = self.window.winfo_children()
        x[-1].destroy()

    def get_id(self):

        ids = DataBase().fetch_all()
        global BUTTON_LIST

        if len(ids) == 0:
            pass
        else:
            x = self.window.winfo_children()
            if x[-1] == self.dropdown_drop_window or x[-1] == self.dropdown_themes_window or \
                    x[-1] == self.calendar_window:
                x[-1].destroy()

            if x[-1] == self.delete_window:
                pass
            else:
                x = self.window.winfo_x()
                y = self.window.winfo_y()

                self.delete_window = tk.Toplevel()
                self.delete_window.overrideredirect(True)
                self.delete_window.geometry("+%d+%d" % (x + 486, y + 216))
                self.delete_window.resizable(False, False)

                self.dropdown_delete = tk.Canvas(self.delete_window)
                self.dropdown_delete.grid(row=0, column=0, sticky="n,w")

                button_counter = 0

                x = self.make_new_list()

                for num in range(x):

                    BUTTON_LIST[button_counter] = tk.Button(self.dropdown_delete, width=2, height=1,
                                                            bg="#A52A2A", fg="#F4A460", font="Courier 12 bold",
                                                            activebackground="#A52A2A", activeforeground="#F4A460",
                                                            text=num + 1, command=lambda t=num:
                    [DataBase().delete_database_entry(t), self.canvas(), self.del_drop_menu()])
                    BUTTON_LIST[button_counter].grid(column=0, row=button_counter)
                    button_counter += 1
