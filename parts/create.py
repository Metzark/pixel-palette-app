from tkinter import *
import tkinter.colorchooser as tkColorChooser
from parts import model


class Create:
    def __init__(self, window, type, exit_func):
        self.current_color = IntVar()
        if type == 'fromscratch':
             self.create_from_scratch(window, exit_func)
        if type == 'updatecreation':
             self.update_creation(window, exit_func)

    def create_from_scratch(self, window, exit_func):
        frame = Frame(window, bg="#d6d6d6",pady=20, padx=20)
        title = Label(frame, text='Create a picture!', fg='#121212', bg='#d6d6d6', font=('Lucida Sans', 24), pady=(10))
        grid = Frame(frame)
        for x in range(20):
            for y in range(20):
                btn = Button(grid)
                btn.config(height=1, width=2, bd=1, command=lambda btn=btn: self.change_cell_color(btn))
                btn.grid(column=x, row=y)
        
         #temp colors array
        hexs = ['#ffffff', '#000000', '#ff0000', '#00ff00', '#0000ff', '#888888', '#435324', '#180054', '#00ffff', '#ff00ff']
        self.hexs = hexs

        colors = Frame(frame, background="#d6d6d6")
        colors_title = Label(colors, text='Colors', fg='#121212', bg='#d6d6d6', font=('Lucida Sans', 16), pady=(5))
        colors_title.pack()
        for i in range (0, 10):
            rad = Radiobutton(colors, text=i, font=('Lucida Sans', 14), fg='#121212', activebackground=hexs[i], selectcolor=hexs[i], indicator=0, value=i, variable=self.current_color, width=10)
            rad.pack(pady=5)

        change_colors = Frame(frame, background='#d6d6d6')
        placeholder_title = Label(change_colors, text='', fg='#121212', bg='#d6d6d6', font=('Lucida Sans', 16), pady=(5))
        placeholder_title.pack()
        for i in range (0, 10):
            btn = Button(change_colors, text="EDIT", command=lambda i=i: self.change_color_value(i), height=1)
            btn.pack(pady=9)

        menu_btns = Frame(frame, background="#d6d6d6")
        exit_btn = Button(menu_btns, text="Exit", fg='#121212', bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 18), bd=0, pady=(10),command=exit_func)
        save_btn = Button(menu_btns, text="Save and Upload", fg='#121212', bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 18), bd=0, pady=(10), command=lambda: self.save_and_upload(exit_func))
        exit_btn.grid(column=0, row= 0)
        save_btn.grid(column=1, row=0)

        title.grid(column=0, row=0)
        grid.grid(column=0, row=1, padx=15)
        colors.grid(column=1, row=1, padx=5)
        change_colors.grid(column=2, row=1, padx=5)
        menu_btns.grid(column=0, row=2)
        frame.pack()


    def update_creation(self, window, exit_func):
        frame = Frame(window, bg="#d6d6d6",pady=20, padx=20)
        title = Label(frame, text='Update your creation!', fg='#121212', bg='#d6d6d6', font=('Lucida Sans', 24), pady=(10))
        title.pack()
        frame.pack()
    

     # Changes active color in model
    def change_active_color(self):
        print(self.current_color.get())

    # Change color in model and on the grid
    def change_cell_color(self, btn):
        btn.config(bg=self.hexs[self.current_color.get()])

    def change_color_value(self, idx):
        color = tkColorChooser.askcolor(title='Choose color')
        self.hexs[idx] = color[1]
        
    def save_and_upload(self, exit):
        exit()