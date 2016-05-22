#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class RadioButton(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.connect("destroy", Gtk.main_quit)

        box = Gtk.Box()
        box.set_orientation(Gtk.Orientation.VERTICAL)
        box.set_spacing(5)
        self.add(box)

        radiobutton1 = Gtk.RadioButton(label="RadioButton 1")
        radiobutton1.connect("toggled", self.on_radio_button_toggled)
        box.pack_start(radiobutton1, True, True, 0)
        radiobutton2 = Gtk.RadioButton(label="RadioButton 2", group=radiobutton1)
        radiobutton2.connect("toggled", self.on_radio_button_toggled)
        box.pack_start(radiobutton2, True, True, 0)
        radiobutton3 = Gtk.RadioButton(label="RadioButton 3", group=radiobutton1)
        radiobutton3.connect("toggled", self.on_radio_button_toggled)
        box.pack_start(radiobutton3, True, True, 0)

    def on_radio_button_toggled(self, radiobutton):
        if radiobutton.get_active():
            print("%s is active" % (radiobutton.get_label()))

window = RadioButton()
window.show_all()

Gtk.main()
