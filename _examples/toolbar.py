#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Toolbar(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(500, -1)
        self.connect("destroy", Gtk.main_quit)

        toolbar = Gtk.Toolbar()
        self.add(toolbar)

        toolbutton = Gtk.ToolButton()
        toolbutton.set_label("New")
        toolbutton.set_is_important(True)
        toolbutton.set_icon_name("gtk-new")
        toolbar.add(toolbutton)

        toggletoolbutton = Gtk.ToggleToolButton()
        toggletoolbutton.set_icon_name("gtk-media-play")
        toolbar.add(toggletoolbutton)

        menu = Gtk.Menu()

        menuitem = Gtk.MenuItem(label="MenuItem")
        menu.append(menuitem)
        menuitem.show()

        menutoolbutton = Gtk.MenuToolButton()
        menutoolbutton.set_menu(menu)
        menutoolbutton.set_icon_name("gtk-open")
        toolbar.add(menutoolbutton)

        separatortoolitem = Gtk.SeparatorToolItem()
        toolbar.add(separatortoolitem)

        radiotoolbutton1 = Gtk.RadioToolButton()
        radiotoolbutton1.set_icon_name("gtk-media-rewind")
        toolbar.add(radiotoolbutton1)
        radiotoolbutton2 = Gtk.RadioToolButton(group=radiotoolbutton1)
        radiotoolbutton2.set_icon_name("gtk-media-forward")
        toolbar.add(radiotoolbutton2)

        separatortoolitem = Gtk.SeparatorToolItem()
        toolbar.add(separatortoolitem)

        toolitem = Gtk.ToolItem()
        toolbar.add(toolitem)
        entry = Gtk.Entry()
        toolitem.add(entry)

window = Toolbar()
window.show_all()

Gtk.main()
