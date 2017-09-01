import paho.mqtt.client as paho
import time
import datetime
import json
import random
import config


def on_connect(client, userdata, flags, rc):
    print("CONNACK received with code %d." % (rc))
 
client = paho.Client()
client.username_pw_set(config.MQTT_USERNAME, config.MQTT_PASSWORD)
client.on_connect = on_connect
client.connect(config.MQTT_HOST, config.MQTT_PORT)

client.loop_start()

msg = {'title': 'Demo sensor'}

while True:
    msg['data'] = random.random() * 20
    msg['timestamp'] = datetime.datetime.utcnow().strftime('%Y-%d-%mT%H:%M:%SZ')
    (rc, mid) = client.publish("hdw", json.dumps(msg), qos=0)
    time.sleep(5)
