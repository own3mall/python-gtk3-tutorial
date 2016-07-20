Signal Theory
=============
GTK+ responds to events which occur while the application is waiting in ``gtk.main()``. When an event, such as a mouse click occurs, control is passed to the appropriate function before returning to ``gtk.main()``.

Control is passed using signals. When an event occurs, the appropriate signal is emitted by the widget that was interacted with. The type of event used by a widget depends on what it is. For example a Button has a ``"clicked"`` event, however a Label does not.

A generic example of a signal is::

  widget.connect("event", function, data)

Firstly, the widget is the name of the widget which have created at construction time. There are many widgets which use signals to communicate with other areas of the application, for example a Button. Next, the event method is the action which has been performed. Each widget has its own particular events which can be emitted. Using our Button example, we would usually set the event to ``"clicked"``. This means that when the Button is clicked, the signal is emitted. Finally the data argument should be passed when the signal is issued and provides the function with extra parameters it may require. Upon connection of a signal, a handler id value is returned which identifies the connected signal.

To disconnect this at a later time::

  widget.disconnect(handler_id)

===============
Arguments Error
===============
When connecting signals from widgets, it is important to pass the correct number of parameters. The number of parameters, and the type depend on the signal being connected. If the number of parameters passed is greater than the number of parameters a function can receive, an error similar to below will be displayed::

  TypeError: function() takes exactly 2 arguments (3 given)

Alternatively, if the number of parameters being provided is fewer than the number that a function can receive, an error similar to below will be displayed::

  TypeError: function() takes exactly 4 arguments (1 given)
