#get your device's EUI
from network import LoRa
import binascii

def print_EUI():
    lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
    print(binascii.hexlify(lora.mac()).upper().decode('utf-8'))