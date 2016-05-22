#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

filechooserdialog = Gtk.FileChooserDialog()
filechooserdialog.set_title("FileChooserDialog")
filechooserdialog.add_button("_Open", Gtk.ResponseType.OK)
filechooserdialog.add_button("_Cancel", Gtk.ResponseType.CANCEL)
filechooserdialog.set_default_response(Gtk.ResponseType.OK)

response = filechooserdialog.run()

if response == Gtk.ResponseType.OK:
    print("File selected: %s" % filechooserdialog.get_filename())

filechooserdialog.destroy()
