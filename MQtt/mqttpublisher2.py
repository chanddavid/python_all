import paho.mqtt.client as mqtt
from random import randrange,uniform
import time



# mqttbroker="mqtt.eclipseprojects.io"
# client=mqtt.Client("Temperature Outside")
# client.connect(mqttbroker)

mqttbroker="localhost"
port=1883
#for local host we dont needed usename and password
username="tankman"
password="tank@123"
publisher=mqtt.Client("Temperature_Inside")
publisher.username_pw_set(username,password)
publisher.connect(mqttbroker,port)


while True:
    randNum=randrange(10)
    publisher.publish("TEMPERATURE1",randNum)
    print("published "+ str(randNum)+ " to TEMPERATURE topic")
    time.sleep(2)

