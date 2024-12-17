# MIT License
# Copyright (c) 2024 CCwhiteX

import command.config
from googletrans import Translator

translator = Translator()

def lang(message, bot):
    try:
        text = message.text
        chat_id = message.chat.id
        text_to_translate = message.text.split(' ', 1)[1]
        translation = translator.translate(text_to_translate, dest=command.config.la)
        bot.send_message(chat_id, translation.text)
        print(f"Получен запрос {text} | Отправлен ответ {translation.text}")
    except IndexError:
        bot.send_message(chat_id, "Аргумент пустой! Правильный ввод команды /lang your text")
