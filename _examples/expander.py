#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Expander(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("Expander")
        self.set_default_size(200, -1)
        self.connect("destroy", Gtk.main_quit)

        expander = Gtk.Expander(label="Expander")
        expander.set_resize_toplevel(True)
        self.add(expander)

        label = Gtk.Label("Label in an Expander")
        label.set_size_request(200, 200)
        expander.add(label)

window = Expander()
window.show_all()

Gtk.main()
