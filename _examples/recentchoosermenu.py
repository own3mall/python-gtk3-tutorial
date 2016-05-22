#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class RecentChooserMenu(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title('RecentChooserMenu')
        self.connect('destroy', Gtk.main_quit)

        menubar = Gtk.MenuBar()
        self.add(menubar)

        menuitem = Gtk.MenuItem('Recent Items')
        menubar.append(menuitem)

        recentchoosermenu = Gtk.RecentChooserMenu()
        recentchoosermenu.connect('item-activated', self.on_item_activated)
        menuitem.set_submenu(recentchoosermenu)

    def on_item_activated(self, recentchoosermenu):
        item = recentchoosermenu.get_current_item()

        if item:
            print("Item selected:")
            print("Name:\t %s" % (item.get_display_name()))
            print("URI:\t %s" % (item.get_uri()))

window = RecentChooserMenu()
window.show_all()

Gtk.main()
