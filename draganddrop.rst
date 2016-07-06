Drag-and-Drop
=============
Drag-and-drop is a complex topic and requires careful setup to allow transferring of information to ensure the drag and drop operations work correctly. The drag and drop operation consists of a drag source and a drop destination, typically both consisting of a widget such as a Button or TreeView.

.. note::

  The drag-and-drop functionality of GTK+ requires a good understanding of the toolkit.

=====
Basic
=====
Source and destination must be declared for most widgets, with a widget being able to be both a source and destination if required. This is set with the methods::

  widget.drag_source_set()
  widget.drag_dest_set()

.. note::

  The basic methods are typically used for widgets such as :doc:`button`, :doc:`label`, or :doc:`image`. Complex widgets such as :doc:`treeview` or :doc:`iconview` typically have their own separate methods which are used to process data retrieval and handling.

Text, image and URI data can be drag-and-dropped, with source and destination types declared where appropriate via::

  widget.drag_source_add_text_targets()
  widget.drag_source_add_image_targets()
  widget.drag_source_add_uri_targets()
  widget.drag_dest_add_text_targets()
  widget.drag_dest_add_image_targets()
  widget.drag_dest_add_uri_targets()

The destination action must also be set and is done using::

  widget.drag_dest_set(flags, targets, actions)

The *flags* value sets the action type which will be taken on behalf of the user for the destination and should be set to one of:

* ``Gtk.DestDefault.MOTION``
* ``Gtk.DestDefault.HIGHLIGHT``
* ``Gtk.DestDefault.DROP``
* ``Gtk.DestDefault.ALL``

The *targets* flags states the drop types the widget accepts, however an empty list can be used if not required. Finally, the *actions* parameter specifies what the destination should do with the dropped data and is set to::

* ``Gdk.DragAction.DEFAULT``
* ``Gdk.DragAction.COPY``
* ``Gdk.DragAction.MOVE``
* ``Gdk.DragAction.LINK``
* ``Gdk.DragAction.PRIVATE``
* ``Gdk.DragAction.ASK``

========
Advanced
========


=======
Signals
=======
A number of signals can be setup on the source and destination objects to control the functionality.

------
Source
------
The source is the object from where the drag and drop operation is started.

* ``"drag-begin"`` - commonly used to setup an icon which will be displayed to the user when the drag operation is started.
* ``"drag-data-get"`` - grab the data which will be transferred to the destination.
* ``"drag-data-delete"`` - delete the data if the drag and drop operation will move rather than copy using ``Gdk.DragAction.MOVE``.
* ``"drag-end"`` - undo any setup begun with the ``"drag-begin"`` signal.

-----------
Destination
-----------
A destination is an object which is the receiver of the drag and drop operation.

* ``"drag-data-received"`` - handling received data once drop has completed.
