ScaleButton
===========
A ScaleButton provides a :doc:`scale` which can be accessed via clicking a button which provides a popup menu showing the scale.

===========
Constructor
===========
The ScaleButton can be constructed using::

  scalebutton = Gtk.ScaleButton(size, min_value, max_value, step, icons)

The *size* parameter indicates the size of the icons within the ScaleButton. The constant should be set to one of the following; ``Gtk.IconSize.INVALID``, ``Gtk.IconSize.MENU``, ``Gtk.IconSize.SMALL_TOOLBAR``, ``Gtk.IconSize.LARGE_TOOLBAR``, ``Gtk.IconSize.BUTTON``, ``Gtk.IconSize.DND``, or ``Gtk.IconSize.DIALOG``. The *min_value*, *max_value* and, *step* values should be set to integers which indicate the minimum and maximum values on the scale, along with the increase and decrease in the value when the + or - buttons are pressed. Finally, the *icons* parameter should be a tuple, which indicates the icons shown when the scale changes.

=======
Methods
=======
To retrieve the value from the ScaleButton run::

  scalebutton.get_value()

Alternatively, to set the value use::

  scalebutton.set_value(value)

If an :doc:`adjustment` is required to be used with the ScaleButton, this can be specified with::

  scalebutton.set_adjustment(adjustment)

The apply icons to the ScaleButton which are adjusted when the scale changes, these can be specified using::

  scalebutton.set_icons(icons)

The *icons* value is a tuple, which lists the icons that should be shown on the ScaleButton.

=======
Example
=======
Below is an example of a ScaleButton:

.. literalinclude:: _examples/scalebutton.py

Download: :download:`ScaleButton <_examples/scalebutton.py>`
