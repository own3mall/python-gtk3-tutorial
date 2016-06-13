#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Frame(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("Frame")
        self.set_default_size(200, 200)
        self.set_border_width(5)
        self.connect("destroy", Gtk.main_quit)

        frame = Gtk.Frame(label="Frame")
        self.add(frame)

        label = Gtk.Label("Label in a Frame")
        frame.add(label)

window = Frame()
window.show_all()

Gtk.main()
