# MIT License
# Copyright (c) 2024 CCwhiteX

import command.config
from telebot import types

buttonName = "Язык переводчика: English"
buttonName1 = "Busybox: Disable"

def toggle_vc():
    command.config.vc = not command.config.vc

def toggle_sw():
    command.config.sw = not command.config.sw
    
def change_language(new_la):
    command.config.la = new_la

def setting(message, bot):
    text = message.text
    chat_id = message.chat.id
    keyboard = types.InlineKeyboardMarkup()
    
    #Кнопка 1
    button1 = types.InlineKeyboardButton(text=buttonName, callback_data="button1")
    keyboard.add(button1)
    #Кнопка 2
    button2 = types.InlineKeyboardButton(text=buttonName1, callback_data="button2")
    keyboard.add(button2)
    
    bot.send_message(chat_id, "Настройки", reply_markup=keyboard)
    
def callback_inline(call, bot):
    global buttonName, buttonName1
    chat_id = call.message.chat.id
    mesa_id = call.message.message_id
    mesa = call.message
    datas = call.data
    if mesa: 
        if datas == "button1":
            if command.config.sw:
                buttonName = "Язык переводчика: Russian"
                change_language('ru')
                toggle_sw()
                bot.edit_message_reply_markup(chat_id, mesa_id, reply_markup=update_markup())
            else:
                buttonName = "Язык переводчика: English"
                change_language('en')
                toggle_sw()
                bot.edit_message_reply_markup(chat_id, mesa_id, reply_markup=update_markup())
        if datas == "button2":
            if command.config.vc:
                buttonName1 = "Busybox: Disable"
                toggle_vc()
                bot.edit_message_reply_markup(chat_id, mesa_id, reply_markup=update_markup())
            else:
                buttonName1 = "Busybox: Enable"
                toggle_vc()
                bot.edit_message_reply_markup(chat_id, mesa_id, reply_markup=update_markup())


def update_markup():
    markup = types.InlineKeyboardMarkup()
    
    button1 = types.InlineKeyboardButton(text=buttonName, callback_data="button1")
    button2 = types.InlineKeyboardButton(text=buttonName1, callback_data="button2")
    
    markup.add(button1)
    markup.add(button2)
    return markup
    