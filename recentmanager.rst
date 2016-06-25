RecentManager
=============
The RecentManager object is the backend of the RecentChooser family, and allows for management of the files that are displayed there.

===========
Constructor
===========
The RecentManager can be constructed using the following::

  recentmanager = Gtk.RecentManager()

=======
Methods
=======
Items can be added to the RecentManager by specifying the URI and calling the method::

  recentmanager.add_item(uri)

They can also be removed based on the URI as well by using::

  recentmanager.remove_item(uri)

Every item can be purged from the RecentManager with::

  recentmanager.purge_items()

Recent items can be retrieved from the RecentManager by calling::

  recentmanager.get_items()

This method returns a list of all the URIs within the RecentManager.

A :doc:`recentinfo` object can be obtained by looking up a URI via the method::

  recentmanager.lookup_item(uri)

To check whether the RecentManager contains a specific URI use::

  recentmanager.has_item(uri)

If the specified *uri* paramter was found, ``True`` is returned.

Items held by the RecentManager can be moved if required::

  recentmanager.move_item(old, new, error)

The *old* and *new* parameters specify the URI strings. An *error* can also be specified which returns a GError object, or ``None`` if not required.
