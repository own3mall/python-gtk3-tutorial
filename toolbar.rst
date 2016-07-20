Toolbar
=======
The Toolbar widget provides access to common features of an application such as Save, Print or Find.

===========
Constructor
===========
A Toolbar can be constructed using the following::

  toolbar = Gtk.Toolbar()

=======
Methods
=======
Items can be added to the Toolbar with::

  toolbar.insert(item, position)

The *item* should be an appropriate ToolItem object. A *position* value indicates the location the item is to be added on the Toolbar, with 0 designating the first place on the Toolbar.

Items can also be removed using::

  toolbar.remove(position)

To retrieve the number of items which are currently displayed on the Toolbar run::

  toolbar.get_n_items()

Alternatively, retrieving the widget at a specified position use::

  toolbar.get_nth_item()

By default, the Toolbar style is specified in the GTK+ global setting. This can be configured with::

  toolpalette.set_style(style)

The *style* parameter should be set to one of the following; ``Gtk.ToolbarStyle.ICONS``, ``Gtk.ToolbarStyle.TEXT``, ``Gtk.ToolbarStyle.BOTH``, ``Gtk.ToolbarStyle.BOTH_HORIZ``. When using ``Gtk.ToolbarStyle.ICONS`` or ``Gtk.ToolbarStyle.TEXT`` only icons or text are displayed. ``Gtk.ToolbarStyle.BOTH`` displays icons and text, with the text positioned beneath the icon. ``Gtk.ToolbarStyle.BOTH_HORIZ`` displays text to the left of the icon.

.. note::

  It is highly recommended not to set a style. This allows GTK+ to use the global setting which ensures your application is consistent with others.

Icon sizes within the Toolbar can be configured with::

  toolbar.set_icon_size(icon_size)

The *icon_size* argument must be set to one of the following values; ``Gtk.IconSize.INVALID``, ``Gtk.IconSize.MENU``, ``Gtk.IconSize.SMALL_TOOLBAR``, ``Gtk.IconSize.LARGE_TOOLBAR``, ``Gtk.IconSize.BUTTON``, ``Gtk.IconSize.DND``, or ``Gtk.IconSize.DIALOG``. The Toolbar takes the global size setting by default.

If the number of icons is larger than the space allocated for the Toolbar, a menu can be shown to provide access to those which have overflown. This functionality can be configured with::

  toolbar.set_show_arrow(show_arrow)

When *show_arrow* is set to ``True``, the menu will be shown when clicking on a button which displays the remaining items in a menu.

=======
Example
=======
Below is an example of a Toolbar and associated items that can be attached:

.. literalinclude:: _examples/toolbar.py

Download: :download:`Toolbar <_examples/toolbar.py>`
