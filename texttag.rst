TextTag
=======
A TextTag can be applied to text contained within a :doc:`textbuffer`. It allows many properties to be applied to the text marked by the TextTag.

TextTag objects are applied to a :doc:`texttagtable`.

===========
Constructor
===========
The TextTag can be constructed using::

  texttag = Gtk.TextTag(name)

A *name* must be applied to the TextTag to identify it. Ideally, it should be descriptive of the properties that the TextTag affects.

=======
Methods
=======
TextTag objects use priorities to control in which order properties are applied::

  texttag.set_priority(priority)

The *priority* is an integer with ``0`` identifying the most important, and the maximum being the number of tags within the TextTagTable minus one.

Retrieving the priorty can be completed with::

  texttag.get_priority()

The properties should then be applied to the TextTag via::

  texttag.set_property("property", value)

The *property* value identifies the change the TextTag will make, whereas *value* is used to set how much the property will change.

==========
Properties
==========
The most common properties that are used with a TextTag are:

* ``"font"`` - a textual string identifying the font type to use
* ``"editable"`` - when the value set to ``True``, allows the user to edit the text within the cell
* ``"justification"`` - can be set to one of ``Gtk.Justification.LEFT``, ``Gtk.Justification.RIGHT``, ``Gtk.Justification.CENTER``, or ``Gtk.Justification.FILL``
* ``"left-margin"`` - a integer value specifying the number of pixels of margin width
* ``"right-margin"`` - a integer value specifying the number of pixels of margin width
* ``"size"`` - an integer providing the text size in Pango units
* ``"size-points"`` - decimal value which sets the text size in points
* ``"strikethrough"`` - specifying this value as ``True`` places a line through the selected text
* ``"underline"`` - setting to ``True`` places a line under the specified text
* ``"wrap-mode"`` - describes the line wrapping when set to either ``Gtk.WrapMode.NONE``, ``Gtk.WrapMode.CHAR``, ``Gtk.WrapMode.WORD``, or ``Gtk.WrapMode.WORD_CHAR``
