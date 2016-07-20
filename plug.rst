Plug
====
A Plug object allows an interface to be embedded in a parent (known as a :doc:`socket`) to provide a frontend which is run in a separate process.

.. note::

  A Plug and Socket can also be used on an X11 supported system (e.g. Linux, BSD, Solaris).

===========
Constructor
===========
The Plug can be constructed using the following::

  plug = Gtk.Plug.new(socket_id)

When a Socket is created, it will return a *socket_id* value which identifies itself uniquely. The *socket_id* should be converted into an integer value.

=======
Methods
=======
The ID number of a Plug can be retrieved via::

  plug.get_id()

To check whether a Plug is currently embedded in a Socket use::

  plug.get_embedded()

When the Plug is embedded, the ``.get_embedded()`` method returns ``True``. If the plug has not been inserted, ``False`` is returned.

=======
Signals
=======
The commonly used signals of an Plug are::

  "embedded" (plug)

An "embedded" event is emitted from the Plug when it is attached to a Socket. When the signal occurs, the Plug is passed as part of the event.

=======
Example
=======
Below is an example of a Plug:

.. note:

  To test the Socket example correctly, you will also need to run the Plug example. The steps to execute this correctly are to run the Socket example from the terminal. This will return a value identifying the Socket. The Plug example should then be run with the value specified as an argument.

.. literalinclude:: _examples/plug.py

Download: :download:`Plug <_examples/plug.py>`
