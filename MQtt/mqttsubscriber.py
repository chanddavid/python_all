import paho.mqtt.client as mqtt
import time



def on_message(client,userdata,message):
    print("Received message: ",str(message.payload.decode("utf-8")))

# mqttbroker="mqtt.eclipseprojects.io"
# client=mqtt.Client("SmartPhone")
# client.connect(mqttbroker)

mqttbroker="localhost"
port=1883
client=mqtt.Client("SmartPhone")
client.connect(mqttbroker,port)



client.subscribe("TEMPERATURE")
client.on_message=on_message

time.sleep(20)
client.loop_forever()

