#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Petri Salminen'
SITENAME = "Petri's Corner"
SITETITLE = 'Petri Salminen'
SITESUBTITLE = 'Open Sourcerer, Data Wizard'
SITEDESCRIPTION = "Petri's thoughts about life and tech"

SITEURL = 'http://localhost:8000'
SITELOGO = SITEURL + '/images/petri_square-140w.webp'
FAVICON = SITEURL + '/images/favicon.ico'

PATH = 'content'

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2020
COPYRIGHT_NAME = "Petri Salminen"
GITHUB_CORNER_URL = "https://github.com/elguitar/salminen.dev"

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
          ('twitter', 'https://twitter.com/PetriSalminen1'),
         )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Allow overriding of Theme templates
THEME_TEMPLATES_OVERRIDES = ['custom_templates']

STATIC_PATHS = ['css', 'images', 'static']

EXTRA_PATH_METADATA = {
    'css/custom.css': {'path':'css/custom.css'},
}

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["slide_reader"]
CUSTOM_CSS = 'css/custom.css'

DISABLE_URL_HASH=True

USE_GOOGLE_FONTS=False
THEME='Flex'

# For the CV

EDUCATION = [{
        'title':'Master of Science (Tech)',
        'time':'2020',
        'organization':'Tampere University',
        'description':'Master\'s Thesis: Towards Smart Building - Utilizing sensor data and building information model in a multi-purpose environment<br>1st Major: Information management and systems<br>2nd Major: Information analytics',
    },
    {
        'title':'Bachelor of Science (Tech)',
        'time':'2018',
        'organization':'Tampere University of Technology',
        'description':'Bachelor\'s Thesis: Data Analytics in Accordance with the European Union\'s General Data Protection Regulation<br>Major: Information and Knowledge Management<br>Minor: Software systems',
    },
    {
        'title':'Secondary School Graduate',
        'time':'2012',
        'organization':'Parolan Lukio',
        'description':'',
    },
]

WORK = [
    {
        'title': 'Software Development Lead',
        'time':'2020 -',
        'organization':'Seravo Oy',
        'description':'Designing software, strategic planning, team leading. Also, the same stuff as Network Service Specialist (see below).'
    },
    {
        'title':'Course Assistant, Master\'s Thesis Worker',
        'time':'2019 - 2020',
        'organization':'Tampere University',
        'description':'Working as a course assistant on courses: Basics for Business Data Analytics and Ohjelmallinen sisällönhallinta (Programmatic Content Management).'
    },
    {
        'title':'Network Service Specialist',
        'time':'2017 - 2020',
        'organization':'Seravo Oy',
        'description':'Developing internal tools, solving customers\' technical problems, customer service, data analytics, cheering people up.'
    },
    {
        'title':'Conscientious Man',
        'time':'2018',
        'organization':'The Summer University of Tampere',
        'description':'Working as a course assistant and assisting staff with IT problems.'
    },
]

IT_SKILLS = [{
        'title':'Python',
        'stars':5,
        'description':'Python is my go-to language after Finnish and English. I am familiar with the following libraries: numpy, scipy, pandas, scikit-learn, keras, matplotlib, reguests, beautifulsoup3, django and flask among others. I have used Python on courses, in my job and with my hobby projects.'
    },
    {
        'title':'R',
        'stars':4,
        'description':'I started using R on a class of statistics. Lately, I have been learning tidyverse (especially dplyer and ggplot2). I also have writed some of my hobby data science documents in Rmarkdown.'
    },
    {
        'title':'Ruby',
        'stars':4,
        'description':'Ruby is my main language at my current job at Seravo. I know the basics of the language and have a love-hate relationship with it.'
    },

    {
        'title':'C++',
        'stars':3,
        'description':'I have used C++ mostly on university courses. For example, Data Structures and Algorithms -course was done using C++, which was very fun!'
    },
    {
        'title':'Matlab',
        'stars':3,
        'description':'I have used Matlab on several mathematics, signal processing and machine learning courses.'
    },
    {
        'title':'Haskell',
        'stars':3,
        'description':'I have tried to learn Haskell on my free time just because it’s hard. Lately, I attended a course of Functional Programming, which involved programming with Haskell. I think that Haskell is fun and challenging.'
    },
    {
        'title':'PHP',
        'stars':3,
        'description':'Since I am working in a company, which hosts WordPress servers, I obviously know PHP. It is not my favourite nor my strength, but I know how to write simple programs and modify existing code.'
    },
    {
        'title':'SQL',
        'stars':3,
        'description':'I know the basic syntax of SQL. I have used SQL on courses and in my job.'
    },
    {
        'title':'HTML, CSS, JS',
        'stars':3,
        'description':'These are not particularly my expertise, but I think that every programmer should no some HTML, CSS and Javascript. I confont problems with these in my job, since I occasionally solve problems with websites.'
    },
    {
        'title':'React',
        'stars':3,
        'description':'I can get my way around React and honestly I like React. Currently trying to understand Redux and Thunk.'
    },
    {
        'title':'Vue.js',
        'stars':2,
        'description':'I managed to do one hobby project with Vue.js. It seems quite simple, but I now that there is more to that iceberg.'
    },

    {
        'title':'Git',
        'stars':5,
        'description':'I am quite a git fanatic. I have used git on courses, in my job and with my hobby projects. I am familiar with different version control workflows. I also know how to work with branches, rebases and merges and I do not panic if something goes wrong.'
    },
    {
        'title':'Linux',
        'stars':5,
        'description':'I have used mainly Linux on my laptops since 2009. I know how to work on Ubuntu, Debian, Fedora and CentOS (RedHat) -based systems. In my current job at Seravo, I have participated in administrating clusters of Linux servers.'
    },
]
