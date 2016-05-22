#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class VolumeButton(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(200, 200)
        self.connect("destroy", Gtk.main_quit)

        grid = Gtk.Grid()
        self.add(grid)

        volumebutton = Gtk.VolumeButton()
        volumebutton.connect("value-changed", self.on_volume_button_changed)
        grid.attach(volumebutton, 0, 0, 1, 1)

    def on_volume_button_changed(self, volumebutton, value):
        print("VolumeButton value: %0.2f" % (value))

window = VolumeButton()
window.show_all()

Gtk.main()
