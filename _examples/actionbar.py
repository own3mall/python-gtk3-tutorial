#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ActionBar(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("ActionBar")
        self.set_default_size(200, 200)
        self.connect("destroy", Gtk.main_quit)

        grid = Gtk.Grid()
        self.add(grid)

        label = Gtk.Label()
        label.set_vexpand(True)
        grid.attach(label, 0, 0, 1, 1)

        actionbar = Gtk.ActionBar()
        actionbar.set_hexpand(True)
        grid.attach(actionbar, 0, 1, 1, 1)

        button = Gtk.Button("Cut")
        actionbar.pack_start(button)
        button = Gtk.Button("Copy")
        actionbar.pack_start(button)
        button = Gtk.Button("Paste")
        actionbar.pack_end(button)

    def run(self):
        self.show_all()

window = ActionBar()
window.run()

Gtk.main()
