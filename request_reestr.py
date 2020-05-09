import webbrowser,time
from selenium import webdriver
import csv
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import openpyxl
import requests
import json
import urllib

#0131fae6-4f05-463d-bef0-7f1f32ff7230
#55.892268
# [35.7988817468766, 35.8119157103966, 55.8231743212821, 55.8305106504981]
# 55.857992, 35.855130
#def request(x_coordinate, y_coordinate):
res = requests.get('https://geocode-maps.yandex.ru/1.x/?format=json&apikey=0131fae6-4f05-463d-bef0-7f1f32ff7230&geocode=' + str(35.855130)+','+str(55.857992)+'&results=1')
if res.status_code == 200:
    print('adress got')
todo = json.loads(res.text)
adress = todo['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text']
adress = adress[8:]
url_egrnspravka = 'https://егрнсправка.рф/search/?search='+adress+'&s='
print(url_egrnspravka)
link = urllib.request.urlopen(url_egrnspravka)
print(link.status)
print(adress)
