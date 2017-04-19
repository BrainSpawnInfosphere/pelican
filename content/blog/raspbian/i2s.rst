Digital Audio (I2S)
=====================

:date: 2016-07-26
:summary: Setting up an RPi3/Raspbian-Jessie with digital audio and avoiding the noise from the Pi's analog output

.. figure:: https://cdn-learn.adafruit.com/assets/assets/000/032/618/medium800/adafruit_products_3006_kit_ORIG.jpg?1464029419
  :align: center


Setting up I2S audio isn't too hard. I used a `Adafruit i2s 3W amp (MAX98357A) <https://www.adafruit.com/products/3006>`_, to
hook it up to my rpi3.

Edit ``/boot/config.txt``::

  # dtparam=audio=off
  dtparam=i2s=on
  dtoverlay=hifhiberry-dac

Create/edit ``/etc/asound.conf`` to setup default audio::

  pcm.!default  {
    type hw card 0
  }
  ctl.!default {
    type hw card 0
  }

Now you have to reboot so the system gets setup correctly (remember, these are boot parameter settings).

Now connect the amp to the rpi:

===== ======
Vin   5V
Gnd   Gnd
DIN   21
BCLK  18
LRCLK 19
===== ======

.. figure:: https://cdn-learn.adafruit.com/assets/assets/000/032/643/medium800/adafruit_products_3006_top_demo_ORIG.jpg?1464037283
  :align: center


Now, lots of instructions on the internet say to disable i2c, but you don't have too. The bottom part of my
``/boot/config.txt`` looks like this::

  # Enable audio (loads snd_bcm2835)
  #dtparam=audio=off
  start_x=1
  gpu_mem=16
  dtparam=i2c_arm=on
  dtparam=i2s=on
  enable_uart=0
  dtoverlay=hifiberry-dac

As you can see, I leave i2c on. Note the ``enable_uart=0`` is so I can use bluetooth. Apparently, the BT module is tied to
the hardware serial port and the don't bother to tell people. You have to spend a lot of time to dig it up.

Test
-----

1. Random static: ``speaker-test -c2``
2. Wave file: ``speaker-test -c2 --test=wav -w /usr/share/sounds/alsa/Front_Center.wav``


References
-----------

* `Adafruit tutorial 1 <https://learn.adafruit.com/adafruit-max98357-i2s-class-d-mono-amp?view=all>`_
* `Adafruit tutorial 2 <https://learn.adafruit.com/raspberry-pi-zero-npr-one-radio?view=all>`_
* `Raspberry Pi Forum discussion <https://www.raspberrypi.org/forums/viewtopic.php?t=97314>`_
* `pimoroni <http://learn.pimoroni.com/tutorial/phat/raspberry-pi-phat-dac-install>`_
* `Raspberry Pi pinout <http://pinout.xyz/>`_
