#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class HeaderBar(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("HeaderBar")
        self.set_default_size(-1, 200)
        self.connect("destroy", Gtk.main_quit)

        headerbar = Gtk.HeaderBar()
        headerbar.set_title("HeaderBar Example")
        headerbar.set_subtitle("HeaderBar Subtitle")
        headerbar.set_show_close_button(True)
        self.set_titlebar(headerbar)

        button = Gtk.Button("Open")
        headerbar.pack_start(button)

window = HeaderBar()
window.show_all()

Gtk.main()
