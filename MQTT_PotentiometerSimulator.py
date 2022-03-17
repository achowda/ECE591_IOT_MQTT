'''
Simulation of Potentiometer values obtained from a potentiometer connected to Raspberry Pi. The Potentiometer readingss will be published under the topic "THRESHOLD"
'''

import paho.mqtt.client as mqtt
import time
from random import randrange,uniform

POTENTIOMETER_THRESHOLD = 0.9

#Broker Config
mqttBroker = "192.168.1.19"
listernerPort = 1883
qosValue = 2
retainFlag = True
topicName = "RaspberrypiA/Threshold"

#Simulate LDR Values
def getPotentiometerReading():
    randNum = uniform(0.0,1.0);
    return randNum

def on_connect(client,userdata,flags,rc):
    print("Result from connect: {}".format(mqtt.connack_string(rc)))
    if(rc != mqtt.CONNACK_ACCEPTED):
        raise IOError("Couldn't establish a connection with MQTT Broker");
    else:
        client.publish(topicName,payload="Online", qos=1, retain=True)

client = mqtt.Client("POT_Reader");
client.loop_start()
#client.username_pw_set(username="anand",password="mqtt");
client.will_set(topicName,payload="Offline", qos=1, retain=True)
client.connect(mqttBroker,listernerPort);


try:
    while True:
        potReading = getPotentiometerReading();
        if(potReading  >  POTENTIOMETER_THRESHOLD): 
            client.publish(topic=topicName,payload=potReading,qos=qosValue,retain=retainFlag)
            print("Just published " + str(potReading) + " to topic " + topicName)
        time.sleep(0.1)


except KeyboardInterrupt:
    #client.publish(topicName,payload="Offline", qos=1, retain=True)
    client.disconnect()
    client.loop_stop()
    print("Potentiometer disconnected");



