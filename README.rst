pymitv4
=======

A Python 3 based control for Xiaomi TV 4

.. figure:: https://i.imgur.com/kOLWhWU.jpg
   :alt: Xiaomi TV 4

Xiaomi TV 4 series

Introduction
------------

This package interfaces with the Xiaomi TV 4 series through its local
HTTP API using Python. Discovery and control features are included.
Support for Xiaomi TV 3 devices is no longer guaranteed.

Supported models
''''''''''''''''

- Xiaomi TV 4 (all sizes)

Compatibility notes
''''''''''''''''''''

- Xiaomi TV 3 models may not work with this version


Documentation
-------------
You can find the documentation on Github here_.

Additional controller endpoints
------------------------------

- ``/controller?action=getsysteminfo`` returns system information in JSON
- ``/controller?action=capturescreen`` grabs a screenshot in binary form
- ``/controller?action=getinstalledapp&count=999&changeIcon=1`` lists installed apps
- ``/controller?action=startapp&type=packagename&packagename=PACKAGE`` starts a package


.. _one.: http://www.mi.com/en/mitv4/65/
.. _here: https://github.com/Arbuzov/pymitv4
