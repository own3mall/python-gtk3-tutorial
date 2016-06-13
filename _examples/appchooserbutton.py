#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class AppChooserButton(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("AppChooserButton")
        self.set_default_size(200, -1)
        self.connect("destroy", Gtk.main_quit)

        appchooserbutton = Gtk.AppChooserButton(content_type="audio/flac")
        appchooserbutton.set_show_dialog_item(True)
        appchooserbutton.connect("changed", self.on_item_changed)
        self.add(appchooserbutton)

    def on_item_changed(self, appchooserbutton):
        app_info = appchooserbutton.get_app_info()
        name = app_info.get_display_name()
        description = app_info.get_description()

        print("Name:\t\t%s" % (name))
        print("Description:\t%s" % (description))

window = AppChooserButton()
window.show_all()

Gtk.main()
