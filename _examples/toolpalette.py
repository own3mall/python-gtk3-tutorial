#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ToolPalette(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(200, 200)
        self.connect("destroy", Gtk.main_quit)

        toolpalette = Gtk.ToolPalette()
        self.add(toolpalette)

        toolitemgroup = Gtk.ToolItemGroup(label="Group 1")
        toolpalette.add(toolitemgroup)

        toolbutton = Gtk.ToolButton()
        toolbutton.set_icon_name("gtk-new")
        toolitemgroup.insert(toolbutton, 0)
        toolbutton = Gtk.ToolButton()
        toolbutton.set_icon_name("gtk-open")
        toolitemgroup.insert(toolbutton, 1)
        toolbutton = Gtk.ToolButton()
        toolbutton.set_icon_name("gtk-save")
        toolitemgroup.insert(toolbutton, 2)

        toolitemgroup = Gtk.ToolItemGroup(label="Group 2")
        toolpalette.add(toolitemgroup)

        toolbutton = Gtk.ToolButton()
        toolbutton.set_icon_name("gtk-about")
        toolitemgroup.insert(toolbutton, 0)
        toolbutton = Gtk.ToolButton()
        toolbutton.set_icon_name("gtk-preferences")
        toolitemgroup.insert(toolbutton, 1)

window = ToolPalette()
window.show_all()

Gtk.main()
