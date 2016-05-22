#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Assistant(Gtk.Assistant):
    def __init__(self):
        Gtk.Assistant.__init__(self)
        self.set_title("Assistant")
        self.set_default_size(400, -1)
        self.connect("cancel", self.on_cancel_clicked)
        self.connect("close", self.on_close_clicked)
        self.connect("apply", self.on_apply_clicked)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.append_page(box)
        self.set_page_type(box, Gtk.AssistantPageType.INTRO)
        self.set_page_title(box, "Page 1: Introduction")
        label = Gtk.Label(label="An 'Intro' page is the first page of an Assistant. It is used to provide information about what configuration settings need to be configured. The introduction page only has a 'Continue' button.")
        label.set_line_wrap(True)
        box.pack_start(label, True, True, 0)
        self.set_page_complete(box, True)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.append_page(box)
        self.set_page_type(box, Gtk.AssistantPageType.CONTENT)
        self.set_page_title(box, "Page 2: Content")
        label = Gtk.Label(label="The 'Content' page provides a place where widgets can be positioned. This allows the user to configure a variety of options as needed. The page contains a 'Continue' button to move onto other pages, and a 'Go Back' button to return to the previous page if necessary.")
        label.set_line_wrap(True)
        box.pack_start(label, True, True, 0)
        self.set_page_complete(box, True)

        self.complete = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.append_page(self.complete)
        self.set_page_type(self.complete, Gtk.AssistantPageType.PROGRESS)
        self.set_page_title(self.complete, "Page 3: Progress")
        label = Gtk.Label(label="A 'Progress' page is used to prevent changing pages within the Assistant before a long-running process has completed. The 'Continue' button will be marked as insensitive until the process has finished. Once finished, the button will become sensitive.")
        label.set_line_wrap(True)
        self.complete.pack_start(label, True, True, 0)
        checkbutton = Gtk.CheckButton(label="Mark page as complete")
        checkbutton.connect("toggled", self.on_complete_toggled)
        self.complete.pack_start(checkbutton, False, False, 0)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.append_page(box)
        self.set_page_type(box, Gtk.AssistantPageType.CONFIRM)
        self.set_page_title(box, "Page 4: Confirm")
        label = Gtk.Label(label="The 'Confirm' page may be set as the final page in the Assistant, however this depends on what the Assistant does. This page provides an 'Apply' button to explicitly set the changes, or a 'Go Back' button to correct any mistakes.")
        label.set_line_wrap(True)
        box.pack_start(label, True, True, 0)
        self.set_page_complete(box, True)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.append_page(box)
        self.set_page_type(box, Gtk.AssistantPageType.SUMMARY)
        self.set_page_title(box, "Page 5: Summary")
        label = Gtk.Label(label="A 'Summary' should be set as the final page of the Assistant if used however this depends on the purpose of your Assistant. It provides information on the changes that have been made during the configuration or details of what the user should do next. On this page only a Close button is displayed. Once at the Summary page, the user cannot return to any other page.")
        label.set_line_wrap(True)
        box.pack_start(label, True, True, 0)
        self.set_page_complete(box, True)

    def on_apply_clicked(self, *args):
        print("The 'Apply' button has been clicked")

    def on_close_clicked(self, *args):
        print("The 'Close' button has been clicked")
        Gtk.main_quit()

    def on_cancel_clicked(self, *args):
        print("The Assistant has been cancelled.")
        Gtk.main_quit()

    def on_complete_toggled(self, checkbutton):
        assistant.set_page_complete(self.complete, checkbutton.get_active())

assistant = Assistant()
assistant.show_all()

Gtk.main()
