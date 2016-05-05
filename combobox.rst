ComboBox
========
A ComboBox provides a drop-down menu of items which can be selected by the user. It is commonly used when there are more than five items to choose from.

Another function is to provide a way to enter values via the keyboard if the option is required.

===========
Constructor
===========
The ComboBox can be constructed using the following::

  combobox = Gtk.ComboBox(model)

A *model* should be assigned to the ComboBox to provide the list of options which are selectable.

ComboBox widgets can also be created with an Entry and/or associated model via::

  combobox = Gtk.ComboBox.new_with_entry()
  combobox = Gtk.ComboBox.new_with_model(model)
  combobox = Gtk.ComboBox.new_with_model_and_entry(model)

=======
Methods
=======
To set the model on the ComboBox after constructing the widget use::

  combobox.set_model(model)

The model is also retrievable::

  combobox.get_model()

In order to return the currently selected item from the ComboBox call::

  combobox.get_active()

The *active* value will return the number identifying the item. The first item will return ``0`` as the index number. If no item is selected, ``-1`` will be returned.

Alternatively, to set the item on the ComboBox use::

  combobox.set_active(active)

A TreeIter object representing the item in the ComboBox can be retrieved via::

  combobox.get_active_iter()

The selected row can also be set based on the TreeIter by::

  combobox.set_active_iter(treeiter)

An id column allows items to be selected based on a unique string value. The column in the model which is to be used for the id is set using::

  combobox.set_id_column(column)

The active id in use can be retrieved via::

  combobox.get_active_id()

Also, the id can be set by calling::

  combobox.set_active_id(id)

If the ComboBox contains a large number of items, it is recommended to display the menu spanning multiple columns. This can be set with::

  combobox.set_wrap_width(width)

The *width* value should be set to the number of columns required.

The number of rows and columns an item should span can be set with the methods::

  combobox.set_row_span_column(row_span)
  combobox.set_column_span_column(column_span)

The *row_span* and *column_span* methods should be set to the column held in the model, which contains an integer detailing the number of rows and columns the item will span when displayed.

To check whether a ComboBox has an associated text entry::

  combobox.get_has_entry()

Text displayed in the dropdown can be assigned a column from the model by::

  combobox.set_entry_text_column(column)

=======
Signals
=======
The commonly used signals of a ComboBox are::

  "changed" (combobox)
  "popup" (combobox)
  "popdown" (combobox)

A ``"changed"`` event occurs when the selected item within the ComboBox is changed. The signals ``"popup"`` and ``"popdown"`` are emitted when the menu object of the Combobox is shown or hidden by the user.

=======
Example
=======
Below is an example of a ComboBox:

.. literalinclude:: _examples/combobox.py

Download: :download:`ComboBox <_examples/combobox.py>`
