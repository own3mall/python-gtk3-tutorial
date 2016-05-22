#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Stack(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(400, 300)
        self.connect("destroy", Gtk.main_quit)

        grid = Gtk.Grid()
        self.add(grid)

        self.stack = Gtk.Stack()
        self.stack.set_vexpand(True)
        self.stack.set_hexpand(True)
        grid.attach(self.stack, 0, 0, 1, 1)

        buttonbox = Gtk.ButtonBox()
        buttonbox.set_layout(Gtk.ButtonBoxStyle.CENTER)
        grid.attach(buttonbox, 0, 1, 1, 1)

        for page in range(1, 4):
            label = Gtk.Label("Stack Content on Page %i" % (page))
            name = "label%i" % page
            self.stack.add_named(label, name)

            button = Gtk.Button("Page %i" % (page))
            button.connect("clicked", self.on_button_clicked, page)
            buttonbox.add(button)

    def on_button_clicked(self, button, page):
        name = "label%i" % page
        self.stack.set_visible_child_name(name)

window = Stack()
window.show_all()

Gtk.main()
