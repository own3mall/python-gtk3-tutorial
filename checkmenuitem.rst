CheckMenuItem
=============
The CheckMenuItem provides a :doc:`checkbutton` for use within a menu structure. It displays a box with associated label that can indicate a checked or unchecked state.

===========
Constructor
===========
The CheckMenuItem can be constructed using the following::

  checkmenuitem = Gtk.CheckMenuItem(label, use_underline)

The *label* parameter specifies the string of text to be displayed in the CheckMenuItem. When *use_underline* is set to ``True``, the character in the label proceeding an underscore will be used as the mnemonic key.

=======
Methods
=======
The label can be applied to the CheckMenuItem after constructing it with::

  checkmenitem.set_label(label)

The active state can also be set with::

  checkmenuitem.set_active(active)

When *active* is set to ``True``, the CheckMenuItem displays a tick in the box indicating an active state.

To retrieve the state of the CheckMenuItem use::

  checkmenuitem.get_active()

When using multiple CheckMenuItem widgets, it may be necessary to indicate an inconsistent state if all other items in the group have a ``True`` or ``False`` value. This can be set via::

  checkmenuitem.set_inconsistent(inconsistent)

To retrieve whether a CheckMenuItem is in an inconsitent state use::

  checkmenuitem.get_inconsistent()

=======
Signals
=======
The common signals of the CheckMenuItem are::

  "toggled" (checkmenuitem)

The ``"toggled"`` signal emits from the widget when the user changes the state to checked or unchecked.

=======
Example
=======
For an example of the MenuItem see the :doc:`menu` page.
