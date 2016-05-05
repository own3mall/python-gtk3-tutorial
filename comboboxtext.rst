ComboBoxText
============
A ComboBoxText provides a simple variant of :doc:`combobox` which is suited to text-only values.

===========
Constructor
===========
The ComboBoxText can be constructed using the following::

  comboboxtext = Gtk.ComboBoxText()

Alternatively, if you wish to allow the user to enter text as well as selecting from the pre-defined list, use::

  comboboxtext = Gtk.ComboBoxText.new_with_entry()

=======
Methods
=======
Items can be added to the dropdown with the following methods::

  comboboxtext.insert(position, id, text)
  comboboxtext.append(id, text)
  comboboxtext.prepend(id, text)

The *id* defines a unique string which identifies the item in the ComboBoxText. The *text* value provides the string to be displayed to the end user. Finally, the *position* on the ``.insert()`` methods sets the location the new item should be added.

If the ComboBoxText is simply used for listing text items, and id values are not required, use::

  comboboxtext.insert_text(position, text)
  comboboxtext.append_text(text)
  comboboxtext.prepend_text(text)

All the items can be removed from the dropdown menu::

  comboboxtext.remove_all()

Alternatively, single items can be deleted base on their listed position in the dropdown menu::

  comboboxtext.remove(position)

The *position* parameter is the location where the item is located within the dropdown, with ``0`` indicating the first item.

To retrieve the text which has been selected call::

  comboboxtext.get_active_text()

Alternatively, the active item id can be retrieved via::

  comboboxtext.get_active_id()

TreeIter objects can also be fetched from the ComboBoxText by using the method::

  comboboxtext.get_active_iter()

Setting a default selected item can be achieved with::

  comboboxtext.set_active(position)

The *position* value must be an integer number representing the location of the item in the dropdown menu.

The active id can also be defined::

  comboboxtext.set_active_id(id)

A row may also be selected based on a known TreeIter with::

  comboboxtext.set_active_iter(treeiter)

=======
Example
=======
Below is an example of a ComboBoxText:

.. literalinclude:: _examples/comboboxtext.py

Download: :download:`ComboBoxText <_examples/comboboxtext.py>`
