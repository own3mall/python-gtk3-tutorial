Paned
=====
A Paned widget provides an adjustable split-screen view. It is commonly used in email clients to separate the various interface elements.

===========
Constructor
===========
The Paned can be constructed using the following::

  paned = Gtk.Paned(orientation)

The *orientation* argument should be set to either ``Gtk.Orientation.HORIZONTAL`` or ``Gtk.Orientation.VERTICAL``.

=======
Methods
=======
To add items to the Paned widget, there are two methods::

  paned.add1(child)
  paned.add2(child)

The ``.add1()`` method adds the child widget to the top or left pane of the container. Calling ``.add2()`` places the child in the bottom or right pane. The child in most cases will be a Grid or Box.

If more flexible packing functionality is requires, the following can be run::

  paned.pack1(child, resize, shrink)
  paned.pack2(child, resize, shrink)

The *resize* argument determines whether the child should expand when the Paned is resized. Setting this to ``True`` set the widget to expand. Setting the *shrink* argument to ``True`` also allows the child to be made smaller than its available area.

To set the position of the expander, call::

  paned.set_position(position)

The *position* value should be an integer in pixels which specifies how wide the left or top pane is.

Retrieving the position from the Paned widget is done via the method::

  paned.get_position()

The *position* value returned is the number of pixels wide the left or top pane is. This is useful when saving the application configuration to a file.

The Paned object also supports a wide-handle, which makes adjustments to the Paned sizes easier::

  paned.set_wide_handle(wide_handle)

When *wide_handle* is set to ``True``, the wide-handle view is enabled.

=======
Signals
=======
The commonly used signals of a Paned are::

  "move-handle" (widget, scroll_type)

The ``"move-handle"`` signals emits two properties when it occurs. The *widget* is that of the Paned upon which the handle move occurred. The *scroll_type* returns the type of scroll action.

=======
Example
=======
Below is an example of a Paned:

.. literalinclude:: _examples/paned.py

Download: :download:`Paned <_examples/paned.py>`
