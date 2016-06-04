EntryCompletion
===============
An EntryCompletion can be attached to an Entry widget to provide suggestions which match the characters entered.

===========
Constructor
===========
The EntryCompletion can be constructed using the following::

  entrycompletion = Gtk.EntryCompletion()

=======
Methods
=======
Once the EntryCompletion has been constructed, a model needs to be attached. This is used to store the potential values which can be matched::

  entrycompletion.set_model(model)

The *model* should be the name of a ListStore object.

Obtaining the model holding the EntryCompletion values can be done with::

  entrycompletion.get_model()

The text column must also be set which refers to which column within the ListStore the potentially matches should be listed::

  entrycompletion.set_text_column(column)

To prevent completion lookups occuring before a certain number have characters have been entered, the following method can be used::

  entrycompletion.set_minimum_key_length(length)

The *length* parameter should be set to an integer value.

To cycle through the position completions within the Entry::

  entrycompletion.set_inline_completion(inline)

When *inline* is set to ``True``, the user can cycle through the matching completions by tabbing.

Alternatively, there is an option to provide a list of completions popped up in a popup window with::

  entrycompletion.set_popup_completion(popup)

Retrieval of the Entry widget associated with the EntryCompletion can be made with::

  entrycompletion.get_entry()

Additional action items can be added to the EntryCompletion if required, either via plain text or markup with::

  entrycompletion.insert_action_text(index, text)
  entrycompletion.insert_action_markup(index, markup)

The *index* value specifies the location in the dropdown menu where the action item will be added. The *markup* parameter allows tags to be added to customise the added text.

An action can also be deleted by specifying the index via::

  entrycompletion.delete_action(index)

=======
Example
=======
Below is an example of a EntryCompletion:

.. literalinclude:: _examples/entrycompletion.py

Download: :download:`EntryCompletion <_examples/entrycompletion.py>`
