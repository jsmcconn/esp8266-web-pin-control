# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import os, machine
#os.dupterm(None, 1) # disable REPL on UART(0)
import gc

# Added for network connect
def do_connect():
    import time
    import network
    network.hostname('rstmgr')
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    #time.sleep(1)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('ssid', 'key')
        while not wlan.isconnected():
            time.sleep(1)
    print('network config:', wlan.ifconfig())

do_connect()

# end added

import webrepl
webrepl.start()
gc.collect()
