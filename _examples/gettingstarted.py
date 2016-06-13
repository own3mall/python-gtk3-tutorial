#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class GettingStarted:
    def __init__(self):
        window = Gtk.Window()
        window.set_title("Getting Started")
        window.connect("destroy", Gtk.main_quit)
        window.show()

GettingStarted()
Gtk.main()
