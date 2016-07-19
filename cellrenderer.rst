CellRenderer
============
The CellRenderer object provides a base for the other members of the CellRenderer family. It provides common methods and properties which may be useful when displaying information in a :doc:`treeview` or :doc:`combobox`.

=======
Methods
=======
The visibility of a particular cell can be toggled with::

  cellrenderer.set_visible(visible)

When the *visible* argument is set to ``False``, the CellRenderer will be hidden.

Sensitivity of a CellRenderer can also be changed via::

  cellrenderer.set_sensitive(sensitive)

Padding can be defined for the width and height by specifying the required value in pixels::

  cellrenderer.set_padding(xpadding, ypadding)

Content within the CellRenderer can be aligned by calling the method::

  cellrenderer.set_alignment(xalign, yalign)

A fixed width and height can also be set by using::

  cellrenderer.set_fixed_size(width, height)

The *width* and *height* can be set to ``-1`` to revert to automatic sizing.
