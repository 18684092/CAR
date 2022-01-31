from machine import RTC
import utime

rtc = RTC()
# https://loboris.eu/forum/showthread.php?tid=12
def settime(ntp_server):

    rtc.ntp_sync(server=ntp_server, tz="<03>3<02>,M10.3.0/0,M2.3.0/0")  # tz code from America_SaoPaulo that is at MicroPython_BUILD/components/micropython/docs/zones.csv file
    tmo = 100
    while not rtc.synced():
        utime.sleep_ms(100)
        tmo -= 1
        if tmo == 0:
            break
    #t = utime.strftime ('%c')

def getDateTime():
    return rtc.now() # get date and time