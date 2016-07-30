CellRendererProgress
====================
A CellRendererProgress allows for the displaying of a :doc:`progressbar` within a TreeView to show the status, or percentage completion of a task. If the process length is unknown, it is preferable to use the :doc:`cellrendererspinner`.

.. note::

  See the :doc:`cellrenderer` page for additional methods available.

===========
Constructor
===========
The CellRendererProgress can be constructed using the following::

  cellrendererprogress = Gtk.CellRendererProgress()

==========
Properties
==========
The configuration of the CellRendererProgress is made using the property functions::

  cellrendererprogress.set_property("item", value)

The property items available for use with the CellRendererProgress are:

* ``"pulse"`` - when the attribute is set to ``True``, the ProgressBar will pulse from side-to-side to indicate activity.
* ``"text"`` - text content to be displayed within the cell.
* ``"value"`` - a value specified between 0 and 100 indicating the amount of progress made.
* ``"inverted"`` - to reverse the direction of the ProgressBar, use ``True`` as the value.

=======
Example
=======
Below is an example of an CellRendererProgress:

.. literalinclude:: _examples/cellrendererprogress.py

Download: :download:`CellRendererProgress <_examples/cellrendererprogress.py>`
