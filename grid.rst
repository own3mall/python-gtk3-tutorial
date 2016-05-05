Grid
====
A Grid widget is an invisible container which allows packing of one or more child widgets into rows and columns. It also supports height-for-width geometry means that widgets are scaled to sizes relative to the size of the space they are allocated.

For more information on packing and the theory behind it using GTK+, see the :doc:`packingtheory` page.

===========
Constructor
===========
The Grid can be constructed using the following::

  grid = Gtk.Grid()

=======
Methods
=======
To attach a child widget to the Grid, call::

  grid.attach(child, left, top, width, height)

The *child* parameter should be the name of the widget which is to be placed within the Grid. The *left* and *top* values should be the row and column numbers which specify where the widget will be placed and the *width* and *height* parameters should be integer values indicating how many rows and columns the widget will span.

When adding multiple widgets to a Grid, it can be time-consuming to call ``.attach()`` repeatedly and enter the correct row and column values. To attach next to a previously added widget, use::

  grid.attach_next_to(child, sibling, side, width, height)

The *child* again should be the name of the widget being added to the Grid. The *sibling* is the name of the widget the child is being added next to. The *position* should be one of ``Gtk.PositionType.LEFT``, ``Gtk.PositionType.RIGHT``, ``Gtk.PositionType.TOP``, or ``Gtk.PositionType.BOTTOM``. The *width* and *height* parameters should be integer values indicating how many rows and columns the widget will span.

To remove columns and rows from the Grid, use the method::

  grid.remove_column(position)
  grid.remove_row(position)

The *position* value is the number of the column or row to be removed. The use of these methods causes the following:

* Any widgets in the column or row are removed
* Any widgets which span the column or row have their height or width shortened
* Any widgets to the right or bottom are shifted

To set the spacing between rows and columns::

  grid.set_row_spacing(spacing)
  grid.set_column_spacing(spacing)

For neatness, it may be useful to set all widgets in a row or column to be an equal size with::

  grid.set_row_homogeneous(homogeneous)
  grid.set_column_homogeneous(homogeneous)

When *homogeneous* is set to True, the widgets will take the same size with the largest child widget dictating the size of all others in the row or column.

To retrieve a widget located at a particular position within the Grid call::

  grid.get_child_at(left, top)

The *left* and *top* values should be specified as integer values identifying the location of the child.

=======
Example
=======
Below is an example of a Grid:

.. literalinclude:: _examples/grid.py

Download: :download:`Grid <_examples/grid.py>`
