'''
A simply MQTT subscriber that subscribes to topic "TEMPERATURE" and continously listens to incoming messages.
'''

import paho.mqtt.client as mqtt
import time

topic1 = "RaspberrypiA/LightSensor"
topic1Status = "Status/RaspberrypiA/LightSensor"
topic2 = "RaspberrypiA/Threshold"
topic2Status = "Status/RaspberrypiA/Threshold"

def on_connect(client, userdata, flags, rc):
    print("Result from connect: {}".format(mqtt.connack_string(rc)))
    if(rc == mqtt.CONNACK_ACCEPTED):
        print("Subscribing to topics " + topic1 + " and " + topic1Status + " and " + topic2 + " and " + topic2Status)
        client.subscribe(topic1)
        client.subscribe(topic1Status)
        client.subscribe(topic2)
        client.subscribe(topic2Status)

def on_message(client, userdata, message):
    print("Received message: Topic: {}. Payload: {} ".format(message.topic,str(message.payload.decode("utf-8"))))


mqttBroker ="192.168.1.19"
listenerPort = 1883

client = mqtt.Client("Raspberry Pi A")
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqttBroker,listenerPort)
client.loop_forever()


