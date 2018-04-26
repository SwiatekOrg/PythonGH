from flask import Flask,render_template
import json
import requests

app = Flask(__name__)

@app.route('/')
def Table():
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    url = "http://api.gios.gov.pl/pjp-api/rest/station/findAll"
    response = requests.get(url, headers)
    response_json = json.loads(response.content.decode('utf-8'))

    Krakow = []
    for i in range(len(response_json)):
        if str(response_json[i]['city']['name']) == "Kraków":
            Krakow.append(response_json[i])

    Czujniki = []
    for i in range(len(Krakow)):
        stace = requests.get('http://api.gios.gov.pl/pjp-api/rest/station/sensors/' + str(Krakow[i]['id']), headers)
        stace_json = json.loads(stace.content.decode('utf-8'))
        Czujniki.append(stace_json)
    czujniki_len = len(Czujniki)

    tab_czujniki_len = []
    for i in range(czujniki_len):
        tab_czujniki_len.append(len(Czujniki[i]))

    pierwiastki = []
    wartosci = []
    godzina = []
    for i in range(czujniki_len):
        pierwiastki.append([])
        wartosci.append([])
        godzina.append([])
        for a in range(tab_czujniki_len[i]):
            czujnik = requests.get('http://api.gios.gov.pl/pjp-api/rest/data/getData/' + str(Czujniki[i][a]['id']),headers)
            czujnik_json = json.loads(czujnik.content.decode('utf-8'))
            for x in range(len(czujnik_json['values'])):
                if czujnik_json['values'][x]['value'] != None:
                    existing_hour_index = x
                    break
            pierwiastki[i].append(czujnik_json['key'])
            wartosci[i].append(float(czujnik_json['values'][existing_hour_index]['value']))
            godzina[i].append(czujnik_json['values'][existing_hour_index]['date'])

    return render_template('html.html', krakow = Krakow,lista_czujnikow = czujniki_len,lista_czujnikow_len = tab_czujniki_len, pierwiastek = pierwiastki, wartosc = wartosci, godzina = godzina)

if __name__ == '__main__':
    app.run(port=5011, debug=True)