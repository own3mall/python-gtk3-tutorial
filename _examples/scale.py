#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import random

class Scale(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(200, 200)
        self.connect("destroy", Gtk.main_quit)

        grid = Gtk.Grid()
        self.add(grid)

        value = random.randint(0, 100)
        adjustment = Gtk.Adjustment(value, 0, 100, 1, 10, 0)

        self.scale = Gtk.Scale(orientation=Gtk.Orientation.VERTICAL, adjustment=adjustment)
        self.scale.set_value_pos(Gtk.PositionType.BOTTOM)
        self.scale.set_vexpand(True)
        self.scale.set_hexpand(True)
        grid.attach(self.scale, 0, 0, 2, 1)

        buttonAdd = Gtk.Button(label="Add Mark")
        buttonAdd.connect("clicked", self.on_add_mark_clicked)
        grid.attach(buttonAdd, 0, 1, 1, 1)

        buttonClear = Gtk.Button(label="Clear Marks")
        buttonClear.connect("clicked", self.on_clear_marks_clicked)
        grid.attach(buttonClear, 1, 1, 1, 1)

        radiobuttonVertical = Gtk.RadioButton(group=None, label="Vertical Scale")
        radiobuttonVertical.orientation = 0
        radiobuttonVertical.connect("toggled", self.on_orientation_clicked)
        grid.attach(radiobuttonVertical, 0, 3, 2, 1)

        radiobuttonHorizontal = Gtk.RadioButton(group=radiobuttonVertical, label="Horizontal Scale")
        radiobuttonHorizontal.orientation = 1
        radiobuttonHorizontal.connect("toggled", self.on_orientation_clicked)
        grid.attach(radiobuttonHorizontal, 0, 2, 2, 1)

    def on_add_mark_clicked(self, button):
        value = self.scale.get_value()
        self.scale.add_mark(value, Gtk.PositionType.LEFT, "Mark")

    def on_clear_marks_clicked(self, button):
        self.scale.clear_marks()

    def on_orientation_clicked(self, radiobutton):
        if radiobutton.orientation == 0:
            self.scale.set_orientation(Gtk.Orientation.VERTICAL)
        else:
            self.scale.set_orientation(Gtk.Orientation.HORIZONTAL)

window = Scale()
window.show_all()

Gtk.main()
