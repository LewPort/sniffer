from time import localtime, sleep, strftime, time
import temp
import csv

LOG_INTERVAL = 1 #secs
TIME_FORMAT = '%d/%m/%Y %H:%M:%S'
DELETE_OLD_LOGS = False
RETENTION_TIME = 72 #Hours of data to be retained
HEADERS = ['Date and Time', 'Unix Timestamp', 'Temp ºC', 'Humidity %']

##sheet = csv.writer(open('csvlog.csv', 'a'), delimiter=',')

def return_cleaned_sheet(doc_path, age_threshold):
    newSheet = []
    with open(doc_path, 'r') as csvFile:
        oldsheet = list(csv.reader(csvFile))
        for row in oldsheet:
            try:
                if float(row[1]) > time() - 60*60*age_threshold:
                    newSheet.append(row)
            except ValueError:
                continue
    return newSheet

def write_headers_if_needed(doc_path, headers=HEADERS):
    with open(doc_path, 'r') as csvFile:
        if list(csv.reader(csvFile))[0] != headers:
            in_sheet = list(csv.reader(csvFile))
            with open(doc_path, 'w') as csvFile:
                out_sheet = csv.writer(csvFile, delimiter=',')
                out_sheet.writerow(headers)
                for row in in_sheet:
                    out_sheet.writerow(row)

def last_row_unix_time(doc_path):
    with open(doc_path, 'r') as csvFile:
        last_time = list(csv.reader(csvFile))[-1][1]
        return float(last_time)
        
    

def logCurrent(doc_path='csvlog.csv', human_time=strftime(TIME_FORMAT,localtime()),
               unix_time=time(),
               temp=temp.temp(),
               humidity=temp.hmd()):
    if DELETE_OLD_LOGS:
        newSheet = return_cleaned_sheet(RETENTION_TIME)
        with open(doc_path, 'w') as csvFile:
            sheet = csv.writer(csvFile, delimiter=',')
            sheet.writerow(HEADERS)
            for row in newSheet:
                sheet.writerow(row)
    with open(doc_path, 'a') as csvFile:
        write_headers_if_needed(doc_path)
        if last_row_unix_time(doc_path) != float(unix_time):
            sheet = csv.writer(csvFile, delimiter=',')
            sheet.writerow([human_time, unix_time, temp, humidity])

def displayLoop():
    print('Logging:')
    while True:
        logCurrent()
        temp.terminalPrint()
        sleep(LOG_INTERVAL)

if __name__ == '__main__':
    logCurrent()

