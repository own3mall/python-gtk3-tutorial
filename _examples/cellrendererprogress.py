#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GObject
import random

class CellRendererProgress(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("CellRendererProgress")
        self.set_default_size(200, 200)
        self.connect("destroy", Gtk.main_quit)

        self.liststore = Gtk.ListStore(str, int)
        self.liststore.append(["Downloading files", 0])
        self.liststore.append(["Parsing access logs", 0])
        self.liststore.append(["Compiling modules", 0])

        treeview = Gtk.TreeView()
        treeview.set_model(self.liststore)
        self.add(treeview)

        cellrenderertext = Gtk.CellRendererText()

        treeviewcolumn = Gtk.TreeViewColumn("Action")
        treeview.append_column(treeviewcolumn)
        treeviewcolumn.pack_start(cellrenderertext, False)
        treeviewcolumn.add_attribute(cellrenderertext, "text", 0)

        cellrendererprogress = Gtk.CellRendererProgress()

        treeviewcolumn = Gtk.TreeViewColumn("Status")
        treeview.append_column(treeviewcolumn)
        treeviewcolumn.pack_start(cellrendererprogress, True)
        treeviewcolumn.add_attribute(cellrendererprogress, "value", 1)

        GObject.timeout_add(250, self.on_pulse_progressbar)

    def on_pulse_progressbar(self):
        for item in self.liststore:
            if item[1] < 100:
                value = random.randint(0, 5)

                if value + item[1] > 100:
                    item[1] = 100
                else:
                    item[1] += value
            else:
                item[1] = 0

        return True

window = CellRendererProgress()
window.show_all()

Gtk.main()
