#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class SearchEntry(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("SearchEntry")
        self.connect("destroy", Gtk.main_quit)

        searchentry = Gtk.SearchEntry()
        searchentry.connect("activate", self.on_search_activated)
        self.add(searchentry)

    def on_search_activated(self, searchentry):
        print("SearchEntry text: %s" % (searchentry.get_text()))

window = SearchEntry()
window.show_all()

Gtk.main()
