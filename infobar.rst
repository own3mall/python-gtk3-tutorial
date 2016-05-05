InfoBar
=======
An InfoBar provides an in-window method of displaying messages to the user. These can be warnings, errors, questions, information or other custom-made messages.

===========
Constructor
===========
The InfoBar can be constructed using the following::

  infobar = Gtk.InfoBar()

=======
Methods
=======
After construction, configuration of the message type may be needed. The InfoBar defaults to ``Gtk.MessageType.INFO``, however it is also possible to display ``Gtk.MessageType.WARNING``, ``Gtk.MessageType.ERROR``, ``Gtk.MessageType.QUESTION`` or ``Gtk.MessageType.OTHER`` with::

  infobar.set_message_type(message_type)

Buttons can be added to the InfoBar to allow different responses to the message. These can be added with::

  infobar.add_button(text, response_id)

The *text* value in the first method is a string of text which should be displayed on the button. The *response_id* parameter in both methods can be set to one of the following:

* ``Gtk.ResponseType.NONE``
* ``Gtk.ResponseType.REJECT``
* ``Gtk.ResponseType.ACCEPT``
* ``Gtk.ResponseType.DELETE_EVENT``
* ``Gtk.ResponseType.OK``
* ``Gtk.ResponseType.CANCEL``
* ``Gtk.ResponseType.CLOSE``
* ``Gtk.ResponseType.YES``
* ``Gtk.ResponseType.NO``
* ``Gtk.ResponseType.APPLY``
* ``Gtk.ResponseType.HELP``

Alternatively, multiple buttons can be added to the InfoBar via::

  infobar.add_buttons(text, response_id, ...)

For every button text added to the list, it must also have an appropriate *response_id*.

When an InfoBar is no longer required, it is recommended to hide it from view with::

  infobar.hide()

If multiple buttons are in use, it may be useful to set one as the default response. This allows the user to press Enter without any other action to run the default action::

  infobar.set_default_response(response_id)

The *response_id* specified here should match one of those specified when using ``.add_button()``.

Another useful feature is to be able to mark a button within the InfoBar as not sensitive. This can be achieved with::

  infobar.set_response_sensitive(response_id, setting)

The *response_id* should be set to one of those specified when using ``.add_button()``. The setting will be a ``True`` or ``False`` value, with ``False`` setting the button as insensitive (or greyed-out).

To configure whether a close button is displayed on the InfoBar, call::

  infobar.set_show_close_button(show_button)

When *show_button* is set to ``True``, a button is shown which allows the InfoBar to be closed. When the button is pressed, the response ``Gtk.ResponseType.CLOSE`` is emitted.

The MessageDialog is constructed using several predefined :doc:`box` widgets which give the shape of the dialog. The *content_area* is the place where you place widgets. The *action_area* is the place where buttons and other actionable widgets are place. Both can be retrieved with the methods::

  infobar.get_content_area()
  infobar.get_action_area()

=======
Signals
=======
The commonly used signals of a InfoBar are::

  "close" (infobar)
  "response" (infobar, response_id)

The ``"close"`` signal emits from the InfoBar when the :kbd:`Escape` key is pressed. A ``"response"`` signal is emitted whenever a button within the InfoBar is clicked. The *response_id* varies depending on which action the user takes.

=======
Example
=======
Below is an example of an InfoBar:

.. literalinclude:: _examples/infobar.py

Download: :download:`InfoBar <_examples/infobar.py>`
