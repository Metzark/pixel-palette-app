from tkinter import *
from parts import play
from parts import create

# Menu class contains functions for loading each menu. Each menu load function destroys
# all window.children and inserts new content afterwards.

class Menu:
    #Exits the program
    def exit_app(window):
        window.destroy()
        
    #Initializes the main menu (Login will eventually call this)
    def init(window):
        try:
            for key in window.children:
                window.children[key].destroy()
        except:
            pass
        finally:
            frame = Frame(window, bg="#d6d6d6",pady=20, padx=20)
            title = Label(frame, text='Pixel Palette', fg='#121212', bg='#d6d6d6', font=('Lucida Sans', 32), pady=(10))
            play_btn = Button(frame, text="Play", fg="#0ED145", bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 24), bd=0, pady=(10), command=lambda: Menu.play_options(window))
            make_btn = Button(frame, text='Create', fg="#00A8F3", bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 24), bd=0, pady=(10), command=lambda: Menu.create_options(window))
            exit_btn = Button(frame, text="Exit", fg='#0a298d', bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 24), bd=0, pady=(10), command= lambda: Menu.exit_app(window))
            title.pack()
            play_btn.pack()
            make_btn.pack()
            exit_btn.pack()
            frame.pack()

    # List of the different play mode options. (Fill in a creation or an image)
    def play_options(window):
        try:
            for key in window.children:
                window.children[key].destroy()
        except:
            pass
        finally:
            frame = Frame(window, bg="#d6d6d6",pady=20, padx=20)
            title = Label(frame, text='Play', fg='#121212', bg='#d6d6d6', font=('Lucida Sans', 32), pady=(10))
            load_creation = Button(frame, text="Fill in a creation", fg="#0ED145", bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 24), bd=0, pady=(10))
            load_from_img = Button(frame, text='Fill in an image', fg="#00A8F3", bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 24), bd=0, pady=(10))
            back_btn = Button(frame, text="back", fg='#0a298d', bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 24), bd=0, pady=(10), command= lambda: Menu.init(window))
            title.pack()
            load_creation.pack()
            load_from_img.pack()
            back_btn.pack()
            frame.pack()

    # List of different create mode options. (Start from scratch or load an existing creation)
    def create_options(window):
        try:
             for key in window.children:
                window.children[key].destroy()
        except:
            pass
        finally:
            frame = Frame(window, bg="#d6d6d6",pady=20, padx=20)
            title = Label(frame, text='Create', fg='#121212', bg='#d6d6d6', font=('Lucida Sans', 32), pady=(10))
            scratch = Button(frame, text="Start from scratch", fg="#0ED145", bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 24), bd=0, pady=(10), command=lambda: Menu.create_from_scratch(window))
            load = Button(frame, text='Load a creation', fg="#00A8F3", bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 24), bd=0, pady=(10))
            back_btn = Button(frame, text="back", fg='#0a298d', bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 24), bd=0, pady=(10), command= lambda: Menu.init(window))
            title.pack()
            scratch.pack()
            load.pack()
            back_btn.pack()
            frame.pack()


    def create_from_scratch(window):
        try:
             for key in window.children:
                window.children[key].destroy()
        except:
            pass
        finally:
            pass


    def create_from_existing_creation(window):
        try:
             for key in window.children:
                window.children[key].destroy()
        except:
            pass
        finally:
            pass

        