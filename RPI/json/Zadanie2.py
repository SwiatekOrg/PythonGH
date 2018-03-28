import json
import requests
import sys
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
 #   print(Czujniki[i])

for i in range(len(Czujniki)):
    print("")
    print(Krakow[i]['stationName'])
    for a in range(len(Czujniki[i])):
        czuj = requests.get('http://api.gios.gov.pl/pjp-api/rest/data/getData/'+str(Czujniki[i][a]['id']), headers)
        czuj_json = json.loads(czuj.content.decode('utf-8'))
        print(str(czuj_json['key']) +" dla "+ str( czuj_json['values'][1]['date']) + " minut temu wartosc " + str(czuj_json['values'][1]['value']))