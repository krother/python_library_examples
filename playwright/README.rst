
How to test web pages?
======================

Playwright is a modern alternative to **Selenium** for remote-controlling a web browser, accessing pages, filling forms and accessing the HTML content.
You can use playwright both for testing web pages and scraping or run it in CI in *headless* mode.

Install it with:

.. code:: text

    pip install playwright
    playwright install



Playwright can remote-control the browsers **Chrome, Firefox and Safari**.
It covers all steps of a web session such as visiting pages, filling forms, and interacting with dynamic page elements.
This makes Playwright excellent for end-to-end tests and extensive automations.

.. literalinclude:: playwright_example.py

.. card::
   :shadow: lg

   **Exercise**

   Run the code. Trace what each line does.

----

Identifying HTML Elements
-------------------------

Since the content and design of web pages change frequently, scripts that depend on exact IDs or element types of an HTML page require high maintenance effort.
Therefore, in addition to the classic ``id``, Playwright uses generic locator functions that refer to the role of a given element:

.. code::
   
   get_by_role()
   get_by_label()
   get_by_title()
   get_by_text()

Using the individual locators can be a bit tricky.
Fortunately, Playwright takes care of most of the work for you.

----

The Test Generator
------------------

Playwright comes with a **Test Generator** that records a browser session and generates code from it.
This allows even complex test cases to be quickly turned into code.

The test generator can be started with:

.. code::

   playwright codegen www.ecosia.org


.. card::
   :shadow: lg

   **Exercise**

   Create a browser automation using the Test Generator.
   Clean up the code a bit and run it.

----

Wait Functions
--------------

Before performing an action, Playwright waits for an element to be

* part of the DOM (the HTML page)
* visible
* stable, i.e. not animated
* responsive to screen events, meaning not hidden behind other elements
* not *"disabled"*

Therefore explicit waiting is often not necessary.
If you do want to wait explicitly, use the method

.. code:: python

   page.is_visible("#element-id")


----

Forms & Drag & Drop
-------------------

The mechanics of forms follow the same principles as locators for other elements.
The only additions are methods like ``.fill()`` and ``.click()``.

Here is an example of a search query:

.. literalinclude:: playwright_form.py


.. seealso::
    
   `playwright.dev/python/ <https://playwright.dev/python/>`__
