import network
import urequests 
import time

SSID = 'ASK4 Wireless'
PASS = ''
TEST_SITE = 'https://jsonplaceholder.typicode.com/todos/1' 

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(SSID, PASS)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())   


def testConnectivity():
    r = urequests.get(url=TEST_SITE)
    print(r.json()['id'])

