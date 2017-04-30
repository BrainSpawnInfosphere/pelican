Install Raspberry Pi (RPi) Zero
======================================

:date: 2017-04-30
:summary: Installing Rasbian on Pi Zero W

.. figure:: {filename}/blog/raspbian/pics/rpi-org.png
	:width: 200px
	:align: center
  
You need to make a couple changes before you put the SD card into the Pi.

In ``config.txt``, add the following to the bottom::

	dtoverlay=dwc2

In ``cmdline.txt``, add this right after ``rootwait``::

	modules-load=dwc2,g_ether

Now put the SD card in the Pi and plug the Pi into your computer with a USB cable.

To give it access to the internet:

* System Preferences
	* Sharing
		* Share your connection from: WiFi (or Ethernet if you have a wired connection)
		* To computers using: RNDIS/Ethernet Gadget
		* Then check/select ``Internet Sharing`` in the service box

**Note:** If you already plugged in your Pi to your computer, you will need to
reboot the Pi using::

	sudo reboot

This process sets up a dhcp server for the ``RNDIS/Ethernet Gadget`` and assigns
it an IP address, then allows it to talk to the internet using WiFi.

A good resource is `here <file:///Users/kevin/Desktop/Connect%20To%20A%20Raspberry%20Pi%20Zero%20With%20A%20USB%20Cable%20And%20SSH.htm>`__
