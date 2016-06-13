#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class CheckButton(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("CheckButton")
        self.connect("destroy", Gtk.main_quit)

        checkbutton = Gtk.CheckButton(label="CheckButton")
        checkbutton.connect("toggled", self.on_check_button_toggled)
        self.add(checkbutton)

    def on_check_button_toggled(self, checkbutton):
        if checkbutton.get_active():
            print("CheckButton toggled on!")
        else:
            print("CheckButton toggled off!")

window = CheckButton()
window.show_all()

Gtk.main()
