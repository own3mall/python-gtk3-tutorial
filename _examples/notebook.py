#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Notebook(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title('Notebook')
        self.set_default_size(300, 200)
        self.connect('destroy', Gtk.main_quit)

        notebook = Gtk.Notebook()
        self.add(notebook)

        for page in range(1, 4):
            label1 = Gtk.Label('Notebook')
            label2 = Gtk.Label()
            label2.set_text('Page %i' % (page))
            notebook.append_page(label1, label2)
            notebook.set_tab_reorderable(label1, True)

window = Notebook()
window.show_all()

Gtk.main()
