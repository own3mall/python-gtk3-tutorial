TreeSelection
=============
A TreeSelection is an object that allows for management of selections within a :doc:`treeview`.

=======
Methods
=======
To set the type of selection which the TreeSelection allows, call::

  treeselection.set_mode(mode)

The *mode* can be set to one of the following:

* ``Gtk.SelectionType.NONE`` - prevents a selection.
* ``Gtk.SelectionType.SINGLE`` - allows none or one item to be selected.
* ``Gtk.SelectionType.BROWSE`` - enforces a single item to be selected.
* ``Gtk.SelectionType.MULTIPLE`` - allows selecting of multiple items by holding the :kbd:`Control` key or by click-and-drag.

By default, ``Gtk.SelectionType.SINGLE`` is the default selection mode.

The selection mode can be gathered with the method::

  treeselection.get_mode()

Retrieval of the selected item when ``Gtk.SelectionType.SINGLE`` or ``Gtk.SelectionType.BROWSE`` is used can be made with::

  treeselection.get_selected()

When the ``.get_selected()`` method is run, both the model used and the selected TreeIter are returned. Both can be used together to retrieve the selected data.

To select or unselect all the items in the TreeSelection call::

  treeselection.select_all()
  treeselection.unselect_all()

Counting the number of selected rows which the TreeSelection has can be done with the method::

  treeselection.count_selected_rows()

The TreeView which is associated with the TreeSelection can be found via::

  treeselection.get_tree_view()

A range of rows can be selected and unselected with::

  treeselection.select_range(start, end)
  treeselection.unselect_range(start, end)

The *start* and *end* parameters take a TreePath object identifying both the first and last rows to be selected.

A check can be made on whether a particular TreeIter or TreePath is selected via::

  treeselection.iter_is_selected(treeiter)
  treeselection.path_is_selected(treepath)

A TreeIter or TreePath can be programatically selected or unselected with the use of::

  treeselection.select_iter(treeiter)
  treeselection.select_path(treepath)
  treeselection.unselect_iter(treeiter)
  treeselection.unselect_path(treepath)

=======
Signals
=======
The common signals of the TreeSelection are

  "changed" (treeselection)

When the currently selected items within the TreeSelection are changed, the ``"changed"`` signal is emitted.
