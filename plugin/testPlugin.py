# MIT License
# Copyright (c) 2024 CCwhiteX

name = " TestPlugin "
version = " v1 "
developer = " TestUser "

def command(bot):
    @bot.message_handler(commands=['test'])
    def info(message):
        chat_id = message.chat.id
        bot.send_message(chat_id, "Плагин для демонстрации работы системы плагинов!")

def register_plugin(bot):
    try:
        print(name + version + developer)
        command(bot)
        print("Плагин загружен!")
    except Exception as err:
        print("Ошибка загрузки плагина! " + str(err))
