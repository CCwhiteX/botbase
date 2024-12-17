# MIT License
# Copyright (c) 2024 CCwhiteX

import requests
import time

def telegram_url(url):
    start_time = time.time()
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        end_time = time.time()
        return end_time - start_time, len(response.content) / (end_time - start_time) / 1024
    except requests.RequestException as err:
        print("Ошибка соединения " + err)

def speedtg():
    tg_url = "https://telegram.org"
    duration, speed = telegram_url(tg_url)
    if duration is not None:
        print(f"Время ответа: {duration:.2f} секунд")
        print(f"Скорость загрузки: {speed:.2f} КБ/с")
