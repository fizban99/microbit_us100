Basic micropython library to read the distance from an ultrasonic sensor US-100 in serial mode
##############################################################################################

This library allows the micro:bit to read the distance from an ultrasonic sensor US-100 (Y401)).

It uses the serial port to communicate with the device and to retrieve both the distance and temperature. By default it assumes pin15 connected to trigger/tx and pin14 connected to echo/rx

.. contents::

.. section-numbering::


Main features
=============

* Get the distance in mm from the sonar to an object.
* Get the temperture measured by the sensor.
* Sample program.


Library usage
=============


distance_mm()
+++++++++++++++++++++++


Get the distance in mm.


.. code-block:: python

   from us100 import US100
   from microbit import sleep


   sonar=US100()
   while True:
       print('%.1f' % (sonar.distance_mm()/10))
       sleep(1000)

temperature()
+++++++++++++++++++++++


Get the temperature from the sonar


.. code-block:: python

   from us100 import US100
   from microbit import sleep


   sonar=US100()
   while True:
       print('%i' % sonar.temperature)
       sleep(1000)

