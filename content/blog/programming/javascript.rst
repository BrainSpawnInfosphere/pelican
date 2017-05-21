Node.js (Javascript)
========================

:date: 2017-05-21
:summary: Javascript snipets and useful libraries

Code
-------

Run code at set intervales:

.. code-block:: javascript

  var ONE_MINUTE = 60 * 1000;

  function showTime() {
    console.log(new Date());
  }

  setInterval(showTime, ONE_MINUTE);


Libraries
------------

- `Moments.js <http://momentjs.com/>`_ : time/date manipulation (16.6k)
- `Chart.js <http://www.chartjs.org/>`_ : scatter, pie, polar, bar, etc charts
- `Purecss <https://purecss.io/>`_ : A set of small, responsive CSS modules that you can use in every web project. Maintained by yahoo.
- `FortAwesome <https://github.com/FortAwesome/Font-Awesome>`_ : 
- `Nunjucks <https://mozilla.github.io/nunjucks/>`_ : a templating engine very similar to python's `jinja2 <http://jinja.pocoo.org/>`_ (8k gzipped)

npm
-------

- `mjpeg server <https://www.npmjs.com/package/raspberry-pi-mjpeg-server>`_ : raspberry pi camera streamer
- `Raspberry pi version <https://www.npmjs.com/package/raspi-ver>`_ : returns the version and other info for your RPi
