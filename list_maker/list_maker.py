# @Daniel Zenglein - "Fiae202207"
import tkinter as tk
from tkinter import messagebox
from database import DataBase

#WINDOW_COUNTER = 0
CANVAS_LIST = []
BUTTON_LIST = []


class ListMaker:
    
    def __init__(self):

        # Main-Window

        self.window = tk.Tk()
        self.window.title("Exam-Dater")
        self.window.geometry("500x500+500+200")
        self.window.resizable(False, False)

        # Images

        self.icon = tk.PhotoImage(file="trashcan.png")

        # Labels and Entry's

        self.background = tk.Canvas(width=500, heigh=500, background="#FAEBD7")
        self.background.grid(row=0, column=0, sticky="n,w")

        self.main_label = tk.Label(text="EXAM - DATER", font="Georgia 30 bold", fg="#8B8378", bg="#FAEBD7")
        self.main_label.grid(row=0, column=0, pady=0, padx=85, sticky="n,w")

        self.first_label = tk.Label(text="Auditor", background="#FAEBD7", font="Georgia 20")
        self.first_label.grid(row=0, column=0, pady=55, padx=33, sticky="n,w")

        self.e_auditor = tk.StringVar()

        self.ent_auditor = tk.Entry(width=7, background="#FAEBD7", font="Georgia 20", fg="#CD853F", state="disabled",
                                    textvariable=self.e_auditor)
        self.ent_auditor.grid(row=0, column=0, pady=100, padx=20, sticky="n,w")

        self.second_label = tk.Label(text="Theme", background="#FAEBD7", font="Georgia 20")
        self.second_label.grid(row=0, column=0, pady=55, padx=220, sticky="n,w")

        self.e_theme = tk.StringVar()

        self.ent_theme = tk.Entry(width=11, background="#FAEBD7", font="Georgia 20", fg="#CD853F",
                                  textvariable=self.e_theme)
        self.ent_theme.grid(row=0, column=0, pady=100, padx=166, sticky="n,w")

        self.date_label = tk.Label(text="Date", background="#FAEBD7", font="Georgia 20")
        self.date_label.grid(row=0, column=0, pady=55, padx=400, sticky="n,w")

        self.e_date = tk.StringVar()

        self.ent_date = tk.Entry(width=7, background="#FAEBD7", font="Helvetica 18", fg="#CD853F",
                                 textvariable=self.e_date)
        self.ent_date.grid(row=0, column=0, pady=100, padx=382, ipadx=1, ipady=2, sticky="n,w")

        self.e_delete = tk.StringVar()

        self.ent_delete = tk.Entry(width=1, background="#FAEBD7", font="Helvetica 18", fg="#CD853F",
                                   textvariable=self.e_delete)
        self.ent_delete.grid(row=0, column=0, pady=153, padx=414, ipadx=2, ipady=2, sticky="n,w")

        if len(DataBase().fetch_all()) == 0:
            self.ent_delete.config(state="disabled")

        # Canvas

        self.list_canvas_1 = tk.Label()
        self.list_canvas_2 = tk.Label()
        self.list_canvas_3 = tk.Label()
        self.list_canvas_4 = tk.Label()
        self.list_canvas_5 = tk.Label()
        self.list_canvas_6 = tk.Label()
        self.list_canvas_7 = tk.Label()
        self.list_canvas_8 = tk.Label()

        # Buttons

        self.save_button = tk.Button(text="Save Date", width=12, heigh=2, font="Georgia 8 bold", fg="#A52A2A",
                                     command=self.save_date)
        self.save_button.grid(row=0, column=0, pady=150, padx=210, sticky="n,w")

        self.delete_button = tk.Button(image=self.icon, width=34, heigh=34,
                                       font="Georgia 8 bold", fg="#FF3030", command=self.get_id)
        self.delete_button.grid(row=0, column=0, pady=150, padx=440, sticky="n,w")

        self.drop_down = tk.Button(width=10, heigh=2, text="Auditors",
                                   font="Georgia 8 bold", fg="#FF3030", command=self.drop_down)
        self.drop_down.grid(row=0, column=0, pady=150, padx=40, sticky="n,w")

        self.dropdown_frame = ()
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

    def canvas(self):

        self.list_canvas_1 = tk.Label(width=35, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold", borderwidth=2,
                                      relief="groove", anchor="nw")
        self.list_canvas_1.grid(row=0, column=0, pady=208, padx=20, sticky="n,w")

        self.list_canvas_2 = tk.Label(width=35, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold", borderwidth=2,
                                      relief="groove", anchor="nw")
        self.list_canvas_2.grid(row=0, column=0, pady=243, padx=20, sticky="n,w")

        self.list_canvas_3 = tk.Label(width=35, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold", borderwidth=2,
                                      relief="groove", anchor="nw")
        self.list_canvas_3.grid(row=0, column=0, pady=278, padx=20, sticky="n,w")

        self.list_canvas_4 = tk.Label(width=35, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold", borderwidth=2,
                                      relief="groove", anchor="nw")
        self.list_canvas_4.grid(row=0, column=0, pady=313, padx=20, sticky="n,w")

        self.list_canvas_5 = tk.Label(width=35, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold", borderwidth=2,
                                      relief="groove", anchor="nw")
        self.list_canvas_5.grid(row=0, column=0, pady=348, padx=20, sticky="n,w")

        self.list_canvas_6 = tk.Label(width=35, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold", borderwidth=2,
                                      relief="groove", anchor="nw")
        self.list_canvas_6.grid(row=0, column=0, pady=383, padx=20, sticky="n,w")

        self.list_canvas_7 = tk.Label(width=35, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold", borderwidth=2,
                                      relief="groove", anchor="nw")
        self.list_canvas_7.grid(row=0, column=0, pady=418, padx=20, sticky="n,w")

        self.list_canvas_8 = tk.Label(width=35, bg="#F4A460", fg="#A52A2A", font="Courier 16 bold", borderwidth=2,
                                      relief="groove", anchor="nw")
        self.list_canvas_8.grid(row=0, column=0, pady=453, padx=20, sticky="n,w")

        global CANVAS_LIST
        CANVAS_LIST = [self.list_canvas_1, self.list_canvas_2, self.list_canvas_3, self.list_canvas_4,
                       self.list_canvas_5, self.list_canvas_6, self.list_canvas_7, self.list_canvas_8]
        self.save_date()

    def save_date(self):

        if self.e_auditor.get() == "":
            pass
        else:
            DataBase().author_new_entry()
            DataBase().make_database_entry(e_auditor=self.ent_auditor.get(), e_theme=self.ent_theme.get(),
                                           e_date=self.ent_date.get())

        self.make_new_list()

    def make_new_list(self):

        new_list = []
        counter = 0
        counter_list = []

        for n in range(len(DataBase().fetch_all())):

            new_string = DataBase().fetch_all()[counter]

            new_list.append(new_string)
            counter_list.append(new_list[counter][0])

            CANVAS_LIST[counter].config(text=f"{new_list[counter][0]} {new_list[counter][1]}"
                                             f"  {new_list[counter][2]} {new_list[counter][3]}")

            counter += 1

            self.clear_var()
            self.ent_delete.config(state="normal")
            self.window.update()
            #self.check_time()

    def get_id(self):

        try:
            del_numb = int(self.e_delete.get())
        except ValueError:

            tk.messagebox.showerror("Python Error!", 'Input only numbers to 8')
            self.ent_delete.delete(0, "end")

        else:
            del_numb = str(del_numb)

            if len(str(del_numb)) > 8:
                tk.messagebox.showerror("Python Error!", 'Input only numbers to 8')
                self.ent_delete.delete(0, "end")

            else:
                del_numb = int(del_numb)

                DataBase().delete_database_entry(del_numb)

                for canvas in CANVAS_LIST:
                    if str(del_numb) in canvas.cget('text')[0:1]:
                        canvas.config(text="")
                        CANVAS_LIST.remove(canvas)
                        self.update()

                self.ent_delete.delete(0, "end")
                self.update()

    def update(self):

        self.canvas()
        self.ent_delete.focus_set()

    def clear_var(self):

        self.ent_auditor.config(state="normal")
        self.ent_auditor.delete(0, "end")
        self.ent_auditor.config(state="disabled")

        self.ent_theme.delete(0, "end")
        self.ent_date.delete(0, "end")


    def drop_down(self):

        global BUTTON_LIST

        self.dropdown_frame = tk.Canvas(width=200)
        self.dropdown_frame.grid(row=0, column=0, pady=50, padx=157, sticky="n,w")

        self.menu_button_1 = tk.Button(self.dropdown_frame, width=20, height=1, bg="#A52A2A", fg="#F4A460",
                                       font="Courier 12 bold",activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_2 = tk.Button(self.dropdown_frame, width=20, height=1, bg="#A52A2A", fg="#F4A460",
                                       font="Courier 12 bold",activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_3 = tk.Button(self.dropdown_frame, width=20, height=1, bg="#A52A2A", fg="#F4A460",
                                       font="Courier 12 bold",activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_4 = tk.Button(self.dropdown_frame, width=20, height=1, bg="#A52A2A", fg="#F4A460",
                                       font="Courier 12 bold",activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_5 = tk.Button(self.dropdown_frame, width=20, height=1, bg="#A52A2A", fg="#F4A460",
                                       font="Courier 12 bold",activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_6 = tk.Button(self.dropdown_frame, width=20, height=1, bg="#A52A2A", fg="#F4A460",
                                       font="Courier 12 bold",activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_7 = tk.Button(self.dropdown_frame, width=20, height=1, bg="#A52A2A", fg="#F4A460",
                                       font="Courier 12 bold",activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_8 = tk.Button(self.dropdown_frame, width=20, height=1, bg="#A52A2A", fg="#F4A460",
                                       font="Courier 12 bold",activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_9 = tk.Button(self.dropdown_frame, width=20, height=1, bg="#A52A2A", fg="#F4A460",
                                       font="Courier 12 bold",activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_10 = tk.Button(self.dropdown_frame, width=20, height=1, bg="#A52A2A", fg="#F4A460",
                                        font="Courier 12 bold",activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_11 = tk.Button(self.dropdown_frame, width=20, height=1, bg="#A52A2A", fg="#F4A460",
                                        font="Courier 12 bold",activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_12 = tk.Button(self.dropdown_frame, width=20, height=1, bg="#A52A2A", fg="#F4A460",
                                        font="Courier 12 bold",activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_13 = tk.Button(self.dropdown_frame, width=20, height=1, bg="#A52A2A", fg="#F4A460",
                                        font="Courier 12 bold",activebackground="#A52A2A", activeforeground="#F4A460")
        self.menu_button_14 = tk.Button(self.dropdown_frame, width=20, height=1, bg="#A52A2A", fg="#F4A460",
                                        font="Courier 12 bold",activebackground="#A52A2A", activeforeground="#F4A460")

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

    def menu_buttons(self, t):

        self.ent_auditor.config(state="normal")
        self.ent_auditor.delete(0, "end")
        self.ent_auditor.insert(0, t)
        self.ent_auditor.config(state="disabled")
        x = self.window.winfo_children()
        x[-1].destroy()
        self.window.update()

        #self.dropdown_frame.destroy()
        #print(NEW_LIST)
        #names = DataBase().check_all_authors()
        #print(names[button_counter])




'''
    def check_time(self):
        print(datetime.datetime.now().date())
        print(datetime.datetime.month)
        print(datetime.datetime.year)
'''