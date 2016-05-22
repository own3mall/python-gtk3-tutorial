#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GdkPixbuf

class AboutDialog(Gtk.AboutDialog):
    def __init__(self):
        logo = GdkPixbuf.Pixbuf.new_from_file_at_size("../_resources/gtk.png", 64, 64)

        Gtk.AboutDialog.__init__(self)
        self.set_title("AboutDialog")
        self.set_name("Programmica")
        self.set_version("1.0")
        self.set_comments("Programming, system and network administration resources")
        self.set_website("https://programmica.com/")
        self.set_website_label("Programmica Website")
        self.set_authors(["Andrew Steele"])
        self.set_logo(logo)
        self.connect("response", self.on_response)

    def on_response(self, dialog, response):
        self.destroy()

aboutdialog = AboutDialog()
aboutdialog.run()
