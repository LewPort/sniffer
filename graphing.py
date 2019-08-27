from matplotlib import pyplot as plt
import csvlogging
import time
import csv

CSVFILE = 'csvlog.csv'

def returnListFromCSV(CSVFILE):
    newList = []
    with open(CSVFILE, 'r') as csvFile:
        newList = list(csv.reader(csvFile))
    return newList

DATA_LIST = returnListFromCSV(CSVFILE)

datetime_x = [row[0] for row in DATA_LIST][1:]
temp_y  = [row[2] for row in DATA_LIST][1:]
humid_y  = [row[3] for row in DATA_LIST][1:]

plt.plot(datetime_x, temp_y, humid_y)

plt.savefig('graph.png')
