FlowBoxChild
============
A FlowBoxChild is a container which is added to the :doc:`flowbox`.

===========
Constructor
===========
Construction of the FlowBoxChild is made via::

  flowboxchild = Gtk.FlowBoxChild()

=======
Methods
=======
The index value of the FlowBoxChild held within the FlowBox can be obtained from::

  flowboxchild.get_index()

The returned index value indicates the position, with ``0`` showing the FlowBoxChild is first in the FlowBox. A ``-1`` value means the FlowBoxChild has not been added to a FlowBox.

To check whether a FlowBoxChild is currently selected call::

  flowboxchild.is_selected()

=======
Example
=======
An example of the FlowBoxChild can be found on the FlowBox page.
