# CAR
Call A Robot using LilyGo SIM7000G Module ESP32 Development board with integrated 4G/GPS and BT/WIFI modules
 - [SIM7000G Manuals](https://simcom.ee/documents/?dir=SIM7000x)

**CURRENTLY testing board and getting used to different Micropythons**

## Install
 - First flash the device as with the [ESP32-MicroPython](https://github.com/18684092/ESP32-MicroPython) although you need to flash [MicroPython_LoBo](https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/firmwares) as this version has specific built in modules such as GSM.
 - Examples to test GPS and GSM of the [LilyGo-SIM7000G](https://github.com/Xinyuan-LilyGO/LilyGO-T-SIM7000G/tree/master/examples/MicroPython_LoBo) can be tried although without a SIM card and APN you will receive `Status: (98, 'Not started')` error and the modem will not respond
 - If you get a `E (1051) MicroPython: Error while opening MicroPython NVS name space` error then you probably did not erase the firmware.
 - If you get a `W (2128) phy_init: failed to load RF calibration data (0x1102), falling back to full calibration` error this is likely to be related to a power supply issue. Use a better cable or do not go through a USB hub. Unplug ESP32 card and try again

## LoBo MicroPython
- [LoBo](https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo) is not maintained any more (since 2018) and ideally standard MicroPython should be used, however specific boards have specific needs and the LilyGo SIM7000G with ESP32 requires GSM module which isnt present within standard MicroPython. 

## Threads
- [LoBo Threads](https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/thread) are slightly different from standard Micro Python threads so many examples will fail. LoBo requires a thread name as first parameter.

## Bluetooth
- LoBo Micropython doesn't have Bluetooth within the network module

## WiFi
- [WiFi.py](https://github.com/18684092/CAR/blob/main/modules/WiFi.py) sets up WiFi successfully. WiFi on standard MicroPython and LoBo is the same. 

## GSM / GPS LilyGo SIM7000G
- Stanard MicroPython doesn't have a GSM module
- LoBo MicroPython does [GSM Module](https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/gsm)
- [AT Commands Manual](https://simcom.ee/documents/SIM7000x/SIM7000%20Series_AT%20Command%20Manual_V1.04.pdf)

## MQTT
- LoBo MicroPython fails to import `micropython-umqtt.simple` and `micropython-umqtt.robust` via `upip.install('micropython-umqtt.robust2')` therefore use:
Git repo [simple2](https://github.com/fizista/micropython-umqtt.simple2) and
[robust2](https://github.com/fizista/micropython-umqtt.robust2)
- [MQTT Manual](https://simcom.ee/documents/SIM7000x/SIM7000%20Series_MQTT_Application%20Note_V1.00.pdf)

## Network Utils
- [uping](https://gist.github.com/shawwwn/91cc8979e33e82af6d99ec34c38195fb) is a handy tool
- [Ping within SIM7000G Manual](https://simcom.ee/documents/SIM7000x/SIM7000%20Series_PING_Application%20Note_V1.00.pdf)

## Battery
- ESP32 Pin 35 (vbat) is connected to ADC but can't be read when powered from USB (it reads 142). On full attenuation should read 4095 - which will be half the battery voltage since vbat is divided by 2 resistors. Obviously you need to find the min and max allowed levels and plot the battery decay to get some idea of power drain. A [guide](https://randomnerdtutorials.com/esp32-esp8266-analog-readings-micropython/) explains.
```
from machine import Pin, ADC

battery = ADC(35)
battery.atten(ADC.ATTN_11DB)

def getBattery():
    #Full range: 0-3.3v
    return battery.read()
```
- SIM7000G has a battery pin (VBAT) and it can be read via an AT command

`gsm.atcmd('AT+CBC', printable=True)`

## Real Time Clock
- module DateTime.py sets the RTC on boot via modified code from [Loboris forum](https://loboris.eu/forum/showthread.php?tid=12)
- [NTP for SIM7000G](https://simcom.ee/documents/SIM7000x/SIM7000%20Series_NTP_Application%20Note_V1.00.pdf)

## TCP/IP
- [AT Commands for TCP/IP SIM7000G](https://simcom.ee/documents/SIM7000x/SIM7000%20Series_TCPIP_Application%20Note_V1.01.pdf)
 
## SIM7000G UART
- [UART Manual](https://simcom.ee/documents/SIM7000x/SIM7000%20Series%20UART%20Application%20Note_V1.00.pdf)