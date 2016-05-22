#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Spinner(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(200, 200)
        self.connect("destroy", Gtk.main_quit)

        grid = Gtk.Grid()
        grid.set_row_spacing(5)
        grid.set_column_spacing(5)
        self.add(grid)

        self.spinner = Gtk.Spinner()
        self.spinner.set_vexpand(True)
        self.spinner.set_hexpand(True)
        grid.attach(self.spinner, 0, 0, 2, 1)

        buttonStart = Gtk.Button("Start")
        buttonStart.connect("clicked", self.on_start_clicked)
        grid.attach(buttonStart, 0, 1, 1, 1)

        buttonStop = Gtk.Button("Stop")
        buttonStop.connect("clicked", self.on_stop_clicked)
        grid.attach(buttonStop, 1, 1, 1, 1)

    def on_start_clicked(self, button):
        self.spinner.start()

    def on_stop_clicked(self, button):
        self.spinner.stop()

window = Spinner()
window.show_all()

Gtk.main()
