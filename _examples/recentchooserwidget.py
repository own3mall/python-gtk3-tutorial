#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class RecentChooserWidget(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title('RecentChooserWidget')
        self.set_default_size(300, 250)
        self.set_border_width(5)
        self.connect('destroy', Gtk.main_quit)

        recentchooserwidget = Gtk.RecentChooserWidget()
        recentchooserwidget.connect('item-activated', self.on_item_activated)
        self.add(recentchooserwidget)

    def on_item_activated(self, recentchooserwidget):
        item = recentchooserwidget.get_current_item()

        if item:
            print('Item selected:')
            print('Name:\t %s' % (item.get_display_name()))
            print('URI:\t %s' % (item.get_uri()))

window = RecentChooserWidget()
window.show_all()

Gtk.main()
