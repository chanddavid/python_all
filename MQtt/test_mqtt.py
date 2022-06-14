from http import client
import paho.mqtt.client as mqtt
import json
import time

# mqttbroker="mqtt.eclipseprojects.io"
# publisher=mqtt.Client("Temperature_Inside")
# publisher.connect(mqttbroker)
# #client=publisher
def on_message(client,userdata,message):
    print("Received message: ",str(message.payload.decode("utf-8")))


mqttbroker="10.10.5.82"
port=1883


sub_client=mqtt.Client("Temperature_Inside")
sub_client.connect(mqttbroker,port)

while True:

    
    sub_client.subscribe("esp32/temperature",1)
    sub_client.on_message=on_message
    # publisher.publish("TEMPERATURE",randNum)
    # print("published "+ str(randNum)+ " to TEMPERATURE topic")
    # time.sleep(2)

