#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

window = Gtk.Window()
window.set_default_size(200, -1)
window.connect("destroy", Gtk.main_quit)

toolbar = Gtk.Toolbar()
window.add(toolbar)

toolbutton1 = Gtk.RadioToolButton(group=None)
toolbutton1.set_label("Preferences")
toolbutton1.set_icon_name("gtk-preferences")
toolbutton1.set_is_important(True)
toolbar.insert(toolbutton1, 0)
toolbutton2 = Gtk.RadioToolButton(group=toolbutton1)
toolbutton2.set_icon_name("gtk-about")
toolbar.insert(toolbutton2, 1)
toolbutton3 = Gtk.RadioToolButton(group=toolbutton1)
toolbutton3.set_icon_name("gtk-help")
toolbar.insert(toolbutton3, 2)

window.show_all()

Gtk.main()
