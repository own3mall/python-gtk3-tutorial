FlowBox
=======
The FlowBox is a container which allows automatic reflowing of child widgets, according to their orientation. When the FlowBox is set to horizontal orientation, widgets are arranged from left to right, and new rows are started when necessary. Vertical orientation arranged children from top to bottom and create a new column when necessary.

The widget is similar to a :doc:`listbox`.

===========
Constructor
===========
The FlowBox can be constructed using::

  flowbox = Gtk.FlowBox()

=======
Methods
=======
Widgets are inserted into the FlowBox via the method::

  flowbox.insert(child, position)

The *child* parameter will typically be another container such as :doc:`box` or :doc:`grid`. Widgets can be inserted however. The *position* value is an integer value, starting at ``0`` which indicates the first position.

Spacing between the children contained in the FlowBox can be set for both column and row::

  flowbox.set_row_spacing(spacing)
  flowbox.set_column_spacing(spacing)

To force all child widgets to be the same size regardless of the size they require::

  flowbox.set_homogeneous(homogeneous)

Items within the FlowBox can be selected or unselected::

  flowbox.select_all()
  flowbox.unselect_all()

Typically, the FlowBox places child widgets automatically. This can lead to an undesirable number in a single row or column. Minimum and maximum numbers can therefore be set::

  flowbox.set_min_children_per_line(minimum)
  flowbox.set_max_children_per_line(maximum)

Controlling the number of clicks it takes to activate an item is configured with::

  flowbox.set_activate_on_single_click(single)

When *single* is set to ``True``, an item is activated on a single click. When using ``False``, a double-click is required.

The number of items in the FlowBox which can be selected is configurable via::

  flowbox.set_selection_mode(mode)

The *mode* value can be set to:

* ``Gtk.Selection.NONE`` - prevent any selection being made.
* ``Gtk.Selection.SINGLE`` - allow only a single selected item.
* ``Gtk.Selection.BROWSE`` - allow one or more selected items.
* ``Gtk.Selection.MULTIPLE`` - allow multiple selected items.

=======
Signals
=======
The commonly used signals of a FlowBox are::

  "activate" (child)
  "select-all" (box)
  "unselect-all" (box)

The ``"activate"`` signal is emitted when the user either single-clicks or double-clicks on a child. The FlowBox emits the ``"select-all"`` and ``"unselect-all"`` signals when all the items are chosen or unchosen.

=======
Example
=======
Below is an example of a FlowBox:

.. literalinclude:: _examples/flowbox.py

Download: :download:`FlowBox <_examples/flowbox.py>`
