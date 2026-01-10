Web-Browsing automatisieren
===========================

In diesem Kapitel geht es darum, einen Browser direkt fernzusteuern, anstatt mit dem Server auf HTTP-Ebene zu interagieren.
Die Hauptmotivation dafür ist, daß bei den meisten Webseiten der Browser Code ausführt, der für das Verhalten der Webseite relevant ist.


Anwendungsfälle
---------------

* Testen des Front-Ends
* End-2-End-Tests
* Seiten mit dynamischen Inhalten (JS-Skripten, nachladen von Inhalten)
* Scraping von Inhalten, an die anders nur schwierig heranzukommen ist.

----

Python-Bibliotheken zur Browser-Automatisierung
-----------------------------------------------

Für lange Zeit war **Selenium** der Goldstandard der Browser-Automatisierung.
In letzter Zeit setzt sich jedoch die modernere und leichtgewichtige Bibliothek **Playwright** durch.
Sie läßt sich installieren mit:

.. code::

   pip install playwright
   playwright install


Playwright kann die Browser **Chrome, Firefox und Safari** fernsteuern.
Sämtliche Schritte einer Web-Session wie Besuchen von Webseiten, Ausfüllen Formularen und dynamische Seitenelemente lassen sich damit abdecken.
Damit ist Playwright ausgezeichnet für End-to-End-Tests und ausgedehnte Automatisierungen geeignet.

.. literalinclude:: playwright_example.py

.. card::
   :shadow: lg

   **Übung**

   Führe den Code aus. Vollziehe nach was die einzelnen Zeilen tun.

----

HTML-Elemente identifizieren
----------------------------

Da sich Inhalt und Design von Webseiten häufig ändern, verursachen Skripte, die von den genauen IDs Arten von Elementen einer HTML-Seite abhängen einen hohen Wartungsaufwand.
Deshalb verwendet Playwright zum lokalisieren von Elementen neben der klassischen ``id`` generische Funktionen, welche sich auf die Funktion eines gegebenen Elements beziehen:

.. code::
   
   get_by_role()
   get_by_label()
   get_by_title()
   get_by_text()

Das Verwenden der einzelnen Locators ist etwas knifflig.
Zum Glück nimmt Playwright einem einen Großteil der Arbeit ab. 

----

Der Test Generator
------------------

Playwright ist mit einem **Test Generator** ausgestattet, der eine Browser-Session aufzeichnet und daraus Code generiert. 
Damit können auch komplizierte Testfälle schnell in Code umgewandelt werden.

Der Test-Generator lässt sich starten mit:

.. code::

   playwright codegen www.ecosia.org


.. card::
   :shadow: lg

   **Übung**

   Erzeuge eine Browser-Automatisierung mit dem Test Generator.
   Räume den Code etwas auf und führe ihn aus.

----

Wartefunktionen
---------------

Vor dem durchführen einer Aktion wartet Playwright darau, dass ein Element

* Teil des DOM-Objekts (der HTML-Seite) ist
* sichtbar ist
* stabil, d.h. nicht animiert
* für Bildschirmereignisse ansprechbar ist, also nicht hinter anderen Elementen verborgen
* nicht *"disabled"* ist

Deshalb ist ein explizites Warten oft nicht notwendig.
Möchte man doch explizit warten tut dies die Methode

.. code:: python

   page.is_visible("#element-id")


----

Formulare & Drag & Drop
-----------------------

Die Mechanik von Formularen funktioniert nach den gleichen Prinzipien wir Lokatoren
für andere Elemente.
Lediglich Methoden wie ``.fill()`` und ``.click()`` kommen hinzu.

Hier ist ein Beispiel für eine Suchanfrage:

.. literalinclude:: playwright_form.py


.. seealso::

   `Playwright Dokumentation <https://playwright.dev/python/docs/intro>`__
