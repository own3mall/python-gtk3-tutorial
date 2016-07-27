CheckButton
===========
A CheckButton displays a small box which is allowed to be in one of three states; checked, unchecked or inconsistent. It is displayed with a :doc:`label` next to it indicating what function the CheckButton performs.

A CheckButton is based on the :doc:`togglebutton` widget, and inherits many of the same methods, properties and signals.

===========
Constructor
===========
The CheckButton can be constructed using::

  checkbutton = Gtk.CheckButton(label)

The *label* parameter allows the associated text to be defined at construction time.

=======
Methods
=======
The label on the CheckButton is definable after construction via::

  checkbutton.set_label(label)

It is good practice to use a mnemonic in the label. This requires an underscore inserted into the label (e.g. "_Cancel"). GTK+ parses the underscore and converts it into an underline beneath the following character, which the user can then access as a shortcut to the function. This is set via::

  checkbutton.set_use_underline(underline)

When *underline* is set to ``True``, the letter after the underscore in the label string will be used as the mnemonic shortcut.

.. note:

  Mnemonic shortcuts are highly useful as an accessibility feature and should be used wherever possible. They are particularly important to people with disabilities as they provide quick access to common functions. To access the function using the mnemonic, hold down :kbd:`ALT` and the appropriate character.

By default, the CheckButton will be in the inactive (unchecked) state. To set the state the following can be used::

  checkbutton.set_active(active)

The *active* parameter should be set to either ``True`` which sets the CheckButton to ticked, or ``False`` which is unticked.

To retrieve the state of the CheckButton::

  checkbutton.get_active()

In some cases, the CheckButton may be set to an inconsistent state, which is used to indicate the status of other CheckButton widgets. For example, three CheckButton's may be a mix of checked and unchecked, which leaves the fourth set as inconsistent. This can be set programatically with::

  checkbutton.set_inconsistent(inconsistent)

To retrieve whether a CheckButton is set as inconsistent use::

  checkbutton.get_inconsistent()

If the CheckButton is in an inconsistent state, ``True`` will be returned.

=======
Signals
=======
The commonly used signals of a CheckButton are::

  "toggled" (checkbutton)

A ``"toggled"`` signal emits from the CheckButton when the mode is changed to active or inactive.

========
Examples
========
Below is an example of a CheckButton:

.. literalinclude:: _examples/checkbutton.py

Download: :download:`CheckButton <_examples/checkbutton.py>`
