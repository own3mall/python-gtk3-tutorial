FileChooser
===========
The FileChooser is an interface which is used by :doc:`filechooserbutton`, :doc:`filechooserwidget`, and :doc:`filechooserdialog` and is constructed when those objects are constructed.

.. note:

  This widget would generally not be called by the application directly. However, the methods it offers are common among the three objects :doc:`fontchooserwidget`, :doc:`fontchooserdialog`, and :doc:`fontbutton`.

=======
Methods
=======
The default action of the FileChooser is to provide functionality to open files.

  filechooser.set_action(action)

The *action* value should be set to one of the following:

* ``Gtk.FileChooserAction.OPEN`` - FileChooser will be used to open a file.
* ``Gtk.FileChooserAction.SAVE`` - FileChooser will be used to save a file.
* ``Gtk.FileChooserAction.SELECT_FOLDER`` - FileChooser will be used to select a folder.
* ``Gtk.FileChooserAction.CREATE_FOLDER`` - FileChooser will be used to create a folder.

By default, the FileChooser allows selection of a single file only. This can be configured with::

  filechooser.set_select_multiple(select_multiple)

The *select_multiple* can be set to ``True`` which allows the user to hold down :kbd:`Control` and select the items with the mouse.

Retreival of the selected filename or uniform resource identifier (URI) is done via::

  filechooser.get_filename()
  filechooser.get_uri()

Alternatively, if you have provided the ability for multiple files to be selected, you must use::

  filechooser.get_filenames()
  filechooser.get_uris()

Another useful function, particular when saving files is to predefine a filename or uri for the file, for example "Unsaved Document".

  filechooser.set_filname(filename)
  filechooser.set_uri(uri)

To configure whether the button to create new folders is visible, call::

  filechooser.set_create_folders(create_folders)

The *create_folders* option should be set to ``False`` if the button is to be hidden.

.. note:

  The ``.set_create_folders()`` option does not apply when the action ``Gtk.FileChooserAction.OPEN parameter is used.

In some cases, the FileChooser should only open local files. This is settable with::

  filechooser.set_local_only(local_only)

A :doc:`filefilter` is able to be added to or removed from the FileChooser by specifying::

  filechooser.add_filter(filefilter)
  filechooser.remove_filter(filefilter)

The list of FileFilter objects associated with the FileChooser can be obtained through::

  filechooser.list_filters()

=======
Signals
=======
The common signals of the FileChooser are as follows::

  "file-activated" (filechooser)

The ``"file-activated"`` signal emits when the user double-clicks a file, or selects a file and presses :kbd:`Enter`.

=======
Example
=======
To view an example for this widget, see the :doc:`filechooserwidget`, :doc`filechooserdialog`, or :doc:`filechooserbutton` examples.
