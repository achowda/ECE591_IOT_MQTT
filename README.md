# ECE591_IOT_MQTT
Implements a raspberry pi based MQTT publisher and subscriber.

## Description
This code contains 2 MQTT publishers (Light Sensor and a Potentiometer) whose data is refreshed every 100ms and published if the readings exceed certain threshold. This code base also contains a MQTT subscriber that subscribes to the light sensor and hte potentiometer topics.

**In this initial commit, the light sensor readings and the potentiometer readings are simulated using the python random number generation library. This will be integrated with real sensors shortly.**

### Code Highlights
  - The file MQTT_LightSensorSimulator.py simulates a light sensor and publishes readings under the topic "LIGHTSENSOR" if the delta between current reading and the previous reading exceeds a constant threshold (default = 0.5).
  - The file MQTT_PotentiometerSimulator.py simulates a potentiometer and publishes readings under the topic "THRESHOLD" if the current reading exceeds a constant threshold (default = 0.9)
  - The file MQTT_Subscriber.py subscribes to the topics "LIGHTSENSOR" and "THRESHOLD". On receiving a message, prints the payload to the console.
  - 

