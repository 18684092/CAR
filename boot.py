import network
import urequests 
import time
import machine
from modules.uping import ping
from modules.WiFi import connect, SSID
from modules.Battery import getBattery
from modules.DateTime import settime, getDateTime

from machine import RTC
import utime

 
print("Connecting to WiFi (" + SSID + ")")
connect()
print("Pinging Google")
ping("www.google.com")

print("Battery:", getBattery())
print("Setting NTP time from uk.pool.ntp.org")
settime("uk.pool.ntp.org")
print(getDateTime())
print("boot.py ends")
