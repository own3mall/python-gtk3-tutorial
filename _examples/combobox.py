#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ComboBox(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("ComboBox")
        self.set_default_size(150, -1)
        self.connect("destroy", Gtk.main_quit)

        liststore = Gtk.ListStore(str)

        for item in ["Debian", "Fedora", "Tiny Core", "Linux Mint", "Mageia"]:
            liststore.append([item])

        combobox = Gtk.ComboBox()
        combobox.set_model(liststore)
        combobox.set_active(0)
        combobox.connect("changed", self.on_combobox_changed)
        self.add(combobox)

        cellrenderertext = Gtk.CellRendererText()
        combobox.pack_start(cellrenderertext, True)
        combobox.add_attribute(cellrenderertext, "text", 0)

    def on_combobox_changed(self, combobox):
        treeiter = combobox.get_active_iter()
        model = combobox.get_model()

        print("ComboBox selected item: %s" % (model[treeiter][0]))

window = ComboBox()
window.show_all()

Gtk.main()
