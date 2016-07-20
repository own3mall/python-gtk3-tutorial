Switch
======
A Switch widget provides a toggle which enables or disables depending on the position of the widget. It is commonly used to indicate the status of a hardware device.

===========
Constructor
===========
The Switch can be constructed using::

  switch = Gtk.Switch()

=======
Methods
=======
To retrieve the state of the Switch as a True or False value::

  switch.get_active()

Alternatively, to set a state on the Switch programmatically::

  switch.set_active(active)

If *active* is set to True, the Switch will be in the On position.

==========
Properties
==========
The height of the slider can be configured with the ``"slider-height"`` property. The default value is 22, with allowed values greater than 22::

  switch.set_property("slider-height", height)

The width can also be defined via ``"slider-width"`` with allowed values greater than the default of 36::

  switch.set_property("slider-width", width)

=======
Signals
=======
The commonly use signals of a Switch are::

  "notify::active" (switch, state)

The ``"notify::active"`` signal emits when the Switch is toggled to either the on or off states.

=======
Example
=======
Below is an example of a Switch:

.. literalinclude:: _examples/switch.py

Download: :download:`Switch <_examples/switch.py>`
