Button
======
The Button widget is commonly used to allow a user to run a command or operation. It can display text and/or icons and provides an easy way for the user to interact with the application.

===========
Constructor
===========
The Button can be constructed using the following::

  button = Gtk.Button(label)

The *label* parameter used in the first constructor allows the entering of text to display on the Button.

=======
Methods
=======
To set the text on the Button after construction::

  button.set_label(text)

Images can also be set on Button widgets with::

  button.set_image(image)

By default, all Button widgets have a border around them. This can be configured using::

  button.set_relief(relief)

The *relief* parameter can be set as follows, with the default being ``Gtk.BorderRelief.NORMAL``. The alternatives are ``Gtk.ReliefStyle.HALF`` which shows no border when the mouse is not hovering over the widget, or ``Gtk.ReliefStyle.NONE`` in which no border is shown at all.

It is good practice to use a mnemonic in the label. This requires an underscore inserted into the label (e.g. "_Cancel"). GTK+ parses the underscore and converts it into an underline beneath the following character, which the user can then access as a shortcut to the function. This is set via::

  button.set_use_underline(underline)

When *underline* is set to ``True``, the letter after the underscore in the label string will be used as the mnemonic shortcut.

.. note:

  Mnemonic shortcuts are highly useful as an accessibility feature and should be used wherever possible. They are particularly important to people with disabilities as they provide quick access to common functions. To access the function using the mnemonic, hold down :kbd:`ALT` and the appropriate character.

When a Button is clicked, the focus is changed to that of the Button. To prevent this happening the following method can be used::

  button.set_focus_on_click(focus)

If *focus* is set to ``False``, the focus will be retained on whichever widget had it last before clicking the Button.

To force a button to show an image, even if the option is disabled globally, use::

  button.set_always_show_image(show_image)

.. note:

  Using ``.set_always_show_image()`` should only be used when the button functionality would be hard to identify without the image. In other cases, the button should follow the global setting.

=======
Signals
=======
The commonly used signals of a Button are::

  "clicked" (button)
  "pressed" (button)
  "released" (button)

The ``"clicked"`` signal is emitted when the user presses, then releases the mouse button when on the Button. A ``"pressed"`` signal emits when the mouse button is pressed above the Button while ``"released"`` emits when the mouse button is released over the Button. In most cases, the ``"clicked"`` signal should be used.

=======
Example
=======
Below is an example of a Button:

.. literalinclude:: _examples/button.py

Download: :download:`Button <_examples/button.py>`
