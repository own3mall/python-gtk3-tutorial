#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class AppChooserWidget(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("AppChooserWidget")
        self.connect("destroy", Gtk.main_quit)

        appchooserwidget = Gtk.AppChooserWidget(content_type="video/webm")
        appchooserwidget.connect("application-activated", self.on_application_activated)
        self.add(appchooserwidget)

    def on_application_activated(self, appchooserwidget, desktopappinfo):
        app_info = appchooserwidget.get_app_info()
        name = app_info.get_display_name()
        description = app_info.get_description()

        print("Name:\t\t%s" % (name))
        print("Description:\t%s" % (description))

window = AppChooserWidget()
window.show_all()

Gtk.main()
