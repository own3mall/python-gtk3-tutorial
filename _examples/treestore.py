#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class TreeStore(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(200, -1)
        self.connect("destroy", Gtk.main_quit)

        treestore = Gtk.TreeStore(str)
        dog = treestore.append(None, ["Dog"])
        treestore.append(dog, ["Fido"])
        treestore.append(dog, ["Spot"])
        cat = treestore.append(None, ["Cat"])
        treestore.append(cat, ["Ginger"])
        rabbit = treestore.append(None, ["Rabbit"])
        treestore.append(rabbit, ["Twitch"])
        treestore.append(rabbit, ["Floppy"])

        treeview = Gtk.TreeView()
        treeview.set_model(treestore)
        self.add(treeview)

        cellrenderertext = Gtk.CellRendererText()

        treeviewcolumn = Gtk.TreeViewColumn("Pet Names")
        treeview.append_column(treeviewcolumn)
        treeviewcolumn.pack_start(cellrenderertext, True)
        treeviewcolumn.add_attribute(cellrenderertext, "text", 0)

window = TreeStore()
window.show_all()

Gtk.main()
