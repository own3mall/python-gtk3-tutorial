ToggleButton
============
A ToggleButton provides a way to indicate three modes of operation; active, inactive and inconsistent. A ToggleButton is used to indicate whether an option is enabled or disabled.

A ToggleButton is based on a :doc:`button` meaning that they use many methods in the same way.

===========
Constructor
===========
A ToggleButton can be constructed using the following::

  togglebutton = Gtk.ToggleButton(label)

=======
Methods
=======
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
