
How to Download a web page?
===========================

The `httpx` library sends HTTP requests to web pages and allows you to read their content.
Most standard tasks are much easier than the standard module `urllib` and implemented cleaner than the outdated `requests` library.
Sending data to web forms via HTTP GET and POST, submitting files and managing cookies are features of this useful library.

Install `httpx` with:

.. code::

    pip install requests

The following code reads a static web page:

.. literalinclude:: example_requests.py

How to submit a HTTP GET request from Python?
=============================================

Here is a search with HTTP GET parameters:

.. literalinclude:: search_with_parameters.py

.. seealso::

   `https://www.python-httpx.org/ <https://www.python-httpx.org/>`__
