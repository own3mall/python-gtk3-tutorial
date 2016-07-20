TextBuffer
==========
A TextBuffer is a backend object which is used in conjuction with a :doc:`textview`. It allows for text to be stored and shared across multiple TextView widgets.

===========
Constructor
===========
The TextTag can be constructed using::

  textbuffer = Gtk.TextBuffer()

.. note:: A TextBuffer object is automatically created when using a TextView, and does not need to be constructed separately in most cases.

=======
Methods
=======
Applying text to the TextBuffer can be done directly using::

  textbuffer.set_text(text, length)

The *text* argument should be the string of text which is to be added. Setting the *length* argument allows limiting the string to a set number of characters. This can be set to ``-1`` if no limit is required.

The text stored in the buffer may be retrieved with::

  textbuffer.get_text(start, end, include_hidden_chars)

The *start* and *end* arguments should be set to TextIter objects which specify the range of text to retrieve. The *include_hidden_chars* parameter when set to ``True`` allows hidden characters to also be retrieved.

Retrieving the entire boundary of text can be completed with::

  textbuffer.get_bounds()

The start and end values returned are TextIter objects which identify the start and end locations of the content.

Alternatively, to retrieve a selection that a user has made issue the method::

  textbuffer.get_selection_bounds()

As with the ``.get_bounds()`` method, this returns a *start* and *end* TextIter object which identifies the selection of the text.

The TextIter start and end objects can also be retrieved individually::

  textbuffer.get_start_iter()
  textbuffer.get_end_iter()

Checking whether the TextBuffer has a selection can be done via::

   textbuffer.get_has_selection()

To retrieve the number of words and characters contained within the buffer use::

  textbuffer.get_word_count()
  textbuffer.get_char_count()

Checking whether a TextBuffer has been modified can be done with::

  textbuffer.get_modified()

To set whether the TextBuffer has been changed use::

  textbuffer.set_modified(modified)

Setting the *modified* argument to ``False`` is commonly used after a document has been saved and the TextBuffer status needs to be set back to unmodified.
