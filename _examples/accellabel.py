#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class AccelLabel(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("AccelLabel")
        self.set_default_size(200, -1)
        self.connect("destroy", Gtk.main_quit)

        grid = Gtk.Grid()
        self.add(grid)

        accelgroup = Gtk.AccelGroup()
        self.add_accel_group(accelgroup)

        accellabel = Gtk.AccelLabel("Button accelerator:")
        accellabel.set_hexpand(True)
        grid.attach(accellabel, 0, 0, 2, 1)

        button = Gtk.Button("Save")
        button.add_accelerator("clicked",
                               accelgroup,
                               Gdk.keyval_from_name("s"),
                               Gdk.ModifierType.CONTROL_MASK,
                               Gtk.AccelFlags.VISIBLE)
        button.connect("clicked", self.on_button_clicked)
        accellabel.set_accel_widget(button)
        grid.attach(button, 0, 1, 2, 1)

    def on_button_clicked(self, button):
        print("Save button clicked")

window = AccelLabel()
window.show_all()

Gtk.main()
