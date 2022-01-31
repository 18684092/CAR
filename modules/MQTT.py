
import network
import utime

def conncb(task):
    print("[{}] Connected".format(task))

def disconncb(task):
    print("[{}] Disconnected".format(task))

def subscb(task):
    print("[{}] Subscribed".format(task))

def pubcb(pub):
    print("[{}] Published: {}".format(pub[0], pub[1]))

def datacb2(msg):
    print("[{}] Data arrived from topic: {}, Message:\n".format(msg[0], msg[1]), msg[2])

def mqtt_t():

    #mqtt = network.mqtt("1", "mqtt://test.mosquitto.org:1883", user="", password="", cleansession=True, connected_cb=conncb, 
        #disconnected_cb=disconncb, subscribed_cb=subscb, published_cb=pubcb, data_cb=datacb2)
    # # secure connection requires more memory and may not work
    # # mqtts = network.mqtt("eclipse", "mqtts//iot.eclipse.org", cleansession=True, connected_cb=conncb, disconnected_cb=disconncb, subscribed_cb=subscb, published_cb=pubcb, data_cb=datacb)
    # mqtt = network.mqtt("eclipse", "ws://iot.eclipse.org:80/ws", cleansession=True, data_cb=datacb)

    # mqtt.start()

    # #mqtt.config(lwt_topic='status', lwt_msg='Disconected')




    # # Wait until status is: (1, 'Connected')
    # mqtt.subscribe('test')
    # mqtt.publish('test', 'Hi from Micropython')
    # mqtt.stop()

    thing = network.mqtt("1", "test.mosquitto.org:1883", user="", password="", cleansession=True, data_cb=datacb2)

    thingspeakChannelId = "1"                           # enter Thingspeak Channel ID
    thingspeakChannelWriteApiKey = "1"   # EDIT - enter Thingspeak Write API Key
    thingspeakFieldNo = 1
    thingSpeakChanelFormat = "json"

    pubchan = "sensors/{:s}/temp/{:s}".format(thingspeakChannelId, thingspeakChannelWriteApiKey)

    subchan = "sensors/{:s}/temp{:s}".format(thingspeakChannelId, thingspeakChannelWriteApiKey)


    thing.start()
    tmo = 0
    while thing.status()[0] != 2:
        utime.sleep_ms(1000)
        tmo += 1
        if tmo > 80:
            print("Not connected")
            break

    # subscribe to channel
    thing.subscribe(subchan)



    # publish to channel
    # Payload can include any of those fields separated b< ';':
    # "field1=value;field2=value;...;field8=value;latitude=value;longitude=value;elevation=value;status=value"
    thing.publish(pubchan, "1=0.2;1=On line")

