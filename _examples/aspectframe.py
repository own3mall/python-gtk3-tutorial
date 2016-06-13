#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class AspectFrame(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("AspectFrame")
        self.set_default_size(200, 200)
        self.set_border_width(5)
        self.connect("destroy", Gtk.main_quit)

        frame = Gtk.AspectFrame(label="AspectFrame",
                                xalign=0.5,
                                yalign=0.5,
                                ratio=1,
                                obey_child=False)
        self.add(frame)

        label = Gtk.Label("Label in an AspectFrame")
        frame.add(label)

window = AspectFrame()
window.show_all()

Gtk.main()
