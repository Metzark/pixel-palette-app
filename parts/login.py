from tkinter import *
from data import airtable

class Login:
    def __init__(self, window, start_app):
        self.create_login(window, start_app)

    def attempt_login(self, window, start_app):
        if(airtable.validate_user(self.username_var.get(), self.password_var.get())):
            start_app(window, self.username_var.get())

    def create_login(self, window, start_app):
        self.username_var = StringVar()
        self.password_var = StringVar()
        frame = Frame(window, bg="#d6d6d6",pady=20, padx=20)
        title = Label(frame, text='Log in', fg='#121212', bg='#d6d6d6', font=('Lucida Sans', 24), pady=(5), padx=100)
        login_div = Frame(frame, bg='#d6d6d6', pady=10)
        username_label = Label(login_div, text='Username',font=('Lucida Sans', 16), bg='#d6d6d6', pady=3, )
        username = Entry(login_div, textvariable=self.username_var, width=50)
        password_label = Label(login_div, text='Password', font=('Lucida Sans', 16), bg='#d6d6d6', pady=3)
        password = Entry(login_div, textvariable=self.password_var, show="*", width=50)
        login_btn = Button(frame, text="Log in", border=0, font=('Lucida Sans', 16),  bg='#d6d6d6', activeforeground='#054f59', activebackground='#d6d6d6', command=lambda: self.attempt_login(window, start_app))
        username_label.pack()
        username.pack()
        password_label.pack()
        password.pack()
        title.pack()
        login_div.pack()
        login_btn.pack()
        frame.pack()