FontButton
==========
The FontButton provides access to a :doc:`fontchooserdialog`. The button is used when space is limited to allow selecting of a font.

===========
Constructor
===========
The FontButton can be constructed using the following::

  fontbutton = Gtk.FontButton(title, font)

When the *title* parameter has been specified, the text string is displayed on the dialog which appears when the FontButton has been clicked. Also, a *font* value can be declared to allow a font, style and size option at construction time.

=======
Methods
=======
The title of the dialog which is displayed can be set with::

  fontbutton.set_title(title)

.. note::

  The FontButton inherits methods from the :doc:`fontchooser` object.

=======
Signals
=======
The commonly used signals of an FontButton are::

  "font-set" (fontbutton)

A ``"font-set"`` signal emits from the FontButton when a font has been selected and the OK button has been pressed on the dialog.

If only certain elements of the font selected are required use the following methods::

  fontbutton.get_font_face()
  fontbutton.get_font_size()
  fontbutton.get_font_desc()

=======
Example
=======
Below is an example of a FontButton:

.. literalinclude:: _examples/fontbutton.py

Download: :download:`FontButton <_examples/fontbutton.py>`
