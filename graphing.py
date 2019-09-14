from time import strftime, strptime, localtime, time
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
import csvlogging
import datetime
import random
import csv

INDOOR_CSVFILE = 'csvlog.csv'
OUTDOOR_CSVFILE = 'outdoor_csvlog.csv'
INDOOR_COLOUR = '#e0474c'
OUTDOOR_COLOUR = '#7acfd6'
GRAPHING_PERIOD = 24
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

INDOOR_DATA_LIST = returnListFromCSV(INDOOR_CSVFILE)
OUTDOOR_DATA_LIST = returnListFromCSV(OUTDOOR_CSVFILE)

indoor_datetime_x = [datetime.datetime.fromtimestamp(float(row[1])) for row in INDOOR_DATA_LIST[1:]]
indoor_temp_y  = [float(row[2]) for row in INDOOR_DATA_LIST[1:]]
indoor_humid_y  = [float(row[3]) for row in INDOOR_DATA_LIST[1:]]

outdoor_datetime_x = [datetime.datetime.fromtimestamp(float(row[1])) for row in OUTDOOR_DATA_LIST[1:]]
outdoor_temp_y  = [float(row[2]) for row in OUTDOOR_DATA_LIST[1:]]
outdoor_humid_y  = [float(row[3]) for row in OUTDOOR_DATA_LIST[1:]]

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot_date(indoor_datetime_x, indoor_temp_y,
              color=INDOOR_COLOUR,
              linestyle='solid',
              marker=None,
              label='Indoor ºc')
ax1.plot_date(outdoor_datetime_x, outdoor_temp_y,
              color=OUTDOOR_COLOUR,
              linestyle='solid',
              marker=None,
              label='Outdoor ºc')
ax1.set_ylim([-40,40])
ax2.plot_date(indoor_datetime_x, indoor_humid_y,
              color=INDOOR_COLOUR,
              linestyle=':',
              marker=None,
              label='Indoor Humid %')
ax2.plot_date(outdoor_datetime_x, outdoor_humid_y,
              color=OUTDOOR_COLOUR,
              linestyle=':',
              marker=None,
              label='Outdoor Humid %')
ax2.set_ylim([0,100])


plt.title('Temperature and Humidity Over %s Hours' % GRAPHING_PERIOD)
#ax1.set_xlabel('Day & Time')
ax1.set_ylabel('Temperature ºc')
ax2.set_ylabel('Humidity %')
fig.legend(loc=(0.2, 0.2))




ax1.grid(True)
ax2.grid(False)
plt.tight_layout()
plt.gcf().autofmt_xdate()
date_format = mpl_dates.DateFormatter('%a %H:%M')
plt.gca().xaxis.set_major_formatter(date_format)

def export(name='./static/graph.png'):                                            
    plt.savefig(name, transparent=True)

if __name__ == '__main__':
    export()

