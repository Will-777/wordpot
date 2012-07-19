#/usr/bin/env python

try:
    from flask import Flask
except ImportError:
    print "\n[X] Please install Flask:"
    print "   $ pip install flask\n"
    exit()

from werkzeug.routing import BaseConverter
from wordpot.plugins_manager import PluginsManager

# ---------------
# Regex Converter
# ---------------

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]

# ------------
# Building app
# ------------

app = Flask('wordpot')
app.url_map.converters['regex'] = RegexConverter

# ----------------------------
# Building the plugins manager
# ----------------------------

pm = PluginsManager()
pm.load()

import wordpot.views
