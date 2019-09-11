import Adafruit_DHT as dht
import pins
import sys

from time import localtime, strftime, sleep


TIMEFORMAT = '%H:%M:%S'
PIN = pins.load()['dht22']

def temp():
    temp = None
    while temp is None:
        temp = dht.read_retry(dht.DHT22, PIN)[1]
    return round(temp, 1)

def hmd():
    h = None
    while h is None:
        h = dht.read_retry(dht.DHT22, PIN)[0]
    return round(h, 1)

def terminalPrint():
    tempdisplay = (str(temp()) + "ºc\n" + str(hmd()) + "%")
    timedisplay = strftime(TIMEFORMAT, localtime()) + '\n'
    sys.stdout.write(timedisplay + tempdisplay + '\033[2A \r')
    sys.stdout.flush()


def testloop():
    print('Press Ctrl+C to cancel\n')
    while True:
        terminalPrint()
        sleep(1)
        

if __name__ == '__main__':
    testloop()
    exit()
