Dead Reckoning and Encoders
===============================

:date: 2017-06-11
:summary: How to use wheel encoders to determine distance travelled

.. figure:: {filename}/blog/robots/pics/usdigital_encoder.gif
  :align: center

There are many types of encoders, above is a US Digital encoder designed to
be mounted on a motor shaft.

.. figure:: {filename}/blog/robots/pics/quadrature_encoder.gif
  :align: center

The optical encoder, shines a series of lights through an encoder disk and
the light is detected or not detected on the other side of the encoder disk
by some photoreceptors. A quadrature encoder has 2 signals, A and B, which
are phased such that they are *never* high or low at the same time. Depending
on the phase of the signals, the direction can be determined.

.. figure:: {filename}/blog/robots/pics/quadrature_animation.gif
  :align: center

The animation shows the signals produced from the movement of the motor
shaft, with the encoder disk attached to it.

.. figure:: {filename}/blog/robots/pics/quadrature_waveform.gif
  :align: center

Again, the wave form from A and B tells us if the wheel (motor shaft
and disk) are moving in the forward or reverse direction. Note that
forward/reverse are arbitray and the engineer needs to determine
if CW or CCW is forward or reverse depending on how the sensor was
mounted to the robot.

.. figure:: {filename}/blog/robots/pics/quadrature_resolution.gif
  :align: center

The resolution of the encoder is determine by how the 2 signals are
read.

- reading A and B on rising edge of A gives you the resolution of how many
  stripes there are on the disk
- reading on the rising and falling edge of A gives you twice the resloution
  of the number of stripes on the disk
- reading both A and B for both rising and falling edges gives you 4 times
  the resolution as the number of stripes on the disk

Now, obviously, the last option gives you the greatest resoution and the
best performance ... so why wouldn't you do it? If the speed of your 
microcontroller is too slow and/or the speed of your wheel is too fast, you
could get stuck answering interrupts all the time and never doing anything
else. You have to balance your system constraints properly.




References
=============

- `Dead Reckoning Wikipedia <https://en.wikipedia.org/wiki/Dead_reckoning>`_
