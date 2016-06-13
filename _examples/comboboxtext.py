#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ComboBoxText(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("ComboBoxText")
        self.set_default_size(150, -1)
        self.connect("destroy", Gtk.main_quit)

        comboboxtext = Gtk.ComboBoxText()
        comboboxtext.append("gnome", "GNOME")
        comboboxtext.append("kde", "KDE")
        comboboxtext.append("xfce", "XFCE")
        comboboxtext.append("lxde", "LXDE")
        comboboxtext.set_active_id("xfce")
        comboboxtext.connect("changed", self.on_comboboxtext_changed)
        self.add(comboboxtext)

    def on_comboboxtext_changed(self, comboboxtext):
        print("ComboBox selected item: %s" % (comboboxtext.get_active_text()))

window = ComboBoxText()
window.show_all()

Gtk.main()
