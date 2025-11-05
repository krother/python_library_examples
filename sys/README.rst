
How to find out where the interpreter is looking for importable modules?
========================================================================

The builtin module `sys` provides an access point to the Python environment.
You find there command line arguments, the import path settings, the standard input, output and error stream and many more.

The `sys.path` variable contains the current directory, everything from the `PYTHONPATH` environment variable, and Pythons own folders.

.. code:: python3

   print(sys.path)


How to call a Python program with command-line parameters?
==========================================================

The variable ``sys.argv`` contains a list of command-line arguments.
The first one is usually the name of the called script.

.. code:: python3

   import sys

   print sys.argv

When you call this program with any of:

::

   python script.py
   python script.py hello world
   python script.py 1 2 3

You should see a difference.

How to terminate a Python program gracefully?
=============================================

The `sys.exit()` function ends execution of the Python interpreter immediately.

.. code:: python3

   import sys

   sys.exit()


.. seealso::

   `Documentation of the sys module <https://docs.python.org/3/library/sys.html>`__
