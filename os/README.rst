
How to check whether a file exists?
===================================

The `os` module provides an easy way to interact with files, directories and other parts of your operating system. It contains many functions to list, change, copy, remove and examine files and directories.

.. code:: python3

   import os

   print(os.path.exists('README.rst'))

How to copy or remove a file from Python?
=========================================

`os` does these as well:

.. code:: python3

   import os

   os.system('cp README.md copy.md')

   os.remove('copy.md')


How to loop over all files in a directory?
==========================================

The following code prints all Python files in a given folder:

.. code:: python3

   import os

   for filename in os.listdir("/home/participant/"):
       if filename.endswith(".py"):
           print(filename)


How to run a command-line program from Python?
==============================================

A very simple way to start other processes is the `os.system()` function.
The following example starts a program to list contents of a folder and redirects the output to a file:

.. code:: python3

   import os

   os.system("ls -l > result.txt")

.. warning::

    `os.system` does not allow for any communication with the running process.
    If it crashes or runs forever, your Python code won't learn about it.
    A safer alternative is the `multiprocessing` module.

.. seealso::
    
    `Documentation of the os module <https://docs.python.org/3/library/os.html>`__
