# MIT License
# Copyright (c) 2024 CCwhiteX

import os
import subprocess
import time
from time import sleep

def stream_output(chat_id, command, bot):
    process = subprocess.Popen(
    ["./busybox"] + command.split(),
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    bufsize=1,
    universal_newlines=True
    )

    initial_message = bot.send_message(chat_id, "Busybox")
    message_id = initial_message.message_id
    full_output = "Busybox\n"
    
    try:
        for line in process.stdout:
            message = line.strip()
            if message:
                full_output += message + "\n"
                bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=full_output)
                sleep(0.4)
        stderr_output = process.stderr.read()
        if stderr_output:
            error_message = stderr_output.strip()
            if error_message:
                full_output += f"Ошибка: {error_message}\n"
                bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=full_output)                            
    except Exception as err:
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f"Произошла ошибка: {str(err)}")

def busybox_install():
    directory = "./bin/"
    sleep(1)
    if os.path.isdir(directory):
        print("[OK] Busybox")
    else:
        try:
            print("[ERROR] Busybox")
            print("Установка busybox...")
            os.mkdir(directory)
            os.system("./busybox --install ./bin")
            sleep(1)
            print("[OK] Busybox")
        except Exception as err:
            print("Ошибка установки! " + str(err))
