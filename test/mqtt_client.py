import sys
sys.path.append('/usr/local/lib/python3.5/dist-packages/')
import paho.mqtt.client as mqtt
import docker
import re

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("processes/#")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    if(msg.topic == "processes"):
        get_processes(msg.payload.decode("utf-8"))

def get_processes(processes_string):
    print(processes_string)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)
docker_client = docker.from_env()
#client.loop_forever();
container = docker_client.containers.run('hello-world',
                                      detach=True)
container.rename("yooo_yoo_miami")
print(container.logs())




