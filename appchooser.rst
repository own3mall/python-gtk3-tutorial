AppChooser
==========
AppChooser is an interface for choosing an application from a list, and is used by the widgets :doc:`appchooserwidget`, :doc:`appchooserdialog`, and :doc:`appchooserbutton`.

=======
Methods
=======
To retrieve the application information from the AppChooser use::

  appchooser.get_app_info()

The method allows for the retrieval of a range of information such as name, description, and application location.

Retrieval of the content type associated with the AppChooser can be fetched by calling::

  appchooser.get_content_type()

The AppChooser can be refreshed manually with the call::

  appchooser.refresh()

Within the dialog, a string of text describes what action the AppChooserDialog will perform. By default this is "Select an application for (filetype) files". This can be changed using::

  appchooserdialog.set_heading(heading)

=======
Example
=======
To view an example of the AppChooser, see the code for the objects :doc:`appchooserwidget`, :doc:`appchooserdialog`, and :doc:`appchooserbutton`.
