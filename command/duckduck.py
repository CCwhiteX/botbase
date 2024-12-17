# MIT License
# Copyright (c) 2024 CCwhiteX

import requests

def duckduck(message, bot):
    try:
        text = message.text
        chat_id = message.chat.id
        question = message.text.split(' ', 1)[1]
        url = f'https://api.duckduckgo.com/?q={question}&format=json&no_redirect=1&no_html=1&skip_disambig=1'
        response = requests.get(url)
        data = response.json()
        if 'RelatedTopics' in data and data['RelatedTopics']:
            answer = data['RelatedTopics'][0].get('Text', 'Нет ответа.')
            if 'FirstURL' in data['RelatedTopics'][0]:
                link = data['RelatedTopics'][0]['FirstURL']
                bot.send_message(chat_id, f"Ответ: {answer} Ссылка: {link}")
                print(f"Получен запрос {text} | Отправлен ответ {answer} и ссылка {link}")
            else:
                bot.send_message(chat_id, f"Ответ: {answer}")
                print(f"Получен запрос {text} | Отправлен ответ {answer}")
        else:
            bot.send_message(chat_id, "Ответ на запрос не найден")
    except IndexError:
        bot.send_message(chat_id, "Аргумент пустой! Правильный ввод команды /go your question") 
        