
How to store data in a SQLite database?
---------------------------------------

The builtin module `sqlite3` manages SQLite databases.
SQLite is a very straightforward SQL database. 
In contrast to **MySQL** or **PostGreSQL**, the data is stored in a single file.
For using the `sqlite3` module you don't need to install or set up anything. 

SQLite is sufficient only for small SQL databases, but Python modules for bigger databases look very similar.

Here is a usage example:

.. literalinclude:: example_sqlite.py

.. seealso:

   `sqlite3 documentation <https://docs.python.org/3/library/sqlite3.html>`__
