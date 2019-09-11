import csvlogging
from outdoor_api import read_json
import graphing

csvlogging.logCurrent(doc_path='csvlog.csv')
csvlogging.logCurrent(doc_path='outdoor_csvlog.csv',
                      human_time=read_json()['time']['date'] + ' ' + read_json()['time']['time'],
                      unix_time=read_json()['time']['unix'],
                      temp=read_json()['ht']['temp'],
                      humidity=read_json()['ht']['humidity'])
graphing.export()
