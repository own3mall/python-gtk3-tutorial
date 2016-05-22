#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Label(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(600, -1)
        self.connect("destroy", Gtk.main_quit)

        grid = Gtk.Grid()
        grid.set_border_width(5)
        grid.set_row_spacing(5)
        grid.set_column_spacing(5)
        self.add(grid)

        label = Gtk.Label("An example of a Label widget.")
        label.set_selectable(True)
        grid.attach(label, 0, 0, 1, 1)
        label = Gtk.Label("This is a label spread across multiple\nlines using the newspace character\nto indicate the line break.")
        grid.attach(label, 0, 1, 1, 1)
        label = Gtk.Label("Tab spaces\tcan also be\tdefined if required.")
        grid.attach(label, 0, 2, 1, 1)
        label = Gtk.Label("Label widgets can also accept underline patterns.")
        label.set_pattern("_____                         _________")
        label.set_line_wrap(True)
        grid.attach(label, 0, 3, 1, 1)

        label = Gtk.Label("Justification options are\nable to align text in the label,\nsuch as to the left.")
        label.set_justify(Gtk.Justification.LEFT)
        grid.attach(label, 1, 0, 1, 1)
        label = Gtk.Label("Centering of text is possible\nto ensure that the margin\nof each sentence is even.")
        label.set_justify(Gtk.Justification.CENTER)
        grid.attach(label, 1, 1, 1, 1)
        label = Gtk.Label("Text can also be right-justified\nto align to the right hand\nmargin of the label.")
        label.set_justify(Gtk.Justification.RIGHT)
        grid.attach(label, 1, 2, 1, 1)
        label = Gtk.Label("Content is also justifiable to ensure that the sentences are evenly distributed. This ensures that the endings of each lines match. It does however require line wrapping to be enabled, and there are no manual breaks.")
        label.set_line_wrap(True)
        label.set_justify(Gtk.Justification.FILL)
        grid.attach(label, 1, 3, 1, 1)

        label = Gtk.Label("An angle can also be specified\nto orient the text.")
        label.set_angle(90)
        grid.attach(label, 2, 0, 1, 3)
        label = Gtk.Label("<a href='http://programmica.com/'>A website link</a>")
        label.set_use_markup(True)
        grid.attach(label, 2, 3, 1, 1)

label = Label()
label.show_all()

Gtk.main()
