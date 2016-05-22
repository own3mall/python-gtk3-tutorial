#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Paned(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title('Paned')
        self.set_default_size(400, 200)
        self.connect('destroy', Gtk.main_quit)

        hpaned = Gtk.Paned()
        hpaned.set_position(150)
        self.add(hpaned)

        label = Gtk.Label(label='Left Pane')
        hpaned.add1(label)

        vpaned = Gtk.Paned(orientation=Gtk.Orientation.VERTICAL)
        vpaned.set_position(75)
        hpaned.add2(vpaned)

        label = Gtk.Label(label='Top Right Pane')
        vpaned.add1(label)

        label = Gtk.Label(label='Bottom Right Pane')
        vpaned.add2(label)

window = Paned()
window.show_all()

Gtk.main()
