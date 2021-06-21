# victron-json-mppt
Python DBUS json mppt solar charger scripts for VenusOS.

### Tested on RPi 3 CCGX


Publishes an MPPT solarcharger on the DBUS based on the dbus definitions here: https://github.com/victronenergy/venus/wiki/dbus#solar-chargers

Both scripts run on startup on the CCGX https://www.victronenergy.com/live/ccgx:root_access#hooks_to_install_run_own_code_at_boot.

example rc.local:
```su root -c "screen -dm -S epever-dbus ~/dbus-service.py"```


## Why?
I have an Epever Tracer MPPT which I needed to integrate with my victron multiplus & CCGX. I didnt want to spend lots of money on a new mppt when my current one works fine (it just doesn't communicate with the victron software)

Initially I tried getting the Tracer MPPT readings directly on the CCGX but turns out modbus would crash a lot and the Epever MPPT wasn't happy with the high rate of readings required to run the service well on DBUS.

## Known issues:
This script 100% relies on keeping the remote json file up to date. I run a separate script every 60 seconds to grab the required modbus values from my Tracer MPPT and publish them to a json file. On smaller arrays, solar isn't likely to fluctuate massively within 60 seconds so an average is fine. This process is stable and that's what counts.

## Special thanks:
I started with this script as a base for how to get it working with CCGX: https://github.com/CarlosBornay/venus-bornaywind
