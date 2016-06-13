#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class EntryCompletion(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("EntryCompletion")
        self.connect("destroy", Gtk.main_quit)

        grid = Gtk.Grid()
        self.add(grid)

        liststore = Gtk.ListStore(str)

        for item in ["Andrew", "Natalie", "Mark", "David", "Daniel", "Anita", "Matthew"]:
            liststore.append([item])

        self.entrycompletion = Gtk.EntryCompletion()
        self.entrycompletion.set_model(liststore)
        self.entrycompletion.set_text_column(0)

        entry = Gtk.Entry()
        entry.set_completion(self.entrycompletion)
        grid.attach(entry, 0, 0, 1, 1)

        radiobuttonPopup = Gtk.RadioButton("Popup Completion")
        radiobuttonPopup.mode = 0
        radiobuttonPopup.connect("toggled", self.on_radiobutton_toggled)
        grid.attach(radiobuttonPopup, 0, 1, 1, 1)
        radiobuttonInline = Gtk.RadioButton("Inline Completion")
        radiobuttonInline.mode = 1
        radiobuttonInline.join_group(radiobuttonPopup)
        radiobuttonInline.connect("toggled", self.on_radiobutton_toggled)
        grid.attach(radiobuttonInline, 0, 2, 1, 1)

    def on_radiobutton_toggled(self, radiobutton):
        if radiobutton.get_active():
            if radiobutton.mode == 0:
                self.entrycompletion.set_popup_completion(True)
                self.entrycompletion.set_inline_completion(False)
            elif radiobutton.mode == 1:
                self.entrycompletion.set_popup_completion(False)
                self.entrycompletion.set_inline_completion(True)


window = EntryCompletion()
window.show_all()

Gtk.main()
