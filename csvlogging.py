from time import localtime, sleep, strftime, time
import temp
import csv

LOG_INTERVAL = 1 #secs
TIME_FORMAT = '%d/%m/%Y %H:%M:%S'
DELETE_OLD_LOGS = False
RETENTION_TIME = 72 #Hours of data to be retained
HEADERS = ['Date and Time', 'Unix Timestamp', 'Temp ºC', 'Humidity %']

sheet = csv.writer(open('csvlog.csv', 'a'), delimiter=',')

def return_cleaned_sheet(age_threshold):
    newSheet = []
    with open('csvlog.csv', 'r') as csvFile:
        oldsheet = list(csv.reader(csvFile))
        for row in oldsheet:
            try:
                if float(row[1]) > time() - 60*60*age_threshold:
                    newSheet.append(row)
            except ValueError:
                continue
    return newSheet

def logCurrent():
    if DELETE_OLD_LOGS:
        newSheet = return_cleaned_sheet(RETENTION_TIME)
        with open('csvlog.csv', 'w') as csvFile:
            sheet = csv.writer(csvFile, delimiter=',')
            sheet.writerow(HEADERS)
            for row in newSheet:
                sheet.writerow(row)
    with open('csvlog.csv', 'a') as csvFile:
        sheet = csv.writer(csvFile, delimiter=',')
        sheet.writerow([strftime(TIME_FORMAT,localtime()),
                        time(),
                        temp.temp(),
                        temp.hmd()])

def displayLoop():
    print('Logging:')
    while True:
        logCurrent()
        temp.terminalPrint()
        sleep(LOG_INTERVAL)

if __name__ == '__main__':
    logCurrent()

