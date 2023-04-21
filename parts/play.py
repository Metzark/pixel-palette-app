from tkinter import *
from parts import model


class Play:
    def __init__(self, window, type, exit_func):
        self.current_color = 0
        if type == 'local':
             self.load_creation_local(window, exit_func)
        if type == 'gallery':
             self.load_creation_gallery(window)
        
    def load_creation_local(self, window, exit_func):
        frame = Frame(window, bg="#d6d6d6",pady=20, padx=20)
        title = Label(frame, text='Fill in by number!', fg='#121212', bg='#d6d6d6', font=('Lucida Sans', 24), pady=(10))
        grid = Frame(frame)
        for x in range(20):
            for y in range(20):
                btn = Button(grid)
                btn.config(height=1, width=2, bd=1)
                btn.grid(column=x, row=y)
        
        #temp colors array
        hexs = ['#ffffff', '#000000', '#ff0000', '#00ff00', '#0000ff', '#888888', '#435324', '#180054', '#00ffff', '#ff00ff']

        colors = Frame(frame, background="#d6d6d6")
        colors_title = Label(colors, text='Colors', fg='#121212', bg='#d6d6d6', font=('Lucida Sans', 16), pady=(5))
        colors_title.pack()
        for i in range (0, 10):
            rad = Radiobutton(colors, text=i, font=('Lucida Sans', 14), fg='#121212', activebackground=hexs[i], selectcolor=hexs[i], indicator=0, value=i, variable=self.current_color, width=10)
            rad.pack(pady=5)

        menu_btns = Frame(frame, background="#d6d6d6")
        exit_btn = Button(menu_btns, text="Exit", fg='#121212', bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 18), bd=0, pady=(10),command=exit_func)
        complete_btn = Button(menu_btns, text="Complete", fg='#121212', bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 18), bd=0, pady=(10))
        exit_btn.grid(column=0, row= 0)
        complete_btn.grid(column=1, row=0)

        title.grid(column=0, row=0)
        grid.grid(column=0, row=1, padx=15)
        colors.grid(column=1, row=1, padx=5)
        menu_btns.grid(column=0, row=2)
        frame.pack()
    
    def load_creation_gallery(self, window):
         pass