import datetime, time
import json
import temp
import sys
import os

_OUTPUT = './static/indoorCondAPI.json'

def get_current():
    api = {
        'time':{'unix': time.time(),
                'date':datetime.datetime.fromtimestamp(time.time()).strftime('%d/%m/%Y'),
                'time':datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')},
        'ht':{'temp': '{0:.1f}'.format(temp.temp()),
              'humidity': round(temp.hmd())},
        }
    return api

def write_json(api):
    with open(_OUTPUT, 'w') as outfile:
        json.dump(api, outfile)

api = None

##api = get_current()
##write_json(api)

while True:
    try:
        api = get_current()
        write_json(api)
        time.sleep(1)
    except KeyboardInterrupt:
        exit()
    except:
        e = sys.exc_info()[0]
        e = str(datetime.datetime.now()) + ": " + str(e) + "\n"
        print(e)
        with open('.indoor_api_error_log.txt', 'a') as error_log:
            error_log.write(e)
        continue
    
    

