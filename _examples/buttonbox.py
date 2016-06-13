#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ButtonBox(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("ButtonBox")
        self.connect("destroy", Gtk.main_quit)

        buttonbox = Gtk.ButtonBox()
        buttonbox.set_orientation(Gtk.Orientation.HORIZONTAL)
        buttonbox.set_spacing(2)
        self.add(buttonbox)

        button = Gtk.Button(label="Sparrow")
        buttonbox.add(button)
        button = Gtk.Button(label="Wren")
        buttonbox.add(button)
        button = Gtk.Button(label="Great Spotted Woodpecker")
        buttonbox.add(button)

window = ButtonBox()
window.show_all()

Gtk.main()
