#/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Box(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("Box")
        self.set_default_size(200, 200)
        self.connect("destroy", Gtk.main_quit)

        hbox = Gtk.Box()
        hbox.set_orientation(Gtk.Orientation.HORIZONTAL)
        hbox.set_spacing(5)
        self.add(hbox)

        label = Gtk.Label(label="Label 1")
        hbox.pack_start(label, True, True, 0)
        label = Gtk.Label(label="Label 2")
        hbox.pack_start(label, True, True, 0)

        vbox = Gtk.Box()
        vbox.set_orientation(Gtk.Orientation.VERTICAL)
        vbox.set_spacing(5)
        hbox.add(vbox)

        label = Gtk.Label(label="Label 3")
        vbox.pack_start(label, True, True, 0)
        label = Gtk.Label(label="Label 4")
        vbox.pack_start(label, True, True, 0)

window = Box()
window.show_all()

Gtk.main()
