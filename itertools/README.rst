
How to flatten a list of lists?
===============================

The builtin module `itertools` contains plenty of functions to work with lists and iterators.
Most functions in this module return *iterators* themselves, so they can be consumed by loops or `next()`. You can also convert them to a list.

Below you find a few examples:

.. literalinclude:: example_itertools.py

.. seealso:: 

    `Documentation of the itertools module <https://docs.python.org/3/library/itertools.html>`__
