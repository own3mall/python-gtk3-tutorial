#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class InfoBar(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("InfoBar")
        self.connect("destroy", Gtk.main_quit)

        grid = Gtk.Grid()
        grid.set_row_spacing(5)
        self.add(grid)

        self.infobar = Gtk.InfoBar()
        self.infobar.set_show_close_button(True)
        self.infobar.connect("response", self.on_infobar_response)
        grid.attach(self.infobar, 0, 0, 1, 1)

        label = Gtk.Label("InfoBar content string.")
        content = self.infobar.get_content_area()
        content.add(label)

        buttonbox = Gtk.ButtonBox()
        grid.attach(buttonbox, 0, 1, 1, 1)

        buttonInformation = Gtk.Button(label="Information")
        buttonInformation.message_type = Gtk.MessageType.INFO
        buttonInformation.connect("clicked", self.on_button_clicked)
        buttonbox.add(buttonInformation)
        buttonQuestion = Gtk.Button(label="Question")
        buttonQuestion.message_type = Gtk.MessageType.QUESTION
        buttonQuestion.connect("clicked", self.on_button_clicked)
        buttonbox.add(buttonQuestion)
        buttonWarning = Gtk.Button(label="Warning")
        buttonWarning.message_type = Gtk.MessageType.WARNING
        buttonWarning.connect("clicked", self.on_button_clicked)
        buttonbox.add(buttonWarning)
        buttonError = Gtk.Button(label="Error")
        buttonError.message_type = Gtk.MessageType.ERROR
        buttonError.connect("clicked", self.on_button_clicked)
        buttonbox.add(buttonError)
        buttonOther = Gtk.Button(label="Other")
        buttonOther.message_type = Gtk.MessageType.OTHER
        buttonOther.connect("clicked", self.on_button_clicked)
        buttonbox.add(buttonOther)

    def on_button_clicked(self, button):
        self.infobar.set_message_type(button.message_type)
        self.infobar.show()

    def on_infobar_response(self, infobar, respose_id):
        self.infobar.hide()

window = InfoBar()
window.show_all()

Gtk.main()
