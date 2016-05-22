#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class LinkButton(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__()
        self.connect("destroy", Gtk.main_quit)

        linkbutton = Gtk.LinkButton(uri="https://programmica.com/",
                                    label="Programmica")
        self.add(linkbutton)

window = LinkButton()
window.show_all()

Gtk.main()
