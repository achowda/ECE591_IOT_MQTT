'''
Simulation of light sensor values to be acquired from an LDR. The LDR values will be published under the topic "LIGHTSENSOR"
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


#Simulate LDR Values
def getLdrReading():
    randNum = uniform(0.0,1.0);
    return randNum

def on_connect(client,userdata,flags,rc):
    print("Result from connect: {}".format(mqtt.connack_string(rc)))
    if(rc != mqtt.CONNACK_ACCEPTED):
        raise IOError("Couldn't establish a connection with MQTT Broker");
    else:
        client.publish(topicName,payload="Online", qos=1, retain=True)

client = mqtt.Client("LDR_Reader");
client.loop_start()
#client.username_pw_set(username="anand",password="mqtt");
client.will_set(topicName,payload="Offline", qos=1, retain=True)
client.connect(mqttBroker,listernerPort);

ldrPrevReading = 0;

try:
    while True:
        ldrReading = getLdrReading();
        if(abs(abs(ldrReading) - abs(ldrPrevReading)) >  LIGHT_SENSOR_DELTA_THRESHOLD): 
            #client.publish(topic="LIGHTSENSOR",payload=ldrReading,qos=qosValue,retain=retainFlag)
            client.publish(topicName,ldrReading,qos=2,retain=True)
            print("Just published " + str(ldrReading) + " to topic " + topicName)
        ldrPrevReading = ldrReading;
        time.sleep(0.1)


except KeyboardInterrupt:
    #client.publish(topicName,payload="Offline", qos=1, retain=True)
    client.disconnect()
    client.loop_stop()
    print("Light Sensor disconnected");



