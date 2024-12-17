# MIT License
# Copyright (c) 2024 CCwhiteX

import os
import sys
import importlib.util
from time import sleep

API_PLUGIN = "1.0.0"

def plugin(bot):
    directory = "./plugin/"
    if os.path.isdir(directory):
        print("Каталог для плагинов присутствует, выполнение скрипта автозапуска!")
        os.system("chmod +x ./autostart.sh")
        os.system("./autostart.sh")
        sleep(1)
        sys.path.append(directory)
        for filename in os.listdir(directory):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = filename[:-3]
                module = importlib.import_module(module_name)
                module.register_plugin(bot)
    else:
        try:
            print("Каталог с плагинами отсутствует!")
            os.mkdir(directory)
            os.system("touch ./autostart.sh")
        except Exception as err:
            print("Ошибка: " + str(err))

