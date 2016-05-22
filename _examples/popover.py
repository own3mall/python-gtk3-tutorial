#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Popover(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("Popover")
        self.set_default_size(250, 250)
        self.connect("destroy", Gtk.main_quit)
        
        box = Gtk.Box()
        box.set_orientation(Gtk.Orientation.VERTICAL)
        self.add(box)

        button = Gtk.Button("Popover Launcher")
        button.connect("clicked", self.on_popover_clicked)
        box.add(button)

        self.popover = Gtk.Popover()
        self.popover.set_position(Gtk.PositionType.RIGHT)
        self.popover.set_relative_to(button)

        box = Gtk.Box()
        box.set_spacing(5)
        box.set_orientation(Gtk.Orientation.VERTICAL)
        self.popover.add(box)

        label = Gtk.Label("A Label widget")
        box.add(label)

        checkbutton = Gtk.CheckButton("A CheckButton widget")
        box.add(checkbutton)
        
    def on_popover_clicked(self, button):
        self.popover.show_all()

window = Popover()
window.show_all()

Gtk.main()
