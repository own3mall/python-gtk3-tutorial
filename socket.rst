Socket
======
A Socket object provides an object for embedding a :doc:`plug`. The Socket is run in a separate process, and the functionality is transparent to the user.

===========
Constructor
===========
The Socket can be constructed using the following::

  socket = Gtk.Socket()

=======
Methods
=======
To retrieve the window ID of the Socket call::

  socket.get_id()

When ``.get_id()`` is called, the unique identifier is for the running socket is returned.

.. note: Before using the ``.get_id()`` method the Socket must have already been added to the toplevel window.

=======
Signals
=======
The commonly used signals of an Socket are::

  "plug-added" (socket)
  "plug-removed" (socket)

The ``"plug-added"`` and ``"plug-removed"`` signals are emitted when the Plug is connected or disconnected from the Socket. In both cases, the Socket on which the Plug was connected is passed.

=======
Example
=======
Below is an example of a Socket:

.. note:

  To test the Socket example correctly, you will also need to run the Plug example. The steps to execute this correctly are to run the Socket example from the terminal. This will return a value identifying the Socket. The Plug example should then be run with the value specified as an argument.

.. literalinclude:: _examples/socket.py

Download: :download:`Socket <_examples/socket.py>`
