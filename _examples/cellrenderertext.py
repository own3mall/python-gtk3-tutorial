#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class CellRendererText(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("CellRendererText")
        self.connect("destroy", Gtk.main_quit)

        self.liststore = Gtk.ListStore(str, str)
        self.liststore.append(["Fedora", "http://fedoraproject.org/"])
        self.liststore.append(["Ubuntu", "http://www.ubuntu.com/"])
        self.liststore.append(["Slackware", "http://www.slackware.com/"])

        treeview = Gtk.TreeView()
        treeview.set_model(self.liststore)
        self.add(treeview)

        cellrenderertext = Gtk.CellRendererText()

        treeviewcolumn = Gtk.TreeViewColumn("Distribution")
        treeviewcolumn.pack_start(cellrenderertext, True)
        treeviewcolumn.add_attribute(cellrenderertext, "text", 0)
        treeview.append_column(treeviewcolumn)

        cellrenderertext = Gtk.CellRendererText()
        cellrenderertext.set_property("editable", True)
        cellrenderertext.connect("edited", self.on_cell_edited)

        treeviewcolumn = Gtk.TreeViewColumn("Website")
        treeviewcolumn.pack_start(cellrenderertext, True)
        treeviewcolumn.add_attribute(cellrenderertext, "text", 1)
        treeview.append_column(treeviewcolumn)

    def on_cell_edited(self, cellrenderertext, treepath, text):
        self.liststore[treepath][1] = text

window = CellRendererText()
window.show_all()

Gtk.main()
