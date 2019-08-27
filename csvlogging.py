from time import localtime, sleep, strftime, time
import temp
import csv

LOGINTERVAL = 1 #secs
TIMEFORMAT = '%d/%m/%Y %H:%M:%S'
TRASHTIME = 72 #Hours of data to be retained
HEADERS = ['DateTime', 'Unix', 'Temp ºC', 'Humidity %']

sheet = csv.writer(open('csvlog.csv', 'a'), delimiter=',')

def returnCleanSheet():
    newSheet = []
    with open('csvlog.csv', 'r') as csvFile:
        oldsheet = list(csv.reader(csvFile))
        for row in oldsheet:
            try:
                if float(row[1]) > time() - 60*60*TRASHTIME:
                    newSheet.append(row)
            except ValueError:
                continue
    return newSheet

def logCurrent():
    newSheet = returnCleanSheet()
    with open('csvlog.csv', 'w') as csvFile:
        sheet = csv.writer(csvFile, delimiter=',')
        sheet.writerow(HEADERS)
        for row in newSheet:
            sheet.writerow(row)
    with open('csvlog.csv', 'a') as csvFile:
        sheet = csv.writer(csvFile, delimiter=',')
        sheet.writerow([strftime(TIMEFORMAT,localtime()),
                        time(),
                        temp.temp(),
                        temp.hmd()])

def displayLoop():
    print('Logging:')
    while True:
        logCurrent()
        temp.terminalPrint()
        sleep(LOGINTERVAL)

if __name__ == '__main__':
    logCurrent()

