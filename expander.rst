Expander
========
An Expander allows seldom used content to be hidden until the user requests it to be displayed. This can be useful for configuration settings which should be changed rarely.

===========
Constructor
===========
The Expander can be constructed using the following::

  expander = Gtk.Expander(label)

The *label* parameter must be set to a textual string which identifies what the Expander is or contains.

=======
Methods
=======
Items can be added to the Expander widget with::

  expander.add(child)

The *child* can be set to any widget type, however it is typical for a Grid or Box to be displayed and other widgets such as Button or Label objects to be added on top of the container.

It can also later be removed via::

  expander.remove(child)

Once a child has been added, it may be necessary add spacing between the top of the Expander and the child content::

  expander.set_spacing(spacing)

The *spacing* value should be an integer identifying the number of pixels worth of space to insert.

To set the Expander label after creation call::

  expander.set_label(label)

A :doc:`label` widget can also be applied if necessary via the method::

  expander.set_label_widget(widget)

To set the Expander to open programatically the following can be called::

  expander.set_expanded(expanded)

When *expanded* is set to ``True``, the Expander will be opened and the child content will be displayed.

Expanding the Expander widget will cause the parent widget (i.e. Window, Dialog) to expand to make room for the content within the Expander. The default action when closing the Expander is to leave the Window at the largest size, rather than shrink to the original. To change this behaviour use::

  expander.set_resize_toplevel(resize)

When *resize* is set to ``True``, the parent will shrink once the Expander is collapsed.

=======
Signals
=======
The commonly used signals of an Expander are::

  "activate" (expander)

The ``"activate"`` signal emits from the Expander when the content is shown or hidden.

=======
Example
=======
Below is an example of a Expander:

.. literalinclude:: _examples/expander.py

Download: :download:`Expander <_examples/expander.py>`
