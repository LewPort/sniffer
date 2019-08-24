import pickle

pin = {
    'dht22': 2
    }

def writePinsOut(pinDict):
    textFile = open('pins.txt', 'wb')
    pickle.dump(pinDict, textFile)
    textFile.close()

def load():
    textFile = open('pins.txt', 'rb')
    return pickle.load(textFile)
