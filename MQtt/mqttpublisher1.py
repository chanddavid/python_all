from http import client
import paho.mqtt.client as mqtt
from random import randrange,uniform
import time
import json
mqttbroker="10.10.5.82"
port=1883
#for local host we dont needed usename and password and use mqtt explorer for data visualization
# username="tankman"
# password="tank@123"

publisher=mqtt.Client("Temperature_Inside")
# publisher.username_pw_set(username,password)
publisher.connect(mqttbroker,port)

while True:
    randNum=randrange(-10,30)
    dict={"d_id":"dev-4","f_id":"freeze-4","org":"apple","temp":randNum,"ip":"10.10.50.151","c_temp":"26"}
    y = json.dumps(dict)
    print(y)
    publisher.publish("apple/freeze-4/dev-4/temperature",y)
    print("published "+ str(randNum)+ " to TEMPERATURE topic")
    time.sleep(1)

