#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Viewport(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(-1, 200)
        self.connect("destroy", Gtk.main_quit)

        scrolledwindow = Gtk.ScrolledWindow()
        self.add(scrolledwindow)

        hadjustment = Gtk.Adjustment()
        vadjustment = Gtk.Adjustment()

        viewport = Gtk.Viewport(hadjustment, vadjustment)
        scrolledwindow.add(viewport)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        viewport.add(box)

        for i in range(1, 16):
            button = Gtk.Button(label="Button %s" % i)
            box.pack_start(button, True, True, 0)

window = Viewport()
window.show_all()

Gtk.main()
