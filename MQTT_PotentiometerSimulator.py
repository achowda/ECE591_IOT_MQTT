'''
Simulation of Potentiometer values obtained from a potentiometer connected to Raspberry Pi. The Potentiometer readingss will be published under the topic "RaspberrypiA/Threshold" and connection status under the topic "Status/RaspberrypiA/Threshold"
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
topicStatus = "Status/RaspberrypiA/Threshold"

#Simulate LDR Values
def getPotentiometerReading():
    randNum = uniform(0.0,1.0);
    return randNum

def on_connect(client,userdata,flags,rc):
    print("Result from connect: {}".format(mqtt.connack_string(rc)))
    if(rc != mqtt.CONNACK_ACCEPTED):
        raise IOError("Couldn't establish a connection with MQTT Broker");

client = mqtt.Client("POT_Reader");
client.on_connect = on_connect
client.will_set(topicStatus,payload="Disconnected", qos=qosValue, retain=True)
client.connect(mqttBroker,listernerPort)
time.sleep(0.1)
client.loop_start()
msgInfo = client.publish(topicStatus,payload="Online", qos=qosValue, retain=False)
print("Just published payload = Online to topic " + topicStatus)

try:
    while True:
        potReading = getPotentiometerReading();
        if(potReading  >  POTENTIOMETER_THRESHOLD): 
            msgInfo = client.publish(topic=topicName,payload=potReading,qos=qosValue,retain=retainFlag)
            msgInfo.wait_for_publish()
            print("Just published " + str(potReading) + " to topic " + topicName)
        time.sleep(0.1)


except KeyboardInterrupt:
    time.sleep(0.3)
    client.disconnect()
    client.loop_stop()
    print("Potentiometer disconnected");

