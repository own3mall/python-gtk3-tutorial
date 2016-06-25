#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class HelloWorld:
    def __init__(self):
        window = Gtk.Window()
        window.connect("destroy", self.close_hello_world)

        button = Gtk.Button("Click here")
        button.connect("clicked", self.print_hello_world)
        window.add(button)

        window.show_all()

    def close_hello_world(self, widget):
        Gtk.main_quit()

    def print_hello_world(self, widget):
        print("Hello World")

if __name__ == "__main__":
    HelloWorld()
    Gtk.main()
