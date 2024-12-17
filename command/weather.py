# MIT License
# Copyright (c) 2024 CCwhiteX

import requests

api_weather = "82ba7179366982a992a2a3b5d66f4e02"

def weather(message, bot):
    try:
        global api_weather
        text = message.text
        chat_id = message.chat.id
        city = message.text.split(' ', 1)[1]
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_weather}&units=metric"  # Замените на ваш API
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            description = data['weather'][0]['description']
            bot.send_message(chat_id, f"Сейчас в городе {city} {temp}°C {description}")
            print(f"Получен запрос {text} | Отправлен ответ {city} {temp}°C {description}")
        else:
            bot.send_message(chat_id, "Город не найден!")
    except IndexError:
        bot.send_message(chat_id, "Аргумент пустой! Правильный ввод команды /weather your city")
        
