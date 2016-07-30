CellRendererToggle
==================
When using a CellRendererToggle, it allows a widget similar to a :doc:`checkbutton` or :doc:`radiobutton` to be displayed within the TreeView.

.. note::

  See the :doc:`cellrenderer` page for additional methods available.

===========
Constructor
===========
The CellRendererToggle can be constructed using the following::

  cellrenderertoggle = Gtk.CellRendererToggle()

=======
Methods
=======
By default, the CellRendererToggle is drawn as a CheckButton. This can be changed to a RadioButton using::

  cellrenderertoggle.set_radio(radio)

When *radio* is set to ``True``, the RadioButton style is drawn.

To make a CellRendererToggle set as active::

  cellrenderertoggle.set_active(active)

When the *active* parameter is set to ``True``, the CellRendererToggle will be shown in the ticked (active) state.

To prevent a CellRendererToggle from being activated::

  cellrenderertoggle.set_activatable(activatable)

==========
Properties
==========
The configuration of the CellRendererToggle is made using the property functions::

  cellrenderertoggle.set_property("item", value)

The property items available for use with the CellRendererToggle are:

* ``"activatable"`` - customise whether the CellRendererToggle is activatable.
* ``"active"`` - this toggles the state of the CellRendererToggle.
* ``"inconsistent"`` - when set to ``True``, the CellRendererToggle can be used to indicate the status of other features.
* ``"radio"`` - if set to ``True``, the CellRendererToggle will be drawn like a RadioButton.

=======
Signals
=======
The commonly used signals of a CellRendererToggle are::

  "toggled" (cellrenderertoggle, path)

The ``"toggled"`` signals emits from the CellRendererToggle when the user clicks to display or remove the tick within the widget. It provides the *path* which identifies the location of the item which has been modified.

=======
Example
=======
Below is an example of a CellRendererToggle:

.. literalinclude:: _examples/cellrenderertoggle.py

Download: :download:`CellRendererToggle <_examples/cellrenderertoggle.py>`
