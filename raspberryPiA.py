from gpiozero import MCP3008
import time
from paho.mqtt import client as mqtt

threshold = 0.2
#preLdr = 0
#prePoten = 0


#broker = "192.168.0.179"
broker = "192.168.43.115"
#broker = "10.2.1.225"
port = 1883
client_id = "A"
topic = ["lightSensor", "threshold"]

def ldr():
    light = MCP3008(0)
    return(light.value)

def potentiometer():
    poten = MCP3008(1)
    return(poten.value)

preLdr = ldr()
prePoten = potentiometer()

def checkSensor(client):
    global preLdr
    global prePoten
    curLdr = ldr()
    curPoten = potentiometer()
    
    #print("LDR: ", curLdr, "  Potentiometer: ", curPoten)
    if abs(curLdr - preLdr) >= threshold or abs(curPoten - prePoten) >= threshold:
        print("LDR: ", curLdr, "  Potentiometer: ", curPoten)
        client.publish(topic[0], payload=str(curLdr), qos=2, retain=True)
        client.publish(topic[1], payload=str(curPoten), qos=2, retain=True)
        print("publish lightSensor & threshold")
        preLdr = curLdr
        prePoten = curPoten
    
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
    global preLdr
    global prePoten
    print(msg.topic, ": ", msg.payload.decode("ascii"))
    if msg.retain == 1:
        if msg.topic == topic[0]:
            preLdr = float(msg.payload.decode("ascii"))
        elif msg.topic == topic[1]:
            prePoten = float(msg.payload.decode("ascii"))
    

def on_disconnect(client, userdata, rc):
    client.connected_flag = False
    client.disconnect_flag = True
    
    print("disconnect gracefully!")

def connect():
    client = mqtt.Client(client_id)
    client.will_set("Status/RaspberryPiA", payload="offline", qos=2, retain=True)
    print("set last will")
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message
    client.connect(host=broker, port=port, keepalive=10)
    while True:
        try:
            client.loop_start()
            checkSensor(client)
            time.sleep(0.1)
            client.loop_stop()
        except KeyboardInterrupt:
            client.disconnect()
            break    

if __name__ == '__main__':
    connect()