from tkinter import *
from models import model


class Play:
    def __init__(self, window, text, exit_func):
        self.model = model.Model(type='fill_from_creation', text=text)
        self.load_creation_local(window, exit_func)
        
    def load_creation_local(self, window, exit_func):
        frame = Frame(window, bg="#d6d6d6",pady=20, padx=20)
        title = Label(frame, text='Fill in by number!', fg='#121212', bg='#d6d6d6', font=('Lucida Sans', 24), pady=(10))
        grid = Frame(frame)
        for x in range(20):
            for y in range(20):
                btn = Button(grid)
                btn.config(text=self.model.get_cell_value(x,y),bg=self.model.get_grid_cell_color(x,y), height=1, width=2, bd=1, command=lambda btn=btn: self.change_cell_color(btn))
                btn.grid(column=y, row=x)
        
       

        colors = Frame(frame, background="#d6d6d6")
        colors_title = Label(colors, text='Colors', fg='#121212', bg='#d6d6d6', font=('Lucida Sans', 16), pady=(5))
        colors_title.pack()
        self.rads = []
        for i in range (0, 10):
            rad = Radiobutton(colors, text=i, font=('Lucida Sans', 14), fg=self.model.getToolbarColor(i), activebackground=self.model.getToolbarColor(i), selectcolor=self.model.getToolbarColor(i), indicator=0, value=i, variable=self.model.selected_color, width=10)
            rad.pack(pady=5)
            self.rads.append(rad)

        menu_btns = Frame(frame, background="#d6d6d6")
        exit_btn = Button(menu_btns, text="Exit", fg='#121212', bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 18), bd=0, pady=(10),command=exit_func)
        complete_btn = Button(menu_btns, text="Complete", fg='#121212', bg='#d6d6d6', activebackground='#d6d6d6', font=('Lucida Sans', 18), bd=0, pady=(10), command=lambda: self.complete(exit_func))
        exit_btn.grid(column=0, row= 0)
        complete_btn.grid(column=1, row=0)
        title.grid(column=0, row=0)
        grid.grid(column=0, row=1, padx=15)
        colors.grid(column=1, row=1, padx=5)
        menu_btns.grid(column=0, row=2)
        frame.pack()

    # Change color in model and on the grid
    def change_cell_color(self, btn):
        # print(self.model.colors[self.model.getSelectedColor()], self.model.get_grid_cell_color(btn.grid_info()["row"], btn.grid_info()["column"]))
        if self.model.getSelectedColor() == self.model.get_cell_value(btn.grid_info()["row"], btn.grid_info()["column"]):
            self.model.change_grid_cell(btn.grid_info()["row"], btn.grid_info()["column"])
            btn.config(bg=self.model.getToolbarColor(self.model.selected_color.get()))

    def complete(self, exit):
        if self.model.check_completed_play():
            self.show_completed(exit)

    def show_completed(self, exit):
        pass