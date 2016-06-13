#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Fixed(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("Fixed")
        self.set_default_size(200, 200)
        self.connect("destroy", Gtk.main_quit)

        fixed = Gtk.Fixed()
        self.add(fixed)

        button = Gtk.Button(label="Button 1")
        fixed.put(button, 40, 60)
        button = Gtk.Button(label="Button 2")
        fixed.put(button, 120, 95)

window = Fixed()
window.show_all()

Gtk.main()
