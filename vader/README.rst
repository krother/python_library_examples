
How to calculate a simple sentiment score for a text?
=====================================================

The `vader` libary provides a straightforward sentiment score.
It is based on a word list, so it is not super accurate and does not catch any nuances.
But it is fast and sufficient for a quick scan.

Installation
------------

::

    pip install vaderSentiment

Usage
-----

.. literalinclude:: vader.py

The sentiment includes a positive, negative and neutral score, which add up to 1.0.
