ListBoxRow
==========
The ListBoxRow is a child container representing a row within the :doc:`listbox` widget.

===========
Constructor
===========
The ListBoxRow object is constructed using the call::

  listboxrow = Gtk.ListBoxRow()

=======
Methods
=======
To check whether a row is currently selected, call::

  listboxrow.is_selected()

A row can be made selectable or not by the method::

  listboxrow.set_selectable(selectable)

When *selectable* is set to ``False``, the row can not be selected by the user.

Rows can also be made activatable with::

  listboxrow.set_activatable(activatable)

A header widget can be assigned to the ListBoxRow via::

  listboxrow.set_header(widget)

The index value of a particular row in the ListBox can be obtained from the method::

  listboxrow.get_index()

A value returned indicates the position in the ListBox, with ``0`` indicating the row is first in the ListBox. A value of ``-1`` indicates the row has not been added to a ListBox.

=======
Example
=======
An example of the ListBoxRow can be found on the ListBox page.
