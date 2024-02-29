import paho.mqtt.client as mqtt
import time

from posgres import Posgres

host = "52.220.91.130"
port = 1883

def on_message (client, userdata, message) :
    raw_message = str(message.payload.decode("utf-8"))
    topic = message.topic
    
    print(int(time.time()), 'Received', topic, raw_message)

def on_subscribe (client, obj, mid, granted_qos) :
    print("Subscribe Succeed")

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("application/0f50f6ff-338d-4dcd-a522-5cfd24f6ffe7/device/24e124136d156431/event/up")
    client.subscribe("application/18ab31a6-9a0d-4a38-a5e3-b3605a9a309f/device/24e124445d186746/event/up")
    client.subscribe("application/c22e4c79-d61a-4e8e-bccd-e39384c913f9/device/24e124141d223816/event/up")
    client.subscribe("application/b50618fe-3073-4e6c-acaf-b1b2ff3af9bf/device/24e124538d222160/event/up")
    client.subscribe("application/99cedc9c-2c85-44a0-9889-63ac556fdeac/device/24e124148d118904/event/up")
    client.subscribe("application/9d59b0e3-5210-4763-9fb3-a6fdc8d511f4/device/24e124535d229796/event/up")
    client.subscribe("application/2b695811-907e-4e92-b1c7-00d2ca2dc3c7/device/24e124743d015542/event/up")


client = mqtt.Client()
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect('52.220.91.130', 1883)
client.loop_forever()
