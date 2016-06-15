Layout
======
A Layout provides an infinite scrolling area for child widgets to be placed on. It can also be used as a surface for custom drawings to be displayed.

If the size of the scrolling area is going to be known before running, it is suggested that a :doc:`fixed` is used.

===========
Constructor
===========
The Layout can be constructed using the following::

  layout = Gtk.Layout(hadjustment, vadjustment)

The *hadjustment* and *vadjustment* parameters should be set to an :doc:`adjustment` object which stores the values of the scrollbars.

=======
Methods
=======
To position widgets on the Layout use::

  layout.put(widget, x, y)

The *widget* parameter specifies the widget which is to be drawn on the Layout. The *x* and *y* values are the co-ordinates of where to place the widget.

Widges can be moved after calling ``.put()`` with::

  layout.move(widget, x, y)

To set the size of the Layout call::

  layout.set_size(width, height)

Alternatively, to retrieve the Layout size use::

  layout.get_size()

The Adjustment objects can be specified after constructing the Layout with::

  layout.set_hadjustment(adjustment)
  layout.set_vadjustment(adjustment)

=======
Example
=======
Below is an example of a Layout:

.. literalinclude:: _examples/layout.py

Download: :download:`Layout <_examples/layout.py>`
