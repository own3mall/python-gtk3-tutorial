ButtonBox
=========
A ButtonBox is an invisible object which allows for manipulation and placement of Button widgets. This is commonly used in preference dialogs which have button widgets in a particular order with certain spacing requirements. There are two varieties of ButtonBox; horizontal and vertical.

===========
Constructor
===========
The ButtonBox can be constructed using the following::

  buttonbox = Gtk.ButtonBox(orientation)

The *orientation* argument should be set to either ``Gtk.Orientation.HORIZONTAL`` or ``Gtk.Orientation.VERTICAL``. However, the default for the ButtonBox is the horizontal mode.

=======
Methods
=======
Button widgets (or other widgets if required) can be added to the ButtonBox using::

  buttonbox.add(child)

They can also be removed if needed by calling::

  buttonbox.remove(child)

A child can be reordered within the ButtonBox via the method::

  buttonbox.reorder_child(child, position)

The *child* specified the child widget to be moved, with the *position* value set as an integer for the new position within the ButtonBox.

ButtonBox supports a number of layouts to customise the appearance of your application. This is done by using::

  buttonbox.set_layout(layout)

The *layout* parameter must be set to one of the following: ``Gtk.ButtonBoxStyle.SPREAD`` forces the buttons to spread out over the maximum space they have available. ``Gtk.ButtonBoxStyle.EDGE`` places the buttons at the edges of the ButtonBox. ``Gtk.ButtonBoxStyle.START`` and ``Gtk.ButtonBoxStyle.END`` place buttons at the start or end of the ButtonBox, depending on the container orientation in use. ``Gtk.ButtonBoxStyle.CENTER`` places buttons in the middle of the ButtonBox container.

By default, there is no spacing between each button with the ButtonBox. This can be configured with::

  buttonbox.set_spacing(spacing)

In some cases it is useful to have a button within the ButtonBox be positioned seperately from the other buttons. This is commonly used for 'Help' or 'About' buttons, and can be set by doing::

  buttonbox.set_child_secondary(child, is_secondary)

The *child* parameter is the name of the Button which is to be positioned separately. Setting the *is_secondary* parameter to ``True`` will separate the button.

By default, all buttons within the ButtonBox are homogeneous. It may be necessary to force one button to be non-homogeneous (for size reasons). This is achievable with::

  buttonbox.set_child_non_homogeneous(child, non_homogeneous)

The *child* parameter is the name of the Button which is to be set as non-homogeneous. The *non_homogeneous* argument should be set to ``True`` to exempt the child from being homogeneous with the other child buttons.

=======
Example
=======
Below is an example of a ButtonBox:

.. literalinclude:: _examples/buttonbox.py

Download: :download:`ButtonBox <_examples/buttonbox.py>`
