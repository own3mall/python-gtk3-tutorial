#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ColorChooserWidget(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title('ColorChooserWidget')
        self.set_border_width(5)
        self.connect('destroy', Gtk.main_quit)

        colorchooserwidget = Gtk.ColorChooserWidget()
        colorchooserwidget.connect('color-activated', self.on_color_activated)
        self.add(colorchooserwidget)

    def on_color_activated(self, colorchooserwidget, color):
        red = (color.red * 255)
        green = (color.green * 255)
        blue = (color.blue * 255)

        print('Hex: #%02x%02x%02x' % (red, green, blue))

window = ColorChooserWidget()
window.show_all()

Gtk.main()
