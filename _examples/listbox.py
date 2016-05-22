#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ListBox(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(200, -1)
        self.connect("destroy", Gtk.main_quit)

        listbox = Gtk.ListBox()
        listbox.connect("row-activated", self.on_row_activated)
        self.add(listbox)

        for count in range(0, 9):
            label = Gtk.Label("Row %i" % (count))
            listbox.add(label)

    def on_row_activated(self, listbox, listboxrow):
        print("Row %i activated" % (listboxrow.get_index()))

window = ListBox()
window.show_all()

Gtk.main()
