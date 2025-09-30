
How to parse a XML file?
========================

The builtin module `xml` parses XML files.
It contains several XML parsers. They all produce a tree of DOM objects for each tag that can be searched and allow access to attributes.

The following code parses the XML file :download:`hamlet.xml`:

.. literalinclude:: parse_xml.py

How to write a XML file?

You can create a tree of DOM objects from scratch and write it to a XML file:

.. literalinclue:: write_xml.py

.. seealso::

   `Documentation of the XML module <https://docs.python.org/3/library/xml.html>`__
