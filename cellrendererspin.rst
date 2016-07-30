CellRendererSpin
================
Using a CellRendererSpin widget provides a :doc:`spinbutton` within a TreeView. The widget contains an entry for manually inputting numbers, as well as two buttons to adjust the value contained up or down.

.. note::

  See the :doc:`cellrenderer` page for additional methods available.

===========
Constructor
===========
The CellRendererSpin can be constructed using the following::

  cellrendererspin = Gtk.CellRendererSpin()

==========
Properties
==========
The configuration of the CellRendererSpin is made using the property functions::

  cellrendererspin.set_property("item", value)

The property items available for use with the CellRendererSpin are:

* ``"digits"`` - the number of digits displayed after the decimal point can be specified for values which require it.
* ``"adjustment"`` - specify the :doc:`adjustment` object from which the current value, hightest and lowest values, and also the incremental value should be taken.

=======
Example
=======
Below is an example of an CellRendererSpin:

.. literalinclude:: _examples/cellrendererspin.py

Download: :download:`CellRendererSpin <_examples/cellrendererspin.py>`
