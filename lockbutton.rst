LockButton
==========
A LockButton provides a way for a user to make changes to system settings that require elevated privileges. The widget is packed with a label and icon identifying the unlock and lock actions.

===========
Constructor
===========
The LockButton can be constructed using the following::

  lockbutton = Gtk.LockButton()

=======
Methods
=======
To set the permission of the LockButton use the method::

  lockbutton.set_permission(permission)

The permission value can also be retrived from the LockButton via::

  lockbutton.get_permission()

=======
Example
=======
Below is an example of a LockButton:

.. literalinclude:: _examples/lockbutton.py

Download: :download:`LockButton <_examples/lockbutton.py>`
