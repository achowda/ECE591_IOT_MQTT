# ECE591_IOT_MQTT
Implements a raspberry pi based MQTT publisher and subscriber.

## Description
This code contains 2 MQTT publishers (Light Sensor and a Potentiometer) whose data is refreshed every 100ms and published if the readings exceed certain threshold. This code base also contains a MQTT subscriber that subscribes to the light sensor and hte potentiometer topics.

**In this initial commit, the light sensor readings and the potentiometer readings are simulated using the python random number generation library. This will be integrated with real sensors shortly.**

### Code Highlights
  - The file MQTT_LightSensorSimulator.py simulates a light sensor and publishes readings under the topic "LIGHTSENSOR" if the delta between current reading and the previous reading exceeds a constant threshold (default = 0.5).
  - The file MQTT_PotentiometerSimulator.py simulates a potentiometer and publishes readings under the topic "THRESHOLD" if the current reading exceeds a constant threshold (default = 0.9)
  - The file MQTT_Subscriber.py subscribes to the topics "LIGHTSENSOR" and "THRESHOLD". On receiving a message, prints the payload to the console.
  - QOS value of 2 is used in this implementation. 

## Setup Block Diagram
![image](https://user-images.githubusercontent.com/99939969/158466937-93a32e5a-5c30-4def-ab5a-247b40982880.png)

## Software Pre-Requisistes


## Sample Output 
![image](https://user-images.githubusercontent.com/99939969/158464778-84f45f37-25ed-48f6-abdb-f2ec4cd222a3.png)

