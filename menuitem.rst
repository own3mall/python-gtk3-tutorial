MenuItem
========
A MenuItem widget is the most basic of the menu item family, and allows a string of text to be displayed.

===========
Constructor
===========

  menuitem = Gtk.MenuItem(label, use_underline)

The *label* parameter defines the text which is to be shown on the MenuItem. The *use_underline* parameter should be set to ``True`` to identify the character with an preceding underscore as an mnemonic key.

=======
Methods
=======
Setting the label text after construction is done using::

  menuitem.set_label(label)

To set whether the MenuItem uses a mnemonic key after constructing call::

  menuitem.set_use_underline(use_underline)

Submenus can be attached to a MenuItem via::

  menuitem.set_submenu(menu)

The *menu* value should be a named :doc:`menu` widget. This should be used for both menus attached to items on a Menubar, and when constructing a tree of menus.

An attached submenu is retrieved using::

  menuitem.get_submenu()

A MenuItem can be programatically activated with the method::

  menuitem.activate()

Space can be reserved for an indicator (such as those displayed when a submenu is available) regardless of whether one is currently added to a MenuItem. This is set via::

  menuitem.set_reserve_indicator(reserve)

=======
Signals
=======
The common signals of a MenuItem are::

  "activate" (menuitem)
  "activate-item" (menuitem)

The ``"activate"`` signal emits when the user clicks on the MenuItem. The ``"activate-item"`` is emitted when the user clicks a MenuItem as with ``"activate"``, however it also emits when a submenu appears. This would be useful for dynamic loading of items in a submenu. In most cases, ``"activate"`` is the correct signal to use.

=======
Example
=======
For an example of the MenuItem see the :doc:`menu` page.
