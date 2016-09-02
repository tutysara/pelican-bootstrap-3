
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'tutysara'
SITENAME = u"tutysara's space"
#SITEURL = 'http://localhost:8080'
SITEURL = 'http://www.tutysara.net'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

TIMEZONE = 'Asia/Calcutta'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.rss.xml'
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('@tutysara', 'http://twitter.com/tutysara', 'icon-twitter'),
          ('github', 'http://github.com/tutysara', 'icon-github'),
          ('+tutysara', 'https://plus.google.com/113376160578552687607/posts', 'icon-google-plus'),)

SOCIAL_OLD = (('twitter', 'http://twitter.com/tutysara'),
          ('github', 'http://github.com/tutysara'),
          ('google-plus', 'https://plus.google.com/113376160578552687607/posts'),)

DEFAULT_PAGINATION = 3

# boot strap theme specific
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 10

DISPLAY_CATEGORIES_ON_MENU = False

MARKUP = ('markdown', 'md' , 'htm', 'html',)
DEFAULT_CATEGORY = ('Articles')

# my customizations
COPY_RIGHT_STRING = "Copyright 2013, tutysara  <a href='http://blog.getpelican.com/'>Powered by Pelican</a> and <a href='https://github.com/tutysara/pelican-bootstrap3-tutysara'>modified Bootstrap 3 theme</a>"
# discus site name
DISQUS_SITENAME = 'tutysarablog'
# google analytics
GOOGLE_ANALYTICS = 'UA-34510369-1'

# Filename Metadata: YYYY-MM-DD-the-rest-before-the-dot-is-the-slug.md, for example
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PAGE_URL ='pages/{slug}/index.html'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# Copy some files over...
FILES_TO_COPY = (("extras/favicon.ico", "favicon.ico"),
                 ("extras/CNAME", "CNAME"),)
# Theme support
THEME = "/Users/tutysara/src/myprojects/pelican-bootstrap3-tutysara"

ADDTHIS_PROFILE = "ra-52530224602b734f"

BOOTSTRAP_THEME = "journal"
USE_OPEN_GRAPH= False
