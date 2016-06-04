FontChooserDialog
=================
The FontChooserDialog provides a :doc:`fontchooserwidget` within a dialog window.

The dialog-variant of the FontChooser family allows for choosing fonts, styling and sizes.

===========
Constructor
===========
The FontChooserDialog can be constructed using the following::

  fontchooserdialog = Gtk.FontChooserDialog(title, parent)

A *title* should be specified via a string of text which identifies the function of the FontChooserDialog. The *parent* parameter can be the name of a Window or Dialog which owns the FontChooserDialog.

=======
Methods
=======
Once the FontChooserDialog has been constructed use::

  fontchooserdialog.run()
  fontchooserdialog.destroy()

.. note::

  If you application only uses a dialog window, the ``Gtk.main()`` call is not required. This is invoked automatically when calling ``fontchooserdialog.run()``.

The title of the dialog which is displayed can be set with::

  fontchooserdialog.set_title(title)

.. note::

  The FontChooserWidget inherits methods from the :doc:`fontchooser` object.

=======
Example
=======
Below is an example of a FontChooserDialog:

.. literalinclude:: _examples/fontchooserdialog.py

Download: :download:`FontChooserDialog <_examples/fontchooserdialog.py>`
