from tkinter.ttk import Frame
from tkinter.simpledialog import askstring, askinteger
from picker import make_choice
from util import get_str


class Map(Frame):
    def __init__(self, deck):
        Frame.__init__(self)
        self.deck = {}  # TODO
        self.deck['number'] = deck
        self.deck['current'] = {}
        self.deck['current']['title'] = 'CIC'
        print("Map starting on deck: " + str(deck))

    def ask_string(self, prompt, title='?'):
        return askstring(title, prompt, parent=self)

    def ask_integer(self, prompt, title='?'):
        return askinteger(title, prompt, parent=self)

    def ask_multiple(self, opts, title='Choice', btnlbl='Choose'):
        return make_choice(opts, title, parent=self, btnlbl=btnlbl)
    
    def update_title(self):
        self.master.title = get_str()['general']['wintitle'].format(deck=self.deck.number,
                                                         room=self.deck.current.title)
