import paho.mqtt.client as mqtt
import time


def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))

mqttbroker = "110.44.123.47"
port = 2883
client = mqtt.Client("P1")
client.connect(mqttbroker, port)


client.subscribe("apple/freeze-3/dev-3/temperature")
client.on_message = on_message

client.loop_forever()
