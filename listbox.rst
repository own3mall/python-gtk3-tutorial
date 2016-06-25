ListBox
=======
The ListBox widget provides a vertical container to display any widgets which are inserted into it. The widget also provides functions for sorting and filtering. It is an alternative to a :doc:`treeview` in some cases, and is suitable for inserting a wide range of widgets quickly.

===========
Constructor
===========
The ListBox can be constructed using::

  listbox = Gtk.ListBox()

=======
Methods
=======
Rows can be inserted into the ListBox using the following statements::

  listbox.add(child)
  listbox.insert(child, position)
  listbox.prepend(child)

The selection mode of the child widgets in the ListBox can be configured::

  listbox.set_selection_mode(selection_mode)

The *selection_mode* parameter can be set to one of the following:

* ``Gtk.Selection.NONE`` - disallow selection of rows.
* ``Gtk.Selection.SINGLE`` - allow a single row to be selected.
* ``Gtk.Selection.BROWSE`` - allow none, one or multiple rows to be selected.

A list of rows currently selected in the ListBox is obtained with::

  listbox.get_selected_rows()

The ``.get_selected_rows()`` method will return a list of :doc:`listboxrow` objects for each selected row.

When there are no child widgets to display in the ListBox, a placeholder can be set instead. This could be a :doc:`label` or :doc:`image` for example.

  listbox.set_placeholder(child)

By default, the ListBoxRow is activated when the user single clicks, however in some cases it may be useful to require a double click.

  listbox.set_activate_on_single_click(single_click)

When *single_click* is set to ``False``, the user requires a double-click to activate the row. This also allows the ``"row-selected"`` signal to work.

=======
Signals
=======
The commonly use signals of a ListBox are::

  "row-activated" (listbox, listboxrow)
  "row-selected" (listbox, listboxrow)

The ``"row-activated"`` signal emits when the user single clicks on the ListBoxRow. If the method ``.activate_on_single_click()`` is set to False, the user must double click. When single click activate is False, the ``"row-selected"`` signal can then be used, and emits when the user highlights a row.

=======
Example
=======
Below is an example of a FlowBox:

.. literalinclude:: _examples/flowbox.py

Download: :download:`FlowBox <_examples/flowbox.py>`
