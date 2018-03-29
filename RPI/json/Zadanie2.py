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
 #   print(Czujniki[i])

for i in range(len(Czujniki)):
    print("")
    print(Krakow[i]['stationName'])
    for a in range(len(Czujniki[i])):

        czuj = requests.get('http://api.gios.gov.pl/pjp-api/rest/data/getData/'+str(Czujniki[i][a]['id']), headers)
        czuj_json = json.loads(czuj.content.decode('utf-8'))

        if czuj_json['values'][0]['value'] == None:
            if czuj_json['values'][1]['value'] == None:
                number = 2
            else:
                number = 1
        else:
            number = 0

        czas = time.localtime()
        dt_str = str(czuj_json['values'][number]['date'])
        dt_obj = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
        czas = (str(str(czas[0]) + "-" + str(czas[1]) + "-" + str(czas[2]) + " " + str(czas[3]) + ":" + str(czas[4]) + ":" + str(czas[5])))
        czas = datetime.strptime(czas, '%Y-%m-%d %H:%M:%S')
        godzina1 = [dt_obj.hour, dt_obj.minute]
        godzina2 = [czas.hour, czas.minute]
        minuta = int((godzina2[0] - godzina1[0]) * 60 + (godzina2[1] - godzina1[1]))


        print(str(czuj_json['key']) + " dla " + str(minuta) + " minut temu wartosc " + str(czuj_json['values'][number]['value']))