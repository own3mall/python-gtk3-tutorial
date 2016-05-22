#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Calendar(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title("Calendar")
        self.connect("destroy", Gtk.main_quit)

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        self.add(hbox)

        self.calendar = Gtk.Calendar()
        self.calendar.connect("day-selected-double-click", self.on_date_selected)
        hbox.pack_start(self.calendar, True, True, 0)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        hbox.pack_start(vbox, False, False, 0)

        checkbuttonHeading = Gtk.CheckButton(label="Show Heading")
        checkbuttonHeading.set_active(True)
        checkbuttonHeading.connect("toggled", self.on_show_heading_change)
        vbox.pack_start(checkbuttonHeading, False, False, 0)

        checkbuttonDayNames = Gtk.CheckButton(label="Show Day Names")
        checkbuttonDayNames.set_active(True)
        checkbuttonDayNames.connect("toggled", self.on_show_days_change)
        vbox.pack_start(checkbuttonDayNames, False, False, 0)

        checkbuttonPreventChange = Gtk.CheckButton(label="Prevent Month/Year Change")
        checkbuttonPreventChange.connect("toggled", self.on_prevent_month_change)
        vbox.pack_start(checkbuttonPreventChange, False, False, 0)

        checkbuttonShowWeeks = Gtk.CheckButton(label="Show Week Numbers")
        checkbuttonShowWeeks.connect("toggled", self.on_show_weeks_change)
        vbox.pack_start(checkbuttonShowWeeks, False, False, 0)

    def on_date_selected(self, calendar):
        year, month, day = self.calendar.get_date()
        month += 1

        print("Date selected: %i/%i/%i" % (year, month, day))

    def on_show_heading_change(self, checkbutton):
        self.calendar.set_property("show-heading", checkbutton.get_active())

    def on_show_days_change(self, checkbutton):
        self.calendar.set_property("show-day-names", checkbutton.get_active())

    def on_prevent_month_change(self, checkbutton):
        self.calendar.set_property("no-month-change", checkbutton.get_active())

    def on_show_weeks_change(self, checkbutton):
        self.calendar.set_property("show-week-numbers", checkbutton.get_active())

window = Calendar()
window.show_all()

Gtk.main()
