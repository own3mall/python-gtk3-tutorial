#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Grid(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("Grid")
        self.connect("destroy", Gtk.main_quit)

        grid = Gtk.Grid()
        grid.set_row_spacing(5)
        grid.set_column_spacing(5)
        self.add(grid)

        button = Gtk.Button(label="Button 1")
        grid.attach(button, 0, 0, 1, 2)
        button = Gtk.Button(label="Button 2")
        grid.attach(button, 1, 0, 1, 1)
        button = Gtk.Button(label="Button 3")
        grid.attach(button, 2, 0, 1, 1)
        button = Gtk.Button(label="Button 4")
        grid.attach(button, 1, 1, 2, 1)

window = Grid()
window.show_all()

Gtk.main()
