AspectFrame
===========
A AspectFrame is a container widget used to group other widgets which perform related functions. It differs from a :doc:`frame` in that child content is scaled depending on the child size, or the specified settngs of the container.

An AspectFrame is based on a Frame and therefore provides many of the same methods.

===========
Constructor
===========
The AspectFrame can be constructed using the following::

  aspectframe = Gtk.AspectFrame(label, xalign, yalign, ratio, obey_child)

The *label* parameter should be set to a string of text which is displayed on the AspectFrame to indicate what the group of child widgets relates to. The *xalign* and *yalign* parameters specify the position of the child within the AspectFrame. The *ratio* value indicates the size of the child with relation to its initial size, and can be set to a float value. Finally, the *obey_child* takes the ratio of the child widget and uses that to determine the AspectFrame size when set to ``True``.

.. note::

  The *ratio* value only applies when *obey_child* is set to ``False``.

=======
Methods
=======
To set the label text on the frame after constructing use::

  aspectframe.set_label(label)

Alternatively, a :doc:`label` widget can be used on the AspectFrame if required by calling::

  aspectframe.set_label_widget(label_widget)

By default, the label is positioned in the top-left corner of the AspectFrame. This can be changed using::

  aspectframe.set_label_align(xalign, yalign)

The *xalign* and *yalign* values should be float values between ``0.0`` and ``1.0``. By default, these values are set to 0.0 and 0.5 on a newly created AspectFrame.

To set the AspectFrame properties relating to the child size after construction use::

  aspectframe.set(xalign, yalign, ratio, obey_child)

Children are able to be added to and removed from the AspectFrame using both::

  aspectframe.add(child)
  aspectframe.remove(child)

=======
Example
=======
Below is an example of a AspectFrame:

.. literalinclude:: _examples/aspectframe.py

Download: :download:`AspectFrame <_examples/aspectframe.py>`
