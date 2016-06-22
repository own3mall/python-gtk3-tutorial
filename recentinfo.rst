RecentInfo
==========
A RecentInfo object holds information on recently accessed files. It is used to retrieve data such as the mime type, when it was last visited or modified, or the URI.

=======
Methods
=======
The following methods are used to obtain information from the RecentInfo::

  recentinfo.get_display_name()
  recentinfo.get_short_name()
  recentinfo.get_uri()
  recentinfo.get_uri_display()
  recentinfo.get_age()
  recentinfo.get_description()
  recentinfo.get_added()
  recentinfo.get_modified()
  recentinfo.get_visited()
  recentinfo.get_applications(length)

Two checks can be made on the last application and whether an application is installed for the document.

  recentinfo.last_application()
  recentinfo.has_application()

An icon for the RecentInfo content can be obtained via::

  recentinfo.get_icon(size)

The method returns a Pixbuf for the given *size* parameter.

A check can be made on whether the document is held locally on the file system with::

  recentinfo.is_local()

To check if a RecentInfo is held by the RecentManager, call the method::

  recentinfo.exists(recentinfo)

Another check is also available to compare RecentInfo objects and see whether they match::

  recentinfo.match(recentinfo1, recentinfo2)
