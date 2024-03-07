import datetime
import time

import schedule
from pprint import pprint
import requests
from config import open_weather_token


def get_weather(city, open_weather_token):
    code_smile = {'Clouds': "облачно \U00002601",
                  'Clear': "ясно \U00002600",
                  "Snow": "снег \U00001f328",
                  "Raine": "дождь \U00002614"
                  }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric")
        data = r.json()
        pprint(data)

        city = data["name"]
        temperature = data["main"]["temp"]
        wind = data["wind"]["speed"]
        wind_gradient = data["wind"]["deg"]

        if 0 < wind_gradient <= 22 or 338 < wind_gradient <= 360:
            wg = "С."
        elif 22 < wind_gradient <= 67:
            wg = "СВ"
        elif 67 < wind_gradient <= 112:
            wg = "В"
        elif 112 < wind_gradient <= 157:
            wg = "ЮВ"
        elif 157 < wind_gradient <= 202:
            wg = "Ю"
        elif 202 < wind_gradient <= 247:
            wg = "ЮЗ"
        elif 247 < wind_gradient <= 292:
            wg = "З"
        elif 292 < wind_gradient <= 338:
            wg = "СЗ"

        weather_discription = data["weather"][0]["main"]

        if weather_discription in code_smile:
            wd = code_smile[weather_discription]
        else:
            wd = "не знаю"

        print(datetime.datetime.now().strftime("%y-%m-%d"))
        print(f'погода в городе :  {city}\nТемпература: {temperature} C, {wd}\nВетер: {wg},  {wind} m/c')

    except Exception as ex:
        print(ex)
        print("проверте назание города")
        main()


def main():
    city = input("Введите город  ")
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()
