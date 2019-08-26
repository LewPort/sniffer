from time import localtime, sleep, strftime, time
import temp
import csv

LOGINTERVAL = 1 #secs
TIMEFORMAT = '%d/%m/%Y %H:%M:%S'
TRASHTIME = 60*60*24 #24 Hours

sheet = csv.writer(open('csvlog.csv', 'a'), delimiter=',')

def log():
    with open('csvlog.csv', 'a') as csvFile:
        sheet = csv.writer(csvFile, delimiter=',')
        sheet.writerow([strftime(TIMEFORMAT,localtime()),
                        time(),
                        temp.temp(),
                        temp.hmd()])

def logloop():
    print('Logging:')
    while True:
        log()
        temp.terminalPrint()
        sleep(LOGINTERVAL)

if __name__ == '__main__':
    log()

