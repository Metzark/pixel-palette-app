from tkinter import *
import tkinter.colorchooser as tkColorChooser
from models import model


class Create:
    def __init__(self, window, type, text, exit_func):
        self.model = model.Model(type=type, text=text)
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
                btn.config(bg='#ffffff', height=1, width=2, bd=1, command=lambda btn=btn: self.change_cell_color(btn))
                btn.grid(column=x, row=y)
        
        colors = Frame(frame, background="#d6d6d6")
        colors_title = Label(colors, text='Colors', fg='#121212', bg='#d6d6d6', font=('Lucida Sans', 16), pady=(5))
        colors_title.pack()
        self.rads = []
        for i in range (0, 10):
            rad = Radiobutton(colors, text=i, font=('Lucida Sans', 14), fg=self.model.getToolbarColor(i), activebackground=self.model.getToolbarColor(i), selectcolor=self.model.getToolbarColor(i), indicator=0, value=i, variable=self.model.selected_color, width=10)
            rad.pack(pady=5)
            self.rads.append(rad)

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
        grid = Frame(frame)
        for x in range(20):
            for y in range(20):
                btn = Button(grid)
                btn.config(bg=self.model.get_grid_cell_color(x,y), height=1, width=2, bd=1, command=lambda btn=btn: self.change_cell_color(btn))
                btn.grid(column=y, row=x)
        
         #temp colors array

        colors = Frame(frame, background="#d6d6d6")
        colors_title = Label(colors, text='Colors', fg='#121212', bg='#d6d6d6', font=('Lucida Sans', 16), pady=(5))
        colors_title.pack()
        self.rads = []
        for i in range (0, 10):
            rad = Radiobutton(colors, text=i, font=('Lucida Sans', 14), fg=self.model.getToolbarColor(i), activebackground=self.model.getToolbarColor(i), selectcolor=self.model.getToolbarColor(i), indicator=0, value=i, variable=self.model.selected_color, width=10)
            rad.pack(pady=5)
            self.rads.append(rad)

        change_colors = Frame(frame, background='#d6d6d6')
        placeholder_title = Label(change_colors, text='', fg='#121212', bg='#d6d6d6', font=('Lucida Sans', 16), pady=(5))
        placeholder_title.pack()
        for i in range (0, 10):
            btn = Button(change_colors, text="EDIT", command=lambda i=i: self.change_color_value(i), height=1)
            btn.pack(pady=9)

        menu_btns = Frame(frame, background="#d6d6d6")
        exit_btn = Button(menu_btns, text="Exit", fg='#121212', bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 18), bd=0, pady=(10),command=exit_func)
        save_btn = Button(menu_btns, text="Save", fg='#121212', bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 18), bd=0, pady=(10), command=lambda: self.save(exit_func))
        upload_btn = Button(menu_btns, text="Save", fg='#121212', bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 18), bd=0, pady=(10), command=lambda: self.save(exit_func))
        exit_btn.grid(column=0, row= 0)
        save_btn.grid(column=1, row=0)

        title.grid(column=0, row=0)
        grid.grid(column=0, row=1, padx=15)
        colors.grid(column=1, row=1, padx=5)
        change_colors.grid(column=2, row=1, padx=5)
        menu_btns.grid(column=0, row=2)
        frame.pack()

    # Change color in model and on the grid
    def change_cell_color(self, btn):
        self.model.change_grid_cell(btn.grid_info()["row"], btn.grid_info()["column"])
        btn.config(bg=self.model.getToolbarColor(self.model.selected_color.get()))

    def change_color_value(self, idx):
        color = tkColorChooser.askcolor(title='Choose color')
        self.model.setToolbarColor(idx, color[1])
        self.rads[idx].config(activebackground=self.model.getToolbarColor(idx), selectcolor=self.model.getToolbarColor(idx), fg=self.model.getToolbarColor(idx))
        
    def save(self, exit):
        self.model.saveCreation()
        exit()

    def upload(self):
        pass