"""
Start a new tkinter window to display the main page
"""
from tkinter import *
from JSON_handler import read_JSON, write_JSON, delete_JSON

class App:
    def __init__(self, master):
        self.label = Label(master,
                           text="Welcome to my movie record\n Please make an option")
        self.label.pack(side="top")

        # frames that are for styling purposes
        frame = Frame(master=master, width=330, height=50)
        frame.pack()

        frame2 = Frame(master=master, width=330, height=50, borderwidth=10)
        frame2.pack()

        #this button access list all movies page
        self.button_1 = Button(frame2, text="List all movies",
                               width=20,
                               height=5,
                               borderwidth=10,
                               command=App.list_movie_page)
        self.button_1.pack(side="left")

        # this button access the add movie page
        self.button_2 = Button(frame2, text="Add movies",
                               width=20,
                               height=5,
                               borderwidth=10,
                               command=App.add_movie_page)
        self.button_2.pack(side="left")

        # the quit button
        self.quit_button_1 = Button(master, text="Quit",
                                  command=master.quit,
                                  width=15,
                                  height=2,
                                  borderwidth=5)
        self.quit_button_1.pack(side="bottom")

    def list_movie_page():
        top = Toplevel()
        top.title("List of Movies")
        label_title = Label(top, text="This is all the list of Movies in my database", font=("Courier", 15))
        label_title.grid(row=0)

        # get data of list of movies
        data = read_JSON.get_data()

        # frame for showing list of movies
        frameList = Frame(top, width=330, height=50)
        frameList.grid(row=1)

        # construct text boxes to display watched movies
        label_watched = Label(frameList, text="Movies Watched", font=("arial", 10, "bold"))
        label_watched.grid(row=0, column=0)
        for number in range(len(data["watched"])):
            label_number = Label(frameList, text=data["watched"][number])
            label_number.grid(row=number+1, column=0)

        # construct text boxes to display pending movies
        label_watched = Label(frameList, text="Movies Pending", font=("arial", 10, "bold"))
        label_watched.grid(row=0, column=1)
        for number in range(len(data["pending"])):
            label_number = Label(frameList, text=data["pending"][number])
            label_number.grid(row=number + 1, column=1)

        # the quit button
        quit_button_2 = Button(top, text="Return to Main Page",
                                  command=top.destroy,
                                  width=15,
                                  height=2,
                                  borderwidth=5)
        quit_button_2.grid(row=5)

        # this button access the delete movie page
        button_3 = Button(top, text="Delete movies", command=App.delete_movie_page)
        button_3.grid(row=6)




    def add_movie_page():
        top = Toplevel()
        top.title("Add Movies")
        label_title = Label(top, text="To add a movie into database\n select if you watched the movie yet and type the name in the text-field")
        label_title.grid(row=0)

        # create a text field for input
        movie_name = StringVar()
        text_box = Label(top, text="Movie Name: ")
        text_box.grid(row=1, column=0)
        text_field = Entry(top, textvariable=movie_name)
        text_field.grid(row=1, column=1)

        # radiobutton for asking if movie is watched or not
        toggle = IntVar()
        toggle_watched = Radiobutton(top, text="watched", variable=toggle, value=1)
        toggle_pending = Radiobutton(top, text="pending", variable=toggle, value=0)
        toggle_watched.grid(row=2, column=0)
        toggle_pending.grid(row=2, column=1)

        # write movie name into database
        def _get_movie():
            movie_name = text_field.get()
            if toggle == 1:
                write_JSON.write_data(True, movie_name)
            else:
                write_JSON.write_data(False, movie_name)

            # display success once database is written and clear input text field
            success = Label(top, text="Success!", fg="green")
            success.grid(row=4)
            text_field.delete(0, END)

        # submit button calls _get_movie function
        button_press = Button(top, text="submit", command=_get_movie)
        button_press.grid(row=3, column=0)

        # quit button
        quit_button_3 = Button(top, text="Return to Main Page", command=top.destroy)
        quit_button_3.grid(row=3, column=1)

    def delete_movie_page():
        top = Toplevel()
        top.title("Delete movie")

        label_title = Label(top, text="select movies to delete from database", font=("Courier", 15))
        label_title.grid(row=0)

        # get data of list of movies
        data = read_JSON.get_data()

        # frame for showing list of movies
        frameList = Frame(top, width=330, height=50)
        frameList.grid(row=1)

        # construct text boxes to display watched movies
        label_watched = Label(frameList, text="Movies Watched", font=("arial", 10, "bold"))
        label_watched.grid(row=0, column=0)
        listbox_watched = Listbox(frameList)
        listbox_watched.grid(row=1, column=0)
        for number in range(len(data["watched"])):
            listbox_watched.insert(END, data["watched"][number])

        # construct list boxes to display pending movies
        label_watched = Label(frameList, text="Movies Pending", font=("arial", 10, "bold"))
        label_watched.grid(row=0, column=1)
        listbox_pending = Listbox(frameList)
        listbox_pending.grid(row=1, column=1)
        for number in range(len(data["pending"])):
            listbox_pending.insert(END, data["pending"][number])

        #function to delete movies from datbase
        def _delete_movies():
            # delete the pending movies
            name = listbox_pending.get(ACTIVE)
            listbox_pending.delete(ACTIVE)
            delete_JSON.delete_data(False, name)

            # delete the watched movies
            name = listbox_watched.get(ACTIVE)
            listbox_watched.delete(ACTIVE)
            delete_JSON.delete_data(True, name)

        # button to delete movies
        delete_button = Button(top, text="Delete Movies", command=_delete_movies)
        delete_button.grid(row=11)

        # the quit button
        quit_button_2 = Button(top, text="Return to List Movies Page",
                               command=top.destroy,
                               width=20,
                               height=2,
                               borderwidth=5)
        quit_button_2.grid(row=5)





def tkinter_mainpage(root):
    app = App(root)
    root.mainloop()
