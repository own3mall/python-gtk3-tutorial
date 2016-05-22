#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Handler:
    def on_button_clicked(self, button):
        print("Button clicked!")

    def on_togglebutton_toggled(self, togglebutton):
        print("ToggleButton toggled!")

    def on_exit_application(self, *args):
        Gtk.main_quit()

builder = Gtk.Builder()
builder.add_from_file("builder.glade")
builder.connect_signals(Handler())

window = builder.get_object("window1")
window.show_all()

Gtk.main()
