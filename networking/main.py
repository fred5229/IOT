import time
import machine
from network import WLAN
from mqtt import MQTTClient # Grapped from https://github.com/pycom/pycom-libraries/blob/master/examples/mqtt/mqtt.py
                            # Add to your /lib folder and upload
import pycom

pycom.heartbeat(False)  # disable the heartbeat LED

# Configuration variables
WIFI_SSID = "Johnny2000"
WIFI_PW = "fedkarma"
MQTT_CLIENT = "xddddd9" # Here you make up a client ID which should be unique
MQTT_HOST = "influx.itu.dk" 
MQTT_USER = "iot2022"
MQTT_PW = "50b1ll10n"
MQTT_TOPIC = "IoT2022sec/fgor" # Test-topic is for testing
MQTT_SSL = True # If possible, always use SSL

print("WiFi: connecting to %s ..." % WIFI_SSID)
# Connect to wifi.
wlan = WLAN(mode=WLAN.STA)
wlan.connect(ssid=WIFI_SSID, auth=(WLAN.WPA2, WIFI_PW))
while not wlan.isconnected():
    machine.idle()
print("WiFi: connected successfully to %s" % WIFI_SSID)

# Connect to MQTT
mqtt = MQTTClient(MQTT_CLIENT, MQTT_HOST, user=MQTT_USER, password=MQTT_PW, ssl=MQTT_SSL)
mqtt.connect()
print("MQTT connected")

# Publish a single message
mqtt.publish(topic=MQTT_TOPIC, msg="hello")