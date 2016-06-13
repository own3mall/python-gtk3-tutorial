#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def file_changed(filechooserbutton):
    print("File selected: %s" % filechooserbutton.get_filename())

window = Gtk.Window()
window.set_title("FileChooserButton")
window.set_default_size(150, -1)
window.connect("destroy", Gtk.main_quit)

filechooserbutton = Gtk.FileChooserButton(title="FileChooserButton")
filechooserbutton.connect("file-set", file_changed)
window.add(filechooserbutton)

window.show_all()

Gtk.main()
