Expander
========
The MenuButton widget displays a menu when the button is clicked.

===========
Constructor
===========
The MenuButton can be constructed using the following::

  menubutton = Gtk.MenuButton()

=======
Methods
=======
Text labels are set onto the MenuButton with the method::

  menubutton.set_label(label)

The label text in most cases will also have a mnemonic shortcut for keyboard accessibility which is defined by using an underscore prior to the character to be used for the shortcut. This feature is enabled with::

  menubutton.set_use_underline(use_underline)

.. note:

  Mnemonic shortcuts are highly useful as an accessibility feature and should be used wherever possible. They are particularly important to people with disabilities as they provide quick access to common functions. To access the function using the mnemonic, hold down :kbd:`Alt` and the appropriate character.

A MenuButton can have a :doc:`menu` added to it::

  menubutton.set_popup(menu)

By default, the menu appears beneath the MenuButton, however this can be configured::

  menubutton.set_direction(direction)

The *direction* parameter can be set to one of the following:

* ``Gtk.ArrowType.NONE``
* ``Gtk.ArrowType.DOWN``
* ``Gtk.ArrowType.UP``
* ``Gtk.ArrowType.LEFT``
* ``Gtk.ArrowType.RIGHT``

=======
Example
=======
Below is an example of a MenuButton:

.. literalinclude:: _examples/menubutton.py

Download: :download:`MenuButton <_examples/menubutton.py>`
