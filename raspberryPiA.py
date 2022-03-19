from gpiozero import MCP3008
import time
from paho.mqtt import client as mqtt

threshold = 0
preLdr = 0
prePoten = 0


broker = "192.168.0.179"
port = 1883
client_id = "A"
topic = ["lightSensor", "threshold"]

def ldr():
    light = MCP3008(0)
    return(light.value)

def potentiometer():
    poten = MCP3008(1)
    return(poten.value)

def checkSensor(client):
    curLdr = ldr()
    curPoten = potentiometer()
    
    
    
    
    
    
    
    if abs(curLdr - preLdr) >= threshold or abs(curPoten - prePoten) >= threshold:
        print("LDR: ", curLdr, "  Potentiometer: ", curPoten)
        client.publish(topic[0], payload=str(curLdr), qos=2)
        client.publish(topic[1], payload=str(curPoten), qos=2)
        print("publish threshold")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        
        
        
        client.subscribe(topic[0], qos=2)
        client.subscribe(topic[1], qos=2)
        print("subscribe")
        
        client.publish("Status/RaspberryPiA", "online", 2, True)
        print("publish online")
        
    else:
        print("Failed to connect, return code %d\n", rc)

def on_message(client, userdate, msg):
    
    print(msg.topic, ": ", msg.payload.decode("ascii"))
    checkSensor(client)
    

def on_disconnect(client, userdata, rc):
    client.connected_flag = False
    client.disconnect_flag = True
    
    print("disconnect gracefully!")

def connect():
    client = mqtt.Client(client_id)
    client.will_set("Status/RaspberryPiA", payload="offline", qos=2, retain=True)
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message
    client.connect(broker, port)
    
    client.loop_start()
    checkSensor(client)
    time.sleep(0.1)
    client.loop_stop()
    client.loop()
    
    
    
    
    
    
    
    client.loop_forever()
    
    
    
    """
    print(1)
    
    client.loop_start()
    print(2)
    
    
    time.sleep(5)
    client.loop_stop()
    client.disconnect()
    
    
    """

if __name__ == '__main__':
    connect()



"""
for i in range(10000):
    
    curLdr = ldr()
    curPoten = potentiometer()
    print("LDR: ", curLrd, "  Potentiometer: ", curPoten)
    
    if abs(curLdr - preLdr) >= threshold or abs(curPoten - prePoten) >= threshold:
        client.publish(topic[0], curLdr)
        client.publish(topic[1], curPoten)
    time.sleep(0.1)
"""

"""
import spidev
import time
 

delay = 0.5
ldr_channel = 0
 

spi = spidev.SpiDev()
spi.open(0, 0)
 
def readadc(adcnum):
    
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, (8 + adcnum) << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data

while True:
    ldr_value = readadc(ldr_channel)
    print(time.time())
    print("LDR Value: %d" % ldr_value)
    time.sleep(delay)
"""