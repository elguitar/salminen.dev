#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://salminen.dev'
SITELOGO = SITEURL + '/images/petri_square.webp'
FAVICON = SITEURL + '/images/favicon.ico'

RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
GOOGLE_ADSENSE = {
    'ca_id': 'ca-pub-7863135966387398',
    'page_level_ads': False,
    'ads': {},
    #    'aside': '8752710348',
    #    'main_menu': '',
    #    'index_top': '',
    #    'index_bottom': '1124188687',
    #    'article_top': '',
    #    'article_bottom': '4843941849',
    #}
}
