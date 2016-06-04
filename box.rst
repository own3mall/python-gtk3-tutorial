Box
===
A Box object is an invisible container which allows packing of child widgets in two modes; vertically-packed and horizontally-packed.

For more information on packing and the theory behind it using GTK+, see the :doc:`packingtheory` page.

..note ::

  The :doc:`grid` widget is recommended in many cases where a Box would have traditionally been used.

===========
Constructor
===========
The Box can be constructed using the following::

  box = Gtk.Box(orientation, spacing)

The *orientation* parameter should be set to one of the following values; ``Gtk.Orientation.HORIZONTAL`` or ``Gtk.Orientation.VERTICAL``. By default, the Box is constructed with the ``Gtk.Orientation.HORIZONTAL`` orientation. The *spacing* value must be an integer value which indicates the amount of pixels between each of the child widgets.

=======
Methods
=======
Items can be packed using two methods; packing at the start of the container or packing at the end. When using a vertical Box, items using ``.pack_start()`` are packed from to the top. If using a horizontal box, packing using ``.pack_start()``, child widgets are added to the left. This is done with::

  box.pack_start(child, expand, fill, padding)
  box.pack_end(child, expand, fill, padding)

The *child* parameter should be the name of the child widget that is being added to the Box. The *expand* property when set to ``True`` indicates that the child should be given extra space if the Box has room for it. When *fill* is set to ``True``, the child widget is allocated the full horizontal or vertical space. The *padding* parameter should be set to an integer value which indicates how much space is put between it and other child widgets in the Box.

Items can also be removed from the Box with::

  box.remove(child)

To reorder child widgets based on position use::

  box.reorder_child(child, position)

The *position* value should be an integer, with ``0`` indicating the first position within the container. Alternatively, negative numbers can be entered which indicates a position from the end of the container.

The orientation of the Box can be changed after construction by::

  box.set_orientation(orientation)

Again, the *orientation* value must be set to either ``Gtk.Orientation.HORIZONTAL`` or ``Gtk.Orientation.VERTICAL``.

To ensure that all child widgets are set to an equal size regardless of their content, use::

  box.set_homogeneous(homogeneous)

By default, *homogeneous* is set to ``False`` and all child widgets are sized based on their content.

The Box spacing can be set after construction with::

  box.set_spacing(spacing)

The *spacing* parameter takes an integer value for the pixel width or height between each item.

Information about how a child is packed into the Box can be obtained via::

  box.query_child_packing(child)

A *child* must be supplied. The function returns a tuple with the packing information (expand, fill, padding, pack type).

If required, the packing values of an already added child can be configured by the method::

  box.set_child_packing(child, expand, fill, padding, pack_type)

The *expand*, *fill*, and *padding* parameters should be of the same type as the ``.pack_start()`` and ``.pack_end()`` methods. The *pack_type* should be set to one of:

* ``Gtk.PackType.START`` - pack at the left or top of the Box.
* ``Gtk.PackType.END`` - pack at the right or bottom of the Box.

A baseline position for the widgets added to the Box can be set with::

  box.set_baseline_position(position)

The *position* should be set to one of:

* ``Gtk.BaselinePosition.TOP`` - align to left or top of Box.
* ``Gtk.BaselinePosition.CENTER`` - alight to center of Box.
* ``Gtk.BaselinePosition.BOTTOM`` - align to right or bottom of Box.

A center widget can be set which is also positioned centrally regardless of other widgets via::

  box.set_center_widget(widget)

=======
Example
=======
Below is an example of a Box:

.. literalinclude:: _examples/box.py

Download: :download:`Box <_examples/box.py>`
