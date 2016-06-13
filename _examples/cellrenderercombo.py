#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class CellRendererCombo(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("CellRendererCombo")
        self.set_default_size(200, 200)
        self.connect("destroy", Gtk.main_quit)

        self.liststoreAppliance = Gtk.ListStore(str, str)
        self.liststoreAppliance.append(["Dishwasher", "Bosch"])
        self.liststoreAppliance.append(["Refrigerator", "Samsung"])
        self.liststoreAppliance.append(["Cooker", "Hotpoint"])

        self.liststoreManufacturers = Gtk.ListStore(str)
        self.liststoreManufacturers.append(["Bosch"])
        self.liststoreManufacturers.append(["Whirlpool"])
        self.liststoreManufacturers.append(["Hotpoint"])
        self.liststoreManufacturers.append(["DeLonghi"])
        self.liststoreManufacturers.append(["Samsung"])

        treeview = Gtk.TreeView()
        treeview.set_model(self.liststoreAppliance)
        self.add(treeview)

        cellrenderertext = Gtk.CellRendererText()

        treeviewcolumn = Gtk.TreeViewColumn("Appliance")
        treeview.append_column(treeviewcolumn)
        treeviewcolumn.pack_start(cellrenderertext, False)
        treeviewcolumn.add_attribute(cellrenderertext, "text", 0)

        cellrenderercombo = Gtk.CellRendererCombo()
        cellrenderercombo.set_property("editable", True)
        cellrenderercombo.set_property("model", self.liststoreManufacturers)
        cellrenderercombo.set_property("text-column", 0)
        cellrenderercombo.connect("changed", self.on_combo_changed)

        treeviewcolumn = Gtk.TreeViewColumn("Manufacturer")
        treeview.append_column(treeviewcolumn)
        treeviewcolumn.pack_start(cellrenderercombo, False)
        treeviewcolumn.add_attribute(cellrenderercombo, "text", 1)

    def on_combo_changed(self, cellrenderercombo, treepath, treeiter):
        self.liststoreAppliance[treepath][1] = self.liststoreManufacturers[treeiter][0]

window = CellRendererCombo()
window.show_all()

Gtk.main()
