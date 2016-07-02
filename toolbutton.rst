ToolButton
==========
A ToolButton is the most basic ToolItem. It should be used within a :doc:`toolbar` or :doc:`toolpalette` to provide clickable buttons. Each ToolButton can contain a label and/or image however the user settings may override the settings defined by the application.

===========
Constructor
===========
The ToolButton can be constructed using the following::

  toolbutton = Gtk.ToolButton(label, icon_widget, icon_name)

The *label* parameter defines the string of text to be displayed on the ToolButton. In all circumstances this should be set. The *icon_widget* allows a widget such as an :doc:`image` to be added, however can be omitted if not required. The *icon_name* allows the name of an icon to be used, which is then loaded from the current theme. This may also be omitted if not needed.

=======
Methods
=======
Custom label text can be used by specifying a string of text in::

  toolbutton.set_label(label)

It is recommended to display a mnemonic character which is identified by using an underscore before the character which is to be identied as mnemonic. This can be turned on with::

  toolbutton.set_use_underline(use_underline)

When *use_underline* is set to ``True``, the underscore if removed and the later after displays a underline.

Alternatively, if custom :doc:`label` or :doc:`image` widgets need to be attached to a ToolButton, use::

  toolbutton.set_label_widget(label_widget)
  toolbutton.set_icon_widget(icon_widget)

An icon name can also be defined which allows an icon from the current theme to be loaded::

  toolbutton.set_icon_name(icon_name)

By default, when the toolbar style is set to display text beside icons, no icons will display text. This is to ensure that only important, or frequently used icons display text, and are therefore more visible to users. This can be set with::

  toolbutton.set_is_important(is_important)

When *is_important* is set to ``True``, the icon text will be displayed.

.. note::

  Icon text is always displayed when text is set to show below icons. This method only affects the text beside icons functionality.

.. note::

  It is good interface design to ensure only important items in the Toolbar have the ``.set_is_important()`` method set.

In some use cases, it may be useful to have an item set to invisible if the Toolbar is configured to either horizontal or vertical mode::

  toolbutton.set_visible_horizontal(visible)
  toolbutton.set_visible_vertical(visible)

By default, all items are shown whether vertical or horizontal. Setting either method to ``False`` will result in the item being hidden.

It is highly recommended to set a :doc:`tooltip` on the ToolButton using::

  toolbutton.set_tooltip_text(text)
  toolbutton.set_tooltip_markup(markup)

=======
Signals
=======
The commonly used signals of an ToolButton are::

  "clicked" (toolbutton)

The ``"clicked"`` signal emits from the ToolButton when the user presses and then releases the mouse button. It can also occur when the item has the focus and the user presses the :kbd:`Return` button for example.

=======
Example
=======
To view an example for this widget, see the Toolbar example.
