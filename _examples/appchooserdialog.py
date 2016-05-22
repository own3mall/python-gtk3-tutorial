#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class AppChooserDialog(Gtk.AppChooserDialog):
    def __init__(self):
        Gtk.AppChooserDialog.__init__(self, content_type="image/png")
        self.set_title("AppChooserDialog")
        self.connect("response", self.on_response)

    def on_response(self, dialog, response):
        if response == Gtk.ResponseType.OK:
            app_info = appchooserdialog.get_app_info()
            name = app_info.get_display_name()
            description = app_info.get_description()

            print("Name:\t\t%s" % (name))
            print("Description:\t%s" % (description))

appchooserdialog = AppChooserDialog()
appchooserdialog.run()
