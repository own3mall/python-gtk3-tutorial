#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class HelloWorld(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("Hello World")
        self.connect("destroy", Gtk.main_quit)

        button = Gtk.Button("Click Here")
        button.connect("clicked", self.on_button_clicked)
        self.add(button)

    def on_button_clicked(self, button):
        print("Hello, World!")

window = HelloWorld()
window.show_all()

Gtk.main()
