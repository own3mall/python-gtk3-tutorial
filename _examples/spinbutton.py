#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class SpinButton(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.connect("destroy", Gtk.main_quit)

        adjustment = Gtk.Adjustment(value=0,
                                    lower=-10,
                                    upper=25,
                                    step_increment=1,
                                    page_increment=5,
                                    page_size=0)
        spinbutton = Gtk.SpinButton(adjustment=adjustment)
        spinbutton.connect("value-changed", self.on_spinbutton_changed)
        self.add(spinbutton)

    def on_spinbutton_changed(self, spinbutton):
        print("SpinButton value: %i" % (spinbutton.get_value_as_int()))

window = SpinButton()
window.show_all()

Gtk.main()
