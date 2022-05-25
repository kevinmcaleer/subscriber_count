# Gets the list of subscribers
# YouTube stats

import paho.mqtt.client as paho
from time import sleep, time
from datetime import datetime, timedelta
from googleapiclient.discovery import build
from secret import api_key

# Replace the IP address below with your own MQTT server address
broker="192.168.1.152"
port=1883

# Give your client a unique id
client_id = "subscriber_counter"

# define the topic to publish to
topic = "/subscribers"

def on_publish(client, userdata, result):    
    # print(f"Number of subscribers: {get_subs()}")
    pass

mqtt_client = paho.Client(client_id=client_id)
mqtt_client.on_publish = on_publish
mqtt_client.connect(broker, port)

youtube = build('youtube', 'v3', developerKey=api_key)

def get_stats():
    """ Returns a dictionary of stats"""
    stats = youtube.channels().list(part='statistics', forUsername='kevinmcaleer28').execute()
    # print(stats)
    return stats

def get_subs():
    """ Returns the subcount """
    stats = get_stats()
    items = stats.get("items")[0]
    statistics = items.get("statistics")
    subs = statistics.get("subscriberCount")
    print(f'Subscriber Count: {subs}')
    return subs

# get the current time
start_time = datetime.now()
#print(f"time is: {start_time}")
message = get_subs()

# interval to wait in minutes before getting the subcount again 
interval = 30

while True or KeyboardInterrupt:
    
    current_time = datetime.now()
    #print(f'Current time is: {current_time}')
    check = start_time + timedelta(minutes=interval)
    #print(f'start: {start_time}, current:{current_time}, check {check}')
    if datetime.now() >= check:
        #print(f'{interval} minutes has elapsed')
        start_time = datetime.now()
        # get the current sub count
        message = get_subs()
    # print(message)
    try:
        mqtt_client.publish(topic, message)
    except:
         print("There was a problem publishing the message") 
    
    sleep(2)

    