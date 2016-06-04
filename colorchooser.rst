ColorChooser
============
The ColorChooser interface is implemented by :doc:`colorchooserdialog`, :doc:`colorchooserwidget` and :doc:`colorbutton` to allow a user to select a colour.

=======
Methods
=======
By default, only colours can be selected within the ColorChooser. To enable setting of transparency call::

  colorchooser.set_use_alpha(use_alpha)

When *use_alpha* is set to ``True``, a slider appears within the dialog to control the amount of transparency.

To retrieve the colour from the ColorChooser use::

  colorchooser.get_color()
  colorchooser.get_rgba()

The ``.get_color()`` method returns a GdkColor object with associated values for red, green and blue. Alternatively, if your ColorChooser allows the selection of transparency values then ``.get_rgba()`` can be used. This also returns values for red, green and blue, and the transparency value, and is known as an GdkRGBA object. All the values returned are between ``0.0`` and ``1.0``.

Colours can also be set specifically on the ColorChooser with::

  colorchooser.set_color(color)
  colorchooser.set_rgba(rgba)

The *color* and *rgba* parameters should be set to the appropriate GdkColor or GdkRGBA objects which specify the values to be used.

=======
Signals
=======
The common signals of the ColorChooser are::

  "color-activated" (colorchooser, color)

The *color* value is returned when the user activates the colour in the chooser, emitting the ``"color-activated"`` signal.

=======
Example
=======
To view an example of the ColorChooser, see the code for the objects :doc:`colorchooserwidget`, :doc:`colorchooserdialog`, and :doc:`colorbutton`.
