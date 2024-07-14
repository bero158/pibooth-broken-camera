
==============
pibooth-broken-camera
==============

|PythonVersions|

``pibooth-broken-camera`` is a plugin for the `pibooth`_ application.

The meaning of this plugin is to make Pibooth more reliable. This plugin is trying to solve dozens of issues with camera, camera state, camera firmware, flash battery, USB connection and many others.
This plugin adds GPhoto2 two restart actions after preview or capture initialy fails. 
The plugin is based on `pibooth_example` "Setup a custom camera" from piboot documentation 
Install
-------

Upload the plugin somewhere and appent the absolute path to your pibooth.cfg (~/.config/pigooth/pibooth.cfg) to parameter 'plugins'
aka: plugins = "/home/pi/pibooth/pibooth-broken-camera/pibooth-broken-camera.py"

Configuration
-------------

The plugin has no configuration. The only option here is you can enable/disable it

Example
-------

Here is an example of the rendering you can get with this plugin on the wait screen:

.. image:: https://github.com/bero158/pibooth-broken-camera/blob/main/docs/images/cam_fail.png
   :align: center
   :alt: Example screenshot

.. --- Links ------------------------------------------------------------------

.. _`pibooth`: https://pypi.org/project/pibooth
.. _`pibooth_example`: https://documentation.pibooth.org/en/stable/sources/plugins/examples.html

.. |PythonVersions| image:: https://img.shields.io/badge/python-3.6+-red.svg
   :target: https://www.python.org/downloads
   :alt: Python 3.6+

https://github.com/bero158/pibooth-myip/blob/main/docs/images/waitscreen.png