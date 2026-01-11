
How to find the most similar string?

The `thefuzz` library does fuzzy string matching using the `Levenshtein distance <https://en.wikipedia.org/wiki/Levenshtein_distance>`__.
It is great to match strings with typos.

Install it with:

.. code::

    pip install thefuzz
    python-Levenshtein

Here is a simple usage example:

.. literalinclude:: fuzzy_search.py

.. seealso::

    `GitHub project page <https://github.com/seatgeek/thefuzz>`__
