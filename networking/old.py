from mqtt import MQTTClient
# from mqtt import MQTTClient_lib as MQTTClient
from network import WLAN
import machine
import time

def sub_cb(topic, msg):
   print(msg)

wlan = WLAN(mode=WLAN.STA)
wlan.connect("Johnny2000", auth=(WLAN.WPA2, "fedkarma"), timeout=5000)

while not wlan.isconnected():  
    machine.idle()
print("Connected to WiFi\n")

client = MQTTClient("xd99", "influx.itu.dk",user="iot2022", password="50b1ll10n", port=8883)

client.set_callback(sub_cb)
client.connect()
client.subscribe(topic="IoT2022sec/battleships")

client.publish(topic="IoT2022sec/battleships", msg="MEL:0 3 5 5 0 3 6 5")
