import requests
import datetime
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import tg_bot_token, open_weather_token

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привет. напиши название города, я пришлю погоду")


@dp.message_handler()
async def get_weather(message: types.Message):
    code_smile = {'Clouds': "облачно \U00002601",
                  'Clear': "ясно \U00002600",
                  "Snow": "снег \U00001f328",
                  "Raine": "дождь \U00002614"
                  }
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?"
            f"q={message.text}&appid={open_weather_token}&units=metric")
        data = r.json()

        city = data["name"]
        temperature = data["main"]["temp"]
        wind = data["wind"]["speed"]
        weather_description = data["weather"][0]["main"]
        wind_gradient = data["wind"]["deg"]
        # region
        if 0 < wind_gradient <= 11.25 or 371.25 < wind_gradient <= 360:
            wg = "С."
        elif 11.25 < wind_gradient <= 33.75:
            wg = "C-СВ"
        elif 33.75 < wind_gradient <= 56.25:
            wg = "СВ"
        elif 56.25 < wind_gradient <= 78.75:
            wg = "B-СВ"
        elif 78.75 < wind_gradient <= 101.25:
            wg = "В"
        elif 101.25 < wind_gradient <= 123.75:
            wg = "B-ЮВ"
        elif 123.75 < wind_gradient <= 146.25:
            wg = "ЮВ"
        elif 146.25 < wind_gradient <= 168.75:
            wg = "Ю-ЮВ"
        elif 168.75 < wind_gradient <= 191.25:
            wg = "Ю"
        elif 191.25 < wind_gradient <= 213.75:
            wg = "Ю-ЮЗ"
        elif 213.75 < wind_gradient <= 236.25:
            wg = "ЮЗ"
        elif 236.25 < wind_gradient <= 258.75:
            wg = "З-ЮЗ"
        elif 258.75 < wind_gradient <= 281.25:
            wg = "ЮЗ"
        elif 281.25 < wind_gradient <= 303.75:
            wg = "З"
        elif 303.75 < wind_gradient <= 326.25:
            wg = " З-СЗ"
        elif 326.25 < wind_gradient <= 348.75:
            wg = "СЗ"
        elif 348.75 < wind_gradient <= 371.25:
            wg = "С-СЗ"
        # endregion
        if weather_description in code_smile:
            wd = code_smile[weather_description]
        else:
            wd = "не знаю"

        await message.reply(f'{datetime.datetime.now().strftime("%y-%m-%d")}\n'
                            f'погода в городе : {city}\nТемпература: {temperature} C, '
                            f'{wd}\nВетер: {wg},  {wind} m/c')

    except:
        await message.reply("проверьте название города \U00002620")


if __name__ == "__main__":
    executor.start_polling(dp)
