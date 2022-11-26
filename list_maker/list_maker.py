# @Daniel Zenglein - "Fiae202207"
import tkinter

import tkcalendar
import tkinter as tk
from tkinter import messagebox
from database import DataBase
import datetime

CANVAS_LIST = []
BUTTON_LIST = []
CALENDAR_COUNTER = 0
NUMBER_LIST = 0


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

        self.list_canvas_1 = tk.Label()
        self.list_canvas_1a = ()
        self.list_canvas_1b = ()
        self.list_canvas_2 = tk.Label()
        self.list_canvas_2a = ()
        self.list_canvas_2b = ()
        self.list_canvas_3 = tk.Label()
        self.list_canvas_3a = ()
        self.list_canvas_3b = ()
        self.list_canvas_4 = tk.Label()
        self.list_canvas_4a = ()
        self.list_canvas_4b = ()
        self.list_canvas_5 = tk.Label()
        self.list_canvas_5a = ()
        self.list_canvas_5b = ()
        self.list_canvas_6 = tk.Label()
        self.list_canvas_6a = ()
        self.list_canvas_6b = ()
        self.list_canvas_7 = tk.Label()
        self.list_canvas_7a = ()
        self.list_canvas_7b = ()
        self.list_canvas_8 = tk.Label()
        self.list_canvas_8a = ()
        self.list_canvas_8b = ()

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
                                       font="Georgia 8 bold", fg="#FF3030", command=self.get_id)
        self.delete_button.grid(row=0, column=0, pady=144, padx=473, sticky="n,w")

        self.calendar_button = ()

        self.dropdown_frame = ()
        self.dropdown_themes_frame = ()
        self.dropdown_themes_window = None
        self.dropdown_drop_window = None

        self.menu_button_1 = ()
        self.menu_button_2 = ()
        self.menu_button_3 = ()
        self.menu_button_4 = ()
        self.menu_button_5 = ()
        self.menu_button_6 = ()
        self.menu_button_7 = ()
        self.menu_button_8 = ()
        self.menu_button_9 = ()
        self.menu_button_10 = ()
        self.menu_button_11 = ()
        self.menu_button_12 = ()
        self.menu_button_13 = ()
        self.menu_button_14 = ()

        self.canvas()

        self.calendar_frame = ()
        self.cal = tkcalendar.Calendar()
        self.calendar_window = None

        self.dropdown_delete = ()

    def canvas(self):

        self.list_canvas_1 = tk.Label(width=15, height=2, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold",
                                      borderwidth=2, relief="groove", anchor="center")
        self.list_canvas_1.grid(row=0, column=0, pady=209, padx=17, sticky="n,w")

        self.list_canvas_1a = tk.Label(width=24, height=2, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold",
                                       borderwidth=2, relief="groove", anchor="center")
        self.list_canvas_1a.grid(row=0, column=0, pady=209, padx=224, sticky="n,w")

        self.list_canvas_1b = tk.Label(width=10, height=2, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold",
                                       borderwidth=2, relief="groove", anchor="center")
        self.list_canvas_1b.grid(row=0, column=0, pady=209, padx=548, sticky="n,w")

        self.list_canvas_2 = tk.Label(width=15, height=2, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold",
                                      borderwidth=2, relief="groove", anchor="center")
        self.list_canvas_2.grid(row=0, column=0, pady=269, padx=17, sticky="n,w")

        self.list_canvas_2a = tk.Label(width=24, height=2, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold",
                                       borderwidth=2, relief="groove", anchor="center")
        self.list_canvas_2a.grid(row=0, column=0, pady=269, padx=224, sticky="n,w")

        self.list_canvas_2b = tk.Label(width=10, height=2, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold",
                                       borderwidth=2, relief="groove", anchor="center")
        self.list_canvas_2b.grid(row=0, column=0, pady=269, padx=548, sticky="n,w")

        self.list_canvas_3 = tk.Label(width=15, height=2, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold",
                                      borderwidth=2, relief="groove", anchor="center")
        self.list_canvas_3.grid(row=0, column=0, pady=329, padx=17, sticky="n,w")

        self.list_canvas_3a = tk.Label(width=24, height=2, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold",
                                       borderwidth=2, relief="groove", anchor="center")
        self.list_canvas_3a.grid(row=0, column=0, pady=329, padx=224, sticky="n,w")

        self.list_canvas_3b = tk.Label(width=10, height=2, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold",
                                       borderwidth=2, relief="groove", anchor="center")
        self.list_canvas_3b.grid(row=0, column=0, pady=329, padx=548, sticky="n,w")

        self.list_canvas_4 = tk.Label(width=15, height=2, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold",
                                      borderwidth=2, relief="groove", anchor="center")
        self.list_canvas_4.grid(row=0, column=0, pady=389, padx=17, sticky="n,w")

        self.list_canvas_4a = tk.Label(width=24, height=2, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold",
                                       borderwidth=2, relief="groove", anchor="center")
        self.list_canvas_4a.grid(row=0, column=0, pady=389, padx=224, sticky="n,w")

        self.list_canvas_4b = tk.Label(width=10, height=2, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold",
                                       borderwidth=2, relief="groove", anchor="center")
        self.list_canvas_4b.grid(row=0, column=0, pady=389, padx=548, sticky="n,w")

        self.list_canvas_5 = tk.Label(width=15, height=2, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold",
                                      borderwidth=2, relief="groove", anchor="center")
        self.list_canvas_5.grid(row=0, column=0, pady=449, padx=17, sticky="n,w")

        self.list_canvas_5a = tk.Label(width=24, height=2, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold",
                                       borderwidth=2, relief="groove", anchor="center")
        self.list_canvas_5a.grid(row=0, column=0, pady=449, padx=224, sticky="n,w")

        self.list_canvas_5b = tk.Label(width=10, height=2, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold",
                                       borderwidth=2, relief="groove", anchor="center")
        self.list_canvas_5b.grid(row=0, column=0, pady=449, padx=548, sticky="n,w")

        self.list_canvas_6 = tk.Label(width=15, height=2, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold",
                                      borderwidth=2, relief="groove", anchor="center")
        self.list_canvas_6.grid(row=0, column=0, pady=509, padx=17, sticky="n,w")

        self.list_canvas_6a = tk.Label(width=24, height=2, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold",
                                       borderwidth=2, relief="groove", anchor="center")
        self.list_canvas_6a.grid(row=0, column=0, pady=509, padx=224, sticky="n,w")

        self.list_canvas_6b = tk.Label(width=10, height=2, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold",
                                       borderwidth=2, relief="groove", anchor="center")
        self.list_canvas_6b.grid(row=0, column=0, pady=509, padx=548, sticky="n,w")

        self.list_canvas_7 = tk.Label(width=15, height=2, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold",
                                      borderwidth=2, relief="groove", anchor="center")
        self.list_canvas_7.grid(row=0, column=0, pady=569, padx=17, sticky="n,w")

        self.list_canvas_7a = tk.Label(width=24, height=2, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold",
                                       borderwidth=2, relief="groove", anchor="center")
        self.list_canvas_7a.grid(row=0, column=0, pady=569, padx=224, sticky="n,w")

        self.list_canvas_7b = tk.Label(width=10, height=2, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold",
                                       borderwidth=2, relief="groove", anchor="center")
        self.list_canvas_7b.grid(row=0, column=0, pady=569, padx=548, sticky="n,w")

        self.list_canvas_8 = tk.Label(width=15, height=2, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold",
                                      borderwidth=2, relief="groove", anchor="center")
        self.list_canvas_8.grid(row=0, column=0, pady=629, padx=17, sticky="n,w")

        self.list_canvas_8a = tk.Label(width=24, height=2, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold",
                                       borderwidth=2, relief="groove", anchor="center")
        self.list_canvas_8a.grid(row=0, column=0, pady=629, padx=224, sticky="n,w")

        self.list_canvas_8b = tk.Label(width=10, height=2, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold",
                                       borderwidth=2, relief="groove", anchor="center")
        self.list_canvas_8b.grid(row=0, column=0, pady=629, padx=548, sticky="n,w")

        global CANVAS_LIST
        CANVAS_LIST = [self.list_canvas_1, self.list_canvas_1a, self.list_canvas_1b, self.list_canvas_2,
                       self.list_canvas_2a, self.list_canvas_2b, self.list_canvas_3, self.list_canvas_3a,
                       self.list_canvas_3b, self.list_canvas_4, self.list_canvas_4a, self.list_canvas_4b,
                       self.list_canvas_5, self.list_canvas_5a, self.list_canvas_5b, self.list_canvas_6,
                       self.list_canvas_6a, self.list_canvas_6b, self.list_canvas_7, self.list_canvas_7a,
                       self.list_canvas_7b, self.list_canvas_8, self.list_canvas_8a, self.list_canvas_8b]

        DataBase().author_new_entry()
        DataBase().theme_new_entry()
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

            CANVAS_LIST[list_counter].config(text=f"{list_number + 1} {new_list[counter][1]}")

            list_counter += 1

            CANVAS_LIST[list_counter].config(text=f"{new_list[counter][2]}")

            list_counter += 1

            CANVAS_LIST[list_counter].config(text=f"{new_list[counter][3]}")

            list_counter += 1
            counter += 1
            list_number += 1

            self.clear_var()
            self.window.update()

        return list_number

    def update(self):

        self.canvas()

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

        self.ent_auditor.config(state="normal")
        self.ent_auditor.delete(0, "end")
        self.ent_auditor.config(state="disabled")
        self.ent_theme.config(state="normal")
        self.ent_theme.delete(0, "end")
        self.ent_theme.config(state="disabled")
        self.ent_date.config(state="normal")
        self.ent_date.delete(0, "end")
        self.ent_date.config(state="disabled")

    def drop_down(self):

        global BUTTON_LIST

        self.dropdown_drop_window = tk.Toplevel()
        self.dropdown_drop_window.overrideredirect(True)
        self.dropdown_drop_window.geometry("210x448+846+284")
        self.dropdown_drop_window.resizable(False, False)

        #print(self.dropdown_drop_window.winfo_x())

        #self.window.bind("<Configure>", self.get_with())

        self.dropdown_frame = tk.Canvas(self.dropdown_drop_window, width=200)
        self.dropdown_frame.grid(row=0, column=0, sticky="n,w")

        self.menu_button_1 = tk.Button(self.dropdown_frame, width=20, height=1, bg="#A52A2A", fg="#F4A460",
                                       font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_2 = tk.Button(self.dropdown_frame, width=20, height=1, bg="#A52A2A", fg="#F4A460",
                                       font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_3 = tk.Button(self.dropdown_frame, width=20, height=1, bg="#A52A2A", fg="#F4A460",
                                       font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_4 = tk.Button(self.dropdown_frame, width=20, height=1, bg="#A52A2A", fg="#F4A460",
                                       font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_5 = tk.Button(self.dropdown_frame, width=20, height=1, bg="#A52A2A", fg="#F4A460",
                                       font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_6 = tk.Button(self.dropdown_frame, width=20, height=1, bg="#A52A2A", fg="#F4A460",
                                       font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_7 = tk.Button(self.dropdown_frame, width=20, height=1, bg="#A52A2A", fg="#F4A460",
                                       font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_8 = tk.Button(self.dropdown_frame, width=20, height=1, bg="#A52A2A", fg="#F4A460",
                                       font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_9 = tk.Button(self.dropdown_frame, width=20, height=1, bg="#A52A2A", fg="#F4A460",
                                       font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_10 = tk.Button(self.dropdown_frame, width=20, height=1, bg="#A52A2A", fg="#F4A460",
                                        font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_11 = tk.Button(self.dropdown_frame, width=20, height=1, bg="#A52A2A", fg="#F4A460",
                                        font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_12 = tk.Button(self.dropdown_frame, width=20, height=1, bg="#A52A2A", fg="#F4A460",
                                        font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_13 = tk.Button(self.dropdown_frame, width=20, height=1, bg="#A52A2A", fg="#F4A460",
                                        font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_14 = tk.Button(self.dropdown_frame, width=20, height=1, bg="#A52A2A", fg="#F4A460",
                                        font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")

        BUTTON_LIST = [self.menu_button_1, self.menu_button_2, self.menu_button_3, self.menu_button_4,
                       self.menu_button_5, self.menu_button_6, self.menu_button_7, self.menu_button_8,
                       self.menu_button_9, self.menu_button_10, self.menu_button_11, self.menu_button_12,
                       self.menu_button_13, self.menu_button_14]

        authors = DataBase().check_all_authors()

        button_counter = 0

        for name in authors:

            BUTTON_LIST[button_counter].configure(text=name, command=lambda t=name: self.menu_buttons(t))
            BUTTON_LIST[button_counter].grid(column=0, row=button_counter)
            button_counter += 1

    def get_with(self, event=None):

        x = self.window.winfo_x() + 346
        y = self.window.winfo_y() + 84
        self.dropdown_drop_window.geometry("+%d+%d" % (x, y))

    def menu_buttons(self, t):

        self.ent_auditor.config(state="normal")
        self.ent_auditor.delete(0, "end")
        self.ent_auditor.insert(0, t)
        self.ent_auditor.config(state="disabled")
        x = self.window.winfo_children()
        x[-1].destroy()
        self.window.update()

    def drop_down_themes(self):

        global BUTTON_LIST

        self.dropdown_themes_window = tk.Toplevel()
        self.dropdown_themes_window.overrideredirect(True)
        self.dropdown_themes_window.geometry("240x320+816+330")
        self.dropdown_themes_window.resizable(False, False)

        self.dropdown_themes_frame = tk.Canvas(self.dropdown_themes_window, width=200)
        self.dropdown_themes_frame.grid(row=0, column=0, sticky="n,w")

        self.menu_button_1 = tk.Button(self.dropdown_themes_frame, width=23, height=1, bg="#A52A2A", fg="#F4A460",
                                       font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_2 = tk.Button(self.dropdown_themes_frame, width=23, height=1, bg="#A52A2A", fg="#F4A460",
                                       font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_3 = tk.Button(self.dropdown_themes_frame, width=23, height=1, bg="#A52A2A", fg="#F4A460",
                                       font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_4 = tk.Button(self.dropdown_themes_frame, width=23, height=1, bg="#A52A2A", fg="#F4A460",
                                       font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_5 = tk.Button(self.dropdown_themes_frame, width=23, height=1, bg="#A52A2A", fg="#F4A460",
                                       font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_6 = tk.Button(self.dropdown_themes_frame, width=23, height=1, bg="#A52A2A", fg="#F4A460",
                                       font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_7 = tk.Button(self.dropdown_themes_frame, width=23, height=1, bg="#A52A2A", fg="#F4A460",
                                       font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_8 = tk.Button(self.dropdown_themes_frame, width=23, height=1, bg="#A52A2A", fg="#F4A460",
                                       font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_9 = tk.Button(self.dropdown_themes_frame, width=23, height=1, bg="#A52A2A", fg="#F4A460",
                                       font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_10 = tk.Button(self.dropdown_themes_frame, width=23, height=1, bg="#A52A2A", fg="#F4A460",
                                        font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_11 = tk.Button(self.dropdown_themes_frame, width=23, height=1, bg="#A52A2A", fg="#F4A460",
                                        font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_12 = tk.Button(self.dropdown_themes_frame, width=23, height=1, bg="#A52A2A", fg="#F4A460",
                                        font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_13 = tk.Button(self.dropdown_themes_frame, width=23, height=1, bg="#A52A2A", fg="#F4A460",
                                        font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_14 = tk.Button(self.dropdown_themes_frame, width=23, height=1, bg="#A52A2A", fg="#F4A460",
                                        font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")

        BUTTON_LIST = [self.menu_button_1, self.menu_button_2, self.menu_button_3, self.menu_button_4,
                       self.menu_button_5, self.menu_button_6, self.menu_button_7, self.menu_button_8,
                       self.menu_button_9, self.menu_button_10, self.menu_button_11, self.menu_button_12,
                       self.menu_button_13, self.menu_button_14]

        themes = DataBase().check_all_themes()

        button_counter = 0

        for theme in themes:

            BUTTON_LIST[button_counter].configure(text=theme, command=lambda t=theme: self.theme_menu_buttons(t))
            BUTTON_LIST[button_counter].grid(column=0, row=button_counter)

            button_counter += 1

    def theme_menu_buttons(self, t):

        self.ent_theme.config(state="normal")
        self.ent_theme.delete(0, "end")
        self.ent_theme.insert(0, t)
        self.ent_theme.config(state="disabled")
        x = self.window.winfo_children()
        x[-1].destroy()
        self.window.update()

    def dis_ev(self):
        pass

    def calendar(self):

        #print(self.dropdown_drop_window.winfo_exists())
        #if tk.Toplevel in self.window.winfo_exists():
            #print(tk.Toplevel)

        self.calendar_window = tk.Toplevel()
        self.calendar_window.overrideredirect(True)
        self.calendar_window.geometry("250x240+805+376")
        self.window.bind("<Configure>", self.calendar_window)
        self.calendar_window.resizable(False, False)

        self.cal = tkcalendar.Calendar(self.calendar_window, selectmode='day')
        self.cal.grid(row=0, column=0, sticky="n,w")

        self.calendar_button = tk.Button(self.calendar_window, width=14, height=1, text="Get Date",
                                         font="Georgia 19 bold", fg="#A52A2A",
                                         command=self.calendar_buttons)
        self.calendar_button.grid(row=1, column=0, padx=2, sticky="")

        print(self.window.winfo_children())

    def calendar_buttons(self):

        if self.calendar_window is not None:
            self.calendar_window.destroy()
            self.calendar_window.update()
            self.calendar_window = None
        c = self.cal.selection_get()
        new_c = datetime.datetime.strftime(c, '%d.%m.%y')
        self.ent_date.config(state="normal")
        self.ent_date.delete(0, "end")
        self.ent_date.insert(0, new_c)
        self.ent_date.config(state="disabled")

    def del_drop_menu(self):

        x = self.window.winfo_children()
        x[-1].destroy()
        self.window.update()
        self.update()

    def get_id(self):

        ids = DataBase().fetch_all()

        if len(ids) == 0:
            pass
        else:

            self.dropdown_delete = tk.Canvas(width=200)
            self.dropdown_delete.grid(row=0, column=0, pady=185, padx=478, sticky="n,w")

            self.menu_button_1 = tk.Button(self.dropdown_delete, width=2, height=1, bg="#A52A2A", fg="#F4A460", text="1",
                                           font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
            self.menu_button_2 = tk.Button(self.dropdown_delete, width=2, height=1, bg="#A52A2A", fg="#F4A460", text="2",
                                           font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
            self.menu_button_3 = tk.Button(self.dropdown_delete, width=2, height=1, bg="#A52A2A", fg="#F4A460", text="3",
                                           font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
            self.menu_button_4 = tk.Button(self.dropdown_delete, width=2, height=1, bg="#A52A2A", fg="#F4A460", text="4",
                                           font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
            self.menu_button_5 = tk.Button(self.dropdown_delete, width=2, height=1, bg="#A52A2A", fg="#F4A460", text="5",
                                           font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
            self.menu_button_6 = tk.Button(self.dropdown_delete, width=2, height=1, bg="#A52A2A", fg="#F4A460", text="6",
                                           font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
            self.menu_button_7 = tk.Button(self.dropdown_delete, width=2, height=1, bg="#A52A2A", fg="#F4A460", text="7",
                                           font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")
            self.menu_button_8 = tk.Button(self.dropdown_delete, width=2, height=1, bg="#A52A2A", fg="#F4A460", text="8",
                                           font="Courier 12 bold", activebackground="#A52A2A", activeforeground="#F4A460")

            BUTTON_LIST = [self.menu_button_1, self.menu_button_2, self.menu_button_3, self.menu_button_4,
                           self.menu_button_5, self.menu_button_6, self.menu_button_7, self.menu_button_8]

            button_counter = 0

            x = self.make_new_list()

            for num in range(x):

                BUTTON_LIST[button_counter].configure(text=num + 1, command=lambda t=num: [DataBase().delete_database_entry(t), self.del_drop_menu()])
                BUTTON_LIST[button_counter].grid(column=0, row=button_counter)
                button_counter += 1

    def win_update(self):

        x = self.window.winfo_children()
        x[-1].destroy()
        self.update()
        self.window.update()





