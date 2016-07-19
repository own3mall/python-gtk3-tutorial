ToolPalette
===========
A ToolPalette is used to display a large number of items. It is similar to a :doc:`toolbar`, however is tailored for use in applications which require more features accessible to the user such as image editing.

===========
Constructor
===========
The ToolPalette can be constructed using the following::

  toolpalette = Gtk.ToolPalette()

=======
Methods
=======
The ToolPalette is the container for :doc:`toolitemgroup` sub-containers, which actually hold the items. These are added to the ToolPalette by::

  toolpalette.add(toolitemgroup)

A ToolItemGroup may also be removed by calling::

  toolpalette.remove(toolitemgroup)

In some cases, it may be required to only display one of the ToolItemGroup objects at any one time with::

  toolpalette.set_exclusive(toolitemgroup, exclusive)

The *toolitemgroup* parameter should be set to a :doc:``toolitemgroup` identifying which should be set to exclusive status. When the *exclusive* parameter is set to ``True``, the ToolItemGroup will display and all other open groups will be closed.

To expand a ToolItemGroup programatically use::

  toolpalette.set_expand(toolitemgroup, expand)

Again, the *toolitemgroup* parameter is a ToolItemGroup which is to be expanded. When the *expand* property is set to ``True``, the items within the group will be opened.

Groups can be set or changed with::

  toolpalette.set_group_position(group, position)

The *group* parameter must be set to a ToolItemGroup which is to be configured. The *position* value should be an integer value indicating the location of the group within the ToolPalette, with ``0`` indicating the first position.

The ToolPalette by default takes the system style for Toolbars. This can be configured to::

  toolpalette.set_style(style)

The *style* parameter should be set to one of the following; ``Gtk.ToolbarStyle.ICONS``, ``Gtk.ToolbarStyle.TEXT``, ``Gtk.ToolbarStyle.BOTH``, ``Gtk.ToolbarStyle.BOTH_HORIZ``. When using ``Gtk.ToolbarStyle.ICONS`` or ``Gtk.ToolbarStyle.TEXT`` only icons or text are displayed. ``Gtk.ToolbarStyle.BOTH`` displays icons and text, with the text positioned beneath the icon. ``Gtk.ToolbarStyle.BOTH_HORIZ`` displays text to the left of the icon.

.. note::

  It is highly recommended not to set a style and to use whichever the GTK+ global setting specifies, for both consistency and usability reasons.

Icon sizes within the ToolPalette can be configured with::

  toolpalette.set_icon_size(icon_size)

The *icon_size* argument must be set to one of the following values; ``Gtk.IconSize.INVALID``, ``Gtk.IconSize.MENU``, ``Gtk.IconSize.SMALL_TOOLBAR``, ``Gtk.IconSize.LARGE_TOOLBAR``, ``Gtk.IconSize.BUTTON``, ``Gtk.IconSize.DND``, or ``Gtk.IconSize.DIALOG``. The ToolPalette takes the global size setting by default.

Customisation of the direction in which items are displayed in the ToolPalette can be made with::

  toolpalette.set_orientation(orientation)

The *orientation* parameter by default is ``Gtk.Orientation.VERTICAL`` in which all groups of added vertically, however ``Gtk.Orientation.HORIZONTAL`` can also be used to add groups horizontally.

=======
Example
=======
Below is an example of a ToolPalette:

.. literalinclude:: _examples/toolpalette.py

Download: :download:`ToolPalette <_examples/toolpalette.py>`
