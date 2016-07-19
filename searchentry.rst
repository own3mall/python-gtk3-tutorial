SearchEntry
===========
The SearchEntry widget provides a tailored interface for searching. Essentially, it is a stardard :doc:`entry` with a find icon when the search field is empty, that then changes to a clear icon when text has been entered. Additional signals are also available which relate to the search functionality.

===========
Constructor
===========
The SearchEntry can be constructed using the following::

  searchentry = Gtk.SearchEntry()

=======
Methods
=======
The text can be retrieved from the SearchEntry::

  searchentry.get_text()

Text can also be added to the SearchEntry with the method::

  searchentry.set_text(text)

Placeholder text can be added to the SearchEntry to describe the function of the widget::

  searchentry.set_placeholder_text(text)

To initiate a default action when the user presses :kbd:`Enter` or :kbd:`Return`, the method used is::

  searchentry.set_activates_default(activates)

Typically, the SearchEntry would only activate a default function when placed in a :doc:`dialog`.

=======
Signals
=======
The commonly used signals of a SearchEntry are::

  "search-changed" (searchentry)
  "next-match" (searchentry)
  "previous-match" (searchentry)
  "stop-search" (searchentry)

The ``"search-changed"`` signal emits each time the user enters a character into the search field after a 150 millisecond delay. The ``"next-match"`` and ``"previous-match"`` signals emit when the user moves between next and previous matches for the search string. Finally, the ``"stop-search"`` is emitted when the user stops a search via keyboard input.

=======
Example
=======
Below is an example of a SearchEntry:

.. literalinclude:: _examples/searchentry.py

Download: :download:`SearchEntry <_examples/searchentry.py>`
