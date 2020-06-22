#!/usr/bin/python

from pymodbus.exceptions import ModbusIOException

__author__ = "Michael Gane"
__version__ = "1.5.8"
__maintainer__ = __author__
__email__ = "victron@ganey.co.uk"

import time  # Library to use delays
from argparse import ArgumentParser
import os  # Library to detect import libraries
import sys  # system command library
from dbus.mainloop.glib import DBusGMainLoop

# importing dbus complements
sys.path.insert(1, os.path.join(os.path.dirname(__file__), './ext/velib_python'))
from vedbus import VeDbusService  # VeDbusItemImportObject paths that are mandatory for services representing products

import gobject
from gobject import idle_add

DBusGMainLoop(set_as_default=True)
dbusservice = VeDbusService('com.victronenergy.solarcharger.epever_ttyUSB1')
#
# mainloop = gobject.MainLoop()
# mainloop.run()

try:
    print "trying something"
    dbusservice.add_path('/Management/ProcessName', __file__)
    dbusservice.add_path('/Management/ProcessVersion',
                         'Version {} running on Python {}'.format(1, sys.version))
    dbusservice.add_path('/Management/Connection', 'ModBus RTU')

    # Create the mandatory objects
    dbusservice.add_path('/DeviceInstance', 291)
    dbusservice.add_path('/ProductId', 0)
    dbusservice.add_path('/ProductName', 'JSON MPPT')
    dbusservice.add_path('/FirmwareVersion', 1)
    dbusservice.add_path('/HardwareVersion', 1)
    dbusservice.add_path('/Connected', 1)
    dbusservice.add_path('/Serial', '01234abcde')

except:
    print "Json mppt has been created before"

try:
    dbusservice.add_path('/State', 0, writeable=True)
    dbusservice.add_path('/Pv/V', 0, writeable=True)
    dbusservice.add_path('/Pv/I', 0, writeable=True)
    dbusservice.add_path('/Dc/0/Voltage', 0, writeable=True)
    dbusservice.add_path('/Dc/0/Current', 0, writeable=True)
    # dbusservice.add_path('/DC/0/Power', 0, writeable=True)
    dbusservice.add_path('/Load/State', 0, writeable=True)
    dbusservice.add_path('/Load/I', 0, writeable=True)
    dbusservice.add_path('/ErrorCode', 0, writeable=True)
    dbusservice.add_path('/Yield/Power', 0, writeable=True)  # Actual input power (Watts)
    dbusservice.add_path('/Yield/User', 0, writeable=True)  # Total kWh produced (user resettable)
    dbusservice.add_path('/Yield/System', 0, writeable=True)  # Total kWh produced (not resettable)
    dbusservice.add_path('/Mode', 0, writeable=True)
    dbusservice.add_path('/MppOperationMode', 0, writeable=True)
except:
    print "Json mppt values created before"


print "Starting main loop..."
mainloop = gobject.MainLoop()
mainloop.run()

exit(0)
