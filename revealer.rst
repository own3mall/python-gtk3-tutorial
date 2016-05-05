Revealer
========
The Revealer widget behaves similar to an :doc:`expander`, however does this using an animation. The child widget can be hidden or unhidden based on the action of another widget such as a button.

===========
Constructor
===========
The Revealer is constructed using the following::

  revealer = Gtk.Revealer()

=======
Methods
=======
Child widgets are added to the Revealer using::

  revealer.add(child)

The item can also be removed from the container via::

  revealer.remove(child)

By default, the Revealer is collapsed. To configure whether it is expanded or collapsed use::

  revealer.set_reveal_child(revealed)

If *revealed* is set to ``True``, the Revealer expands to reveal the child widget. When ``False`` is specified, the Revealer is collapsed again.

A number of transition types can be used to animate the Revealer using the method::

  revealer.set_transition_type(transition_type)

The *transition_type* can be set to one of the following:

* ``Gtk.TransitionType.NONE``
* ``Gtk.TransitionType.CROSSFADE``
* ``Gtk.TransitionType.SLIDE_RIGHT``
* ``Gtk.TransitionType.SLIDE_LEFT``
* ``Gtk.TransitionType.SLIDE_UP``
* ``Gtk.TransitionType.SLIDE_DOWN``

The duration of the animation can also be configured::

  revealer.set_transition_duration(duration)

The *duration* value is a value in milliseconds. By default, the Revealer takes 250 milliseconds to complete the transition.

=======
Example
=======
Below is an example of a Revealer:

.. literalinclude:: _examples/revealer.py

Download: :download:`Revealer <_examples/revealer.py>`
