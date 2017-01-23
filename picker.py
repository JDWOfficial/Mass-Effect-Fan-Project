from tkinter.ttk import Button, Label
from tkinter import Toplevel, Listbox, END, ACTIVE, X


class ChoiceFrame (Toplevel):
    def __init__ (self, title, parent=None):
        Toplevel.__init__(self)
        self.title(title)
        self.resizable(0,0)
        self.attributes("-toolwindow",1)
        if parent:
            print('Hi')
            self.transient(parent)
        lbl = Label(self, text=title)
        lbl.pack()
        self.listbox = Listbox(self)
        self.listbox.pack()
        self.listbox.focus_set()
        self.selection = None



def make_choice (options, title, btnlbl='Choose', parent=None):
    win = ChoiceFrame(title, parent)
    for option in options:
        win.listbox.insert(END, option)

    def callback ():
        win.selection = win.listbox.get(ACTIVE)
        win.destroy()
    
    btn = Button(win, text=btnlbl, command=callback)
    btn.pack(fill=X)
    #win.pack()

    win.mainloop()

    return win.selection
