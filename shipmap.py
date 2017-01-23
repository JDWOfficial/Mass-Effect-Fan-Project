from tkinter import Canvas
from tkinter.ttk import Frame
from tkinter.simpledialog import askstring, askinteger
from picker import make_choice
from util import get_str


class Map(Frame):
    def __init__(self, deck):
        Frame.__init__(self)
        print("Map starting on deck: " + str(deck))
        self.deck = Deck(self)
        self.deck.pack()
        self.update_title()

    def ask_string(self, prompt, title='?'):
        return askstring(title, prompt, parent=self)

    def ask_integer(self, prompt, title='?'):
        return askinteger(title, prompt, parent=self)

    def ask_multiple(self, opts, title='Choice', btnlbl='Choose'):
        return make_choice(opts, title, parent=self, btnlbl=btnlbl)

    def update_title(self):
        self.master.title(
            get_str()['general']['wintitle'].format(
                deck=self.deck.number,
                room=self.deck.current.title))


class Deck(Canvas):
    def __init__(self, parent):
        Canvas.__init__(self, parent, width=750, height=400)
        self.number = 0
        self.current = Room()


class Room():
    def __init__(self):
        self.title = 'CIC'
