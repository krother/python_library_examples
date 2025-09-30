
How to write a JSON file?
=========================

The builtin module `json` module converts Python dictionaries to JSON and back.
The *JavaScript Object Notation (JSON)* is frequently used to send structured data around the web or store it painlessly in files.
The `json` modules utilizes the similarity of the JSON format to Python dictionaries.

.. code:: python3

   import json

   data = {"apples": 1, "bananas": "two", "cherries": [3,4,5]}
   with open("data.json", "w") as f:
        jj = json.dumps(data)
        f.write(jj)

.. note::

   You could write to the file directly with `json.dump`.

How to read a JSON file?
========================

Loading a JSON data structure from a file results in a list or dictionary:

.. code:: python3

   with open("data.json") as f:
       data = json.loads(f.read())
   print(data)

Instead of parsing a string object, you could parse from the file directly with `json.load()`

.. seealso::
    
    `Documentation of the json module <docs.python.org/3/library/json.html>`__
    