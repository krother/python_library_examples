
How to create a 2D game in the terminal?
========================================

The `curses` library creates x/y output in a console window.
It supports colors and Unicode tiles (depending on your terminal).
`curses` is installed with Python by default.

On Windows you may need to install `windows-curses`.

Running the example:
--------------------

In :download:`pac.py`, you find a minimalistic Pac game.
Run it from a terminal.


.. warning::

   If you get the error message:

   ``curses function returned NULL``

   It likely means that your window is too small.

.. seealso::

   My first contact with curses was inspired by `manti_go <https://github.com/JoNiederhut/manti_go>`__ written by my course participants.
