#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class FileFilter(Gtk.FileChooserDialog):
    def __init__(self):
        Gtk.FileChooserDialog.__init__(self)
        self.set_title("FileFilter")
        self.add_button("_Cancel", Gtk.ResponseType.CLOSE)
        self.add_button("_Open", Gtk.ResponseType.OK)
        self.connect("response", self.on_response)

        filefilter = Gtk.FileFilter()
        filefilter.set_name("All Items")
        filefilter.add_pattern("*")
        self.add_filter(filefilter)

        filefilter = Gtk.FileFilter()
        filefilter.set_name("Audio")
        filefilter.add_mime_type("audio/flac")
        filefilter.add_mime_type("audio/ogg")
        self.add_filter(filefilter)

        filefilter = Gtk.FileFilter()
        filefilter.set_name("Images")
        filefilter.add_pattern("*.png")
        filefilter.add_pattern("*.jpg")
        filefilter.add_pattern("*.bmp")
        self.add_filter(filefilter)

    def on_response(self, filechooserdialog, response):
        filechooserdialog.destroy()

dialog = FileFilter()
dialog.run()
