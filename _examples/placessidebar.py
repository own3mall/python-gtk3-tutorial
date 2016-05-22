#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gio

class PlacesSidebar(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.connect("destroy", Gtk.main_quit)

        placessidebar = Gtk.PlacesSidebar()
        placessidebar.connect("open-location", self.on_open_location)
        self.add(placessidebar)

    def on_open_location(self, placessidebar, location, flags):
        location = placessidebar.get_location()

        print("Opened URI: %s" % (GLocalFile.get_uri(location)))

window = PlacesSidebar()
window.show_all()

Gtk.main()
