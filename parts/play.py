from tkinter import *
from parts import model


class Play:
    def __init__(self, window, text, exit_func):
        self.current_color = IntVar()
        self.load_creation_local(window, exit_func)
        
    def load_creation_local(self, window, exit_func):
        frame = Frame(window, bg="#d6d6d6",pady=20, padx=20)
        title = Label(frame, text='Fill in by number!', fg='#121212', bg='#d6d6d6', font=('Lucida Sans', 24), pady=(10))
        grid = Frame(frame)
        for x in range(20):
            for y in range(20):
                btn = Button(grid)
                btn.config(bg='#ffffff', height=1, width=2, bd=1, command=lambda btn=btn: self.change_cell_color(btn))
                btn.grid(column=x, row=y)
        
        #temp colors array
        hexs = ['#ffffff', '#000000', '#ff0000', '#00ff00', '#0000ff', '#888888', '#435324', '#180054', '#00ffff', '#ff00ff']
        self.hexs = hexs

        colors = Frame(frame, background="#d6d6d6")
        colors_title = Label(colors, text='Colors', fg='#121212', bg='#d6d6d6', font=('Lucida Sans', 16), pady=(5))
        colors_title.pack()
        for i in range (0, 10):
            rad = Radiobutton(colors, text=i, font=('Lucida Sans', 14), fg='#121212', activebackground=hexs[i], selectcolor=hexs[i], indicator=0, value=i, variable=self.current_color, width=10, command=self.change_active_color)
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


    # Changes active color in model
    def change_active_color(self):
        pass

    # Change color in model and on the grid
    def change_cell_color(self, btn):
        btn.config(bg=self.hexs[self.current_color.get()])
        print(btn.grid_info()["row"], btn.grid_info()["column"])
