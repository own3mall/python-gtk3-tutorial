#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class RecentChooserDialog(Gtk.RecentChooserDialog):
    def __init__(self):
        Gtk.RecentChooserDialog.__init__(self)
        self.set_title('RecentChooserDialog')
        self.set_default_size(250, -1)
        self.add_button('Cancel', Gtk.ResponseType.CANCEL)
        self.add_button('OK', Gtk.ResponseType.OK)
        self.set_default_response(Gtk.ResponseType.OK)
        self.connect('response', self.on_response)

    def on_response(self, recentchooserdialog, response):
        if response == Gtk.ResponseType.OK:
            item = recentchooserdialog.get_current_item()

            if item:
                print('Item selected:')
                print('Name:\t %s' % (item.get_display_name()))
                print('URI:\t %s' % (item.get_uri()))

dialog = RecentChooserDialog()
dialog.run()
dialog.destroy()
