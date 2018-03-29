import json
import requests
from datetime import datetime
import time


headers = {'Content-Type': 'application/json; charset=utf-8'}
url = "http://api.gios.gov.pl/pjp-api/rest/station/findAll"
response = requests.get(url, headers)
response_code = response.status_code
response_json = json.loads(response.content.decode('utf-8'))

Krakow = []
for i in range(len(response_json)):
    if str(response_json[i]['city']['name']) == "Kraków":
        Krakow.append(response_json[i])
#for i in range(len(Krakow)):
    #print(Krakow[i])

Czujniki = []
for i in range(len(Krakow)):
    stace = requests.get('http://api.gios.gov.pl/pjp-api/rest/station/sensors/'+str(Krakow[i]['id']), headers)
    stace_code = stace.status_code
    stace_json = json.loads(stace.content.decode('utf-8'))
    Czujniki.append(stace_json)
#for i in range(len(Czujniki)):
    #print(Czujniki[i])

current_time = datetime.now()
for i in range(len(Czujniki)):
    print("")
    print(Krakow[i]['stationName'])
    for a in range(len(Czujniki[i])):
        czujnik = requests.get('http://api.gios.gov.pl/pjp-api/rest/data/getData/'+str(Czujniki[i][a]['id']), headers)
        czujnik_json = json.loads(czujnik.content.decode('utf-8'))
        for x in range(len(czujnik_json['values'])):
            if czujnik_json['values'][x]['value'] != None:
                existing_hour_index = x
                break
        czujnik_time = datetime.strptime(str(czujnik_json['values'][existing_hour_index]['date']), '%Y-%m-%d %H:%M:%S')
        print(str(czujnik_json['key']) + " dla " + str(int((current_time-czujnik_time).total_seconds()//60)) + " minut temu wartosc " + str(czujnik_json['values'][existing_hour_index]['value']))