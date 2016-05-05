FileFilter
==========
A FileFilter object is used in conjunction with FileChooser-based widgets, to limit the type of files which can be viewed. For example, to limit a FileChooser to only view music files, a FileFilter can be used.

===========
Constructor
===========
The FileFilter can be constructed using the following::

  filefilter = Gtk.FileFilter()

.. note::

  A FileFilter must be created for each file type which is to be filtered.

=======
Methods
=======
To set the name of the FileFilter use::

  filefilter.set_name(name)

Retrieving the name of a particular filter is possible using::

  filefilter.get_name()

To limit files which can be displayed by extension use::

  filefilter.add_pattern(pattern)

The *pattern* parameter should be a string, which uses wildcard entries. For example using ``"*.flac"`` would permit only files which end with the .flac extension.

Files can also be limited according to their mime-type::

  filefilter.add_mime_type(mime_type)

A *mime_type* is a content filter which uses content within the header of the file to identify it. Example of a mime types are ``"image/png"``, ``"video/mp4"``, and ``"text/html"``.

=======
Example
=======
Below is an example of a FileFilter:

.. literalinclude:: _examples/filefilter.py

Download: :download:`FileFilter <_examples/filefilter.py>`
