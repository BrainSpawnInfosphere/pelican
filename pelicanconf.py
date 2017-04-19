#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# coloring code snipets
# pygmentize -S monokai -f html -a .highlight > pygment.css
# pygmentize -f html -a .highligh > pygment.css

AUTHOR = u'walchko'
SITENAME = u'Planet Express'
SITESUBTITLE = "Our crew is replaceable. Your package isn't."
SITEURL = 'http://walchko.github.io/'

PATH = 'content'

# DELETE_OUTPUT_DIRECTORY = False don't use this, it wipes the .git directory
# OUTPUT_PATH = '/Users/kevin/google_drive/github/walchko.github.io/'

TIMEZONE = 'US/Mountain'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 1000

PLUGIN_PATHS = ['./pelican-plugins']

# PLUGINS = ["render_math", 'code_include', 'simple_footnotes', 'sitemap']
PLUGINS = ["render_math", 'code_include', 'sitemap']
# render_math - latex equations
# sitemap - for spiders, listed in robot.txt
# code_include - include code from other files
# simple_footnotes - may not use

MATH_JAX = {'align': 'left'}

USE_FOLDER_AS_CATEGORY = True

STATIC_PATHS = [
    'blog/engineering/pics',
    'blog/macOS/pics',
    'blog/raspbian/pics',
    'blog/robots/pics',
    'blog/cyber/pics',
    'blog/computers/pics',
    'blog/arch_linux/pics',
    'blog/programming/pics',
    'blog/repo/pics',
    'pages/pics',
    'pages/Publications',
    # 'images',
    'extra/robots.txt',
    'extra/favicon.ico'
]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

# used by sitemap plugin and robots.txt
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

GITHUB_ADDRESS = 'http://github.com/walchko'
SO_ADDRESS = 'http://stackoverflow.com/users/5374768/kevin'
SE_ADDRESS = 'http://raspberrypi.stackexchange.com/users/1677/kevin'

# number of words in a summary
SUMMARY_MAX_LENGTH = 100

DEFAULT_DATE_FORMAT = ('%a %d %B %Y')

THEME = './themes/kevin'

ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}"
TAG_SAVE_AS = "tag/{slug}/index.html"

MENUITEMS = (('About Me', 'about.html'), ('Colophon', 'colophon.html'), ('Topics', 'categories.html'), ('Blog', 'archives.html'))

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True