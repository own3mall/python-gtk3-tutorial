StackSwitcher
=============
The StackSwitcher is a controller for the :doc:`stack` widget. It allows switching between the various child widgets of the Stack.

===========
Constructor
===========
The StackSwitcher is constructed using the call::

  stackswitcher = Gtk.StackSwitcher()

=======
Methods
=======
To add the Stack which is to be controlled by the StackSwitcher, call::

  stackswitcher.set_stack(stack)

Retrieval of the attached Stack is made with::

  stackswitcher.get_stack()

=======
Example
=======
Below is an example of an StackSwitcher:

.. literalinclude:: _examples/stackswitcher.py

Download: :download:`StackSwitcher <_examples/stackswitcher.py>`
