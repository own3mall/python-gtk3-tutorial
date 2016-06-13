#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Button(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("Button")
        self.connect("destroy", Gtk.main_quit)

        button = Gtk.Button(label="Button")
        button.connect("clicked", self.on_button_clicked)
        self.add(button)

    def on_button_clicked(self, button):
        print("Button has been clicked!")

window = Button()
window.show_all()

Gtk.main()
