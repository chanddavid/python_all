from http import client
import paho.mqtt.client as mqtt
from random import randrange,uniform
import time
mqttbroker="localhost"
port=1883
#for local host we dont needed usename and password and use mqtt explorer for data visualization
username="tankman"
password="tank@123"

publisher=mqtt.Client("Temperature_Inside")
publisher.username_pw_set(username,password)
publisher.connect(mqttbroker,port)

while True:
    randNum=uniform(10.0,11.0)
    publisher.publish("TEMPERATURE",randNum)
    print("published "+ str(randNum)+ " to TEMPERATURE topic")
    time.sleep(2)

