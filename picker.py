from tkinter.ttk import Button, Frame, Label
from tkinter import Listbox, END, ACTIVE, X

class ChoiceFrame (Frame):
    def __init__ (self, title):
        Frame.__init__(self)
        self.master.title(title)
        self.master.resizable(0,0)
        self.master.attributes("-toolwindow",1)
        lbl = Label(self, text=title)
        lbl.pack()
        self.listbox = Listbox(self)
        self.listbox.pack()
        self.selection = None



def make_choice (options, title, btnlbl='Choose'):
    win = ChoiceFrame(title)
    for option in options:
        win.listbox.insert(END, option)

    def callback ():
        win.selection = win.listbox.get(ACTIVE)
        win.master.destroy()
    
    btn = Button(win, text=btnlbl, command=callback)
    btn.pack(fill=X)
    win.pack()

    win.mainloop()

    return win.selection
