#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class FlowBox(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("FlowBox")
        self.set_default_size(200, 200)
        self.connect("destroy", Gtk.main_quit)

        flowbox = Gtk.FlowBox()
        flowbox.connect("child-activated", self.on_child_activated)
        self.add(flowbox)

        for count in range(0, 9):
            label = Gtk.Label("Row %i" % (count))
            flowbox.add(label)

    def on_child_activated(self, flowbox, flowboxchild):
        print("Child %i activated" % (flowboxchild.get_index()))

window = FlowBox()
window.show_all()

Gtk.main()
