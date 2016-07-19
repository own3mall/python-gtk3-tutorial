Entry
=====
Entry widgets provide a way for the user to enter text. Usually they are tailored for small amounts of text such as a username, street name, or file name.

===========
Constructor
===========
The Entry can be constructed using::

  entry = Gtk.Entry(entrybuffer)

The *entrybuffer* parameter should be set to an :doc:`entrybuffer` if required. In most cases, it won't be needed and can be omitted.

=======
Methods
=======
The entered text can be retrieved from the Entry with the method::

  entry.get_text()

Text can be inserted into the Entry using::

  entry.set_text(text)

Using the ``.set_text()`` method will overwrite any existing contents in the Entry.

Alternatively, it can be inserted with::

  entry.insert_text(text, length, position)

The *text* value is the string of text to be inserted. The *length* parameter is the length of the new text being inserted, however in most cases using ``-1`` is sufficient; as GTK+ will automatically calculate the length. Finally, the *position* parameter will specify the location in number of characters where the text will be placed.

Text can be removed from the Entry via::

  entry.delete_text(start, end)

The *start* and the *end* values indicate the range of characters to be removed.

The Entry supports returning a string of characters from a requested range::

  entry.get_chars(start, end)

Limiting the number of characters which can be typed into the Entry is set with::

  entry.set_max_length(length)

To prevent editing of the Entry use::

  entry.set_editable(editable)

When set to ``False``, the Entry will not accept any text input.

Entry widgets are useful for receiving password input. However, it is good practice to mask the input as it is being typed to improve security::

  entry.set_visibility(visibility)

When *visibility* is set to ``False``, eah character will be masked with a ``*``.

The mask character can be changed if required via::

  entry.set_invisible_char(character)

By default, when an Entry is focused, the text within the Entry is selected. In cases where the user is not likely to want to replace all the text, an alternative function can be used to provide focus but not select the text::

  entry.grab_focus_without_selecting()

In some cases, it is preferable to have the Entry perform an action when the user presses :kbd:`Enter`. Commonly this would be a continue function in a dialog::

  entry.set_activates_default(activates)

In some cases, it may be useful to include some placeholder text in the Entry, which indicates the purpose of the widget::

  entry.set_placeholder_text(text)

A useful function for web browsers or other widgets which load content is to display a progress bar within the Entry::

  entry.set_progress_fraction(fraction)

The *fraction* value is a number between ``0.0`` and ``1.0`` indicating 0% and 100% respectively.

The width of Entry in characters can be specified using the method::

  entry.set_width_chars(width)

If required, icons can be placed in the Entry. There are two types; primary and secondary. The primary icon is placed on the left side of the Entry, preceding the text. Secondary icons are placed at the right-hand side of the Entry.

  entry.set_icon_from_pixbuf(position, pixbuf)

The *position* value should be set to either ``Gtk.EntryIconPosition.PRIMARY`` or ``Gtk.EntryIconPosition.SECONDARY``. The *pixbuf* value is the image to be inserted.

Icons can also be made insensitive to prevent an action::

  entry.set_icon_sensitive(position, sensitive)

When *sensitive* is set to ``False``, the icon specified will appear greyed-out.

If an icon has been specified, tooltip text can also be set describing the function of the icon.

  entry.set_icon_tooltip_text(position, tooltip)
  entry.set_icon_tooltip_markup(position, tooltip)

The ``.set_icon_tooltip_text()`` takes plain text only. Alternatively, styled text can be specified using ``.set_icon_tooltip_markup()``.

Entry widgets also support input types. This describes the function of the widget, and is useful as an accessibility function.

  entry.set_input_purpose(purpose)

The *purpose* should be set to one of the following values:

* ``Gtk.InputPurpose.FREE_FORM``
* ``Gtk.InputPurpose.ALPHA``
* ``Gtk.InputPurpose.DIGITS``
* ``Gtk.InputPurpose.NUMBER``
* ``Gtk.InputPurpose.PHONE``
* ``Gtk.InputPurpose.URL``
* ``Gtk.InputPurpose.EMAIL``
* ``Gtk.InputPurpose.NAME``
* ``Gtk.InputPurpose.PASSWORD``
* ``Gtk.InputPurpose.PIN``

Hints are also available which allow the input to be tailored as required. This is done via::

  entry.set_input_hints(hints)

The *hints* value can be set to one of:

* ``Gtk.InputHint.NONE`` - no special behaviour.
* ``Gtk.InputHint.SPELLCHECK`` - suggest spell checking for errors.
* ``Gtk.InputHint.NO_SPELLCHECK`` - suggest no spell checking takes place.
* ``Gtk.InputHint.WORD_COMPLETION`` - suggestion word completion should be used.
* ``Gtk.InputHint.LOWERCASE`` - suggest to lowercase all text.
* ``Gtk.InputHint.UPPERCASE_CHARS`` - suggest to capitalise all text.
* ``Gtk.InputHint.UPPERCASE_WORDS`` - suggest to capitalise first letter in all words.
* ``Gtk.InputHint.UPPERCASE_SENTENCES`` - suggest to capitalise first word in each sentence.
* ``Gtk.InputHint.INHIBIT_OSK`` - suggest onscreen keyboard not be shown.
* ``Gtk.InputHint.VERTICAL_WRITING`` - text is vertical.

=======
Signals
=======
The commonly used signals of an Entry are::

  "changed" (entry)
  "activate" (entry)
  "icon-press" (entry, icon_pos, event)
  "icon-release" (entry, icon_pos, event)
  "backspace" (entry)
  "populate-popup" (entry, menu)

The ``"changed"`` signal is emitted whenever there is a change to the Entry. The ``"activate"`` signal is emitted whenever the Enter button is pressed when the Entry has focus. An ``"icon-press"`` signal is emitted when any mouse button is pressed down on either the primary or secondary icons. An ``"icon-release"`` is much the same as ``"icon-press"`` except emits when the mouse button is released. The ``"backspace"`` signal emits whenever the user presses the Backspace key. Using ``"populate-popup"`` allows items to be dynamically places in the context menu of the Entry prior to it being displayed.

========
Examples
========
Below is an example of a Entry:

.. literalinclude:: _examples/entry.py

Download: :download:`Entry <_examples/entry.py>`
