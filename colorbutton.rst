ColorButton
===========
A ColorButton is used to select colour and transparency via a dialog which appears when the user clicks the button. It is commonly used in applications where space is limited.

===========
Constructor
===========
The ColorButton can be constructed using the following::

  colorbutton = Gtk.ColorButton()

=======
Methods
=======
The title of the dialog which appears when clicking on the ColorButton can be set with::

  colorbutton.set_title(title)

.. note::

  The ColorButton inherits methods from the :doc:`colorchooser` object.

========
Examples
========
Below is an example of a ColorButton:

.. literalinclude:: _examples/colorbutton.py

Download: :download:`ColorButton <_examples/colorbutton.py>`
