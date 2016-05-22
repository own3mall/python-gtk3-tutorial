#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class CellRendererToggle(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.connect("destroy", Gtk.main_quit)

        self.liststore = Gtk.ListStore(str, bool)
        self.liststore.append(["Ethernet", True])
        self.liststore.append(["Wireless", True])
        self.liststore.append(["Bluetooth", False])
        self.liststore.append(["3g Mobile", True])

        treeview = Gtk.TreeView()
        treeview.set_model(self.liststore)
        self.add(treeview)

        cellrenderertext = Gtk.CellRendererText()

        cellrenderertoggle = Gtk.CellRendererToggle()
        cellrenderertoggle.connect("toggled", self.on_cell_toggled)

        treeviewcolumn = Gtk.TreeViewColumn("Connection Type")
        treeviewcolumn.pack_start(cellrenderertext, False)
        treeviewcolumn.add_attribute(cellrenderertext, "text", 0)
        treeview.append_column(treeviewcolumn)

        treeviewcolumn = Gtk.TreeViewColumn("Status")
        treeviewcolumn.pack_start(cellrenderertoggle, False)
        treeviewcolumn.add_attribute(cellrenderertoggle, "active", 1)
        treeview.append_column(treeviewcolumn)

    def on_cell_toggled(self, cellrenderertoggle, treepath):
        self.liststore[treepath][1] = not self.liststore[treepath][1]

window = CellRendererToggle()
window.show_all()

Gtk.main()
