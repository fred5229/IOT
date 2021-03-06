#Hello World from pycom LoPy

import machine,  pycom, time

pycom.heartbeat(False)

print("")
print("Hello World from pycom LoPy")
print("On-board RGB LED will blink 10 times")

def blink():
    pycom.rgbled(0x007f00) # green
    time.sleep(0.15)
    pycom.rgbled(0x7f7f00) # yellow
    time.sleep(0.15)
    pycom.rgbled(0x7f0000) # red
    time.sleep(0.15)
    pycom.rgbled(0)             # off
    time.sleep(.55)
    return
    
for x in range(0, 10):  
    print("*",  end="")
    blink()

print("")    
pycom.heartbeat(True)