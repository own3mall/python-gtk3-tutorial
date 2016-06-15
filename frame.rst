Frame
=====
A Frame is a container widget used to group other widgets which perform related functions.

===========
Constructor
===========
The Frame can be constructed using the following::

  frame = Gtk.Frame(label)

The *label* parameter should be set to a string of text which is displayed on the Frame to indicate what the group of child widgets relates to.

=======
Methods
=======
To set the label text on the frame after constructing use::

  frame.set_label(label)

Alternatively, a :doc:`label` widget can be used on the Frame if required by calling::

  frame.set_label_widget(label_widget)

By default, the label is positioned in the top-left corner of the Frame. This can be changed using::

  frame.set_label_align(xalign, yalign)

The *xalign* and *yalign* values should be float values between ``0.0`` and ``1.0``. By default, these values are set to 0.0 and 0.5 on a newly created Frame.

Children are able to be added to and removed from the Frame using both::

  frame.add(child)
  frame.remove(child)

=======
Example
=======
Below is an example of a Frame:

.. literalinclude:: _examples/frame.py

Download: :download:`Frame <_examples/frame.py>`
