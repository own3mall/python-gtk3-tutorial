TextTagTable
============
A TextTagTable is an invisible object which is used to hold :doc:`texttag` objects.

===========
Constructor
===========
The TextTagTable can be constructed using::

  texttagtable = Gtk.TextTagTable()

=======
Methods
=======
TextTag objects can be added and removed from the TextTagTable using::

  texttagtable.add(texttag)
  texttagtable.remove(texttag)

To find a TexTag within the table, use the method::

  texttagtable.lookup(name)

Returning the number of TextTag objects contained within the table can be done with::

  texttagtable.get_size()

=======
Signals
=======
The commonly used signals of a TextTagTable are::

  "tag-added" (texttagtable, tag)
  "tag-removed" (texttagtable, tag)
  "tag-changed" (texttagtable, tag, size_changed)

The ``"tag-added"`` and ``"tag-removed"`` signals emit when a TextTag is added or removed from the table. Both return the name of the TextTag added or removed. The ``"tag-changed"`` signal gets emitted when tags are changed. If the change affects the number of tags contained in the table, the *size_changed* parameter returns ``True``.
