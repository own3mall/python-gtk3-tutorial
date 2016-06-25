Viewport
========
A Viewport adds the ability to scroll widgets which do not natively support scrolling (e.g. Grid, Box).

===========
Constructor
===========
The Viewport can be constructed using the following::

  viewport = Gtk.Viewport(hadjustment, vadjustment)

The *hadjustment* and *vadjustment* parameters are optional and can be specified :doc:`adjustment` objects.

=======
Methods
=======
Rather than create Adjustment objects manually, these can be retrieved from the Viewport with::

  viewport.get_hadjustment()
  viewport.get_vadjustment()

If you do use manually created Adjustment objects, these can be attached after construction by calling::

  viewport.set_hadjustment(hadjustment)
  viewport.set_vadjustment(vadjustment)

The shadow type places a shadow type around the Viewport, and is set via::

  viewport.set_shadow_type(shadow)

The *shadow* should be set to one of the following:

* ``Gtk.ShadowType.NONE`` - no outline.
* ``Gtk.ShadowType.IN`` - outline bevelled inwards.
* ``Gtk.ShadowType.OUT`` - outline bevelled outwards.
* ``Gtk.ShadowType.ETCHED_IN`` - outline sunken.
* ``Gtk.ShadowType.ERCHED_OUT`` - outline raised.

The window objects which are created with the Viewport can be obtained via the methods::

  viewport.get_bin_window()
  viewport.get_view_window()

The ``.get_bin_window()`` method returns the window of the entire Viewport. The ``.get_view_window()`` method returns the window holding the content of the Viewport.

=======
Example
=======
Below is an example of a Viewport:

.. literalinclude:: _examples/viewport.py

Download: :download:`Viewport <_examples/viewport.py>`
