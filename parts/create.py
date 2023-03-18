from tkinter import *
from parts import model


class Create:
    def __init__(self, window):
        frame = Frame(window, bg="#d6d6d6",pady=20, padx=20)
        title = Label(frame, text='Create a picture!', fg='#121212', bg='#d6d6d6', font=('Lucida Sans', 24), pady=(10))
        title.pack()
        frame.pack()
        pass

    