Menu
====
There are two types of menu which can be constructed. Both use the Menu widget however are used for different implementations. These are the Application menu which is displayed via a :doc:`menubar`, and provides access to all features of the application. Alternatively, a context menu appears when the user right-clicks on an interface and provides access to common functions.

===========
Constructor
===========
The Menu can be constructed using the following::

  menu = Gtk.Menu()

=======
Methods
=======
Items can be added to the Menu using the following three methods::

  menu.append(menuitem)
  menu.prepend(menuitem)
  menu.insert(menuitem, position)

The *menuitem* parameter should be the MenuItem which is to be added to the Menu. Items added using the ``.append()`` method are added at the end of the Menu, whereas when using the ``.prepend()`` method items are added to the top of the Menu. When using the ``.insert()`` parameter, a *position* must be specified which indicates the position where the items are to be added within the Menu.

It is also possible to remove items from the Menu with::

  menu.remove(menuitem)

To move an item within a Menu call::

  menu.reorder_child(menuitem, position)

An :doc:`accelgroup` can be attached to the Menu using::

  menu.set_accel_group(accelgroup)

Enabling the Menu to reserve space for menu items as it would for toggles or icons, this can be enabled via::

  menu.set_reserve_toggle_size(reserve)

When the *reserve* value is set to ``True``, the text will be indented within the menu regardless of whether there are any icons or toggle indicators.

=======
Example
=======
Below is an example of a Menu, MenuBar and associated MenuItem widgets:

.. literalinclude:: _examples/menu.py

Download: :download:`Menu <_examples/menu.py>`
