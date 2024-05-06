import requests
from flask import Flask, render_template
from datetime import datetime
import http.client
import json
app = Flask(__name__)

api_key = '51s14ZcgWr620sMgeGHoSU:77pzvwpISFqRXwEi96s6gm'

def get_weather_data(year):
    # Belirli bir yıl için istek gönderme
    start_date = f"01.01.{year}"
    end_date = f"31.12.{year}"
    response = requests.get('https://api.collectapi.com/weather/getWeather?data.city=bodrum', params={'start_date': start_date, 'end_date': end_date, 'city': 'bodrum'}, headers={'Authorization': 'apikey ' + api_key})
    data = response.json()
    weather_data = data['result']
    return weather_data

def calculate_average_temperature(weather_data):
    # Hava durumu verilerinden sıcaklık değerlerini al
    temperatures = [float(entry['degree']) for entry in weather_data]
    # Sıcaklık değerlerinin ortalamasını hesapla
    average_temperature = sum(temperatures) / len(temperatures)
    return average_temperature

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graphic')
def graphicbodrum():
  

    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = {
        'content-type': "application/json",
        'authorization': "apikey 51s14ZcgWr620sMgeGHoSU:77pzvwpISFqRXwEi96s6gm"
        }

    conn.request("GET", "/weather/getWeather?data.lang=tr&data.city=bodrum", headers=headers)

    res = conn.getresponse()
    data = res.read()
    print(type(data))
    jsonObject = json.loads(data.decode("utf-8"))
    
    datas = []
    dictData = {} 
    # print the keys and values
    for key in jsonObject['result']:
        #value = jsonObject[key]
        print("The key and value:",key['degree'])
        dictData = {'date':key['date'], 'degree':key['degree']}

        datas.append(dictData)

    print(datas)
    #print(data.decode("utf-8"))
    # Bugünün tarihini al
    today = datetime.today()
    # Belirli yıllara ait hava durumu verilerini al
    weather_data_2024 = get_weather_data(2024)
    weather_data_2022 = get_weather_data(2022)
    weather_data_2020 = get_weather_data(2020)
    weather_data_2018 = get_weather_data(2018)
    # Ortalama sıcaklık değerlerini hesapla
    average_temperature_2024 = calculate_average_temperature(weather_data_2024)
    average_temperature_2022 = calculate_average_temperature(weather_data_2022)
    average_temperature_2020 = calculate_average_temperature(weather_data_2020)
    average_temperature_2018 = calculate_average_temperature(weather_data_2018)
    # Şablonu render et
    return render_template('graphic.html', 
                         
                          datas=datas)

"""@app.route('/graphic')
def graphicankara():

    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = {
        'content-type': "application/json",
        'authorization': "apikey 51s14ZcgWr620sMgeGHoSU:77pzvwpISFqRXwEi96s6gm"
        }

    conn.request("GET", "/weather/getWeather?data.lang=tr&data.city=ankara", headers=headers)

    ress = conn.getresponse()
    datad = ress.read()
    print(type(datad))
    jsonObjects = json.loads(datad.decode("utf-8"))
    
    datass = []
    dictDatas = {} 
    # print the keys and values
    for key in jsonObjects['result']:
        #value = jsonObject[key]
        print("The key and value:",key['degree'])
        dictDatas = {'date':key['date'], 'degree':key['degree']}

        datass.append(dictDatas)

    print(datass)
    #print(data.decode("utf-8"))
    # Bugünün tarihini al
    today = datetime.today()
    # Belirli yıllara ait hava durumu verilerini al
    weather_data_2024 = get_weather_data(2024)
    weather_data_2022 = get_weather_data(2022)
    weather_data_2020 = get_weather_data(2020)
    weather_data_2018 = get_weather_data(2018)
    # Ortalama sıcaklık değerlerini hesapla
    average_temperature_2024 = calculate_average_temperature(weather_data_2024)
    average_temperature_2022 = calculate_average_temperature(weather_data_2022)
    average_temperature_2020 = calculate_average_temperature(weather_data_2020)
    average_temperature_2018 = calculate_average_temperature(weather_data_2018)
    # Şablonu render et
    return render_template('graphic.html', 
                         
                          datass=datass)"""
def graphicbodrum():
  

    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = {
        'content-type': "application/json",
        'authorization': "apikey 51s14ZcgWr620sMgeGHoSU:77pzvwpISFqRXwEi96s6gm"
        }

    conn.request("GET", "/weather/getWeather?data.lang=tr&data.city=ankara", headers=headers)

    res = conn.getresponse()
    data = res.read()
    print(type(data))
    jsonObject = json.loads(data.decode("utf-8"))
    
    datas = []
    dictData = {} 
    # print the keys and values
    for key in jsonObject['result']:
        #value = jsonObject[key]
        print("The key and value:",key['degree'])
        dictData = {'date':key['date'], 'degree':key['degree']}

        datas.append(dictData)

    print(datas)
    #print(data.decode("utf-8"))
    # Bugünün tarihini al
    today = datetime.today()
    # Belirli yıllara ait hava durumu verilerini al
    weather_data_2024 = get_weather_data(2024)
    weather_data_2022 = get_weather_data(2022)
    weather_data_2020 = get_weather_data(2020)
    weather_data_2018 = get_weather_data(2018)
    # Ortalama sıcaklık değerlerini hesapla
    average_temperature_2024 = calculate_average_temperature(weather_data_2024)
    average_temperature_2022 = calculate_average_temperature(weather_data_2022)
    average_temperature_2020 = calculate_average_temperature(weather_data_2020)
    average_temperature_2018 = calculate_average_temperature(weather_data_2018)
    # Şablonu render et
    return render_template('graphic.html', 
                         
                          datas=datas)
if __name__ == '__main__':
    app.run(debug=True)
