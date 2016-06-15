Image
=====
The Image widget is able to display a variety of Image types within an application, and supports a number of formats including PNG, JPG, BMP, SVG, GIF, XPM.

===========
Constructor
===========
The Image can be constructed using the following::

  image = Gtk.Image()

=======
Methods
=======
After construction, there are a number of methods which can be used to display different image types. The common ones are::

  image.set_from_file(file_path)
  image.set_from_pixbuf(pixbuf)
  image.set_from_resource(resource_path)

The pixel size of the Image object can be set and retrieved with the methods::

  image.set_pixel_size(size)
  image.get_pixel_size()

To clear the graphic from the Image::

  image.clear()

Retrieval of the type of image currently held in the Image object can be done with::

  image.get_storage_type()

=======
Example
=======
Below is an example of a Image:

.. literalinclude:: _examples/image.py

Download: :download:`Image <_examples/image.py>`
