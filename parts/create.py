from tkinter import *

#Initializes the Create menu
def init(window, main_menu_init):
    try:
         for key in window.children:
            window.children[key].destroy()
    except:
        pass
    finally:
        frame = Frame(window, bg="#d6d6d6",pady=20, padx=20)
        title = Label(frame, text='Create', fg='#121212', bg='#d6d6d6', font=('Lucida Sans', 32), pady=(10))
        scratch = Button(frame, text="Start from scratch", fg="#0ED145", bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 24), bd=0, pady=(10))
        load = Button(frame, text='Load a creation', fg="#00A8F3", bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 24), bd=0, pady=(10))
        back_btn = Button(frame, text="back", fg='#F5454C', bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 24), bd=0, pady=(10), command= lambda: main_menu_init())
        title.pack()
        scratch.pack()
        load.pack()
        back_btn.pack()
        frame.pack()
