
How to read a Word Document?
----------------------------

`python-docx` reads and writes Word documents (`.docx`).

A straightforward library to access documents in MS Word format. Available features include text, labeled sections, pictures and tables.

Install it with:

.. code::

    pip install python-docx


The following code reads the document in :download:`hamlet.docx`:

.. literalinclude:: read_word_doc.py

How to write a Word Document?
-----------------------------

Writing a Word document is not very complicated either:

.. literalinclude:: create_doc.py

.. hint::

    With `python-docx` it is possible to read a word document, modify the content and write the result without losing existing format information.

.. seealso::

   `python-docx.readthedocs.org <https://python-docx.readthedocs.org>`__
