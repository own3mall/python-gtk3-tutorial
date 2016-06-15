Notebook
========
A Notebook widget is a container which displays content in a tab-based fashion. The differing content can be viewed by clicking on appropriate tabs.

===========
Constructor
===========
The Notebook can be constructed using the following::

  notebook = Gtk.Notebook()

=======
Methods
=======
There are three options for adding pages to a Notebook. These are as follows::

  notebook.append_page(child, label)
  notebook.prepend_page(child, label)
  notebook.insert_page(child, label, position)

The ``.append_page()`` method adds pages to the end of the Notebook whereas ``.prepend_page()`` adds to the beginning. Calling ``.insert_page()`` adds pages to a particular location identified by *position*. The *child* parameter is the name of the widget which will be added to the Notebook page (commonly a Grid or Box). The *label* parameter specifies the :doc:`label` widget which holds the title text of the page.

Pages can also be removed by specifying the position by calling::

  notebook.remove_page(position)

The *position* value is a number identifying the current position of the tab to be removed, with ``0`` indicating the first tab.

To retrieve the number of pages which the Notebook holds::

  notebook.get_n_pages()

Retrieval of the child contained at a particular page number can be retrieved with::

  notebook.get_nth_page()

To return the page number of the currently visible page call the method::

  notebook.get_current_page()

Setting the currently active page on the Notebook can be achieved with::

  notebook.set_current_page(position)

By default, the Notebook shows tabs of all pages, however in some cases it may be useful to turn off the tab bar (for example if only one tab is visible). This can be toggled calling::

  notebook.set_show_tabs(show_tabs)

If the Notebook contains a large number of tabs, it is recommended to enable scrolling to prevent the tab titles shrinking too much and preventing the title from being visible. This can be set with::

  notebook.set_scrollable(scrollable)

Another useful feature would be to allow reordering of the tabs within the Notebook::

  notebook.set_tab_reorderable(reorderable)

When *reorderable* is set to ``True``, the user can drag-and-drop tabs into alternate positions.

In some cases, advanced functionality with extra widgets may need to be provided. This can be setup by using an Action Area::

  notebook.set_action_widget(child, pack_type)

The *child* argument should be set to the widget which is to be added (usually this would be a Box). The *pack_type* parameter should be set to one of either ``Gtk.PackType.START`` or ``Gtk.PackStart.END`` which controls where the Action Area is positioned.

=======
Signals
=======
The common signals of the Notebook are::

  "page-added" (notebook, child, page_num)
  "page-removed" (notebook, child, page_num)
  "page-reordered" (notebook, child, page_num)
  "switch-page" (notebook, page, page_num)

The ``"page-added"`` and ``"page-removed"`` signals emit the *child* widget and the page number in *page_num* whenever a page is added or removed from the Notebook. The same values are also emitted whenever a Notebook page is moved via ``"page-reordered"``. The ``"switch-page"`` signal emits each time the user changes which tab is active. This emits the values *page* which contains the page widget, and the *page_num* identifying the current page number index.

=======
Example
=======
Below is an example of a Notebook:

.. literalinclude:: _examples/notebook.py

Download: :download:`Notebook <_examples/notebook.py>`
