#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MessageDialog(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("MessageDialog")
        self.connect("destroy", Gtk.main_quit)

        buttonbox = Gtk.ButtonBox()
        self.add(buttonbox)

        buttonInformation = Gtk.Button(label="Information")
        buttonInformation.message_type = Gtk.MessageType.INFO
        buttonInformation.connect("clicked", self.on_message_clicked)
        buttonbox.add(buttonInformation)
        buttonWarning = Gtk.Button(label="Warning")
        buttonWarning.message_type = Gtk.MessageType.WARNING
        buttonWarning.connect("clicked", self.on_message_clicked)
        buttonbox.add(buttonWarning)
        buttonQuestion = Gtk.Button(label="Question")
        buttonQuestion.message_type = Gtk.MessageType.QUESTION
        buttonQuestion.connect("clicked", self.on_message_clicked)
        buttonbox.add(buttonQuestion)
        buttonError = Gtk.Button(label="Error")
        buttonError.message_type = Gtk.MessageType.ERROR
        buttonError.connect("clicked", self.on_message_clicked)
        buttonbox.add(buttonError)
        buttonOther = Gtk.Button(label="Other")
        buttonOther.message_type = Gtk.MessageType.OTHER
        buttonOther.connect("clicked", self.on_message_clicked)
        buttonbox.add(buttonOther)

        self.messagedialog = Gtk.MessageDialog(message_format="MessageDialog")
        self.messagedialog.set_transient_for(self)
        self.messagedialog.set_title("MessageDialog")
        self.messagedialog.set_markup("<span size='12000'><b>This is a MessageDialog widget.</b></span>")
        self.messagedialog.format_secondary_text("The MessageDialog can display a main message, and further secondary content.")
        self.messagedialog.add_button("_Close", Gtk.ResponseType.CLOSE)

    def on_message_clicked(self, button):
        self.messagedialog.set_property("message-type", button.message_type)

        self.messagedialog.run()
        self.messagedialog.hide()

window = MessageDialog()
window.show_all()

Gtk.main()
