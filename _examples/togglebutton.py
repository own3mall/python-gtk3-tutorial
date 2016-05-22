#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ToggleButton(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("ToggleButton")
        self.connect("destroy", Gtk.main_quit)
        
        grid = Gtk.Grid()
        self.add(grid)
        
        togglebutton1 = Gtk.ToggleButton("ToggleButton 1")
        togglebutton1.connect("toggled", self.on_toggle_button_toggled)
        grid.attach(togglebutton1, 0, 0, 1, 1)
        
        togglebutton2 = Gtk.ToggleButton("ToggleButton 2")
        togglebutton2.connect("toggled", self.on_toggle_button_toggled)
        grid.attach(togglebutton2, 0, 1, 1, 1)
        
    def on_toggle_button_toggled(self, togglebutton):
        if togglebutton.get_active():
            print("%s has been toggled on" % (togglebutton.get_label()))
        else:
            print("%s has been toggled off" % (togglebutton.get_label()))

window = ToggleButton()
window.show_all()

Gtk.main()
