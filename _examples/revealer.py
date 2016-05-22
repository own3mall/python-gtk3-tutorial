#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Revealer(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.connect("destroy", Gtk.main_quit)

        grid = Gtk.Grid()
        self.add(grid)

        self.revealer = Gtk.Revealer()
        self.revealer.set_reveal_child(True)
        grid.attach(self.revealer, 0, 0, 1, 1)

        label = Gtk.Label("Label in a Revealer")
        self.revealer.add(label)

        button = Gtk.Button("Reveal")
        button.connect("clicked", self.on_reveal_clicked)
        grid.attach(button, 0, 1, 1, 1)

    def on_reveal_clicked(self, button):
        reveal = self.revealer.get_reveal_child()
        self.revealer.set_reveal_child(not reveal)

window = Revealer()
window.show_all()

Gtk.main()
