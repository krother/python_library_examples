How to connect Python to MongoDB?
=================================

The `pymongo` library connects to a Mongo database server.
It is capable of interacting with both local and remote databases.
To connect to a local instance, no extra parameters are necessary.

Install it with:

.. code::

    pip install pymongo

Launch MongoDB through docker
-----------------------------

To try MongoDB, it is best to launch it in a local docker container:

.. code::

    docker run -d -p 27017:27017 mongo

Run queries
-----------

The following code connects and runs a few queries:

.. literalinclude:: pymongo_connect.py

.. seealso::

   `Pymongo documentation <http://api.mongodb.org/python/current/>`__
