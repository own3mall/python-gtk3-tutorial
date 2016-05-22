#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GObject

class ProgressBar(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.connect("destroy", Gtk.main_quit)

        self.progressbar = Gtk.ProgressBar()
        self.progressbar.set_show_text(True)
        self.add(self.progressbar)

        GObject.timeout_add(500, self.update_progressbar)

    def update_progressbar(self):
        fraction = self.progressbar.get_fraction() + 0.1

        if fraction <= 1.0:
            self.progressbar.set_fraction(fraction)
        else:
            self.progressbar.set_fraction(0.0)

        return True

window = ProgressBar()
window.show_all()

Gtk.main()
