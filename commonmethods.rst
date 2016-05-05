Common Methods
==============
There are a number of methods which apply to many widgets. These include:

::

  .set_sensitive(sensitive)

Setting *sensitive* to ``False`` greys-out a widget and prevents the user from using it.

::

  .set_visible(visible)

The *visible* parameter when set to ``False`` removes the widget from view from the user.

::

  .get_visible()

The ``.get_visible()`` method returns ``True`` when the widget is being shown, and ``False`` when hidden.

::

  .show()
  .show_all()
  .hide()

The ``.show()`` and ``.show_all()`` methods display widgets on screen, however ``.show_all()`` will display the parent and all subsequent child widgets. The ``.hide()`` method prompts GTK+ to hide the widget from display.

::

  .destroy()

Calling ``.destroy()`` deletes the widget and frees up the resources it was using.

::

  .set_size_request(width, height)

Using ``.set_size_request()`` allows configuring a widget based on the width and height in pixels.

::

  .is_focus()

To check whether a widget has the focus, call ``.is_focus()``. If the widget is currently the focus, ``True`` is returned.

::

  .set_can_focus(can_focus)

The *can_focus* parameter when set to ``False`` prevents the widget from accepting the input focus if required.

::

  .set_vexpand(expand)
  .set_hexpand(expand)

Items added to a :doc:`grid` by default are shrunk to the size of the content they contain. When the *expand* parameter is set to ``True``, the item is sized to fit the space vertically, horizontally or both.
