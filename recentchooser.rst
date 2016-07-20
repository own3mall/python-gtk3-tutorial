RecentChooser
=============
The RecentChooser is an interface for the objects :doc:`recentchooserwidget`, :doc:`recentchooserdialog`, and :doc:`recentchoosermenu`. It is used to display recently opened files for quick access by the user. It is commonly used by the :doc:`filechooser` family, however can be used in other applications.

=======
Methods
=======
The selected items can be fetched from the RecentChooser using::

  recentchooser.get_current_item()
  recentchooser.get_current_uri()

Both the ``.get_current_item()`` and ``.get_current_uri()`` methods return a single item.

If multiple item selection is enabled, the method to use to return all selected items is::

  recentchooser.get_items()

If a file can not be found, it may be useful to customise whether it can be viewed in the recent list::

  recentchooser.set_show_not_found(show_not_found)

To configure whether only local files are displayed use::

  recentchooser.set_local_only(local_only)

If there is a requirement to allow the user to select multiple items from the chooser use::

  recentchooser.set_select_multiple(multiple)

When *multiple* is set to ``True``, the user can hold down the :kbd:`Control` key and click with the mouse.

To limit the number of items which are displayed use the method::

  recentchooser.set_limit(limit)

The *limit* value should be an integer value, however it can also be set to ``-1`` to display all files.

The sorting type of the list can be configured by specifying::

  recentchooser.set_sort_type(sort_type)

The *sort_type* should be set to one of ``Gtk.RecentSortType.NONE``, ``Gtk.RecentSortType.MRU`` which shows most recently used at the top, and ``Gtk.RecentSortType.LRU`` which sorts by least recently used.

By default, the RecentChooserWidget shows icons relating to the file type. These can be disabled with::

  recentchooser.set_show_icons(show_icons)

When *show_icons* is set to ``False``, only the filenames will be shown.

In many cases, it may be useful to limit the files listed in the RecentChooser to those only openable by the application. This can be set using either method::

  recentchooser.add_filter(filter)
  recentchooser.set_filter(filter)

Filters can be removed with::

  recentchooser.remove_filter(filter)

In the case of ``.add_filter()``, ``.set_filter()``, and ``.remove_filter()``, the object should be a :doc:`recentfilter`.

A list of RecentFilter objects attached to the RecentChooser can be found via::

  recentchooser.list_filters()

=======
Signals
=======
The common functions of the RecentChooser are::

  "item-activated" (recentchooser)
  "selection-changed (recentchooser)

The ``"item-activated"`` signal is emitted when the user either double-clicks on an item, or presses :kbd:`Enter` while an item is selected. Alternatively, a ``"selection-changed"`` signal emits when the selection changes via the mouse of keyboard.
