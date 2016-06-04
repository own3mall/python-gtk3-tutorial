FileChooserWidget
=================
A FileChooserWidget provides a widget for selecting files and folders from disks and network shares.

.. note:

  In most cases, a FileChooserWidget would not be needed. A :doc:`filechooserdialog` and :doc:`filechooserbutton` will most commonly be used.

===========
Constructor
===========
The FileChooserWidget can be constructed using the following::

  filechooserwidget = Gtk.FileChooserWidget(action)

The *action* parameter dictates what the FileChooserWidget can do. It should be set to one of ``Gtk.FileChooserAction.OPEN`` which allows opening of files, ``Gtk.FileChooserAction.SAVE`` which allows files to be saved, ``Gtk.FileChooserAction.SELECT_FOLDER`` which enables selecting of folders and ``Gtk.FileChooserAction.CREATE_FOLDER`` which creates folders based on a specified name.

=======
Methods
=======

.. note::

  The FileChooserWidget inherits methods from the :doc:`filechooser` object.

=======
Example
=======
Below is an example of a FileChooserWidget:

.. literalinclude:: _examples/filechooserwidget.py

Download: :download:`FileChooserWidget <_examples/filechooserwidget.py>`
