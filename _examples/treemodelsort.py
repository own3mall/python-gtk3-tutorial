#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class TreeModelSort(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(200, -1)
        self.connect("destroy", Gtk.main_quit)

        liststore = Gtk.ListStore(str)
        liststore.append(["Mark"])
        liststore.append(["Chris"])
        liststore.append(["Tim"])
        liststore.append(["David"])
        liststore.append(["Keith"])

        treemodelsort = Gtk.TreeModelSort(liststore)
        treemodelsort.set_sort_column_id(0, Gtk.SortType.ASCENDING)

        treeview = Gtk.TreeView()
        treeview.set_model(treemodelsort)
        self.add(treeview)

        cellrenderertext = Gtk.CellRendererText()
        treeviewcolumn = Gtk.TreeViewColumn("Name", cellrenderertext, text=0)
        treeview.append_column(treeviewcolumn)

window = TreeModelSort()
window.show_all()

Gtk.main()
