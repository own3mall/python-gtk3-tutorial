TextMark
========
A TextMark is an object used within a :doc:`textbuffer` to preserve a location within text. It remains valid across changes to the buffer, including insertion or deletion of text around the TextMark.

===========
Constructor
===========
The TextMark can be constructed using the following::

  textmark = Gtk.TextMark(name, left_gravity)

The *name* parameter should specify a unique name which identifies the TextMark. Alternatively, it can be set to ``None`` to provide an anonymous TextMark. The *left_gravity* attribute should be a Boolean value, and when set to ``False``, forces the TextMark to the right when text is inserted.

=======
Methods
=======
To enable a TextMark to be visible via a horizontal line placed in the text, use::

  textmark.set_visible(visible)

By default, TextMark objects are not visible, however specifying ``True`` will show them within the TextView.

We can also check on the visibility status of a TextMark via::

  textmark.get_visible()

To retrieve the name of a TextMark call::

  textmark.get_name()

If the TextMark wasn't given a name at construction time, ``None`` will be returned as the name.

A check on whether a TextMark has been deleted can be made using::

  textmark.get_deleted()

If ``True`` is returned, the TextMark has been deleted.
