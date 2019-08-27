from matplotlib import pyplot as plt
import csvlogging
from time import strftime, localtime
import csv

CSVFILE = 'csvlog.csv'

def returnListFromCSV(CSVFILE):
    newList = []
    with open(CSVFILE, 'r') as csvFile:
        newList = list(csv.reader(csvFile))
    return newList

def shortTime(time):
    time = float(time)
    try:
        shortened_time = strftime("%a %H", localtime(time))
    except ValueError:
        pass
    return shortened_time

DATA_LIST = returnListFromCSV(CSVFILE)

datetime_x = [shortTime(row[1]) for row in DATA_LIST[1:]]
standard_y = [n for n in range(10,100, 5)]
temp_y  = [row[2] for row in DATA_LIST[1:]]
humid_y  = [row[3] for row in DATA_LIST[1:]]

plt.plot(datetime_x, temp_y)
plt.plot(datetime_x, humid_y)
plt.grid(True)
plt.axis(tight=True,auto=True)


plt.savefig('graph.png', dpi=150)
