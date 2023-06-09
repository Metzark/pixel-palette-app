from tkinter import *
from tkinter import filedialog
from modes import play
from modes import create

# Menu class contains functions for loading each menu. Each menu load function destroys
# all window.children and inserts new content afterwards.

class Menu:
    #Exits the program
    def exit_app(window):
        window.destroy()
        
    #Initializes the main menu (Login will eventually call this)
    def init(window, user):
        try:
            for key in window.children:
                window.children[key].destroy()
        except:
            pass
        finally:
            frame = Frame(window, bg="#d6d6d6",pady=20, padx=20)
            title = Label(frame, text='Pixel Palette', fg='#121212', bg='#d6d6d6', font=('Lucida Sans', 32), pady=(10))
            play_btn = Button(frame, text="Play", fg="#0ED145", bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 24), bd=0, pady=(10), command=lambda: Menu.play_options(window, user))
            make_btn = Button(frame, text='Create', fg="#00A8F3", bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 24), bd=0, pady=(10), command=lambda: Menu.create_options(window, user))
            exit_btn = Button(frame, text="Exit", fg='#F5454C', bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 24), bd=0, pady=(10), command= lambda: Menu.exit_app(window))
            title.pack()
            play_btn.pack()
            make_btn.pack()
            exit_btn.pack()
            frame.pack()

    # List of the different play mode options. (Fill in a creation or an image)
    def play_options(window, user):
        try:
            for key in window.children:
                window.children[key].destroy()
        except:
            pass
        finally:
            frame = Frame(window, bg="#d6d6d6",pady=20, padx=20)
            title = Label(frame, text='Play', fg='#121212', bg='#d6d6d6', font=('Lucida Sans', 32), pady=(10))
            load_creation = Button(frame, text="Fill in a local creation", fg="#0ED145", bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 24), bd=0, pady=(10), command=lambda: Menu.play_local(window, user))
            back_btn = Button(frame, text="back", fg='#F5454C', bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 24), bd=0, pady=(10), command= lambda: Menu.init(window, user))
            title.pack()
            load_creation.pack()
            back_btn.pack()
            frame.pack()

    # List of different create mode options. (Start from scratch or load an existing creation)
    def create_options(window, user):
        try:
             for key in window.children:
                window.children[key].destroy()
        except:
            pass
        finally:
            frame = Frame(window, bg="#d6d6d6",pady=20, padx=20)
            title = Label(frame, text='Create', fg='#121212', bg='#d6d6d6', font=('Lucida Sans', 32), pady=(10))
            scratch = Button(frame, text="Start from scratch", fg="#0ED145", bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 24), bd=0, pady=(10), command=lambda: Menu.create_from_scratch(window, user))
            load = Button(frame, text='Load a creation', fg="#00A8F3", bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 24), bd=0, pady=(10), command=lambda: Menu.update_existing_creation(window, user))
            back_btn = Button(frame, text="back", fg='#F5454C', bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 24), bd=0, pady=(10), command= lambda: Menu.init(window, user))
            title.pack()
            scratch.pack()
            load.pack()
            back_btn.pack()
            frame.pack()


    # Creates Play with parameter 'local'
    def play_local(window, user):
        try:
             for key in window.children:
                window.children[key].destroy()
        except:
            pass
        finally:
            path = filedialog.askopenfilename()
            file = open(path, 'r')
            text = file.readlines()
            play.Play(window, text, exit_func=(lambda: Menu.init(window, user)))

    # Creates Create with parameter 'fromscratch'
    def create_from_scratch(window, user):
        try:
             for key in window.children:
                window.children[key].destroy()
        except:
            pass
        finally:
            create.Create(window, type='fromscratch', text='', exit_func=(lambda: Menu.init(window, user)), user=user)


    # Creates Create with parameter 'updatecreation'
    def update_existing_creation(window, user):
        try:
             for key in window.children:
                window.children[key].destroy()
        except:
            pass
        finally:
            path = filedialog.askopenfilename()
            file = open(path, 'r')
            text = file.readlines()
            create.Create(window, type="updatecreation", text=text, exit_func=(lambda: Menu.init(window, user)), user=user)

        