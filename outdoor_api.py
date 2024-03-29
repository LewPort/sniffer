import time, datetime
import urllib.request
import json

_URL = "http://api.openweathermap.org/data/2.5/weather?q=Hamilton&units=metric&APPID=677f6b056af14113e02f38ae1b18f342"
_FILE = "./static/outdoorCondAPI.json"

def get_data():
    try:
        with urllib.request.urlopen(_URL) as url:
            data = json.loads(url.read().decode())
        return data
    except:
        return None

def temp(data):
    if data:
        temp = data['main']['temp']
        temp = temp
        return round(temp, 1)
    else:
        return "Temp N/A"

def humidity(data):
    if data:
        humidity = data['main']['humidity']
        return round(humidity, 1)
    else:
        return "Humidity N/A"

def reportTime(data):
    if data:
        time = data['dt']
        return time
    else:
        return "Time N/A"

def return_current(data):
    if data:
        api = {
            'time':{'unix': reportTime(data),
                    'date':datetime.datetime.fromtimestamp(reportTime(data)).strftime('%d/%m/%Y'),
                    'time':datetime.datetime.fromtimestamp(reportTime(data)).strftime('%H:%M')},
            'ht':{'temp': temp(data),
                  'humidity': humidity(data)}
            }
        return api

def write_json(api):
    if api:
        with open(_FILE, 'w') as outfile:
            json.dump(api, outfile)
    else:
        print('No API data downloaded from server')

def read_json():
    with open(_FILE) as raw_json:
        json_data = str(json.load(raw_json))
        return eval(json_data)

api = None
api = return_current(get_data())
write_json(api)

##while True:
##    api = return_current(get_data())
##    write_json(api)
##    time.sleep(5*60)
