# ECE591_IOT_MQTT
Implements a raspberry pi based MQTT publisher and subscriber.

## Description
This code contains 2 MQTT publishers (Light Sensor and a Potentiometer) whose data is refreshed every 100ms and published if the readings exceed certain threshold. This code base also contains a MQTT subscriber that subscribes to the light sensor and hte potentiometer topics.

**In this initial commit, the light sensor readings and the potentiometer readings are simulated using the python random number generation library. This will be integrated with real sensors shortly.**

### Code Highlights
  - The file MQTT_LightSensorSimulator.py simulates a light sensor and publishes readings under the topic "LIGHTSENSOR" if the delta between current reading and the previous reading exceeds a constant threshold (default = 0.5).
  - The file MQTT_PotentiometerSimulator.py simulates a potentiometer and publishes readings under the topic "THRESHOLD" if the current reading exceeds a constant threshold (default = 0.9)
  - The file MQTT_Subscriber.py subscribes to the topics "LIGHTSENSOR" and "THRESHOLD". On receiving a message, prints the payload to the console.
  - MQTT QOS value of 2 is used in this implementation. 
  - The MQTT Broker running on a host PC is used in this setup. Please edit all 3 files to supply the correct MQTT Broker host address.

## Setup Block Diagram
![image](https://user-images.githubusercontent.com/99939969/158471171-325cd05c-deb0-4729-bdd9-0ef1da063f77.png)

**NOTE: Sensor Interface implementation in progress. Simulated sensor data is used in the current implementation**

## Software Pre-Requisistes
  - Mosquitto MQTT Broker is used in this setup, since it is open source and easily to deploy. Mosquitto is available for download in this link - https://mosquitto.org/files/binary/win64/mosquitto-2.0.14-install-windows-x64.exe. To deploy the MQTT broker on a windows laptop, run the cmd `net start mosquitto`.
  - Please edit the following lines in the mosquitto.conf file usually installed in location * *"C:\ProgramFiles\mosquitto"* * on a Windows PC.
    ![image](https://user-images.githubusercontent.com/99939969/158472696-d3f7a9d1-92af-476a-93a1-59d768ebde42.png)
    **NOTE: You may also need to disable firewall from blocking connections by adding exceptions in the windows firewall for inbound connections on port no. 1883**
    ![image](https://user-images.githubusercontent.com/99939969/158473585-db66d687-e68b-40ea-a7b5-415ae3e0f058.png)


  - Paho MQTT Libraries for MQTT client side code running on raspberry pi - 'pip install paho-mqtt'

## Sample Simultion Output 
![image](https://user-images.githubusercontent.com/99939969/158464778-84f45f37-25ed-48f6-abdb-f2ec4cd222a3.png)

