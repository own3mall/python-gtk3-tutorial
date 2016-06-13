#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def font_changed(fontbutton):
    print("Font selected: %s" % fontbutton.get_font_name())

window = Gtk.Window()
window.set_title("FontButton")
window.set_default_size(150, -1)
window.connect("destroy", Gtk.main_quit)

fontbutton = Gtk.FontButton(title="FontButton")
fontbutton.connect("font-set", font_changed)
window.add(fontbutton)

window.show_all()

Gtk.main()
