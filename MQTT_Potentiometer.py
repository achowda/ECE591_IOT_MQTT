'''
Simulation of Potentiometer values obtained from a potentiometer connected to Raspberry Pi. The Potentiometer readingss will be published under the topic "RaspberrypiA/Threshold" and connection status under the topic "Status/RaspberrypiA/Threshold"
'''

import paho.mqtt.client as mqtt
import time
from random import randrange,uniform
from MCP3008 import MCP3008

POTENTIOMETER_THRESHOLD = 0.4

#Broker Config
mqttBroker = "192.168.1.19"
listernerPort = 1883
qosValue = 2
retainFlag = True
topicName = "RaspberrypiA/Threshold"
topicStatus = "Status/RaspberrypiA/Threshold"
adc = MCP3008()

#Simulate LDR Values
def getPotentiometerReading():
    value = (adc.read(channel=0) / 1023.0)
    print("Potentiometer reading = " + str(value))
    return value

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
        time.sleep(1.0)


except KeyboardInterrupt:
    time.sleep(0.3)
    client.disconnect()
    client.loop_stop()
    print("Potentiometer disconnected");

