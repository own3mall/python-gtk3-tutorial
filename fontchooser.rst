FontChooser
===========
The FontChooser is an interface which is used by :doc:`fontchooserwidget`, :doc:`fontchooserdialog`, and :doc:`fontbutton`.

.. note:

  This widget would generally not be called by the application directly. However, the methods it offers are common among the three objects :doc:`fontchooserwidget`, :doc:`fontchooserdialog`, and :doc:`fontbutton`.

=======
Methods
=======
To retrieve the font family, attributes (bold, italic, etc), or the size selected, use the methods::

  fontchooser.get_font_family()
  fontchooser.get_font_face()
  fontchooser.get_font_size()

Finally, the call for retrieving the actual font selected is::

  fontchooser.get_font()

To retrieve a normalised string from the FontChooser, describing the font selected use::

  fontchooser.get_font_desc()

The ``.get_font_desc()`` method will return a string such as "Cantarell Bold Italic 12".

It is also possible to set the font using a description::

  fontchooser.set_font_desc(font_desc)

.. note::

  When using ``.set_font_desc()``, the font description entered may change. For example, if you enter "Bold Droid Sans", the FontChooser may change this to "Droid Sans Bold 12".

The FontChooser objects also support setting a font::

  fontchooser.set_font(font)

A preview entry can be used to allow the user to test the font selected. This can be enabled or disabled via::

  fontchooser.set_show_preview_entry(show_entry)

The default value  is ``True`` which shows the preview entry.

The preview text is the string which showcases the font, size, and other attributes. By default, this is set to "The quick brown fox jumped over the lazy dog.", however can be customised using::

  fontchooser.set_preview_text(preview_text)

If required, the preview text can also be returned::

  fontchooser.get_preview_text()

=======
Signals
=======
The commonly used signals of an FontChooserDialog are::

  "font-activated" (fontchooserdialog, font)

The ``"font-activated"`` event emits from the FontChooserDialog when a font is selected either via double-clicking with the mouse, or by pressing the Enter/Return key.

=======
Example
=======
To view an example of the FontChooser, see the code for the objects :doc:`fontchooserwidget`, :doc:`fontchooserdialog`, and :doc:`fontbutton`.
