FROM  python:3.10.8-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "main_weather_tg_bot.py" ]

