#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import random

class LevelBar(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(150, -1)
        self.connect("destroy", Gtk.main_quit)

        levelbar = Gtk.LevelBar()
        levelbar.set_min_value(0)
        levelbar.set_max_value(10)
        levelbar.set_value(random.randint(0, 10))
        self.add(levelbar)

window = LevelBar()
window.show_all()

Gtk.main()
