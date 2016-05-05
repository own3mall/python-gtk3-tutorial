LevelBar
========
The LevelBar widget can be used as a level indicator. Typical usage cases would be displaying the strength of a password or the charge of a battery.

===========
Constructor
===========
The LevelBar is constructed with the following::

  levelbar = Gtk.LevelBar()

Minimum and maximum values of the LevelBar can also be specified when the widget is constructed via::

  levelbar = Gtk.LevelBar.new_for_interval(min_value, max_value)

The *min_value* and *max_value* should be integers which define the minimum and maximum permissable values the LevelBar allows.

=======
Methods
=======
A minimum and maximum value should be set on the LevelBar which defines the range of values which can be entered::

  levelbar.set_min_value(value)
  levelbar.set_max_value(value)

If required, the minimum and maximum values can also be retrieved::

  levelbar.get_min_value()
  levelbar.get_max_value()

The actual level can then be displayed::

  levelbar.set_value(value)

To retrieve the value from the levelbar, use the method::

  levelbar.get_value()

The update mode of the LevelBar indicates how the widget updates when the value is changed. There are two modes for this::

  levelbar.set_mode(mode)

The *mode* value can be set to either ``Gtk.LevelBarMode.CONTINUOUS``. This updates the LevelBar continuously with each update. Alternatively, ``Gtk.LevelBarMode.DISCRETE`` causes the LevelBar to update when the LevelBar stops value stops changing for a short time.

By default, horizontal LevelBar widgets fill from left-to-right, and vertical widgets update from bottom-to-top. This operation can be inverted however via::

  levelbar.set_inverted(inverted)

A LevelBar provides an offset value which places a marker on the widget for a specified value.

  levelbar.add_offset_value(name, value)

The *name* parameter is a textual name identifying the offset value. The *value* itself can be either an integer or decimal. When an offset value with the same name is provided, the existing value is overwritten.

To remove the offset value, call::

  levelbar.remove_offset_value(name)

Finally, retrieval of the offset value is possible via::

  levelbar.get_offset_value(name)

=======
Signals
=======
The commonly used signals of a LevelBar are::

  "offset-changed" (name)

Whenever an offset value associated with the LevelBar is changed, the ``"offset-changed"`` is emitted, along with the name of the offset which has been adjusted.

=======
Example
=======
Below is an example of a LevelBar:

.. literalinclude:: _examples/levelbar.py

Download: :download:`LevelBar <_examples/levelbar.py>`
