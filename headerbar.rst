HeaderBar
=========
A HeaderBar allows child widgets to be inserted into it, and centered within. It also allows a title to be shown, and also centered with respect to the width of the HeaderBar.

===========
Constructor
===========
The HeaderBar is constructed using the call::

  headerbar = Gtk.HeaderBar()

=======
Methods
=======
To set the title on the HeaderBar use::

  headerbar.set_title(title)

The title can also be retrieved with::

  headerbar.get_title()

HeaderBar widgets also support subtitles and would be used to provide information to the user about the current view.

  headerbar.set_subtitle(subtitle)

If required, other widgets can be set as the title with the method::

  headerbar.set_custom_title(child)

Items can be packed into the HeaderBar with the two methods::

  headerbar.pack_start(child)
  headerbar.pack_end(child)

The close button within the HeaderBar can be shown or hidden with::

  headerbar.set_show_close_button(show_button)

The *show_button* value should be set to ``True`` or ``False`` depending on whether the object is shown or not.

=======
Example
=======
Below is an example of an HeaderBar:

.. literalinclude:: _examples/headerbar.py

Download: :download:`HeaderBar <_examples/headerbar.py>`
