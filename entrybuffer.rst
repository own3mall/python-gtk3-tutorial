EntryBuffer
===========
An EntryBuffer contains text which can be displayed inside an :doc:`entry`. Its purpose is to allow that text to be shared between multiple Entry widgets.

.. note::

   To use an Entry widget, an EntryBuffer object is not required and in most cases will not be needed.

===========
Constructor
===========
The EntryBuffer can be constructed using the following::

  entrybuffer = Gtk.EntryBuffer(text)

The *text* string may be omitted, however any text entered will be displayed in Entry widgets connected to the EntryBuffer.

=======
Methods
=======
To retrieve text from the EntryBuffer, use the method::

  entrybuffer.get_text()

To set text on the EntryBuffer after construction::

  entrybuffer.set_text(text, n_chars)

The *text* parameter should be set to the text which is to be displayed in the EntryBuffer. The *n_chars* parameter is an integer value limiting the number of characters which can be entered. If there is to be no limit, use ``-1``.

To insert text into the EntryBuffer at a specific position, the following can be used::

  entrybuffer.insert_text(position, text)

The *position* value is the number of characters along the text should be inserted at with ``0`` designated as the beginning of the EntryBuffer. The *text* parameter should be the string of text to be inserted.

Deletion of text from the EntryBuffer can also be done with::

  entrybuffer.delete_text(position, n_chars)

The *position* parameter should be the starting position of the cursor. The *n_chars* parameter indicates the number of characters from the position to be deleted. When set to a negative number, all characters up to the cursor are deleted.

Retrieval of the number of characters currently stored in the EntryBuffer is achieved by using::

  entrybuffer.get_length()

Setting the maximum number of characters that the EntryBuffer can accept construction can be completed with::

  entrybuffer.set_max_length(length)

To check the maximum length the EntryBuffer can accept::

  entrybuffer.get_max_length()

=======
Signals
=======
The commonly used signals of an EntryBuffer are::

  "inserted-text" (buffer, position, chars, n_chars)
  "deleted-text" (buffer, position, n_chars)

The ``"inserted-text"`` and ``"deleted-text"`` signals are activated when textual values are added to or deleted from the EntryBuffer. Both pass the EntryBuffer, the position at which the change occurred, and the number of characters that were added and removed. The ``"inserted-text"`` signal however has an extra value which passes the string of chracters which were inserted.

=======
Example
=======
Below is an example of a EntryBuffer:

.. literalinclude:: _examples/entrybuffer.py

Download: :download:`EntryBuffer <_examples/entrybuffer.py>`
