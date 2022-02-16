from network import WLAN
wlan = WLAN() # we call the constructor without params
# turn off Wifi
wlan.deinit()
print('Turned off WiFi')