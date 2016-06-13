#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class CellRendererSpin(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("CellRendererSpin")
        self.set_default_size(150, -1)
        self.connect("destroy", Gtk.main_quit)

        self.liststore = Gtk.ListStore(str, int)
        self.liststore.append(["Oranges", 5])
        self.liststore.append(["Bananas", 2])
        self.liststore.append(["Apples", 3])

        treeview = Gtk.TreeView()
        treeview.set_model(self.liststore)
        self.add(treeview)

        cellrenderertext = Gtk.CellRendererText()

        adjustment = Gtk.Adjustment(0, 0, 10, 1, 1, 0)
        cellrendererspin = Gtk.CellRendererSpin()
        cellrendererspin.set_property("editable", True)
        cellrendererspin.set_property("adjustment", adjustment)
        cellrendererspin.connect("edited", self.on_cell_edited)

        treeviewcolumn = Gtk.TreeViewColumn("Fruit")
        treeview.append_column(treeviewcolumn)
        treeviewcolumn.pack_start(cellrenderertext, False)
        treeviewcolumn.add_attribute(cellrenderertext, "text", 0)

        treeviewcolumn = Gtk.TreeViewColumn("Quantity")
        treeview.append_column(treeviewcolumn)
        treeviewcolumn.pack_start(cellrendererspin, False)
        treeviewcolumn.add_attribute(cellrendererspin, "text", 1)

    def on_cell_edited(self, cellrendererspin, treepath, value):
        self.liststore[treepath][1] = int(value)

window = CellRendererSpin()
window.show_all()

Gtk.main()
