from sense_hat import SenseHat
from time import sleep
from datetime import datetime 
import paho.mqtt.client as paho

# Replace with the IP or URI of the MQTT server you use
mqtt_server = '192.168.1.152' 

# A unique name for this client when connecting to the MQTT server
client_id = "sensehat"

update_frequency_in_seconds = 5
sense = SenseHat()

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("$SYS/#")

def on_message(client, userdata, msg):
    print("messgae received")
    print(msg.topic+" "+str(msg.payload))

def on_message_print(client, userdata, message):
    print(f"message:{message}, userdata:{userdata}")

client = paho.Client(client_id=client_id)
client.on_connect = on_connect
client.on_message = on_message_print
client.connect(host=mqtt_server)

topic = '/subscribers'
client.subscribe(topic=topic)


while True:
    sleep(1)

sense.show_message(message)