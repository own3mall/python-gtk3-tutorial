#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def color_activated():
    color = colorchooserdialog.get_rgba()

    red = (color.red * 255)
    green = (color.green * 255)
    blue = (color.blue * 255)

    print('Hex: #%02x%02x%02x' % (red, green, blue))

colorchooserdialog = Gtk.ColorChooserDialog()

if colorchooserdialog.run() == Gtk.ResponseType.OK:
    color_activated()

colorchooserdialog.destroy()
