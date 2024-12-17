# MIT License
# Copyright (c) 2024 CCwhiteX

import os
import platform
import subprocess

name = "fetch"
version = "v1-fetch"
developer = "CCwhiteX"

def get_username():
    try:
        return os.getlogin()
    except Exception:
        return os.environ.get('USER') or os.environ.get('LOGNAME') or 'Неизвестный пользователь'

def get_os():
    return platform.system() + " " + platform.release()

def get_kernel_version():
    return platform.uname().release

def get_shell():
    return os.environ.get('SHELL', 'Неизвестная оболочка').split('/')[-1]

def get_memory_usage():
    try:
        mem_info = subprocess.check_output(['free', '-h']).decode('utf-8').splitlines()[1].split()
        total_memory = mem_info[1]
        used_memory = mem_info[2]
        return f"{used_memory}/{total_memory}"
    except Exception as e:
        return f"Ошибка при получении использования памяти: {str(e)}"

def get_cpu_info():
    try:
        return subprocess.check_output(['lscpu']).decode('utf-8').splitlines()[0]
    except Exception as e:
        return f"Ошибка при получении информации о ЦП: {str(e)}"

def command(bot):
    @bot.message_handler(commands=['fetch'])
    def info(message):
        chat_id = message.chat.id
        inf = f"""
        Fetch System
        Имя пользователя: {get_username()}
        ОС: {get_os()}
        Версия ядра: {get_kernel_version()}
        Оболочка: {get_shell()}
        Использование памяти: {get_memory_usage()}
        Информация о ЦП: {get_cpu_info()}       
        """
        bot.send_message(chat_id, inf)

def register_plugin(bot):
    try:
        print(name + " " + version + " " + developer)
        command(bot)
        print("Плагин загружен!")
    except Exception as err:
        print("Ошибка загрузки плагина! " + str(err))