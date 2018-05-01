from flask import Flask,render_template
import json
import requests
from datetime import datetime
from classes import Stations,Sensors,Sensor,Station

app = Flask(__name__)

@app.route('/')
def Table():
    station = Stations()
    city_stations = station.get_city_data("Kraków")

    sensors = Sensors(city_stations)
    Czujniki = sensors.city_sensors

    czujniki_len = len(Czujniki)
    tab_czujniki_len = []
    for i in range(czujniki_len):
        tab_czujniki_len.append(len(Czujniki[i]))

    for i in range(czujniki_len):
        station.streets.append(Station(city_stations[i]['stationName']))
        for a in range(tab_czujniki_len[i]):
            station.streets[i].sensors.append(Sensor('http://api.gios.gov.pl/pjp-api/rest/data/getData/' + str(Czujniki[i][a]['id'])))

    return render_template('html2.html', krakow = city_stations,lista_czujnikow = czujniki_len,lista_czujnikow_len = tab_czujniki_len, all = station)

if __name__ == '__main__':
    app.run(port=5011, debug=True)