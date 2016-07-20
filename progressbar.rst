ProgressBar
===========
A ProgressBar is used to display progress of an operation visually. It is used when there is a long-running operation in progress, which requires the user to be updated on how long it will take or how much has been completed.

===========
Constructor
===========
The ProgressBar can be constructed using the following::

  progressbar = Gtk.ProgressBar(orientation)

The *orientation* value allows the ProgressBar to be set to operate in two ways. By default, ``Gtk.Orientation.HORIZONTAL`` is used forcing the ProgressBar to move left-to-right. Alternatively, using ``Gtk.Orientation.VERTICAL`` allows the ProgressBar to move from top-to-bottom.

=======
Methods
=======
To set the amount of job which has been completed call::

  progressbar.set_fraction(fraction)

The *fraction* parameter should be a value between ``0.0`` and ``1.0``, with the float value indicating the percentage of the job that has been completed.

Alternatively, the amount completed can be retrieved using::

  progressbar.get_fraction()

The value returned to the *fraction* variable will be a value between ``0.0`` and ``1.0``.

To display text within the ProgressBar, use::

  progressbar.set_text(text)

The *text* parameter should be a string of text informing the user of time remaining or number remaining.

If text is to be displayed using the ``.set_text()`` method, then you will also need to explicitly show the text with::

  progressbar.set_show_text(show_text)

Setting the *show_text* argument to ``True`` displays whatever text was provided to the ``.set_text()`` method. If no text was set using the ``.set_text()`` method, then the percentage completion of the ProgressBar is used.

In some cases it may not be known how much of a job has been completed however it is still required to display feedback to the user. An alternative to setting a percentage completion is to use::

  progressbar.pulse()

Using pulsing allows the bar to bounce from side-to-side indicating that a job is in progress. Every time the bar is to be moved, the ``.pulse()`` method should be called. It is commonly used within a loop which is executed while the job is in progress.

The step each pulse increments is set via::

  progressbar.set_pulse_step(step)

The *step* value should be a number between ``0.0`` and ``1.0``.

In some cases, particularly when using right-to-left languages, it may be useful to also set the ProgressBar to operate backwards. This can be set with::

  progressbar.set_inverted(inverted)

When *inverted* is set to ``True``, a horizontal bar will move from right-to-left and a vertical will move bottom-to-top.

=======
Example
=======
Below is an example of a ProgressBar:

.. literalinclude:: _examples/progressbar.py

Download: :download:`ProgressBar <_examples/progressbar.py>`
