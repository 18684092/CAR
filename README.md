# CAR
Call A Robot using TTGO T-SIM7000G Module ESP32 Development board with integrated 4G/GPS and BT/WIFI modules

## Install
 - First flash the device as with the [ESP32-MicroPython](https://github.com/18684092/ESP32-MicroPython) although you need to flash [MicroPython_LoBo](https://github.com/loboris/MicroPython_ESP32_psRAM_LoBo/wiki/firmwares) as this version has specific built in modules such as GSM.
 - Examples to test GPS and GSM of the [LilyGo-SIM7000G](https://github.com/Xinyuan-LilyGO/LilyGO-T-SIM7000G/tree/master/examples/MicroPython_LoBo) can be tried although without a SIM card and APN you will receive `Status: (98, 'Not started')` error and the modem will not respond
 - If you get a `E (1051) MicroPython: Error while opening MicroPython NVS name space` error then you probably did not erase the firmware.
 - If you get a `W (2128) phy_init: failed to load RF calibration data (0x1102), falling back to full calibration` error this is likely to be related to a power supply issue. Use a better cable or do not go through a USB hib. Unplug ESP32 card and try again



 
 