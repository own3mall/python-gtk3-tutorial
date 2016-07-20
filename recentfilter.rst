RecentFilter
============
A RecentFilter works in conjunction with the RecentChooser family of widgets. It is used to provide configurability over what is displayed within the RecentChooser's.

===========
Constructor
===========
The RecentFilter can be constructed using the following::

  recentfilter = Gtk.RecentFilter()

.. note::

  A RecentFilter must be created for each filter type needed.

=======
Methods
=======
To set the name which identifies the RecentFilter use::

  recentfilter.set_name(name)

The name of the RecentFilter can also be retrieved with::

  recentfilter.get_name()

Filtering by the file extension, or a particular portion of the filename can be done using::

  recentfilter.add_pattern(pattern)
  recentfilter.add_application(application)

The *pattern* should be set to a string of text, which matches that of the required items. To limit by extension, and example string of ".odt" is used, with the asterisk identifying a wildcard. The use of ``.add_application()`` allows specifying a name for an application and filtering based on that name.

Alternatively, to limit by mime type use::

  recentfilter.add_mime_type(mime_type)

Limiting the RecentChooser-list by a set number of days can be set with::

  recentfilter.add_age(days)

The *days* value should be set to an integer value indicating the number of days or fewer with which items should be displayed.

=======
Example
=======
Below is an example of a RecentFilter:

.. literalinclude:: _examples/recentfilter.py

Download: :download:`RecentFilter <_examples/recentfilter.py>`
