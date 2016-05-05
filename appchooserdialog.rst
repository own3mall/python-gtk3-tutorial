AppChooserDialog
================
The AppChooserDialog provides a dialog container which allows selecting or opening of applications. The dialog lists applications which are associated with the specified file type.

===========
Constructor
===========
The AppChooserDialog can be constructed using the following::

  appchooserdialog = Gtk.AppChooserDialog(flags, content_type)

The *flags* parameter should be set to ``Gtk.DialogFlags.MODAL`` or ``Gtk.DialogFlags.DESTROY_WITH_PARENT``. The *content_type* value should be set to the mimetype of the file which is to be opened.

A *title* should be placed on the AppChooserDialog indicating the function::

  appchooserdialog.set_title(title)

To ensure correct positioning of the dialog on the parent window, use::

  appchooserdialog.set_transient_for(parent)

..note :

  The AppChooserDialog utilises the :doc:`appchooser` backend for common methods and functions.

=======
Methods
=======
When the AppChooserDialog has been created use::

  appchooserdialog.run()
  appchooserdialog.destroy()

=======
Signals
=======
The commonly used signals of a AppChooserDialog are::

  "response" (dialog, response_id)
  "close" (dialog)

The ``"close"`` event occurs when the user presses the :kbd:`Escape` button on the keyboard, or the ``Gtk.ResponseType.CLOSE`` response is met. Alternatively, ``"response"`` can be emitted when anything happens within the AppChooserDialog. Both events emit the AppChooserDialog object with the function, however the ``"response"`` signal also emits a response_id value of the event that occurred within the AppChooserDialog.

=======
Example
=======
Below is an example of a AppChooserDialog:

.. literalinclude:: _examples/appchooserdialog.py

Download: :download:`AppChooserDialog <_examples/appchooserdialog.py>`
