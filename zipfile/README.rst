
How to create a zip archive?
============================

With the builtin module `zipfile`, you can add both existing files and strings to a zip file. If you are adding strings you need to specify the file name it is written to. When you extract files to a folder, the output folder is automatically created.

.. code:: python3

   import zipfile

   z = zipfile.ZipFile('archive.zip', 'w')
   z.write('myfile.txt')                   # already existing file
   z.writestr('test.txt', 'Hello World')   # string to new file
   z.close()

How to read a zip archive?
==========================

List the contents of a zip file:

.. code:: python3

   z = zipfile.ZipFile('archive.zip')
   print(z.namelist())


Extract a file to a new folder:

.. code:: python3

   print(z.extract('test.txt', 'myfolder'))
   z.close()


.. seealso::

   `Documentation of the zipfile module <https://docs.python.org/3/library/zipfile.html>`__
