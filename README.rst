Collectclient - a client for `Collector`_
=========================================

.. _Collector: https://github.com/FFM/Collector

This is a python module to ease statistics collection: the module will
automatically generate the right data out of your (json-serializable) data
- timestamp it etc.

Dependencies
------------

* pyzmq==2.2.0

Installation
------------

``pip install git+https://github.com/FFM/Collectclient``

Usage
-----

Usage is simple::
  
  import collectclient
  c=collectclient.Collect(test="dummy",resource="address") # assumes collector is running on 127.0.0.1:25500
  c.write("FOO")


