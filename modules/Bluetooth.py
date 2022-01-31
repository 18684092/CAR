# https://docs.pycom.io/firmwareapi/pycom/network/bluetooth/

from network import Bluetooth as bluetooth
import time

def demo():
    bt = bluetooth()
    bt.start_scan(-1)

    while True:
        adv = bt.get_adv()
        if adv and bt.resolve_adv_data(adv.data, bluetooth.ADV_NAME_CMPL) == 'Heart Rate':
            try:
                conn = bt.connect(adv.mac)
                services = conn.services()
                for service in services:
                    time.sleep(0.050)
                    if type(service.uuid()) == bytes:
                        print('Reading chars from service = {}'.format(service.uuid()))
                    else:
                        print('Reading chars from service = %x' % service.uuid())
                    chars = service.characteristics()
                    for char in chars:
                        if (char.properties() & bluetooth.PROP_READ):
                            print('char {} value = {}'.format(char.uuid(), char.read()))
                conn.disconnect()
                break
            except:
                print("Error while connecting or reading from the BLE device")
                break
        else:
            time.sleep(0.050)