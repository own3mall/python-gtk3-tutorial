#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GdkPixbuf

distributions = ["fedora", "mandriva", "zenwalk", "knoppix", "debian"]

class IconView(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("IconView")
        self.connect("destroy", Gtk.main_quit)

        self.liststore = Gtk.ListStore(str, GdkPixbuf.Pixbuf, str)

        iconview = Gtk.IconView()
        iconview.set_model(self.liststore)
        iconview.set_text_column(0)
        iconview.set_pixbuf_column(1)
        iconview.set_tooltip_column(2)
        iconview.connect("item-activated", self.on_iconview_activated)
        self.add(iconview)

        image = Gtk.Image()

        for item in distributions:
            path = "../_resources/%s.ico" % (item)
            image.set_from_file(path)
            pixbuf = image.get_pixbuf()

            name = item.capitalize()
            tooltip = "%s tooltip example" % (name)

            self.liststore.append([name, pixbuf, tooltip])

    def on_iconview_activated(self, iconview, treepath):
        print("Selected item: %s" % (self.liststore[treepath][0]))

window = IconView()
window.show_all()

Gtk.main()
