#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Petri Salminen'
SITENAME = "Petri's Corner"
SITETITLE = 'Petri Salminen'
SITESUBTITLE = 'Open Sourcerer, Data Wizard'
SITEDESCRIPTION = "Petri's thoughts about life and tech"

SITEURL = 'http://localhost:8000'
SITELOGO = SITEURL + '/images/petri_square.jpg'
FAVICON = SITEURL + '/images/favicon.ico'

PATH = 'content'

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2019
TIMEZONE = 'Europe/Helsinki'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('About', SITEURL + 'about'),
#         ('Contact', SITEURL + 'contact'))

# Social widget
SOCIAL = (
          ('facebook', 'https://fb.com/elguitarpete'),
          ('github', 'https://github.com/elguitar'),
          ('linkedin','https://www.linkedin.com/in/petri-salminen/'),
         )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True 
THEME='Flex'
