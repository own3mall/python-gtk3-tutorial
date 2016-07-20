SpinButton
==========
A SpinButton provides an Entry with two associated Button widgets that allow numerical values to be entered via the keyboard, or selected by moving up or down.

===========
Constructor
===========
A SpinButton can be constructed using the following::

  spinbutton = Gtk.SpinButton(adjustment, climb_rate, digits)

The *adjustment* parameter should be set to the name of an Adjustment object which determines the minimum and maximum values. Setting the *climb_rate* controls how fast the values change when the up or down buttons are held. The *digits* parameter is an integer value that when set controls how many numbers after the decimal point are shown.

=======
Methods
=======
The value within the SpinButton can be retrieved using one of the following::

  spinbutton.get_value()
  spinbutton.get_value_as_int()

When using ``.get_value_as_int()``, the number retrieved from the SpinButton will be in integer format. Alternatively, use ``.get_value()`` if the number needs to be returned as a decimal.

Setting of the value within the SpinButton is possible with::

  spinbutton.set_value(value)

The number of digits which will be displayed in the SpinButton can be set as::

  spinbutton.set_digits(digits)

To set the Adjustment after construction::

  spinbutton.set_adjustment(adjustment)

The update method can be configured with::

  spinbutton.set_update_policy(policy)

When *policy* is set to ``Gtk.UpdatePolicy.ALWAYS``, the SpinButton will display any content entered, even if it is not valid (i.e. out of range, alphabetical, etc). Alternatively, if ``Gtk.UpdatePolicy.UPDATE_IF_VALID`` is used, the SpinButton will revert to the last 'good' value if the content entered is invalid.

Control over whether non-numeric data can be entered is set with::

  spinbutton.set_numeric(numeric)

The *numeric* parameter is a Boolean value which when set to ``False``, allows alphabetical characters to be entered and accepted.

If a number out of range (higher than the maximum, lower than the minimum), the SpinButton can be configured to adjust the opposite limit value with::

  spinbutton.set_wrap(wrap)

The *wrap* parameter should be set to ``True`` to enable the value wrapping feature. By default, this is set to ``False`` meaning that if a number out of range is entered, the SpinButton rounds to the nearest limit.

To force the SpinButton to force the value to the nearest step increment, use::

  spinbutton.set_snap_to_ticks(snap)

The SpinButton can be span programmatically using::

  spinbutton.spin(direction, increment)

The *direction* value indicates which way the SpinButton will move. This should be a constant from:

* ``Gtk.Spin.STEP_FORWARD``
* ``Gtk.Spin.STEP_BACKWARD``
* ``Gtk.Spin.PAGE_FORWARD``
* ``Gtk.Spin.PAGE_BACKWARD``
* ``Gtk.Spin.HOME``
* ``Gtk.Spin.END``
* ``Gtk.Spin.USER_DEFINED``

The *increment* parameter is the value by which the SpinButton will change.

To manually force an update to the SpinButton::

  spinbutton.update()

=======
Signals
=======
The commonly used signals of a SpinButton are::

  "value-changed" (spinbutton)

The ``"value-changed"`` emits from the widget when the value contained within the SpinButton is adjusted, either via text entry or the adjusting buttons.

=======
Example
=======
Below is an example of a SpinButton:

.. literalinclude:: _examples/spinbutton.py

Download: :download:`SpinButton <_examples/spinbutton.py>`
