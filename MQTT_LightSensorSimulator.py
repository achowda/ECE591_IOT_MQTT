'''
Simulation of light sensor values to be acquired from an LDR. The LDR values will be published under the topic "RaspberrypiA/LightSensor" and the status will be published under the topic "Status/RaspberrypiA/LightSensor"
'''

import paho.mqtt.client as mqtt
import time
from random import randrange,uniform

LIGHT_SENSOR_DELTA_THRESHOLD = 0.5

#Broker Config
mqttBroker = "192.168.1.19"
listernerPort = 1883
qosValue = 2
retainFlag = True
topicName = "RaspberrypiA/LightSensor"
topicStatus = "Status/RaspberrypiA/LightSensor"


#Simulate LDR Values
def getLdrReading():
    randNum = uniform(0.0,1.0);
    return randNum

def on_connect(client,userdata,flags,rc):
    print("Result from connect: {}".format(mqtt.connack_string(rc)))
    if(rc != mqtt.CONNACK_ACCEPTED):
        raise IOError("Couldn't establish a connection with MQTT Broker");

client = mqtt.Client("LDR_Reader");
client.on_connect = on_connect
client.will_set(topicStatus,payload="Disconnected", qos=qosValue, retain=True)
client.connect(mqttBroker,listernerPort)
time.sleep(0.1)
client.loop_start()
client.publish(topicStatus,payload="Online", qos=qosValue, retain=False)
print("Just published payload = Online to topic " + topicStatus)

ldrPrevReading = 0;

try:
    while True:
        ldrReading = getLdrReading();
        if(abs(abs(ldrReading) - abs(ldrPrevReading)) >  LIGHT_SENSOR_DELTA_THRESHOLD): 
            msgInfo = client.publish(topicName,ldrReading,qos=qosValue,retain=retainFlag)
            msgInfo.wait_for_publish()
            print("Just published " + str(ldrReading) + " to topic " + topicName)
        ldrPrevReading = ldrReading;
        time.sleep(0.1)


except KeyboardInterrupt:
    time.sleep(0.3)
    client.disconnect()
    client.loop_stop()
    print("Light Sensor disconnected");



