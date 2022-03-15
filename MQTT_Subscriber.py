'''
A simply MQTT subscriber that subscribes to topic "TEMPERATURE" and continously listens to incoming messages.
'''

import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Result from connect: {}".format(mqtt.connack_string(rc)))
    if(rc == mqtt.CONNACK_ACCEPTED):
        print("Subscribing to topics LIGHTSENSOR and THRESHOLD")
        client.subscribe("LIGHTSENSOR")
        client.subscribe("THRESHOLD")

def on_message(client, userdata, message):
    print("Received message: Topic: {}. Payload: {} ".format(message.topic,str(message.payload.decode("utf-8"))))


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed with QOS = "+str(granted_qos))


mqttBroker ="192.168.1.19"
listenerPort = 1883

client = mqtt.Client("Raspberry Pi A")
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect(mqttBroker,listenerPort)
#client.subscribe("LIGHTSENSOR")
#client.subscribe("THRESHOLD")
client.loop_forever()


