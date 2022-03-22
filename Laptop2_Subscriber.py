'''
A MQTT subscriber to run on Laptop #2 that subscribes to topics and continously listens to incoming messages.
It will write to a log file whenever a message is received, as well as keep track of when LED1 is turned on/off. 
'''

import paho.mqtt.client as mqtt
from datetime import datetime
import logging

logging.basicConfig(filename="Laptop2.log", format='%(asctime)s %(message)s', filemode='w') 
logger=logging.getLogger() 
logger.setLevel(logging.INFO)

topic = ["lightSensor", "threshold", "LightStatus", "Status/RaspberryPiA", "Status/RaspberryPiC"]

def on_connect(client, userdata, flags, rc):
    print("Result from connect: {}".format(mqtt.connack_string(rc)))
    if(rc == mqtt.CONNACK_ACCEPTED):
        print("Subscribing to topics " + topic[0] + ", " + topic[1] + ", " + topic[2] + ", " + topic[3] + ", " + topic[4])
        client.subscribe(topic[0])
        client.subscribe(topic[1])
        client.subscribe(topic[2])
        client.subscribe(topic[3])
        client.subscribe(topic[4])

def on_message(client, userdata, message):
    print("Received message: Topic: {}. Payload: {} ".format(message.topic,str(message.payload.decode("utf-8"))) + " Time: " + str(datetime.now()) )
    logger.info("Received message: Topic: {}. Payload: {} ".format(message.topic,str(message.payload.decode("utf-8"))) + " Time: " + str(datetime.now()) )
    if(message.topic == "LightStatus" and str(message.payload.decode("utf-8")) == "TurnOn"):
       print("LED1 ON: " + " Time: " + str(datetime.now()))
       logger.info("LED1 ON: " + " Time: " + str(datetime.now()))
    elif(message.topic == "LightStatus" and str(message.payload.decode("utf-8")) == "TurnOff"):
       print("LED1 OFF: " + " Time: " + str(datetime.now()))
       logger.info("LED1 OFF: " + " Time: " + str(datetime.now()))

mqttBroker ="192.168.1.9"
listenerPort = 1883

client = mqtt.Client("laptop2")
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqttBroker,listenerPort)
client.loop_forever()