#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GdkPixbuf

class CellRendererPixbuf(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("CellRendererPixbuf")
        self.connect("destroy", Gtk.main_quit)

        liststore = Gtk.ListStore(str, GdkPixbuf.Pixbuf)

        icon = GdkPixbuf.Pixbuf.new_from_file_at_size("../_resources/fedora.ico", 16, 16)
        liststore.append(["Fedora", icon])
        icon = GdkPixbuf.Pixbuf.new_from_file_at_size("../_resources/opensuse.ico", 16, 16)
        liststore.append(["OpenSuSE", icon])
        icon = GdkPixbuf.Pixbuf.new_from_file_at_size("../_resources/gentoo.ico", 16, 16)
        liststore.append(["Gentoo", icon])

        treeview = Gtk.TreeView()
        treeview.set_model(liststore)
        self.add(treeview)

        cellrenderertext = Gtk.CellRendererText()

        treeviewcolumn = Gtk.TreeViewColumn("Distribution")
        treeview.append_column(treeviewcolumn)
        treeviewcolumn.pack_start(cellrenderertext, True)
        treeviewcolumn.add_attribute(cellrenderertext, "text", 0)

        cellrendererpixbuf = Gtk.CellRendererPixbuf()

        treeviewcolumn = Gtk.TreeViewColumn("Logo")
        treeview.append_column(treeviewcolumn)
        treeviewcolumn.pack_start(cellrendererpixbuf, False)
        treeviewcolumn.add_attribute(cellrendererpixbuf, "pixbuf", 1)

window = CellRendererPixbuf()
window.show_all()

Gtk.main()
