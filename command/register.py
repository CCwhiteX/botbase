# MIT License
# Copyright (c) 2024 CCwhiteX

import os
import sys
from time import sleep

USER_IDS_FILE = "user_ids.txt"

def add_user_id(user_id):
    with open(USER_IDS_FILE, 'a') as f:
        f.write(f"{user_id}\n")

def register(message, bot):
    user_id = message.from_user.id
    directory_users = "./users/" + str(user_id)
    if os.path.isdir(directory_users):
        bot.send_message(user_id, "Вы уже зарегистрированы!")
    else:
        try:
            bot.send_message(user_id, "Регистрация...")
            os.mkdir(directory_users)
            sleep(1)
            add_user_id(user_id)
            bot.send_message(user_id, "Вы успешно зарегистрировались!")
            print(f"Зарегистрирован новый пользователь: {user_id}")      
        except Exception as err:
            bot.send_message(user_id, "Ошибка регистрациии! Попробуйте позже.")
            print(f" Ошибка регистрации {user_id} : {err}")
    	