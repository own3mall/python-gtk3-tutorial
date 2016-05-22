#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Statusbar(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.connect("destroy", Gtk.main_quit)

        grid = Gtk.Grid()
        grid.set_column_spacing(5)
        self.add(grid)

        buttonPush = Gtk.Button("Push")
        buttonPush.connect("clicked", self.on_push_clicked)
        grid.attach(buttonPush, 0, 0, 1, 1)

        buttonPop = Gtk.Button("Pop")
        buttonPop.connect("clicked", self.on_pop_clicked)
        grid.attach(buttonPop, 1, 0, 1, 1)

        buttonRemove = Gtk.Button("Remove All")
        buttonRemove.connect("clicked", self.on_remove_all_clicked)
        grid.attach(buttonRemove, 2, 0, 1, 1)

        self.statusbar = Gtk.Statusbar()
        self.context = self.statusbar.get_context_id("example")
        grid.attach(self.statusbar, 0, 1, 3, 1)

        self.count = 0

    def on_push_clicked(self, button):
        self.count += 1

        message = "Message number %i" % (self.count)
        self.statusbar.push(self.context, message)

    def on_pop_clicked(self, button):
        self.statusbar.pop(self.context)

    def on_remove_all_clicked(self, button):
        self.statusbar.remove_all(self.context)

window = Statusbar()
window.show_all()

Gtk.main()
