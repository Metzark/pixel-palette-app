from tkinter import *
from parts import menu

def createWindow():
    window = Tk()
    window.title('Pixel Palette')
    window.configure(bg='#F5454C', pady=40)
    window.geometry('896x504')
    window.minsize(width=896, height=504)
    window.iconphoto(True, icon := PhotoImage(file='imgs/logo-sm.png'))
    return window

window = createWindow()
menu.Menu.init(window)
window.mainloop()

