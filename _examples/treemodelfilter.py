#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

products = (("Apple", "Fruit", "£0.20"),
            ("Bleach", "Cleaning", "£1.20"),
            ("Bird Seed", "Pets", "£2.50"),
            ("Banana", "Fruit", "£0.35"),
            ("Beer", "Alcohol", "£2.75"),
            ("Cornflakes", "Cereal", "£1.10"),
            ("Pineapple", "Fruit", "£0.75"),
           )

class TreeModelFilter(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.connect("destroy", Gtk.main_quit)

        grid = Gtk.Grid()
        grid.set_row_spacing(5)
        self.add(grid)

        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_vexpand(True)
        scrolledwindow.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.NEVER)
        grid.attach(scrolledwindow, 0, 0, 1, 1)

        liststore = Gtk.ListStore(str, str, str)
        self.treemodelfilter = liststore.filter_new()
        self.treemodelfilter.set_visible_func(self.filter_visible, products)

        self.combobox = Gtk.ComboBoxText()
        self.combobox.append_text("All")
        self.combobox.set_active(0)
        self.combobox.connect("changed", self.on_category_changed)
        grid.attach(self.combobox, 0, 1, 1, 1)

        for product in products:
            liststore.append(product)

            self.combobox.append_text(product[1])

        treeview = Gtk.TreeView()
        treeview.set_model(self.treemodelfilter)
        scrolledwindow.add(treeview)

        cellrenderertext = Gtk.CellRendererText()
        treeviewcolumn = Gtk.TreeViewColumn("Product", cellrenderertext, text=0)
        treeview.append_column(treeviewcolumn)
        treeviewcolumn = Gtk.TreeViewColumn("Category", cellrenderertext, text=1)
        treeview.append_column(treeviewcolumn)
        treeviewcolumn = Gtk.TreeViewColumn("Price", cellrenderertext, text=2)
        treeview.append_column(treeviewcolumn)

    def on_category_changed(self, combobox):
        self.treemodelfilter.refilter()

    def filter_visible(self, model, treeiter, data):
        show = False

        if model[treeiter][1] == self.combobox.get_active_text():
            show = True
        elif self.combobox.get_active_text() == "All":
            show = True

        return show

window = TreeModelFilter()
window.show_all()

Gtk.main()
