# MIT License
# Copyright (c) 2024 CCwhiteX

import configparser
import telebot
import threading
import command.config
import time
import os
from command.lang import lang
from command.weather import weather
from command.duckduck import duckduck
from command.setting.setting import setting
from command.busybox import busybox_install, stream_output
from command.plugin import plugin
from command.register import register
from console.Console import console
from console.UserManager import is_admin, is_banlist, is_userlist

def load_config(filename):
    try:
        config = configparser.ConfigParser()
        config.read(filename)
        return config
        print("Конфигурация загружена!")
    except Exception as err:
        print("Ошибка загрузки конфигурации!")
        
config_file = 'config.ini'
config = load_config(config_file)

def cons():
    cs = threading.Thread(target=console)
    cs.start()

bot = telebot.TeleBot(config['CONFIG']['token_telegram'])

busybox_install()
plugin(bot)
cons()

@bot.message_handler(commands=['start', 'register'])
def handle_register(message):
    register(message, bot)


@bot.message_handler(func=lambda message: is_banlist(message.from_user.id))
def blockyou(message):
    bot.send_message(message.from_user.id, "Вы заблокированы")


@bot.message_handler(func=lambda message: is_userlist(message.from_user.id))
def noreg(message):
    bot.send_message(message.from_user.id, "Вы не зарегистрированы, выполните команду /register")
    

@bot.message_handler(commands=['help'])
def menu(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, """
    Команды: 
    /lang {text} - Перевести текст
    /weather {city} - Погода в городе
    /go {question} - Запросы в DuckDuckGO
    /setting - Настройки бота
    """)

@bot.message_handler(commands=['setting'])
def handle_setting(message):
    if is_admin(message.from_user.id):
        setting(message, bot)
    else:
        bot.send_message(message.from_user.id, "Нет прав доступа")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    from command.setting.setting import callback_inline
    callback_inline(call, bot)

@bot.message_handler(commands=['lang'])
def handle_lang(message):
    lang(message, bot)

@bot.message_handler(commands=['weather'])
def handle_weather(message):
    weather(message, bot)
    
@bot.message_handler(commands=['go'])
def handle_duckduck(message):
    duckduck(message, bot)

@bot.message_handler(content_types=['text'])
def logical(message):
    text = message.text
    chat_id = message.chat.id
    if text == "su":
        bot.send_message(chat_id, "Команда заблокирована в целях безопасности")
    else:
        if command.config.vc:
            thread = threading.Thread(target=command.busybox.stream_output, args=(chat_id, text, bot))
            thread.start()
        else:
            bot.send_message(chat_id, "Команд нет! Включите busybox в настройках.")

bot.infinity_polling()