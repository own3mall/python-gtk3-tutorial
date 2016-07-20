VolumeButton
============
A VolumeButton is used to control the volume within an application. It is very similar to a :doc:`scalebutton`.

===========
Constructor
===========
The VolumeButton can be constructed using::

  volumebutton = Gtk.VolumeButton()

=======
Methods
=======
To retrieve the current value from the VolumeButton use::

  volumebutton.get_value()

Alternatively, to set a particular value run::

  volumebutton.set_value(value)

The *value* argument must be an integer value between ``0`` and ``100``.

=======
Example
=======
Below is an example of a VolumeButton:

.. literalinclude:: _examples/volumebutton.py

Download: :download:`VolumeButton <_examples/volumebutton.py>`
