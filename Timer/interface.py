# from tkinter import *
# from ttkthemes import *
# from timer import Timer
# from functools import partial

# class App:

#     def __init__(self, master):
#         Label(master, text="Timer Length: ").grid(row=0, column=0)
#         e1 = Entry(master)
#         e1.grid(row=0, column=1)

#         Button(
#             master, text="start", fg="red",
#             command=lambda: self.create_new_timer(int(e1.get()))
#         ).grid(row=0, column=2)

#     def create_new_timer(self, val):
#         timer = Timer(name="Name", seconds=val)
#         timer.start()

#     def timer_complete(self):
#         print("Timer has completed!")

# root = Tk()
# root.title = "Testing"
# root.geometry("300x200")

# app = App(root)

# root.mainloop()
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from timer import Timer

class App:
    def __init__(self, master):

        ttk.Label(master, text="Timer Length: ").grid(row=0, column=0)

        tkVar = StringVar(root)
        choices = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }
        tkVar.set(0)
        ttk.OptionMenu(master, tkVar, *choices).grid(row=0, column=1)

        ttk.Button(
            master, text="start",
            command=lambda: self.create_new_timer(int(tkVar.get()))
        ).grid(row=0, column=2)

    def create_new_timer(self, val):
        timer = Timer(name="Name", seconds=val)
        timer.start()

    def timer_complete(self):
        print("Timer has completed!")

root = ThemedTk(theme="clearlooks")
app = App(root)

root.mainloop()