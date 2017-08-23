SHELL=/bin/bash
PY?=python2
PELICAN?=pelican
PELICANOPTS= -D

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
# OUTPUTDIR=/Users/kevin/github/walchko.github.io
OUTPUTDIR=$(BASEDIR)/www
CONFFILE=$(BASEDIR)/pelicanconf.py

GITHUB_PAGES_BRANCH=master

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make clean                          remove the generated files         '
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ -d $(OUTPUTDIR) ] && cd $(OUTPUTDIR); rm -fr *

.PHONY: html help clean
