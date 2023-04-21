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
            exit_btn = Button(frame, text="Exit", fg='#F5454C', bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 24), bd=0, pady=(10), command= lambda: Menu.exit_app(window))
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
            load_creation = Button(frame, text="Fill in a local creation", fg="#0ED145", bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 24), bd=0, pady=(10), command=lambda: Menu.play_local(window))
            load_from_gallery= Button(frame, text='Fill in a creation from gallery', fg="#00A8F3", bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 24), bd=0, pady=(10), command=lambda: Menu.play_gallery(window))
            back_btn = Button(frame, text="back", fg='#F5454C', bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 24), bd=0, pady=(10), command= lambda: Menu.init(window))
            title.pack()
            load_creation.pack()
            load_from_gallery.pack()
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
            load = Button(frame, text='Load a creation', fg="#00A8F3", bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 24), bd=0, pady=(10), command=lambda: Menu.update_existing_creation(window))
            back_btn = Button(frame, text="back", fg='#F5454C', bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 24), bd=0, pady=(10), command= lambda: Menu.init(window))
            title.pack()
            scratch.pack()
            load.pack()
            back_btn.pack()
            frame.pack()


    # Creates Play with parameter 'local'
    def play_local(window):
        try:
             for key in window.children:
                window.children[key].destroy()
        except:
            pass
        finally:
            play.Play(window, type='local', exit_func=(lambda: Menu.init(window)))


    # Creates Play with parameter 'gallery'
    def play_gallery(window):
        try:
             for key in window.children:
                window.children[key].destroy()
        except:
            pass
        finally:
            play.Play(window, type='gallery', exit_func=(lambda: Menu.init(window)))

    # Creates Create with parameter 'fromscratch'
    def create_from_scratch(window):
        try:
             for key in window.children:
                window.children[key].destroy()
        except:
            pass
        finally:
            create.Create(window, 'fromscratch', exit_func=(lambda: Menu.init(window)))


    # Creates Create with parameter 'updatecreation'
    def update_existing_creation(window):
        try:
             for key in window.children:
                window.children[key].destroy()
        except:
            pass
        finally:
            create.Create(window, 'updatecreation', exit_func=(lambda: Menu.init(window)))

        