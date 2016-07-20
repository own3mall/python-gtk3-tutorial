Spinner
=======
The Spinner widget is used to show activity in progress. Usually, the Spinner is used when it is not known how long the action may take. A common example of its use is to indicate the loading of a web page.

===========
Constructor
===========
The Spinner can be constructed using::

  spinner = Gtk.Spinner()

=======
Methods
=======
The two methods which allow starting and stopping of the Spinner are::

  spinner.start()
  spinner.stop()

==========
Properties
==========
To check whether the Spinner is active, the property call is::

  spinner.get_property("active")

If the Spinner is running, ``True`` is returned.

Whether the Spinner is running or not is able to be set using::

  spinner.set_property("active", active)

When *active* is set to ``True``, the Spinner animation begins.

========
Examples
========
Below is an example of a Spinner:

.. literalinclude:: _examples/spinner.py

Download: :download:`Spinner <_examples/spinner.py>`
