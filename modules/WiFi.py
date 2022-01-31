import network
import urequests 
import time
import binascii

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
    line = binascii.hexlify(wlan.config('mac')).decode('utf-8')

    # Get MAC
    l = [line[i:i+2] for i in range(0, len(line), 2)]
    
    # Convert into 6 hex digits
    mac=""
    for i,value in enumerate(l):
        mac += value
        if i+1 < len(l):
            mac +=":"

    print('Device MAC:', mac)  

    
def testConnectivity():
    r = urequests.get(url=TEST_SITE)
    print(r.json()['id'])

