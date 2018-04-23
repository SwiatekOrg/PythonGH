from flask import Flask,render_template
import json
import requests

app = Flask(__name__)

@app.route('/')
def Table():
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
        stace = requests.get('http://api.gios.gov.pl/pjp-api/rest/station/sensors/' + str(Krakow[i]['id']), headers)
        stace_code = stace.status_code
        stace_json = json.loads(stace.content.decode('utf-8'))
        Czujniki.append(stace_json)
    #for i in range(len(Czujniki)):
        #print(Czujniki[i])

    dct = {}
    for i in range(len(Czujniki)):
        print(len(Czujniki))
        dct['list_%s' % i] = []
        for a in range(len(Czujniki[i])):
            print(len(Czujniki[i]))
            czujnik = requests.get('http://api.gios.gov.pl/pjp-api/rest/data/getData/' + str(Czujniki[i][a]['id']),headers)
            dct['list_%s' % i][a] = json.loads(czujnik.content.decode('utf-8'))
    print(dct['list_0'][0])
    print(dct['list_1'])
    print(dct['list_3'])

    return render_template('html.html', krakow = Krakow,lista_czujnikow = Czujniki, wartosci = dct)

if __name__ == '__main__':
    app.run(port=5011, debug=True)