#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MenuButton(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.connect("destroy", Gtk.main_quit)

        menubutton = Gtk.MenuButton("MenuButton")
        self.add(menubutton)

        menu = Gtk.Menu()
        menubutton.set_popup(menu)

        for count in range(1, 6):
            menuitem = Gtk.MenuItem("Item %i" % (count))
            menuitem.connect("activate", self.on_menuitem_activated)
            menu.append(menuitem)

        menu.show_all()

    def on_menuitem_activated(self, menuitem):
        print("%s Activated" % (menuitem.get_label()))

window = MenuButton()
window.show_all()

Gtk.main()
