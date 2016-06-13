#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Entry(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("Entry")
        self.connect("destroy", Gtk.main_quit)

        entry = Gtk.Entry()
        entry.set_placeholder_text("Entry text here...")
        entry.connect("activate", self.on_entry_activated)
        self.add(entry)

    def on_entry_activated(self, entry):
        print("Entry text: %s" % (entry.get_text()))

window = Entry()
window.show_all()

Gtk.main()
