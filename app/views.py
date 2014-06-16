__author__ = 'buddha'
from . import app
import models
from BeautifulSoup import BeautifulStoneSoup
from pprint import pprint
# import simplejson
import urllib, urllib2
from flask import render_template, flash, redirect, url_for


class TMError(Exception):
    pass

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/busroutes')
def busroutes(carrier=40, debug=1, format='json', **kwargs):

    TM_BASE = 'http://developer.metro.net/tm/routes.php'
    APIKEY = 'euVh%2A%26Kz.%3FrA.fQ%3A%7ER%23O'
    kwargs.update({
    'apikey': 	APIKEY,
    'carrier': 	carrier,
    'format': 	format
    })

    url = TM_BASE + '?' + urllib.urlencode(kwargs)

    if debug: print url
    if (format=='json'):
#        result = simplejson.load(urllib.urlopen(url))
        result = urllib.urlopen(url)
        if 'Error' in result:
            # An error occurred; raise an exception
            raise TMError, result['Error']
#       return result['routes']['item']
        return urllib.urlopen(url)
    else:
        xml = urllib2.urlopen(url)
        soup = BeautifulStoneSoup(xml)
        return soup.prettify()

    return url;

