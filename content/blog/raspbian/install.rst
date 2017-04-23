Install Raspberry Pi (RPi)
============================

:date: 2015-01-02
:summary: Installing Rasbian
:modified: 2016-11-27

.. figure:: {filename}/blog/raspbian/pics/rpi-org.png
	:width: 200px
	:align: center


Where to buy?
-------------

I always buy mine from `Adafruit <https://www.adafruit.com>`__, they
have tons of other great stuff at great prices. They also make make lots
of example code and drivers available for their products.

Install
--------

`Raspbian <http://www.raspbian.org>`__ is a Raspberry optimized version
of Debian. The version installed here is based on Debian Jessie.

::

    [kevin@raspberrypi ~]$ lscpu
    Architecture:          armv6l
    Byte Order:            Little Endian
    CPU(s):                1
    On-line CPU(s) list:   0
    Thread(s) per core:    1
    Core(s) per socket:    1
    Socket(s):             1

Note this output doesn't really tell you much other than it is ARMv6.

Copying an image to the SD Card in Mac OS X
-------------------------------------------

.. figure:: {filename}/blog/raspbian/pics/sd.jpg
   :width: 200px
   :alt: sd logo

These commands and actions need to be performed from an account that has
administrator privileges.

1. Download the image from a `mirror or
   torrent <http://www.raspberrypi.org/downloads>`__.

2. Verify if the the hash key is the same (optional), in the terminal
   run::

       shasum ~/Downloads/debian6-19-04-2012.zip

3. Extract the image::

       unzip ~/Downloads/debian6-19-04-2012.zip

4. Attach the SD Card to the computer and identify the mount point::

       df -h

   Record the device name of the filesystem's partition, e.g.
   ``/dev/disk3s1``

5. Unmount the partition so that you will be allowed to overwrite the
   disk, note that unmount is **NOT** the same as eject:

   ::

       sudo diskutil unmount /dev/disk3s1

6. Write the image to the card with this command:

   ::

       sudo dd bs=1m if=rasbian.img of=/dev/rdisk3

7. After the dd command finishes, eject the card:

   ::

       sudo diskutil eject /dev/disk3

8. Insert it in the raspberry pi, and have fun

Pi Zero Only
----------------

You need to make a couple more changes before you put the SD card into the Pi.

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

Configuration
--------------

Once you download and install Raspbian you have to configure it for it to be useful.

#. ``sudo raspi-config`` and change
    #. update ``raspi-config`` via the advanced option, update
    #. hostname
    #. memory split between GPU and RAM
	#. set local to en_US.UTF-8 UTF-8 (the default is en-GB)
    #. resize the file system to the size of your disk
    #. set correct timezone via the internationalization option
    #. turn on I2C interface
#. ``sudo apt-get update`` and then ``sudo apt-get upgrade``
#. ``sudo apt-get install apt-show-versions``
#. ``wget https://bootstrap.pypa.io/get-pip.py`` and then ``python get-pip.py``
#. ``sudo apt-get install rpi-update`` and then ``sudo rpi-update`` to update the kernel
#. Fix the pip paths so you don't have to use sudo (that is a security risk)
    #. ``sudo chown -R pi /usr/local``
    #. ``sudo chown -R pi /usr/lib/python2.7/dist-packages``
#. Fix the ``pip`` compile issues ``sudo apt-get install python-dev``
#. Find outdated python libraries with ``pip list --outdated`` then update them with ``pip install -U package_name``

Useful Software
-----------------

Add the following software with::

	sudo apt-get install <package> <package> ...

Some useful packages are:

* cmake
* build-essential
* python-dev
* nmap
* arp-scan
* htop
* git


Add the following software with::

	pip install <package> <package> ...

* pyarchey
* numpy

Headless
----------

Raspbian is now posting images for a *Lite* version of Raspbian, I suggest you
use that if you are doing headless.

SSH Login
---------

To increase security, you can disable password logins and rely on ssh
public keys. To do this, take a look
`here <https://wiki.archlinux.org/index.php/SSH_Keys>`__ for details.
Basic steps are:

1. Generate an ssh key::

       ssh-keygen

2. Copy the public key (.pub) to the server you will connect to::

       ssh-copy-id username@remote-server.org

3. Edit /etc/ssh/sshd\_config to disable password logins::

       PasswordAuthentication no
       ChallengeResponseAuthentication no

OSX
~~~~

On OSX install ``ssh-copy-id`` via ``brew`` and in a terminal window on OSX::

    ssh-copy-id pi@raspberry.local
