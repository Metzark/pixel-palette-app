from tkinter import *
from parts import play as Play
from parts import create as Create

#Exits the program
def exit_app(window):
    window.destroy()
        
#Initializes the main menu (Login will eventually call this)
def init(window):
    #frame key in window.children is "!frame", use to destroy frame
    try:
        for key in window.children:
            window.children[key].destroy()
    except:
        pass
    finally:
        frame = Frame(window, bg="#d6d6d6",pady=20, padx=20)
        title = Label(frame, text='Pixel Palette', fg='#121212', bg='#d6d6d6', font=('Lucida Sans', 32), pady=(10))
        play_btn = Button(frame, text="Play", fg="#0ED145", bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 24), bd=0, pady=(10), command= lambda: Play.init(window, lambda: init(window)))
        make_btn = Button(frame, text='Create', fg="#00A8F3", bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 24), bd=0, pady=(10), command= lambda: Create.init(window, lambda: init(window)))
        exit_btn = Button(frame, text="Exit", fg='#F5454C', bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 24), bd=0, pady=(10), command= lambda: exit_app(window))
        title.pack()
        play_btn.pack()
        make_btn.pack()
        exit_btn.pack()
        frame.pack()
