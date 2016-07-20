TreeView
========
A TreeView is a table-style widget that allows for displaying information in columns and rows. It can be used to display a variety of information in different styles through the user of cell types. The TreeView is the most advanced widget to implement and has a high-learning curve.

===========
Constructor
===========
The TreeView can be constructed using the following::

  treeview = Gtk.TreeView(model)

The *model* parameter should be set to either a :doc:`liststore` or :doc:`treestore`, depending on the data which is to be displayed.

=======
Methods
=======
The model can also be set after construction using::

  treeview.set_model(model)

Attaching :doc:`treeviewcolumn` objects to the TreeView can be done in a number of ways::

  treeview.append_column(column)
  treeview.prepend_column(column)
  treeview.insert_column(column, position)

The *column* parameter should be set to the column name which is to be attached. The *position* parameter within the ``.insert_column()`` method allows the specification of a position value where the column should be added, with ``0`` indicating the first place.

A column can also be removed if necessary with::

  treeview.remove_column(column)

To fetch the number of columns within the TreeView::

  treeview.get_n_columns()

By default, the column headers will be visible. These can be disabled with::

  treeview.set_headers_visible(headers_visible)

When *headers_visible* is set to ``False``, the column headers will not be shown even if there is a title set on them.

The TreeView supports basic searching of data. This can be enabled with::

  treeview.set_enable_search(enable_search)

If *enable_search* is set to ``True``, when the user begins typing a text entry appears with the characters to issue the search by.

When setting the ``.set_enable_search()`` method to ``True``, the first column will be used to test the search string against. This can be modified with::

  treeview.set_search_column(search_column)

The *search_column* should be set to the integer value of the column which is to be searched.

=======
Example
=======
For an example of the TreeView widget, see either the documentation for :doc:`liststore` or :doc:`treestore`.
