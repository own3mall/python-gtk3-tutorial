LinkButton
==========
The LinkButton is similar to a Button widget, however its only function is to display website links and when clicked, open the system default browser to display the website.

===========
Constructor
===========
The LinkButton can be constructed using the following::

  linkbutton = Gtk.LinkButton(uri, label)

The *uri* parameter should be set to the web address of the website which the LinkButton links to. The *label* parameter is optional, however is much neater when set as it displays the website name rather than link.

=======
Methods
=======
To set the *uri* of the LinkButton after construction use::

  linkbutton.set_uri(uri)

Alternatively, the label can be set with::

  linkbutton.set_label(label)

The method to retrive the *uri* from the LinkButton is::

  linkbutton.get_uri()

The following method exists to check whether the link has been visited::

  linkbutton.get_visited()

=======
Signals
=======
The commonly used signals of an LinkButton are::

  "activate-link" (linkbutton)

An ``"activate-link"`` signal is emitted when the user clicks on the LinkButton. By default, clicking on the LinkButton opens a web browser but the signal can be used to cause another function with custom behaviour to be run.

=======
Example
=======
Below is an example of a LinkButton:

.. literalinclude:: _examples/linkbutton.py

Download: :download:`LinkButton <_examples/linkbutton.py>`
