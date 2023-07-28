#!/usr/bin/python -u

__author__ = "Michael Gane"
__version__ = "1.5.8"
__maintainer__ = __author__
__email__ = "victron@ganey.co.uk"

import time  # Library to use delays
import os  # Library to detect import libraries
import sys  # system command library
import urllib.request as ur
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
    '/Yield/User': 129,
    '/Yield/System': 129,
}


def update_dbus(items):
    for key in items:
        print ("Setting: ", key, items[key])
        os.system('dbus --system com.victronenergy.solarcharger.epever_ttyUSB3 ' + key + ' SetValue %' + str(items[key]))


def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    for key, value in x.items():
        print("key is: ", key + "Value is : ", value)
        if key in x and key in y:
            z[key] = y[key]
    return z


while 1:
    #print(sys.version)

    # set the remote address of json file here:
    url = "http://raspberrypi.local/solar.json"
    print ("Reading from remote :", url)

    #import urllib.request as ur
    #s = ur.urlopen("http://www.google.com")
    #sl = s.read()
    #print(sl)

    try:
        response = ur.urlopen(url)
        print("response is : ", response)
        data = json.loads(response.read())
        print("json data is : ", data)

        if data:
            print ("Got data: " % data)
            time.sleep(1)
            update_dbus(merge_two_dicts(values, data))
        else:
            print ("Failed, using defaults: " % values)
            update_dbus(values)
            time.sleep(2)
    except Exception as error:
    # handle the exception
        print("An exception occurred:", error) # An exception occurred: division by zero
        update_dbus(values)
        time.sleep(2)
