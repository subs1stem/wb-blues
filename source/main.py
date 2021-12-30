import time

import bluetooth

from mqtt_publisher import *

publish_meta(MODULE_NAME, '')

for address in DEVICES:
    name = '{name} - {mac}'.format(name=DEVICES[address],
                                   mac=address)
    publish_control(data=0,
                    name=name,
                    data_type='alarm',
                    units='',
                    error='')

while True:
    nearby_devices = bluetooth.discover_devices(duration=BT_SCAN_DURATION)
    #  print(nearby_devices)
    for mac in DEVICES:
        name = '{name} - {mac}'.format(name=DEVICES[mac],
                                       mac=mac)
        if mac in nearby_devices:
            publish_control(data=1,
                            name=name,
                            data_type='alarm',
                            units='',
                            error='')
        else:
            publish_control(data=0,
                            name=name,
                            data_type='alarm',
                            units='',
                            error='')
    time.sleep(0.1)
