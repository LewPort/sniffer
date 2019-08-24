import Adafruit_DHT as dht
import time
import pins
import sys

PIN = pins.load()['dht22']

def temp():
    temp = dht.read_retry(dht.DHT22, PIN)[1]
    return round(temp, 1)

def hmd():
    h = dht.read_retry(dht.DHT22, PIN)[0]
    return round(h, 1)

def test():
    print('Press Ctrl+C to cancel\n\n')
    while True:
        display = (str(temp()) + "ºc\n" + str(hmd()) + "%")
        sys.stdout.write('\033[1A \r' + display)
        sys.stdout.flush()
        time.sleep(1)

if __name__ == '__main__':
    test()
    exit()
