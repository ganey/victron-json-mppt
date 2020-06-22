#!/usr/bin/python -u

__author__ = "Michael Gane"
__version__ = "1.5.8"
__maintainer__ = __author__
__email__ = "victron@ganey.co.uk"

import time  # Library to use delays
import os  # Library to detect import libraries
import sys  # system command library
import urllib
import json

# importing dbus complements
sys.path.insert(1, os.path.join(os.path.dirname(__file__), './ext/velib_python'))

# default start values
values = {
    '/State': '2',  # fault
    '/Connected': 0,
    '/Pv/V': 0,
    '/Pv/I': 0,
    '/Dc/0/Voltage': 0,
    '/Dc/0/Current': 0,
    '/Yield/Power': 0,
    '/Yield/User': 0,
    '/Yield/System': 0,
}


def update_dbus(items):
    for key in items:
        print "Setting: ", key, items[key]
        os.system('dbus --system com.victronenergy.solarcharger.epever_ttyUSB1 ' + key + ' SetValue %' + str(items[key]))


def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    for key, value in x.items():
        if key in x and key in y:
            z[key] = y[key]
    return z


while 1:

    print "Reading from remote:"
    # set the remote address of json file here:
    url = "http://192.168.1.100/solar.json"

    try:
        response = urllib.urlopen(url)
        data = json.loads(response.read())

        if data:
            print "Got data: " % data
            time.sleep(1)
            update_dbus(merge_two_dicts(values, data))
        else:
            print "Failed, using defaults: " % values
            update_dbus(values)
            time.sleep(2)
    except:

        print "Failed to process data from remote"
        update_dbus(values)
        time.sleep(2)
