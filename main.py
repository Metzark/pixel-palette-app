from tkinter import *
from parts import menu

def createWindow():
    window = Tk()
    window.title('Pixel Palette')
    window.configure(bg='#054f59', pady=40)
    window.geometry('896x704')
    window.minsize(width=896, height=704)
    window.iconphoto(True, icon := PhotoImage(file='imgs/logo-sm.png'))
    return window

window = createWindow()
menu.Menu.init(window)
window.mainloop()

