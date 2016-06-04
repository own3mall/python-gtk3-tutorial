ColorChooserDialog
==================
A ColorChooserDialog provides a dialog window from which a user can choose a colour from a palette offered.

===========
Constructor
===========
The ColorChooserDialog is constructed using::

  colorchooserdialog = Gtk.ColorChooserDialog()

=======
Methods
=======
Once the ColorChooserDialog has been constructed use::

  colorchooserdialog.run()
  colorchooserdialog.destroy()

.. note::

  If you application only uses a dialog window, the ``Gtk.main()`` call is not required. This is invoked automatically when calling ``colorchooserdialog.run()``.

A title should be set on the ColorChooserDialog indicating the function of the dialog::

  colorchooserdialog.set_title(title)

.. note::

  The ColorChooserDialog inherits methods from the :doc:`colorchooser` object.

========
Examples
========
Below is an example of a ColorChooserDialog:

.. literalinclude:: _examples/colorchooserdialog.py

Download: :download:`ColorChooserDialog <_examples/colorchooserdialog.py>`
