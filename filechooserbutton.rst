FileChooserButton
=================
The FileChooserButton provides access to a :doc:`filechooserdialog`. The button is used when space is limited to allow selecting of a file.

===========
Constructor
===========
The FileChooserButton can be constructed using the following::

  filechooserbutton = Gtk.FileChooserButton(action)

The *action* parameter should be set to either ``Gtk.FileChooserAction.OPEN`` which allows opening of files, ``Gtk.FileChooserAction.SAVE`` which allows files to be saved, ``Gtk.FileChooserAction.SELECT_FOLDER`` which enables selecting of folders and ``Gtk.FileChooserAction.CREATE_FOLDER`` which creates folders based on a specified name.

=======
Methods
=======
To specify a title on the dialog that appears, use the method::

  filechooserbutton.set_title(title)

.. note::

  The FileChooserButton inherits methods from the :doc:`filechooser` object.

=======
Signals
=======
The signals used by the FileChooserButton are::

  "file-set" (filechooserbutton)

When the user picks a file, the ``"file-set"`` signal emits.

=======
Example
=======
Below is an example of a FileChooserButton:

.. literalinclude:: _examples/filechooserbutton.py

Download: :download:`FileChooserButton <_examples/filechooserbutton.py>`
