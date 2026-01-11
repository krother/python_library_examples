
How to optimize a linear problem?
---------------------------------

PuLP is a simple **Linear Problem Solver**. It solves systems with many linear equations, e.g. Sudokus, scheduling trains and many more. For complex LES problems you will need commercial software (like Gurobi), but PuLP helps you get the taste of it.

Install it with:

.. code::

    pip install pulp

The example below solves a magic square (insert the numbers 1..9 in to a 3x3 square
so that all rows and columns sum up to 15):

.. literalinclude:: magic_square.py
