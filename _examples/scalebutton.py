#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ScaleButton(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(200, 200)
        self.connect("destroy", Gtk.main_quit)

        grid = Gtk.Grid()
        self.add(grid)

        scalebutton = Gtk.ScaleButton()
        scalebutton.set_icons(("gtk-go-down", "gtk-go-up"))
        scalebutton.connect("value-changed", self.on_scale_button_changed)
        grid.attach(scalebutton, 0, 0, 1, 1)

    def on_scale_button_changed(self, scalebutton, value):
        print("ScaleButton value: %0.2f" % (value))

window = ScaleButton()
window.show_all()

Gtk.main()
