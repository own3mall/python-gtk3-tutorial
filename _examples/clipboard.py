#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk

class Clipboard(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("Clipboard")
        self.connect("destroy", Gtk.main_quit)

        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

        grid = Gtk.Grid()
        self.add(grid)

        self.entry = Gtk.Entry()
        grid.attach(self.entry, 0, 0, 1, 1)

        buttonCutText = Gtk.Button(label="Cut Text")
        buttonCutText.connect("clicked", self.on_copy_text, "cut")
        grid.attach(buttonCutText, 1, 0, 1, 1)

        buttonCopyText = Gtk.Button(label="Copy Text")
        buttonCopyText.connect("clicked", self.on_copy_text, "copy")
        grid.attach(buttonCopyText, 2, 0, 1, 1)

        buttonPasteText = Gtk.Button(label="Paste Text")
        buttonPasteText.connect("clicked", self.on_paste_text)
        grid.attach(buttonPasteText, 3, 0, 1, 1)

    def on_copy_text(self, button, action):
        content = self.entry.get_text()

        if action == "cut":
            self.entry.set_text("")

        self.clipboard.set_text(content, -1)

    def on_paste_text(self, button):
        content = self.clipboard.wait_for_text()
        self.entry.set_text(content)

window = Clipboard()
window.show_all()

Gtk.main()
