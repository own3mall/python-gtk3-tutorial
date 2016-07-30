CellRendererSpinner
===================
The CellRendererSpinner provides a :doc:`spinner` widget within a TreeView, to indicate activity of a job. It is commonly use to indicate the activity of a process whose length is unknown. An alternative when the length of the process is known is the :doc:`cellrendererprogress`.

.. note::

  See the :doc:`cellrenderer` page for additional methods available.

===========
Constructor
===========
The CellRendererSpinner can be constructed using the following::

  cellrendererspinner = Gtk.CellRendererSpinner()

==========
Properties
==========
The configuration of the CellRendererSpin is made using the property functions::

  cellrendererspin.set_property("item", value)

The property items available for use with the CellRendererSpin are:

* ``"active"`` - the active property configures whether the CellRendererSpinner is displayed in the cell or not.
* ``"pulse"`` - the pulse value is set to indicate whether the animation is running. This would be updated twelve times in 750 milliseconds.
* ``"size"`` - the size property can be specified to indicate the size of the Spinner widget. The value should be set to one of the following; ``Gtk.IconSize.INVALID``, ``Gtk.IconSize.MENU``, ``Gtk.IconSize.SMALL_TOOLBAR``, ``Gtk.IconSize.LARGE_TOOLBAR``, ``Gtk.IconSize.BUTTON``, ``Gtk.IconSize.DND``, or ``Gtk.IconSize.DIALOG``.

=======
Example
=======
Below is an example of a CellRendererSpinner:

.. literalinclude:: _examples/cellrendererspinner.py

Download: :download:`CellRendererSpinner <_examples/cellrendererspinner.py>`
