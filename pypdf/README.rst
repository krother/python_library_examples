
How to merge multiple PDFs into one?
------------------------------------

The `pypdf` library manipulates PDF documents on the page level, e.g. merging two or more PDFs.

Install it with:

.. code::

    pip install pypdf

The following code merges all PDF files from the input path into a single one:

.. literalinclude:: merge.py

How to merge multiple images into a PDF
---------------------------------------

With `pypdf` you can also merge images into a PDF:

.. literalinclude:: merge_images.py
