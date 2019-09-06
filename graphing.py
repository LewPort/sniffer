from time import strftime, strptime, localtime, time
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
import csvlogging
import datetime
import random
import csv

CSVFILE = 'csvlog.csv'
T_COLOUR = '#e0474c'
H_COLOUR = '#7acfd6'
GRAPHING_PERIOD = 72
plt.style.use('dark_background')

def returnListFromCSV(CSVFILE):
    new_list = []
    with open(CSVFILE, 'r') as csvFile:
        for row in csv.reader(csvFile):
            try:
                if float(row[1]) > time() - 60*60*GRAPHING_PERIOD:
                    new_list.append(row)
            except ValueError:
                continue 
    return new_list

DATA_LIST = returnListFromCSV(CSVFILE)

datetime_x = [datetime.datetime.fromtimestamp(float(row[1])) for row in DATA_LIST[1:]]
temp_y  = [float(row[2]) for row in DATA_LIST[1:]]
humid_y  = [float(row[3]) for row in DATA_LIST[1:]]

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

templine = ax1.plot_date(datetime_x, temp_y,
              color=T_COLOUR,
              linestyle='solid',
              marker=None,
              label='Temperature ºc')
ax1.set_ylim([0,40])
humidline = ax2.plot_date(datetime_x, humid_y,
              color=H_COLOUR,
              linestyle='solid',
              marker=None,
              label='Humidity %')
ax2.set_ylim([0,100])


plt.title('Indoor Temperature and Humidity Over %s Hours' % GRAPHING_PERIOD)
ax1.set_xlabel('Day & Time')
ax1.set_ylabel('Temperature ºc')
ax2.set_ylabel('Humidity %')
ax1.legend(loc=2)
ax2.legend(loc=1)




ax1.grid(True)
ax2.grid(False)
plt.tight_layout()
plt.gcf().autofmt_xdate()
date_format = mpl_dates.DateFormatter('%a %H:%M')
plt.gca().xaxis.set_major_formatter(date_format)

def export(name='./static/graph.png'):
##    os.system('rm ./static/graph.png*')                                            
    plt.savefig(name, transparent=True)

if __name__ == '__main__':
    export()

