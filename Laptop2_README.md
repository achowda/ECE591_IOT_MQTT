# Laptop 2 MQTT Subscriber

## Description
This code implements a MQTT subscriber that subscribes to the topics "lightSensor", threshold", "LightStatus", "Status/RaspberryPiA", and "Status/RaspberryPiC".
It will first establish a connection to the MQTT broker running on laptop #1, then it will constantly listen for new incoming messages that get published to any of the subscribed topics.
It creates a log file which keeps a record of each incoming message along with the time stamps, as well as time stamps for when LED1 is turned on or off.

## Execution Instructions
  - Use the package manager pip to install Paho MQTT Libraries.
```bash
pip install paho-mqtt
```
  - Edit the mqttBroker ip address on line 36 to be the ip address of the MQTT broker running on laptop #1.
 
  - You may execute this code from the command line.
```bash
python Laptop2_Subscriber.py
```
  - You will find the log file located in the same directory that the code is located.

## Sample Output 
![image](https://user-images.githubusercontent.com/17738048/159798980-985b07a1-42ae-460e-afeb-4056998cefdf.png)
