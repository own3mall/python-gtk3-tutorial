#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GdkX11
import cairo

def expose(drawingarea, context):
    pass

window = Gtk.Window()
window.set_title("DrawingArea")
window.set_default_size(600, 400)
window.connect("destroy", Gtk.main_quit)

drawingarea = Gtk.DrawingArea()

drawingarea.connect("draw", expose)
window.add(drawingarea)
window.show_all()

Gtk.main()
