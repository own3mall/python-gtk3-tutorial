#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def font_chooser(fontchooserwidget, font):
    print("Font selected: %s" % font)

window = Gtk.Window()
window.set_title("FontChooserWidget")
window.connect("destroy", Gtk.main_quit)

fontchooserwidget = Gtk.FontChooserWidget()
fontchooserwidget.connect("font-activated", font_chooser)
window.add(fontchooserwidget)

window.show_all()

Gtk.main()
