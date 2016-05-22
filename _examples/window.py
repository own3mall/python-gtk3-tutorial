#/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("Window")
        self.connect("destroy", Gtk.main_quit)

window = Window()
window.show()

Gtk.main()
