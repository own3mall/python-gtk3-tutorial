Fixed
=====
A Fixed container provides a surface which allows the positioning of child widgets at fixed co-ordinates.

Fixed is very similar to the :doc:`layout` container, however it does not provide an infinite scrolling area. It should be used when the size of the Fixed area will be known.

===========
Constructor
===========
The Fixed can be constructed using the following::

  fixed = Gtk.Fixed()

=======
Methods
=======
To position widgets on the Fixed use::

  fixed.put(widget, x, y)

The *widget* value should be the child widget which is being added to the Fixed container. Specifying the *x* and *y* values specifies the co-ordinates that the child should be placed at.

To move the child widget after construction call::

  fixed.move(widget, x, y)

=======
Example
=======
Below is an example of a Fixed:

.. literalinclude:: _examples/fixed.py

Download: :download:`Fixed <_examples/fixed.py>`
