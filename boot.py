import network
import urequests 
import time
from modules.uping import ping
from modules.WiFi import connect, SSID
from modules.Battery import getBattery

 
print("Connecting to WiFi (" + SSID + ")")
connect()
print("Pinging Google")
ping("www.google.com")

print("Battery:", getBattery())
print("boot.py ends")
