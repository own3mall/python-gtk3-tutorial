#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk

class SearchBar(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(250, -1)
        self.set_title("SearchBar")
        self.connect("key-press-event", self.on_key_event)
        self.connect("destroy", Gtk.main_quit)

        grid = Gtk.Grid()
        self.add(grid)

        label = Gtk.Label("Press Control+F to initiate find")
        grid.attach(label, 0, 0, 1, 1)

        self.searchbar = Gtk.SearchBar()
        grid.attach(self.searchbar, 0, 1, 1, 1)

        searchentry = Gtk.SearchEntry()
        self.searchbar.connect_entry(searchentry)
        self.searchbar.add(searchentry)

    def on_key_event(self, widget, event):
        shortcut = Gtk.accelerator_get_label(event.keyval, event.state)

        if shortcut in ("Ctrl+F", "Ctrl+Mod2+F"):
            if self.searchbar.get_search_mode():
                self.searchbar.set_search_mode(False)
            else:
                self.searchbar.set_search_mode(True)

window = SearchBar()
window.show_all()

Gtk.main()
