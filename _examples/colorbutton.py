#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ColorButton(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title('ColorButton')
        self.set_default_size(200, -1)
        self.connect('destroy', Gtk.main_quit)

        colorbutton = Gtk.ColorButton()
        colorbutton.connect('color-set', self.on_color_set)
        self.add(colorbutton)

    def on_color_set(self, colorbutton):
        color = colorbutton.get_rgba()

        red = (color.red * 255)
        green = (color.green * 255)
        blue = (color.blue * 255)

        print('Hex: #%02x%02x%02x' % (red, green, blue))

window = ColorButton()
window.show_all()

Gtk.main()
