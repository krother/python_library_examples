
How to format the current time as a string?
===========================================

The builtin module `time` contains a convenient one-stop function:

.. code:: python3

   import time

   print(time.asctime())

An alternative is to retrieve the time and date as a `datetime` object that can be formated to custom strings:

.. code:: python3

   print(time.strftime('%a %d.%m.', time.localtime()))

How to use a datetime object?
=============================

The `date` and `datetime` objects have attributes for time components:

.. code:: python3

   import datetime

   date = datetime.date(2025, 9, 30)
   print(date.year, date.month, date.day)

You can use explicit attribute names when creating date objects:

.. code:: python3

   timestamp = datetime.datetime(year=2025, month=9, day=30, hour=7, minute=25, second=0)
   print(timestamp.minute)

How to let a program wait for a while?
======================================

The `time.sleep()` function gives back control to the Python interpreter. If you are running multiple threads they may do something.

.. code:: python3
    
   import time

   time.sleep(3)

Note that if you are in an asynchronous function, you will have to use `asyncio.sleep()`.

.. code:: python3

    import asyncio

    async def wait():
        await asyncio.sleep(3)

    asyncio.run(wait())

.. seealso::

   -  `Documentation for the time module <https://docs.python.org/3/library/time.html>`__
   -  `Documentation for the datetime module <https://docs.python.org/3/library/datetime.html>`__
