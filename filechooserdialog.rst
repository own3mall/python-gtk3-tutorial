FileChooserDialog
=================
A FileChooserDialog provides a FileChooserWidget within a dialog window.

The dialog-variant of the FileChooser allows for selecting of files and folders.

===========
Constructor
===========
The FileChooserDialog can be constructed using the following::

  filechooserdialog = Gtk.FileChooserDialog(action, buttons)

The *action* parameter should be set to either ``Gtk.FileChooserAction.OPEN`` which allows opening of files, ``Gtk.FileChooserAction.SAVE`` which allows files to be saved, ``Gtk.FileChooserAction.SELECT_FOLDER`` which enables selecting of folders and ``Gtk.FileChooserAction.CREATE_FOLDER`` which creates folders based on a specified name. The *buttons* pareameter is a tuple of buttons and response_id values which will be displayed in the dialog.

=======
Methods
=======
Once the FileChooserDialog has been constructed use::

  filechooserdialog.run()
  filechooserdialog.destroy()

.. note::

  If your application only uses a FileChooserDialog, the ``Gtk.main()`` call is not required. This is invoked automatically when calling ``filechooserdialog.run()``.

The title of the dialog which is displayed can be set with::

  filechooserdialog.set_title(title)

When using a FileChooserDialog, the parent window should be defined. This ensures correct positioning of the dialog when it appears::

  filechooserdialog.set_parent(parent)

Generally, the *parent* parameter will be a :doc:`window` or some other dialog type.

.. note::

  The FileChooserDialog inherits methods from the :doc:`filechooser` object.

=======
Example
=======
Below is an example of a FileChooserDialog:

.. literalinclude:: _examples/filechooserdialog.py

Download: :download:`FileChooserDialog <_examples/filechooserdialog.py>`
