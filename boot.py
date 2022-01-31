import network
import urequests 
import time
from modules.uping import ping
from modules.WiFi import connect, SSID


 
print("Connecting to WiFi (" + SSID + ")")
connect()
print("Pinging Google")
ping("www.google.com")
print("boot.py ends")
