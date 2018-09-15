"""
Start a new tkinter window to display the main page
"""
from tkinter import *


class App:
    def __init__(self, master):
        self.label = Label(master,
                           text="Welcome to my movie record\n Please make an option")
        self.label.pack(side="top")

        frame = Frame(master=master, width=330, height=50)
        frame.pack()

        frame2 = Frame(master=master, width=330, height=50, borderwidth=10)
        frame2.pack()

        self.button_1 = Button(frame2, text="List all movies",
                               width=20,
                               height=5,
                               borderwidth=10)
        self.button_1.pack(side="left")

        self.button_2 = Button(frame2, text="Add movies",
                               width=20,
                               height=5,
                               borderwidth=10)
        self.button_2.pack(side="left")

        self.quit_button = Button(master, text="Quit",
                                  command=master.quit,
                                  width=15,
                                  height=2,
                                  borderwidth=5)
        self.quit_button.pack(side="bottom")


def tkinter_mainpage(root):
    app = App(root)
    root.mainloop()
