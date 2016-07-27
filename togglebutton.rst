ToggleButton
============
A ToggleButton provides a way to indicate three modes of operation; active, inactive and inconsistent. A ToggleButton is used to indicate whether an option is enabled or disabled.

A ToggleButton is based on a :doc:`button` meaning that they use many methods in the same way.

===========
Constructor
===========
A ToggleButton can be constructed using the following::

  togglebutton = Gtk.ToggleButton(label)

A *label* should be defined which is used to identify the purpose of the ToggleButton widget.

=======
Methods
=======
The ToggleButton label can be set after construction by the method::

  togglebutton.set_label(label)

It is good practice to use a mnemonic in the label. This requires an underscore inserted into the label (e.g. "_Cancel"). GTK+ parses the underscore and converts it into an underline beneath the following character, which the user can then access as a shortcut to the function. This is set via::

  togglebutton.set_use_underline(underline)

When *underline* is set to ``true``, the letter after the underscore in the label string will be used as the mnemonic shortcut.

.. note:

  Mnemonic shortcuts are highly useful as an accessibility feature and should be used wherever possible. They are particularly important to people with disabilities as they provide quick access to common functions. To access the function using the mnemonic, hold down :kbd:`Alt` and the appropriate character.

To retrieve the state of a ToggleButton use::

  togglebutton.get_active()

Setting the state of the ToggleButton programatically can be done with::

  togglebutton.set_active(active)

When *active* is set to ``True``, the ToggleButton will appear in a depressed state.

An inconsistent state can be set on a ToggleButton which can be used to indicate whether other widgets are at the correct values. For example, if three ToggleButtons are a mix of active and inactive, the fourth may display an inconsistent state. This can be retrieved with::

  togglebutton.get_inconsistent()

Set the inconsistent parameter on the following method to ``True`` to activate the inconsistent state::

  togglebutton.set_inconsistent(inconsistent)

=======
Signals
=======
The commonly used signals of an ToggleButton are::

  "toggled" (togglebutton)

When the ToggleButton widget is clicked, the ``"toggled"`` signal is emitted. This occurs when the state is changed from active and inactive, and vice-versa.

=======
Example
=======
Below is an example of a ToggleButton:

.. literalinclude:: _examples/togglebutton.py

Download: :download:`ToggleButton <_examples/togglebutton.py>`
