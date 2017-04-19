![](pics/ship.jpg)

# Github Pages

[![Build Status](https://travis-ci.org/walchko/walchko.github.io.svg?branch=master)](https://travis-ci.org/walchko/walchko.github.io)

This is how I used Pelican to create a static website to host a personal page
on Github.

## Pelican

A quick overview of the [instructions](http://docs.getpelican.com/) or
[instructions](http://pelican.readthedocs.io/en/stable/) are:

	pip install typogrify
	pip install Markdown
	pip install pelican
	mkdir project
	cd project
	pelican-quickstart

## Plugins

The plugins are a submodule of my git repo:

    git submodule add https://github.com/getpelican/pelican-plugins

## Workflow

1. Edit rst files
2. To preview everything before pushing do: `make html`
3. Then look in `www`
4. If everything is fine, then push to github and travis-ci will automagically
build/publish the website
