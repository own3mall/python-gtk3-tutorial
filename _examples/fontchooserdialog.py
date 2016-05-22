#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

fontchooserdialog = Gtk.FontChooserDialog()
fontchooserdialog.set_title("FontChooserDialog")

response = fontchooserdialog.run()

if response == Gtk.ResponseType.OK:
    print("Font selected: %s" % fontchooserdialog.get_font())

fontchooserdialog.destroy()
