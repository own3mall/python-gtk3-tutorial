AccelGroup
==========
An AccelGroup represents a group of accelerators which provide access to functions via the keyboard.

===========
Constructor
===========
The AccelGroup can be constructed using::

  accelgroup = Gtk.AccelGroup()

=======
Methods
=======
An accelerator is connected to the AccelGroup using the call::

  accelgroup.connect(accel_key, modifiers, flags, closure)

A previously connected accelerator can also be disconnected by::

  accelgroup.disconnect(closure)

To allow or prevent changes to the Accelerator's within the AccelGroup use::

  accelgroup.lock()
  accelgroup.unlock()

The AccelGroup can also be checked to see whether it is locked using::

  accelgroup.get_is_locked()

If ``True`` is returned from the method, no accelerators may be added to the AccelGroup.

=======
Example
=======
For an example of an AccelGroup, see the :doc:`accellabel` page.
